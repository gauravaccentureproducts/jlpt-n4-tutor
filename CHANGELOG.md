# Changelog

All notable changes to JLPT N4 Tutor will be documented here. Format: [Keep a Changelog](https://keepachangelog.com).

## [Unreleased]

(Pass-2 — content authoring; native review; native audio re-record; FSRS-4.)

## [0.1.0] — 2026-05-04

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
