# Attesting Muse's TEE

An illustrated, interactive article about confidential virtual machines and remote
attestation. Plain HTML, CSS, and JavaScript with local fonts and responsive artwork.

- [Read the article](https://maceip.github.io/attesting-muse-tee/)
- [Download the review skills](https://maceip.github.io/attesting-muse-tee/downloads/muse-review-skills.zip)

## Run locally

```sh
python3 -m http.server 8847
```

Open `http://localhost:8847/`. HTTPS or localhost enables the browser SHA-256 demo.
No dependency installation is required.

## Review skills

The repository bundles two portable Agent Skills:

- **design-review**: preserve the article's visual design while reviewing responsive
  layouts, sticky artwork, accessibility, performance, and restrained interactions.
- **attestation-review**: review claims and trust boundaries, separate examples from
  evidence, and assess measurements, freshness, channel binding, verifier policy,
  and reproducible-build provenance when implementation artifacts are available.

| Tool | Bundled discovery location | Example invocation |
| --- | --- | --- |
| Codex | `.agents/skills/` | `$design-review` or `$attestation-review` |
| Google Antigravity / agy | `.agents/skills/` | `/design-review` or `/attestation-review` |
| Cursor | `.agents/skills/` | Ask Agent to use `design-review` or `attestation-review` |
| Claude Code | `.claude/skills/` | `/design-review` or `/attestation-review` |
| Grok Build | `.claude/skills/` through Claude compatibility | `/design-review` or `/attestation-review` |

Open the cloned repository in your coding tool. If it was already open when the
skill folders were added, reload the project/session to refresh discovery. The ZIP
contains the same folders, references, and usage notes; extract it into the app's
repository root. No API keys, account setup, or global configuration changes are
part of the skill bundle.

Edit `.agents/skills/`, then run `python3 scripts/sync_skills.py`. Claude-compatible
copies are ordinary files so GitHub ZIP downloads and Windows clones work without
symlinks. The repository check rejects stale copies. These paths follow the
[OpenAI](https://learn.chatgpt.com/docs/build-skills),
[Claude Code](https://code.claude.com/docs/en/skills),
[Antigravity](https://www.antigravity.google/docs/skills?tab=ide),
[Cursor](https://prod.cursor.com/docs/skills), and
[Grok](https://docs.x.ai/build/features/skills-plugins-marketplaces) documentation.
Directory compatibility and skill structure are checked; this does not claim an
end-to-end model execution in each vendor's application.

## Check and publish

```sh
python3 scripts/check.py
python3 scripts/package.py
```

The first command checks local resources, anchors, social metadata, and skill
copies. The second stages the static site in `_site/`, builds the skill ZIP, and
creates `dist/attesting-muse-publication-ready.zip` with the web app and skills.
Neither command substitutes for a browser review after visual or behavior changes.

GitHub Actions validates and deploys `main` to GitHub Pages. Pull requests run the
checks and package step without deploying. See [PUBLISHING.md](PUBLISHING.md).

## Scope

This is an independent explainer, not a Meta product or a production attestation
service. The SHA-256 demo runs locally; the report/measurement examples are fixtures.
Font licenses and their source information are included in `assets/fonts/`.
