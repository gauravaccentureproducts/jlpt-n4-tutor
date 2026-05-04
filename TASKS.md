# JLPT N4 Tutor — Tasks

**Last updated:** 2026-05-04 (Pass-1 skeleton complete)

## Live site

- Repo: `https://github.com/<org>/jlpt-n4-tutor` (configure on first deploy)
- Live URL: `https://<org>.github.io/jlpt-n4-tutor/` (configure)
- Engine tests: 0/0 (`tests.html` ported; needs N4-specific test data)
- CI invariants: 33/33 expected green on empty corpus (verify after first build)

## Status snapshot

- **Version:** v0.1.0 (Pass-1 skeleton)
- **SW version:** `jlpt-n4-tutor-v1`
- **Grammar:** 0 patterns (target ~210)
- **Vocab:** 0 entries (target ~1500)
- **Kanji:** 0 glyphs (target 280 = 106 N5 prerequisite + 174 N4 new)
- **Reading:** 0 passages (target ~30)
- **Listening:** 0 items (target ~30)
- **Questions:** 0 total (target ~530)
- **Mock-test papers:** 0 (target ~32)
- **Audio:** 0 MP3s (target ~600 synthetic)
- **Locales:** 5 (en/vi/id/ne/zh) — shell ported, N4 strings TBD
- **Routes:** 21 routes wired in router (most render empty until content lands)

## External-blocked backlog

- **EB-1:** Native-recorded listening audio. Ship synthetic gtts in v1; native re-record per item in v2.
- **EB-2:** Native-teacher review. Ship LLM-only audit in v1; native sign-off in v2.
- **EB-3:** Translation of brief to Japanese. v2.
- **EB-4:** FSRS-4 SRS migration. SM-2 in v1.
- **EB-5:** Stroke-order SVGs for 280 kanji (KanjiVG fetch). Pass-2.

## Pass-1 (initial skeleton, 2026-05-04)

### Done

- [x] Repo skeleton at `<JLPT-root>/N4/`, git init.
- [x] Directory structure per spec §29.
- [x] Copied 7 directories from N5: `.claude`, `.github`, `css`, `fonts`, `js`, `locales`, `tools`.
- [x] Copied 6 root files from N5: `index.html`, `manifest.webmanifest`, `sw.js`, `tests.html`, `playwright.config.js`, `package.json`.
- [x] Token substitution `n5` → `n4`: `jlpt-n5-tutor`, `JLPT N5`, `n5_kanji_*`, `n5_vocab_*`, `grammar_n5`, `vocabulary_n5`, `kanji_n5`, `*_questions_n5`.
- [x] Brand kanji `五` → `四` in `css/main.css`.
- [x] Favicon SVG embedded data URI: `N5` → `N4` in `index.html`, `manifest.webmanifest`.
- [x] SW cache version reset: `jlpt-n4-tutor-v1`.
- [x] `data/*.json` skeleton: 6 entity files + 3 whitelist files + audio_manifest + papers/manifest, all empty arrays + populated `_meta`.
- [x] `KnowledgeBank/*.md` skeleton: 9 files (3 catalogues + 5 question files + sources).
- [x] N4-specific top-level files: `README.md`, `CHANGELOG.md`, `TASKS.md` (this file), `MEMORY.md`, `PRIVACY.md`, `CONTENT-LICENSE.md`, `NOTICES.md`.
- [x] N4 spec lives at repo root: `procedure-manual-build-next-jlpt-level.N4.md`.
- [x] Bootstrap inventories present: `n4-grammar-inventory.md`, `n4-kanji-inventory.md`, `n4-vocab-inventory-sample.md`, `n4-inventory-manifest.md`, `N4-PLANNING.md`.

### Deferred (defaults applied per N4 spec §39.2 / §0.A.2)

- **Native voice budget** → synthetic TTS via gtts. Mark all listening items `voice: "synthetic"`. v2 native re-record per item.
- **Native teacher review** → LLM-only via `tools/llm_audit.py`. Mark all hand-authored entries `review_status: "llm_only"`.
- **Translation of brief to Japanese** → English-only ship. EB-3.
- **Subscription / monetisation** → free, no monetisation.
- **SRS algorithm** → SM-2 (FSRS-4 deferred to v2).
- **Handwriting kanji practice** → defer to v2.
- **IME-typing input mode** → defer to v2 (kana-strict in v1).
- **Reading-comprehension speed test** → defer to v2.
- **Mock test mode timing** → use JLPT.jp official N4 timing (125 min total: 30/60/35).

