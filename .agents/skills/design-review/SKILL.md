---
name: design-review
description: Review and polish this illustrated article's responsive layout, accessibility, performance, and interactions while preserving its established visual design.
---

# Design review

Use the actual rendered article and the requested change as the baseline. A request
to review produces findings; a request to fix authorizes relevant local fixes.
Preserve artwork, typography, section order, and the page's visual proportions
unless the user requests a redesign.

Read [article-specific checks](references/article-checks.md) for the vault behavior,
breakpoints, and demo states. Work from `index.html`, `assets/article.css`, and
`assets/article.js`; do not introduce a framework or runtime dependency for routine
polish. Keep production assets local and preserve font licenses.

Inspect desktop and mobile before editing. Prioritize clipped or unreachable
content, broken interactions, layout shifts, keyboard/touch failures, then visual
polish. Reproduce a concrete failure and make the smallest cohesive correction.
Do not add animation, shadows, hover movement, or UI controls merely to make the
review visibly productive.

Run `python3 scripts/check.py` from the repository root. Preview with
`python3 -m http.server 8847` or the available project browser. Exercise changed
controls with keyboard and touch where applicable. Inspect screenshots at the
affected widths and compare before/after; source inspection and a passing static
check do not establish rendered behavior. For a full publication review, also
check no-JavaScript and reduced-motion behavior, browser errors, resource failures,
and sharing metadata at the deployment URL.

Report findings by impact with a file/element, reproduction or screenshot evidence,
and the smallest useful fix. Distinguish changes made, browser behavior exercised,
and checks that could not run. Keep review notes outside the reader-facing UI.
Publishing or pushing follows the user's current authorization, not this skill.
