"""Enrich kanji_n4.md and data/kanji.json with per-glyph examples.

For each N4-tier kanji entry without examples, finds 2-5 vocab entries
whose form contains that kanji and uses them as examples.

Idempotent: skips entries that already have examples.
"""
import io, json, re, sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent

# Load
kanji = json.loads((ROOT / 'data' / 'kanji.json').read_text(encoding='utf-8'))
vocab = json.loads((ROOT / 'data' / 'vocab.json').read_text(encoding='utf-8'))['entries']
whitelist = set(json.loads((ROOT / 'data' / 'n4_kanji_whitelist.json').read_text(encoding='utf-8')))

KANJI_RE = re.compile(r'[一-鿿]')

def all_kanji_in_scope(s):
    return all((not KANJI_RE.match(c)) or c in whitelist for c in s)

# Filter vocab to in-scope entries (forms whose all kanji are in N4 whitelist)
in_scope_vocab = [v for v in vocab if all_kanji_in_scope(v.get('form', ''))]
print(f'In-scope vocab pool: {len(in_scope_vocab)}')

# Build: kanji -> list of vocab entries containing it
kanji_to_vocab = {}
for v in in_scope_vocab:
    form = v.get('form', '')
    if not form:
        continue
    # Skip kana-only forms
    if not any(KANJI_RE.match(c) for c in form):
        continue
    for c in form:
        if KANJI_RE.match(c) and c in whitelist:
            kanji_to_vocab.setdefault(c, []).append(v)

# Enrich each kanji entry
enriched = 0
for entry in kanji['entries']:
    if entry.get('examples'):
        continue
    g = entry.get('glyph')
    if not g:
        continue
    candidates = kanji_to_vocab.get(g, [])
    if not candidates:
        # No vocab entry contains this kanji; leave examples empty
        continue
    # Prefer N4-tier vocab examples; fall back to any in-scope
    n4_first = sorted(candidates, key=lambda v: 0 if v.get('tier') == 'core_n4' else 1)
    examples = []
    seen_forms = set()
    for v in n4_first:
        form = v.get('form', '')
        if form in seen_forms:
            continue
        seen_forms.add(form)
        examples.append({
            'form': form,
            'reading': v.get('reading', ''),
            'gloss': (v.get('gloss', '') or '').split(';')[0].strip(),
        })
        if len(examples) >= 5:
            break
    if examples:
        entry['examples'] = examples
        enriched += 1

print(f'Enriched {enriched} kanji with examples')

# Write back data/kanji.json
(ROOT / 'data' / 'kanji.json').write_text(
    json.dumps(kanji, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'data/kanji.json updated')

# Update KnowledgeBank/kanji_n4.md to include examples per glyph
kb_path = ROOT / 'KnowledgeBank' / 'kanji_n4.md'
text = kb_path.read_text(encoding='utf-8')
# For each kanji entry block, find the closing line and append examples
# Block format: `- **{kanji}**  (tier: ...)` followed by sub-bullets

def replace_block(text, glyph, examples):
    """Add an `examples` sub-bullet to the block starting at `- **{glyph}**`."""
    pattern = re.compile(
        r'(- \*\*' + re.escape(glyph) + r'\*\*\s+\(tier:[^\n]*\n'
        r'(?:  - [^\n]*\n)+)',
        re.MULTILINE
    )
    m = pattern.search(text)
    if not m:
        return text
    block = m.group(1)
    if '  - examples:' in block:
        return text  # already has examples
    ex_strs = [f'{e["form"]}({e["reading"]}, {e["gloss"]})' for e in examples[:5]]
    new_line = '  - examples: ' + '; '.join(ex_strs) + '\n'
    return text[:m.end()] + new_line + text[m.end():]

updated = 0
for entry in kanji['entries']:
    if not entry.get('examples'):
        continue
    g = entry['glyph']
    new_text = replace_block(text, g, entry['examples'])
    if new_text != text:
        text = new_text
        updated += 1

kb_path.write_text(text, encoding='utf-8')
print(f'kanji_n4.md updated: {updated} entries got examples line')
