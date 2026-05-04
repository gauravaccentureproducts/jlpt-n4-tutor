# JLPT N4 Tutor — Memory

Last refreshed: 2026-05-04 (Pass-1 skeleton complete). Keep under 200 lines.

## Project location

- Root: `C:\Users\gaurav.l.srivastava\Documents\VS Code\JLPT\N4\`
- Source: vanilla HTML / ES modules / CSS, no build step for runtime
- Tests: `tests-e2e/` (Playwright smoke + a11y)
- Branch: `main` (no remote configured yet — first deploy will configure)
- HEAD: (initial commit pending)

## Sibling repos (level-agnostic context)

- `<JLPT-root>/N5/` — source repo for architectural inheritance.
- `<JLPT-root>/N3/`, `N2/`, `N1/` — not yet created.
- `<JLPT-root>/procedure-manual-build-next-jlpt-level.md` — level-agnostic playbook.

## Key files

- `procedure-manual-build-next-jlpt-level.N4.md` — **the spec.** Single source of truth for what this app must do.
- `README.md` — quick orientation.
- `CHANGELOG.md` — release history.
- `TASKS.md` — Pass-1/Pass-2/Pass-3 backlog.
- `index.html`, `sw.js`, `manifest.webmanifest` — static PWA shell.
- `js/app.js` — entry; router + skeleton renderer.
- `js/home.js`, `js/learn.js`, `js/test.js`, `js/drill.js`, `js/review.js`, `js/settings.js` — main route handlers.
- `js/storage.js` — LocalStorage wrappers + SM-2 SRS math.
- `css/main.css` — Zen Modern design system.
- `tools/build_data.py` — KB markdown → data/*.json. Most-important script.
- `tools/check_content_integrity.py` — 33-invariant CI gate.
- `KnowledgeBank/*.md` — source-of-truth content (markdown). All currently skeleton.
- `data/*.json` — runtime data (regenerated). All currently skeleton with `_meta` populated.

## Current state (2026-05-04)

- **Pass-1 skeleton complete.** Every directory + structural file in place.
- All token substitutions applied (`n5` → `n4`, `JLPT N5` → `JLPT N4`, brand `五` → `四`).
- All `data/*.json` are skeleton — empty arrays, populated `_meta`.
- All `KnowledgeBank/*.md` are skeleton — section headers only.
- N4 spec doc at repo root.
- Bootstrap inventories present for grammar / kanji / vocab.

## Pending / next up

1. **Verify CI green on empty corpus** — `python tools/check_content_integrity.py`.
2. **Initial commit + first push** to GitHub Pages target repo.
3. **Pass-2 Layer 3** — kanji whitelist + catalogue authoring.
4. **Pass-2 Layer 4** — vocabulary corpus authoring.
5. **Pass-2 Layer 5** — grammar catalogue authoring.

See `TASKS.md` for the full Pass-2 backlog.

## Permission posture

- `.claude/settings.local.json` carries `defaultMode: bypassPermissions` + broad allow rules + destructive-op deny list. Inherited from N5.
- For autonomous operation: launch Claude Code with `--dangerously-skip-permissions`.
- Deny list still gates: `git push --force`, `rm -rf`, `git reset --hard`, `git branch -D`, etc.

## Workflow (per `.claude/CLAUDE.md`)

1. Edit `KnowledgeBank/*.md` (source of truth — never edit `data/*.json` directly).
2. Run `python tools/build_data.py` to regenerate JSON.
3. Run `python tools/check_content_integrity.py` — must exit 0.
4. Commit. Push.
5. CI re-runs integrity check; deploys to GitHub Pages on green.

## Critical gotchas

- **PoS by section is anti-pattern AP-1.** Tag PoS per WORD, not per thematic section. Group-2 verbs in section 30 (Existence/Possession) must NOT inherit `verb-1` default.
- **Cross-reference hygiene:** any pattern-retirement pass must repoint `contrasts.with_pattern_id` and `form_rules.conjugations.label "See n4-XXX"` references. JA-32 catches.
- **Mid-line clipping on tile cards:** `flex: 1` + `display: -webkit-box` + `-webkit-line-clamp: N` + fixed parent height = mid-line crop. Use `max-height: Nlh` + remove `flex: 1` + `margin-top: auto` on action element.
- **Stale module state on URL nav:** reset `view='finished'/'results'` when URL navigates away. Mid-attempt state preserves on refresh.
- **Cache-bust contract:** bumping `CACHE_VERSION` in `sw.js` is necessary but not sufficient — `index.html` must also bump `?v=N` on the entry script. ES modules are cached by URL.
- **iOS auto-zoom:** all inputs need `font-size: 16px` minimum at `≤768px`.

## Decisions made (per spec §39.2 / §0.A.2 defaults)

| Decision | Choice | Rationale |
|---|---|---|
| Audio source | Synthetic gtts | Native re-record deferred to v2 (EB-1). |
| Native review | LLM-only via `tools/llm_audit.py` | Native sign-off deferred to v2 (EB-2). |
| Translation | English-only | EB-3. |
| Monetisation | Free, no telemetry | Hard constraint. |
| SRS algorithm | SM-2 | FSRS-4 deferred to v2 (EB-4). |
| Handwriting practice | Defer | v2. |
| IME-typing input | Defer (kana-strict v1) | v2. |
| Reading speed test | Defer | v2. |
| Mock test timing | JLPT.jp official N4 (125 min: 30/60/35) | Per spec §A.9. |

## GitHub Pages deployment notes

- Target repo: `jlpt-n4-tutor`.
- Live URL: `<org>.github.io/jlpt-n4-tutor/`.
- Base path: `/jlpt-n4-tutor/`.
- All asset paths relative.
- Hash routing only (`#/...`).
- `404.html` fallback redirects to `./`.
- Workflow at `.github/workflows/pages-build.yml`.

## What this session did

- Created the N4 spec at `<JLPT-root>/N4/procedure-manual-build-next-jlpt-level.N4.md` (2898 lines).
- Bootstrapped the N4 repo skeleton at `<JLPT-root>/N4/`.
- Applied token substitutions across all copied files.
- Wiped content from data/ and KnowledgeBank/ to skeleton state.
- Created N4-specific top-level files (this file, README, CHANGELOG, TASKS, PRIVACY, CONTENT-LICENSE, NOTICES).
- Did NOT yet: run integrity check, initial commit, push.

## Next session start

Read `TASKS.md` for the Pass-2 backlog. The recommended first action is "verify CI green on empty corpus" (one shell command).
