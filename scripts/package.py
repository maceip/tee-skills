#!/usr/bin/env python3
"""Stage only public site assets and bundle portable review skills."""
from pathlib import Path
import shutil
import subprocess
import sys
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
DIST = ROOT / "dist"


def add_tree(archive, directory):
    for path in sorted(directory.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts and path.name != ".DS_Store":
            archive.write(path, path.relative_to(ROOT).as_posix())


subprocess.run([sys.executable, str(ROOT / "scripts/check.py")], check=True)
if SITE.exists():
    shutil.rmtree(SITE)
SITE.mkdir()
DIST.mkdir(exist_ok=True)
shutil.copy2(ROOT / "index.html", SITE / "index.html")
for name in ("assets", "img"):
    shutil.copytree(ROOT / name, SITE / name)
(SITE / ".nojekyll").touch()
(SITE / "downloads").mkdir()
skill_zip = SITE / "downloads/muse-review-skills.zip"
with ZipFile(skill_zip, "w", ZIP_DEFLATED) as archive:
    for name in (".agents/skills", ".claude/skills"):
        add_tree(archive, ROOT / name)
    archive.write(ROOT / "scripts/sync_skills.py", "scripts/sync_skills.py")
    archive.writestr("SKILLS.md", """# Muse review skills

Extract these folders into the article repository root and reload your coding tool.
Codex, Antigravity (agy), and Cursor discover .agents/skills/. Claude Code and Grok
Build (via Claude compatibility) discover .claude/skills/.

Invoke design-review for visual, responsive, accessibility, and interaction work;
invoke attestation-review for TEE claims and evidence/policy reviews. Codex accepts
$design-review and $attestation-review; Claude, agy, and Grok accept slash commands.
In Cursor, ask Agent to use the named skill.

Edit canonical files under .agents/skills/, then run python3 scripts/sync_skills.py
to update the Claude/Grok copies. The article and its check script are in the app:
https://github.com/maceip/attesting-muse-tee

The skills are review instructions, not a hardware attestation implementation.
""")
bundle = DIST / "attesting-muse-publication-ready.zip"
with ZipFile(bundle, "w", ZIP_DEFLATED) as archive:
    for name in ("index.html", "README.md", "PUBLISHING.md", "AGENTS.md", "CLAUDE.md", ".gitignore"):
        archive.write(ROOT / name, name)
    for name in ("assets", "img", ".agents", ".claude", ".github", "scripts"):
        add_tree(archive, ROOT / name)
    archive.write(skill_zip, "downloads/muse-review-skills.zip")
print(f"Staged site: {SITE}")
print(f"Web app and skills: {bundle}")
