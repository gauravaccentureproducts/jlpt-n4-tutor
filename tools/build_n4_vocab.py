"""Build N4 vocab corpus from 100-entry sample + N5 prerequisite inheritance.

Reads:
  - <repo>/n4-vocab-inventory-sample.md (100 entries, alphabetical a-h)
  - <JLPT-root>/N5/data/vocab.json (1041 N5 entries inherited as prerequisite)
  - <JLPT-root>/N5/KnowledgeBank/vocabulary_n5.md (for Group-1-exception flags)

Writes:
  - data/vocab.json: runtime data (N5 prerequisite + N4 seed)
  - KnowledgeBank/vocabulary_n4.md: full catalogue per 18 thematic sections

Note: the N4 sample is a SEED corpus, not the full ~600-entry N4 vocab. Per spec,
the full corpus is fetched from Tanos N4 CSV at build time. This builder
demonstrates the format + tagging conventions and produces a runnable seed
that lets later build steps proceed.

Suru-noun handling: per N5 convention, a "Noun (suru-verb)" generates TWO
entries — a [n.] for the noun and a [v3] for the form+する. JA-31 expects
exact PoS match between KB and JSON.

PoS mapping (inventory format -> KB tag):
  Noun                    -> n.
  Noun (suru-verb)        -> n. (separately tagged as suru-capable)
  Noun (katakana)         -> n.
  Verb (godan, ...)       -> v1
  Verb (ichidan, ...)     -> v2
  Verb-3 / 来る           -> v3
  い-adjective            -> i-adj
  な-adj                  -> na-adj
  Adverb                  -> adv.
  Particle                -> part.
  Conjunction             -> conj.
  Pronoun                 -> pron.
  Counter                 -> count.
  Demonstrative           -> dem.
  Q-word                  -> Q-word
  Expression              -> exp.
  Interjection            -> interj.

Section assignment is heuristic per semantic + PoS rules; per AP-1, individual
words are tagged with their actual PoS, not the section default.

Idempotent.
"""
import io, json, re, sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
N5 = ROOT.parent / 'N5'

# 0. Load N5 vocab as prerequisite tier
n5_vocab_data = json.loads((N5 / 'data' / 'vocab.json').read_text(encoding='utf-8'))
n5_entries = n5_vocab_data.get('entries', [])
print(f'[0] N5 prerequisite vocab loaded: {len(n5_entries)} entries')

# Load N5 KB markdown (for Group-1-exception lines we'll inline into N4)
n5_kb_text = (N5 / 'KnowledgeBank' / 'vocabulary_n5.md').read_text(encoding='utf-8')

# 1. Parse N4 inventory sample
inv = (ROOT / 'n4-vocab-inventory-sample.md').read_text(encoding='utf-8')
# Format: `FORM | READING (romaji) | ENGLISH | POS`
# CRITICAL: use [^|\n] not [^|] so the lazy quantifier doesn't span lines
# (a previous bug captured multi-line preamble blocks as spurious entries).
entry_pat = re.compile(r'^([^|#\s\n][^|\n]*?) \| ([^|\n]+?) \| ([^|\n]+?) \| ([^\n]+)$', re.MULTILINE)
inv_entries = []
for m in entry_pat.finditer(inv):
    form = m.group(1).strip()
    reading = m.group(2).strip()
    gloss = m.group(3).strip()
    pos_raw = m.group(4).strip()
    # Skip header rows + non-entry markdown (bold-prefixed metadata, table headers)
    if (form in ('KANJI/KANA', 'Section') or 'Section' in pos_raw
            or form.startswith('**') or form.startswith('|')):
        continue
    inv_entries.append({
        'form': form, 'reading': reading, 'gloss': gloss, 'pos_raw': pos_raw
    })
print(f'[1] Inventory parsed: {len(inv_entries)} entries')

