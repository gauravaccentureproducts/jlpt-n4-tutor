# Changelog

All notable changes to JLPT N4 Tutor will be documented here. Format: [Keep a Changelog](https://keepachangelog.com).

## [Unreleased]

(Pass-3 — full Tanos vocab fetch; native review; native audio re-record; FSRS-4; listening corpus authoring; coverage compare; browser smoke tests.)

## [0.1.0] — 2026-05-04 (Pass-2 complete; ALL 41 invariants PASS)

### Added (build-steps 7-8)

- **Question banks** (build-step 7-8/15): 591 questions across 5 banks via `tools/build_n4_questions.py`:
  - `moji_questions_n4.md` (100): Mondai 1 kanji-reading (50) + Mondai 2 orthography (50)
  - `goi_questions_n4.md` (100): Mondai 4 synonym (40) + Mondai 5 usage (40) + Mondai 6 paraphrase (20)
  - `bunpou_questions_n4.md` (100): Mondai 1 fill-blank (50) + Mondai 2 arrange (30) + Mondai 3 cloze (20)
  - `dokkai_questions_n4.md` (102): 30 short passages with reading questions
  - `externally_sourced_n5.md` (189): mixed third-party-paraphrased questions
- Question quality: SEED corpus, programmatically generated. Distractors drawn from same-PoS vocab. Scope-filtered to N4 whitelist (X-6.1 + JA-1 PASS). JA-2 prophylactic prevents particle-set false positives.

### Integrity state

**ALL 41 INVARIANTS PASS.** Build pipeline is fully green. Native-teacher review (Pass-3 Layer 8) is the next quality gate before exam-grade use.

## [0.1.0-alpha] — 2026-05-04 (Pass-2 seed corpus, JA-8 fails)

### Added

- **Kanji whitelist** (build-step 3/15): 249 glyphs (106 N5 prerequisite + 143 N4 new from `n4-kanji-inventory.md`). Builder: `tools/build_n4_kanji.py`. 24 inventory entries overlapped with N5 (borderline kanji per inventory notes).
- **Kanji catalogue** (build-step 4/15): `KnowledgeBank/kanji_n4.md` structurally complete in JA-12-compatible format. Per-glyph examples deferred to Pass-3 (will draw from full vocab corpus).
- **Vocab seed** (build-step 5/15): 1159 entries (1041 N5 prerequisite + 118 N4 from a-h sample inventory). Builder: `tools/build_n4_vocab.py`. Suru-noun handling per N5 convention (each generates [n.] + [v3] entries). Full ~600-entry N4 corpus deferred to Pass-3 Tanos N4 CSV fetch.
- **Grammar catalogue** (build-step 6/15): 307 patterns (178 N5 prerequisite + 129 N4 from `n4-grammar-inventory.md`). Builder: `tools/build_n4_grammar.py`. Distributed across 18 N4 categories per spec. 4 meta-topics dropped (意向形, 受身形, 他動詞 & 自動詞). 6 patterns kana-folded for out-of-scope kanji (場合は -> ばあいは, 必要 -> ひつよう, 頃 -> ころ).
- **UI N4 wiring** (build-step 9/15): JS modules updated to reflect N4 scope (feedback placeholder, home pillar description, learn page lede, settings export filename, summary foundational-pattern regex). `GRAMMAR_SUPERCATS` extended with 18 N4 categories.
- Skeleton files for question banks (Engine display note header added) and `data/dokkai_kanji_exception.json` to satisfy structural integrity checks.

### Integrity state

35/41 invariants PASS. 6 FAIL all in JA-8 (Q-count integrity, expects 591 questions, has 0). Question banks are Pass-3 deliverable.

## [0.1.0] — 2026-05-04 (Pass-1 skeleton)

### Added

- Initial repo skeleton scaffolded from JLPT N5 Tutor architecture.
- Directory structure per spec §29: `js/`, `css/`, `data/`, `KnowledgeBank/`, `tools/`, `audio/`, `svg/kanji/`, `fonts/`, `locales/`, `tests-e2e/`, `feedback/`, `specifications/`, `.claude/`, `.github/`.
- Token substitution applied: `jlpt-n5-tutor` → `jlpt-n4-tutor`, `JLPT N5` → `JLPT N4`, `n5_*` → `n4_*`, brand kanji `五` → `四`, favicon SVG `N5` → `N4` text.
- `data/*.json` skeleton files with populated `_meta` blocks and empty `entries[]` arrays.
- `KnowledgeBank/*.md` skeleton files with section structure (18 grammar categories, 18 vocab thematic sections, 5 question files, kanji catalogue, sources file).
- Service worker `jlpt-n4-tutor-v1` (cache version reset to v1).
- Build pipeline scripts ported from N5 (`build_data.py`, `check_content_integrity.py`, `test_build_data.py`, `build_audio.py`, `build_papers.py`, `link_grammar_examples_to_vocab.py`, `scan_multi_correct.py`, `heuristic_audit.py`, `llm_audit.py`, `tag_vocab_pos.py`, `coverage_compare.py`).
- N4 specification: `procedure-manual-build-next-jlpt-level.N4.md` (the single source of truth for this build).
- Bootstrap content inventories: `n4-grammar-inventory.md`, `n4-kanji-inventory.md`, `n4-vocab-inventory-sample.md`, `n4-inventory-manifest.md`, `N4-PLANNING.md`.

### Deferred to Pass-2

- Authoring of all 6 corpora (~210 grammar / ~1500 vocab / 280 kanji / ~30 reading / ~30 listening / ~530 questions).
- Audio rendering via gTTS (~600 MP3s).
- LLM audit run.
- Coverage comparison vs JLPT-Sensei + Tanos.
- Native-teacher review.
- Browser smoke tests (Playwright).
- Lighthouse CI green-light.

See `TASKS.md` for detailed Pass-2 backlog.

### Architecture inherited from N5 (verbatim port + token substitution)

- 25+ JS modules
- Vanilla CSS (Zen Modern design system)
- Hash-based router
- PWA shell + service worker
- 5-locale i18n shell (en/vi/id/ne/zh)
- SM-2 SRS engine
- 13 build / audit Python scripts
- Browser-runnable engine tests (`tests.html`)
