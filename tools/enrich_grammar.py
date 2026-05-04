"""Enrich N4 grammar patterns with form_rules + examples + explanation_en.

For each N4-tier pattern that lacks these fields, generates seed content:
- explanation_en: derived from meaning_en
- form_rules: attaches_to inferred from pattern's leading kana/kanji structure
- examples: 2 template sentences using in-scope vocab + the pattern, with
  vocab_ids satisfying JA-17

Idempotent: skips patterns that already have non-empty fields.

Quality: SEED-grade. Native-teacher review (Pass-4 Layer 8) recommended
before exam-grade use.
"""
import io, json, re, sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent

grammar_data = json.loads((ROOT / 'data' / 'grammar.json').read_text(encoding='utf-8'))
vocab = json.loads((ROOT / 'data' / 'vocab.json').read_text(encoding='utf-8'))['entries']

# Pre-categorize vocab by PoS for quick template-filling
vocab_by_pos = {}
for v in vocab:
    pos = v.get('pos', 'noun')
    vocab_by_pos.setdefault(pos, []).append(v)

# Quick lookup: form -> id (for vocab_ids)
form_to_id = {v['form']: v.get('id') for v in vocab if v.get('form') and v.get('id')}

KANJI_RE = re.compile(r'[一-鿿]')

def sample_vocab(pos, n=1):
    """Return up to n vocab entries of the given pos. Falls back to noun."""
    pool = vocab_by_pos.get(pos, []) or vocab_by_pos.get('noun', [])
    return pool[:n] if pool else []

def make_explanation(meaning_en):
    """Generate a basic explanation from the meaning_en field."""
    m = (meaning_en or '').strip().rstrip('.')
    if not m:
        return 'Used to express a specific grammatical relation; see Pass-4 native-teacher review for details.'
    return f'Used to express: {m}. See native-teacher review for nuance and register notes.'

def infer_attaches_to(pattern):
    """Heuristic inference of what verb/noun forms the pattern attaches to."""
    p = pattern
    if p.endswith(('る', 'う', 'く', 'ぐ', 'す', 'つ', 'ぬ', 'ぶ', 'む')):
        return ['verb_dictionary', 'verb_stem']
    if p.startswith(('〜た', 'たり', 'た')):
        return ['verb_ta_form']
    if p.startswith(('〜て', 'て')):
        return ['verb_te_form']
    if p.startswith(('〜ない', 'ない')):
        return ['verb_nai_form']
    if p.startswith(('〜ば', 'ば')):
        return ['verb_ba_form']
    if 'と思う' in p or 'と言う' in p:
        return ['plain_clause']
    if '〜よう' in p or 'よう' in p:
        return ['verb_volitional']
    if 'られる' in p:
        return ['verb_passive', 'verb_potential']
    if 'させる' in p:
        return ['verb_causative']
    return ['verb', 'na_adjective', 'noun']  # generic fallback

def make_examples(pattern_obj):
    """Generate 2 template example sentences for a pattern.

    Templates are intentionally simple: subject + pattern + ます/です.
    Native review (Pass-4) will replace these with naturalistic sentences.
    """
    pat = pattern_obj.get('pattern', '')
    meaning = pattern_obj.get('meaning_en', '').split(';')[0].strip()
    # Pull a noun + verb subject set from in-scope vocab
    nouns = sample_vocab('noun', 5)
    verbs = sample_vocab('verb-1', 5) + sample_vocab('verb-2', 5)
    if not nouns or not verbs:
        return []
    n1 = nouns[0]
    v1 = verbs[0] if verbs else None
    examples = []
    # Example 1: noun-based template
    if n1.get('form') and v1 and v1.get('form'):
        ja1 = f'{n1["form"]}は {pat}です。' if not pat.endswith(('る', 'い', 'う')) else f'{n1["form"]}を {pat}。'
        examples.append({
            'ja': ja1,
            'form': 'affirmative',
            'translation_en': f'(Seed example for {pat}: {meaning}.)',
            'vocab_ids': [form_to_id[n1['form']]] if n1['form'] in form_to_id else [],
        })
    # Example 2: verb-based template
    if len(verbs) > 1:
        v2 = verbs[1]
        if v2.get('form'):
            ja2 = f'{v2["form"]}{pat}。' if pat.startswith(('〜', 'と', 'ば')) else f'{v2["form"]}と {pat}言います。'
            examples.append({
                'ja': ja2,
                'form': 'affirmative',
                'translation_en': f'(Seed example using {v2["form"]}: {meaning}.)',
                'vocab_ids': [form_to_id[v2['form']]] if v2['form'] in form_to_id else [],
            })
    return examples

def make_common_mistakes(pattern_obj):
    """Generate 1 generic common-mistake placeholder."""
    pat = pattern_obj.get('pattern', '')
    return [{
        'wrong': f'(common N4 mistake involving {pat} — to be authored by native reviewer)',
        'right': f'{pat} (correct usage)',
        'why': 'Pass-4 native-teacher review will populate the specific common mistake here.',
    }]

# Enrich
enriched = 0
for p in grammar_data['patterns']:
    if p.get('tier') != 'core_n4':
        continue
    changed = False
    if not p.get('explanation_en'):
        p['explanation_en'] = make_explanation(p.get('meaning_en', ''))
        changed = True
    if not p.get('form_rules', {}).get('attaches_to'):
        p['form_rules'] = {
            'attaches_to': infer_attaches_to(p['pattern']),
            'conjugations': [],
        }
        changed = True
    if not p.get('examples'):
        p['examples'] = make_examples(p)
        changed = True
    if not p.get('common_mistakes'):
        p['common_mistakes'] = make_common_mistakes(p)
        changed = True
    if changed:
        enriched += 1

print(f'Enriched {enriched} N4 grammar patterns with seed content')

(ROOT / 'data' / 'grammar.json').write_text(
    json.dumps(grammar_data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'data/grammar.json updated')
