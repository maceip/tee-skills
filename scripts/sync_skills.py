#!/usr/bin/env python3
"""Keep portable Claude/Grok skill copies aligned with the canonical skills."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".agents/skills"
TARGET = ROOT / ".claude/skills"


def files(path):
    return {p.relative_to(path): p.read_bytes() for p in path.rglob("*") if p.is_file()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail on drift without writing")
    args = parser.parse_args()
    for skill in sorted(SOURCE.iterdir()):
        if not (skill / "SKILL.md").is_file():
            continue
        target = TARGET / skill.name
        if args.check:
            if files(skill) != files(target):
                raise SystemExit(f"Skill copy is stale: {target.relative_to(ROOT)}; run python3 scripts/sync_skills.py")
        else:
            # These two named destinations are generated copies, not user settings.
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(skill, target)
    print("Skill copies match." if args.check else "Updated Claude/Grok skill copies.")


if __name__ == "__main__":
    main()