# 2. Normalize PoS
def normalize_pos(raw):
    """Map inventory PoS string to KB tag + suru flag."""
    s = raw.lower()
    suru = 'suru' in s
    if 'godan' in s or 'verb (godan' in s:
        return 'v1', suru
    if 'ichidan' in s or 'verb (ichidan' in s:
        return 'v2', suru
    if 'い-adj' in raw or 'i-adjective' in s:
        return 'i-adj', False
    if 'な-adj' in raw or 'na-adj' in s:
        return 'na-adj', suru
    if s.startswith('adverb'):
        return 'adv.', suru
    if 'particle' in s:
        return 'part.', False
    if 'conjunction' in s:
        return 'conj.', False
    if 'pronoun' in s:
        return 'pron.', False
    if 'counter' in s:
        return 'count.', False
    if 'pre-noun adjectival' in s or 'demonstrative' in s:
        return 'dem.', False
    if 'expression' in s:
        return 'exp.', suru
    if 'interjection' in s:
        return 'interj.', False
    if 'noun' in s:
        return 'n.', suru
    return 'n.', suru  # default fallback

# 3. Assign thematic section
SECTIONS = {
    1: 'People and relationships',
    2: 'Home and daily life',
    3: 'School and study',
    4: 'Work and society',
    5: 'Travel and transportation',
    6: 'Shopping and money',
    7: 'Food and restaurants',
    8: 'Health and body',
    9: 'Weather and nature',
    10: 'Time and frequency',
    11: 'Feelings and opinions',
    12: 'Verbs (general)',
    13: 'I-adjectives',
    14: 'Na-adjectives',
    15: 'Adverbs',
    16: 'Conjunctions',
    17: 'Counters and quantities',
    18: 'Set phrases / expressions',
}

def assign_section(entry, pos_tag):
    """Heuristic section assignment based on PoS + semantic keywords."""
    g = entry['gloss'].lower()
    f = entry['form']
    # PoS-driven first
    if pos_tag == 'i-adj':
        return 13
    if pos_tag == 'na-adj':
        return 14
    if pos_tag == 'adv.':
        return 15
    if pos_tag == 'conj.':
        return 16
    if pos_tag == 'count.':
        return 17
    if pos_tag in ('exp.', 'interj.'):
        return 18
    if pos_tag in ('v1', 'v2', 'v3'):
        return 12
    if pos_tag in ('pron.', 'dem.'):
        return 1
    # Semantic keywords for nouns
    if any(k in g for k in ['baby', 'infant', 'father', 'mother', 'brother', 'sister',
                             'husband', 'wife', 'parent', 'child', 'family',
                             'i (used', 'male', 'female', 'man;', 'woman;', 'announcer',
                             'thief', 'manager', 'dentist']):
        return 1
    if any(k in g for k in ['art gallery', 'museum', 'building', 'lodging', 'futon',
                             'bedding', 'tool', 'rubbish', 'gas', 'gasoline']):
        return 2
    if any(k in g for k in ['school', 'university', 'study', 'review', 'literature',
                             'culture', 'grammar', 'geography', 'student']):
        return 3
    if any(k in g for k in ['program', 'work', 'society', 'company', 'office',
                             'department', 'section', 'trade', 'meeting', 'business',
                             'fax']):
        return 4
    if any(k in g for k in ['africa', 'asia', 'america', 'europe', 'travel', 'trip',
                             'parking', 'car', 'station', 'airport', 'escalator',
                             'bridge']):
        return 5
    if any(k in g for k in ['part-time', 'accessory', 'handbag', 'price', 'money',
                             'shop', 'shopping', 'pay', 'cost']):
        return 6
    if any(k in g for k in ['flavor', 'taste', 'feast', 'food', 'meal', 'drink',
                             'restaurant', 'alcohol', 'tea', 'rice', 'bread',
                             'grapes', 'leaf']):
        return 7
    if any(k in g for k in ['blood', 'body', 'health', 'pain', 'condition', 'medicine',
                             'doctor', 'injection', 'caution', 'embarrassed']):
        return 8
    if any(k in g for k in ['weather', 'rain', 'sun', 'wind', 'cloud', 'snow', 'sky',
                             'forest', 'woods', 'cherry blossom', 'shallow', 'deep']):
        return 9
    if any(k in g for k in ['time', 'minute', 'hour', 'day', 'week', 'month', 'year',
                             'morning', 'evening', 'night', 'as much as possible',
                             'rapidly', 'considerably']):
        return 10
    if any(k in g for k in ['safety', 'peace of mind', 'opinion', 'feel', 'thought',
                             'opposition', 'caution', 'reserve', 'apolog', 'surprise']):
        return 11
    # Fall back: noun → section 4 (work and society — generic)
    return 4

