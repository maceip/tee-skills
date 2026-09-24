# Publishing this article

The public article is hosted at https://tee.public.computer/ from
https://github.com/maceip/tee-skills.

The DNS CNAME for `tee.public.computer` points directly to `maceip.github.io`.
GitHub Pages has `tee.public.computer` configured as its custom domain with
**Enforce HTTPS** enabled. The previous `https://maceip.github.io/tee-skills/`
address redirects to the custom domain. DNS itself is not an HTTP redirect.
This project deploys through Actions, so GitHub manages the custom domain in
Pages settings; a repository `CNAME` file is not required.

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
`img/social-preview.jpg` (1200 × 630, approximately 119 KB). It uses the supplied
artwork; the original `img/social-preview.png` remains available. The smaller
JPEG is a baseline RGB image with dimensions and descriptive alt text, served
directly over HTTPS without an image redirect. Checks enforce a project budget
of 300 KB, not a claimed platform limit. This metadata-only image adds no image
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
