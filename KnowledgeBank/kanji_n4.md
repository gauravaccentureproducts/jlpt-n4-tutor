# JLPT N4 Kanji

Source-of-truth catalogue. Whitelist = N5 ∪ N4 = 280 glyphs (106 N5 prerequisite + 174 N4 new).
Build pipeline parses into `data/kanji.json`. Schema per §14 / Appendix A.3.

Entry format per glyph:
```
## <glyph>  (tier: n5_prerequisite | core_n4)
- on: <on-yomi list, katakana>
- kun: <kun-yomi list, hiragana, slot in parens>
- primary: <reading>  (kind: on | kun)
- meanings: <english list>
- recognition_priority: 1 | 2 | 3
- stroke_order_svg: svg/kanji/<glyph>.svg
- examples:
  - <form> (<reading>) - <gloss>
  - <form> (<reading>) - <gloss>
- notes: <optional>
```

---

## N5 prerequisite kanji (106)

(Port verbatim from <source-repo>/KnowledgeBank/kanji_n5.md, retag tier: n5_prerequisite. See §8 migration table.)

## N4 new kanji (174)

(Author per §14 + cross-reference n4-kanji-inventory.md / jlptsensei.com / tanos.co.uk)
