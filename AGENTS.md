# Working on this article

This is a static illustrated article. `index.html`, `assets/article.css`, and
`assets/article.js` are the editable sources; `img/` and `assets/fonts/` are local
assets. There is no application build system or backend.

Preserve the established artwork, typography, section order, and page geometry
unless the task requests a design change. The three desktop vaults, ground grids,
and contact shadows share one sticky figure; do not give them independent scroll
transforms. Mobile figures are in normal document flow.

Use `.agents/skills/design-review/SKILL.md` for visual, responsive, accessibility,
performance, and interaction reviews. Use
`.agents/skills/attestation-review/SKILL.md` for attestation claims, trust-boundary
reviews, or verifier-policy work. These are task-specific skills, not requirements
to audit the whole article for every small change.

The browser SHA-256 demo hashes one text line. The measurement toggle uses fixture
values. Neither is a hardware attestation verifier or evidence of a live TEE.

Preview: `python3 -m http.server 8847`. Validate repository assets and metadata:
`python3 scripts/check.py`. Build the deployment package and skill download:
`python3 scripts/package.py`. For UI changes, also inspect the running page and
exercise the changed interaction at relevant desktop and mobile widths.

Canonical skills live in `.agents/skills/`. After editing them, run
`python3 scripts/sync_skills.py` to refresh Claude/Grok copies. CI checks drift.
Pushing `main` deploys GitHub Pages; publishing still follows the current user's
task authorization. Do not infer new deployment permission from a review alone.
