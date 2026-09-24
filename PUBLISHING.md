# Publishing this article

The public article is hosted at https://maceip.github.io/attesting-muse-tee/ from
https://github.com/maceip/attesting-muse-tee.

Pushing `main` runs `.github/workflows/pages.yml`: validate local resources and
metadata, check synchronized skills, stage static assets, package the downloadable
skills, and deploy `_site/` to GitHub Pages. Pull requests validate and package
without deploying. Pages uses the GitHub Actions source.

Run `python3 scripts/package.py` locally to reproduce the deployment directory and
`dist/attesting-muse-publication-ready.zip`. The ZIP contains the web app, review
skills, documentation, and deployment workflow. Upload `index.html`, `assets/`,
`img/`, and `downloads/` together when using another static host. Relative page
assets also work when the article is hosted in a subdirectory. There is no browser
build step, backend, or runtime dependency on a font service.

Use HTTPS for the interactive SHA-256 demo. The article remains readable without
JavaScript; interactive controls are disabled when scripting is unavailable. If
browser crypto is unavailable, the demo explains that limitation instead of showing
a substitute hash. Preview locally with `python3 -m http.server 8847` and open
`http://localhost:8847/`.

Keep the font license files in `assets/fonts/` with the publication. Original
full-resolution artwork is included alongside smaller WebP sources. The browser
selects a suitable source for each screen.

Open Graph, X cards, and Article JSON-LD reference the public HTTPS article URL and
`img/social-preview.png` (2192 × 1152). The supplied artwork is unchanged, with
image dimensions and descriptive alt text. This metadata-only image adds no image
download to normal page rendering. If moving hosts, update the canonical link,
`og:url`, social image URLs, JSON-LD article/image URLs, README links, and the
publication URL in `scripts/check.py`. No author identity, social handle, or
publication date is inferred from the repository account.

Verify an unauthenticated request to the public article, image, and skill download
after deployment. A successful workflow is deployment evidence; it does not itself
prove a social service has refreshed its cached preview.

For a separately managed host, enable HTTP compression and cache revalidation for
HTML, CSS, and JavaScript. Asset filenames are not fingerprinted, so do not assign
an immutable year-long cache policy without versioning. GitHub Pages controls its
own response headers.
