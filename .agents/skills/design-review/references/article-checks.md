# Article-specific design checks

## Vaults and layout

- The vault artwork in scenes `#s3`, `#s4`, and `#s5` shares `.vault-stage` with
  `.vault-ground` and `.vault-contact`, inside the sticky `.art` figure. Inspect
  entry, mid-scroll, and release. Grid/shadow offsets must stay constant relative
  to the artwork. Do not attach the ground to the viewport or another scroll layer.
- Desktop starts at 901px. The ground uses faint 1px `#E5E7EB` lines at 15%
  opacity, crossing at +/-30 degrees, with radial edge fading. Its 210% image-box
  width is roughly 2.5 times the visible vault width because the bitmap has margins.
  The contact shadow uses 20% black and 24px blur. Keep the grid behind adjacent text.
- At 900px and below, scene artwork is in normal flow and the desktop ground is
  hidden. Preserve the intended mobile stacking order and readable whitespace.
- For a full review sample 320, 390, 768, 900, 901, and 1440px, plus both sides of
  any breakpoint you change. Check long hashes/tables and chat avatars, not only the
  hero. Local horizontal scrolling is intentional; whole-page horizontal overflow
  is a defect. Check font loading before drawing spacing conclusions.

## Interaction and accessibility

- `#demo-line`: initially modified; editing to the published line produces MATCH.
  Rapid edits must show the latest digest. Reset restores the line and must not
  open the mobile keyboard. The full SHA-256 is exposed in the digest title;
  the visible digest is intentionally shortened.
- `#meas-toggle`: flips fixture bytes, text, and `aria-pressed`; a second activation
  restores the original. Keyboard Enter/Space and touch should work.
- Without JavaScript, the article stays readable and demo controls stay disabled.
  Without Web Crypto, show the unavailable state instead of a fabricated digest.
- Preserve visible focus, the skip link, descriptive control labels, empty alt on
  redundant chat avatars, meaningful artwork alt, and native keyboard semantics.
  Overflow regions receive a tab stop only while they overflow. Check arrow-key
  scrolling and touch panning without trapping page scrolling.
- Existing standalone controls have 44px minimum touch targets; narrow mobile
  inputs use 16px type. Inline prose links need readable spacing, not button styling.
  Hover behavior is gated to a fine pointer; reduced motion disables optional motion.

## Loading and publication

- Keep image intrinsic sizes and responsive sources. The hero has high priority;
  below-fold artwork loads lazily. Avoid preloading every image or font.
- Compare actual transferred bytes and request timing at the same viewport/DPR/cache
  state when claiming performance improvement. Do not infer speed from file count.
- Validate canonical, Open Graph, X, and JSON-LD URLs against the real hosting
  subdirectory. The social image must return an image to an unauthenticated request.
  Inspect the actual page at its public URL after an authorized deployment.