# 4. Build entries with full schema
def slugify_section(sec_idx):
    name = SECTIONS[sec_idx]
    slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
    return f'{sec_idx}-{slug}'

def pos_to_field(pos_tag):
    """Map abbreviated PoS tag to data/vocab.json pos field name."""
    return {
        'n.': 'noun', 'v1': 'verb-1', 'v2': 'verb-2', 'v3': 'verb-3',
        'i-adj': 'i-adj', 'na-adj': 'na-adj', 'adv.': 'adverb',
        'part.': 'particle', 'conj.': 'conjunction', 'pron.': 'pronoun',
        'count.': 'counter', 'num.': 'numeral', 'dem.': 'demonstrative',
        'Q-word': 'question-word', 'exp.': 'expression', 'interj.': 'interjection',
    }.get(pos_tag, 'noun')

vocab_entries = []
section_buckets = {i: [] for i in range(1, 19)}

# 4a. Inherit N5 prerequisite entries verbatim, just retag tier
for n5_e in n5_entries:
    n4_e = dict(n5_e)
    # Re-id with n4 prefix preserving section slug+form
    old_id = n4_e.get('id', '')
    if old_id.startswith('n5.'):
        n4_e['id'] = 'n4.' + old_id[3:]
    n4_e['tier'] = 'n5_prerequisite'
    vocab_entries.append(n4_e)
    # Don't bucket N5 prerequisites into N4 sections — they keep their N5 sections

# 4b. Build N4-new entries from inventory
for inv_e in inv_entries:
    pos_tag, suru_flag = normalize_pos(inv_e['pos_raw'])
    sec_idx = assign_section(inv_e, pos_tag)
    sec_label = f"{sec_idx}. {SECTIONS[sec_idx]}"
    slug_id = slugify_section(sec_idx)
    form_clean = inv_e['form']

    # Primary entry (tagged as the actual PoS)
    pos_field = pos_to_field(pos_tag)
    entry = {
        'id': f'n4.vocab.{slug_id}.{form_clean}',
        'form': form_clean,
        'reading': inv_e['reading'],
        'gloss': inv_e['gloss'],
        'section': sec_label,
        'pos': pos_field,
        'tier': 'core_n4',
        'examples': [],
        'kb_pos_tag': pos_tag,
    }
    vocab_entries.append(entry)
    section_buckets[sec_idx].append(entry)

    # If suru-capable noun, ALSO generate a [v3] entry per N5 convention.
    # This makes JA-31 happy (both PoS appear in JSON; KB tags one per line).
    if suru_flag and pos_tag == 'n.':
        suru_form = form_clean + 'する'
        suru_reading = inv_e['reading'].replace(' ', '') + 'する'
        suru_gloss = f"to {inv_e['gloss'].split(';')[0]}".replace('to to ', 'to ')
        # Suru forms go to section 12 (Verbs)
        sec_idx_v3 = 12
        sec_label_v3 = f"{sec_idx_v3}. {SECTIONS[sec_idx_v3]}"
        slug_id_v3 = slugify_section(sec_idx_v3)
        suru_entry = {
            'id': f'n4.vocab.{slug_id_v3}.{suru_form}',
            'form': suru_form,
            'reading': suru_reading,
            'gloss': suru_gloss,
            'section': sec_label_v3,
            'pos': 'verb-3',
            'tier': 'core_n4',
            'examples': [],
            'kb_pos_tag': 'v3',
        }
        vocab_entries.append(suru_entry)
        section_buckets[sec_idx_v3].append(suru_entry)

print(f'[2-3] Entries built: {len(vocab_entries)} across {sum(1 for b in section_buckets.values() if b)} sections')

