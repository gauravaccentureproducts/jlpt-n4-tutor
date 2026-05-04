// Level-picker page (Level 1) and placeholder pages for N3-N1.
//
// This is the JLPT N4 deploy. The corpus + study tools here cover N4;
// N5 is a SIBLING DEPLOY at https://gauravaccentureproducts.github.io/jlpt-n5-tutor/.
// Clicking the N5 card cross-navigates to that origin. The N5 card carries
// `external: true` so the renderer adds rel="noopener" + data-external.
//
// N3-N1 are not yet built. Their cards render disabled (visible but
// non-focusable) — clicked-but-unavailable would be misleading.
//
// (Fix 2026-05-04: prior to this commit, this file was a stale copy of the
// N5 levels.js where N4 was `available: false` and N5 had a same-origin
// `#/home` href. On the N4 origin that resolved N5 clicks to the N4
// dashboard. Both entries are now corrected: N4 is the local-origin home,
// N5 is the cross-origin sibling.)

const LEVELS = [
  {
    id: 'n5',
    code: 'N5',
    label: 'Beginner',
    desc: 'Basic Japanese — 177 grammar patterns, 1003 vocab, 106 kanji, 60 dokkai/listening drills.',
    href: 'https://gauravaccentureproducts.github.io/jlpt-n5-tutor/',
    available: true,
    external: true,  // cross-origin to a sibling deploy; not a same-origin hash route
  },
  {
    id: 'n4',
    code: 'N4',
    label: 'Elementary',
    desc: 'Builds on N5 with everyday topics, basic written passages, and lower-frequency kanji.',
    href: '#/home',          // Routes into the N4 dashboard (this site)
    available: true,
  },
  {
    id: 'n3',
    code: 'N3',
    label: 'Intermediate',
    desc: 'Bridge between elementary and upper-intermediate Japanese — natural-speed listening.',
    href: '#/n3',
    available: false,
  },
  {
    id: 'n2',
    code: 'N2',
    label: 'Upper-intermediate',
    desc: 'Newspapers, business contexts, and abstract grammar; expected for university entry.',
    href: '#/n2',
    available: false,
  },
  {
    id: 'n1',
    code: 'N1',
    label: 'Advanced',
    desc: 'Logical reasoning, formal/literary registers, all major grammar at native speed.',
    href: '#/n1',
    available: false,
  },
];

export function renderLevels(container) {
  container.innerHTML = `
    <section class="levels-page">
      <header class="levels-header">
        <h1 class="levels-title">JLPT</h1>
        <p class="levels-subtitle">Choose a level to start. Each level has its own grammar, vocabulary, kanji, reading, and listening study material.</p>
      </header>
      <div class="levels-grid">
        ${LEVELS.map(lvl => {
          // Available levels render as anchors (clickable). Unavailable
          // levels render as <div> with aria-disabled — visible, in
          // their own grid cell, but not focusable + not clickable.
          // Keeps the layout intact without inviting a click that
          // would route to a "nothing here" placeholder.
          if (lvl.available) {
            // External links (sibling deploys like the N5 tutor) carry
            // rel="noopener" + data-external so the renderer can mark
            // them visually and the user understands they're switching
            // to a separate app.
            const externalAttrs = lvl.external
              ? ' rel="noopener" data-external="true"'
              : '';
            return `
              <a class="level-card is-available" href="${lvl.href}" data-level="${lvl.id}"${externalAttrs}>
                <span class="level-card-code">${lvl.code}</span>
                <h2 class="level-card-label">${lvl.label}</h2>
                <p class="level-card-desc">${lvl.desc}</p>
                <span class="level-card-arrow" aria-hidden="true">→</span>
              </a>
            `;
          }
          return `
            <div class="level-card is-disabled" data-level="${lvl.id}"
                 aria-disabled="true"
                 title="Content not yet available">
              <span class="level-card-code">${lvl.code}</span>
              <h2 class="level-card-label">${lvl.label}</h2>
              <p class="level-card-desc">${lvl.desc}</p>
            </div>
          `;
        }).join('')}
      </div>
      <p class="levels-foot">
        N5 + N4 are live. N3 → N1 will fill in over time.
      </p>
    </section>
  `;
}

// Single placeholder renderer used for #/n3, #/n2, #/n1.
// Differentiates by reading the route name out of location.hash.
// (N4 is no longer a placeholder route on this deploy — N4 IS this site.)
export function renderLevelPlaceholder(container) {
  const m = (location.hash || '').match(/^#\/(n[1-3])(?:$|\/)/i);
  const code = (m ? m[1] : 'N?').toUpperCase();
  const lvl = LEVELS.find(l => l.id === code.toLowerCase()) || {
    code, label: 'Level', desc: '',
  };
  container.innerHTML = `
    <section class="level-placeholder">
      <p class="level-placeholder-back">
        <a href="#/levels">← All JLPT levels</a>
      </p>
      <h1 class="level-placeholder-title">JLPT ${esc(code)}</h1>
      <p class="level-placeholder-label">${esc(lvl.label)}</p>
      <div class="level-placeholder-card">
        <p class="level-placeholder-headline">Content not yet available.</p>
        <p>${esc(lvl.desc)}</p>
        <p>This site currently ships the JLPT N4 corpus only. ${esc(code)} content is on the roadmap.</p>
      </div>
      <p class="level-placeholder-foot">
        <a href="#/home" class="btn-action btn-action-secondary">Open JLPT N4 instead</a>
      </p>
    </section>
  `;
}

function esc(s) {
  return String(s ?? '').replace(/[&<>"']/g, c => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[c]));
}