## Pass-2 (content authoring, target 2026-08-04)

### Layer 0 — verify CI (must ship first)

- [ ] Run `python tools/check_content_integrity.py` and confirm green on empty corpus.
- [ ] Fix any invariants that fail on empty content (these would be tooling bugs, not data issues).
- [ ] Run `python tools/test_build_data.py` and confirm green.

### Layer 3 — Kanji whitelist + catalogue (~3-6 hr)

- [ ] Build `data/n4_kanji_whitelist.json` from `n4-kanji-inventory.md` + N5 prerequisites = 280 glyphs.
- [ ] Build `data/n4_kanji_readings.json` per glyph: on/kun/primary.
- [ ] Author `KnowledgeBank/kanji_n4.md`: per-glyph entry per spec §14.2.
- [ ] Run X-6.9 invariant; fix primary-reading issues.
- [ ] Fetch 280 KanjiVG SVGs into `svg/kanji/`.

### Layer 4 — Vocabulary corpus (~6-12 hr)

- [ ] Author `KnowledgeBank/vocabulary_n4.md` ~1500 entries grouped by 18 thematic sections (per spec §13.2).
- [ ] Apply per-WORD PoS rule (anti-pattern AP-1).
- [ ] `tools/build_data.py` derives `data/vocab.json`.
- [ ] `tools/tag_vocab_pos.py` verifies PoS coverage.
- [ ] JA-31 invariant: vocab PoS parity (KB ↔ JSON, homograph-aware).

### Layer 5 — Grammar catalogue (~8-16 hr)

- [ ] Cross-reference Bunpro N4 + Tanos N4 + Genki II + Minna II.
- [ ] Tier per pattern (per spec §12.3).
- [ ] Author `KnowledgeBank/grammar_n4.md` ~210 patterns across 18 categories (per §12.2).
- [ ] 2-5 examples each + common-mistakes block per pattern.
- [ ] `tools/link_grammar_examples_to_vocab.py` for vocab_ids homograph-aware linkage.

### Layer 6 — Reading + Listening (~6-10 hr)

- [ ] Author `KnowledgeBank/dokkai_questions_n4.md`: ~30 passages per spec §15.
- [ ] Author `KnowledgeBank/chokai_questions_n4.md`: ~30 listening items per §16.
- [ ] `tools/build_audio.py` synthetic TTS pass.

### Layer 7 — Question banks (~12-24 hr)

- [ ] `moji_questions_n4.md` ~150 questions per Mondai 1/2/3.
- [ ] `goi_questions_n4.md` ~150 questions per Mondai 4/5/6.
- [ ] `bunpou_questions_n4.md` ~100 questions per Mondai 1/2/3.
- [ ] `tools/scan_multi_correct.py` — fix every flag.
- [ ] `tools/heuristic_audit.py` — apply auto-fixes.
- [ ] `tools/build_papers.py` — slice into 15-question papers.

### Layer 8 — Audit + tests + deploy

- [ ] `tools/llm_audit.py` over question banks (~$10-15 API).
- [ ] `tools/coverage_compare.py` vs jlptsensei.com / tanos.co.uk.
- [ ] Browser smoke test via `tests-e2e/p0-smoke.spec.js`.
- [ ] Lighthouse CI green: PWA=100, Perf≥90 mobile, A11y≥95.
- [ ] axe-core scan: zero serious / critical violations.
- [ ] First deploy to `<org>.github.io/jlpt-n4-tutor/`.
- [ ] Tag `v1.0.0`.

## Pass-3 (post-launch, target 2026-09-04)

- [ ] Native-teacher review of grammar patterns (commission reviewer).
- [ ] Native-recorded listening audio for top-priority items.
- [ ] Coverage gap fixes from Pass-2 §coverage_compare.
- [ ] FSRS-4 SRS migration.

## Known limitations (v0.1.0)

- Skeleton only — every content array is empty.
- Pages will render but show "no content" empty states until Pass-2 lands.
- Audio pipeline ported but no MP3s rendered (no content to render against).
- No N4-specific Playwright tests yet.

## Recommended next action

Run `python tools/check_content_integrity.py` and verify it exits 0 on empty corpus. If any invariant fails, fix the tooling (the empty-corpus state should be valid). Then start Pass-2 Layer 3 (kanji whitelist).