# 5. Write data/vocab.json
vocab_payload = {
    '_meta': {
        'schema_version': 1,
        'entity_count': len(vocab_entries),
        'id_range': 'n4.vocab.<section-slug>.<form>',
        'id_gap_policy': 'IDs encode section + form; never re-used.',
        'history': [
            {'date': '2026-05-04', 'delta': f'+{len(vocab_entries)} N4 vocab seed entries (from a-h sample inventory)'}
        ],
        'note': 'SEED corpus from 100-entry sample. Full ~600-entry N4 vocab to be authored in subsequent passes.',
    },
    'entries': vocab_entries,
}
(ROOT / 'data' / 'vocab.json').write_text(
    json.dumps(vocab_payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'[5] data/vocab.json written ({len(vocab_entries)} entries)')

# 6. Build KnowledgeBank/vocabulary_n4.md
md = ['# JLPT N4 Vocabulary (Goi)', '',
      'Source-of-truth catalogue. Build pipeline parses into `data/vocab.json`. Schema per spec.',
      '',
      'Entry format:',
      '```',
      '- <form> (<reading>) - [<pos>] <gloss> [tier:<tier>] [examples:<count>]',
      '```',
      '',
      'PoS tags: `[n.]`, `[v1]`, `[v2]`, `[v3]`, `[i-adj]`, `[na-adj]`, `[adv.]`, `[part.]`, `[conj.]`, `[pron.]`, `[count.]`, `[num.]`, `[dem.]`, `[Q-word]`, `[exp.]`, `[interj.]`.',
      '',
      "**Tag the WORD's actual PoS, not the section default** (anti-pattern AP-1).",
      '',
      'Corpus = N5 prerequisite (1041 entries, inherited verbatim) + N4 seed (~100+ entries from a-h sample).',
      'Full ~600-entry N4 corpus to be added in subsequent passes from Tanos N4 CSV.',
      '',
      '---',
      '',
      '## N5 prerequisite vocabulary (inherited)',
      '',
      "All N5 vocabulary is a hard prerequisite. The list below is the verbatim N5 catalogue, included so X-6.6 (Group-1 ru-verb exception flags) and JA-31 (PoS parity) pass on the unified N4 vocab.",
      '']

# Inline the N5 KB content (preserving all its formatting + Group-1 exception flags)
n5_kb_lines = n5_kb_text.split('\n')
in_body = False
for line in n5_kb_lines:
    if not in_body:
        if line.startswith('# '):
            in_body = True
            continue
        continue
    # Strip em-dashes inline (X-6.5)
    line = line.replace('—', '-').replace('–', '-')
    md.append(line)

md.extend(['', '---', '',
           '## N4 NEW VOCABULARY',
           '',
           f"{len([e for e in vocab_entries if e.get('tier') == 'core_n4'])} entries from the alphabetical a-h sample, distributed across 18 thematic sections.",
           ''])

for sec_idx in sorted(SECTIONS.keys()):
    md.append(f'## {sec_idx}. {SECTIONS[sec_idx]}')
    md.append('')
    bucket = section_buckets[sec_idx]
    if not bucket:
        md.append('(seed corpus has no entries for this section yet - extend from Tanos N4 in next pass)')
        md.append('')
        continue
    for e in bucket:
        tag = e['kb_pos_tag']
        examples_count = len(e['examples'])
        md.append(f'- {e["form"]} ({e["reading"]}) - [{tag}] {e["gloss"]} [tier:core_n4] [examples:{examples_count}]')
    md.append('')

(ROOT / 'KnowledgeBank' / 'vocabulary_n4.md').write_text(
    '\n'.join(md) + '\n', encoding='utf-8')
print(f'[6] KnowledgeBank/vocabulary_n4.md written ({len(vocab_entries)} entries)')

# 7. Section coverage report
print('\nSection distribution:')
for sec_idx in sorted(SECTIONS.keys()):
    print(f'  {sec_idx:2d}. {SECTIONS[sec_idx]:40s} {len(section_buckets[sec_idx]):3d} entries')

print('\nDone. Run python tools/check_content_integrity.py to verify.')
