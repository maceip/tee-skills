#!/usr/bin/env python3
"""Check publication assets and metadata without third-party dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
import json
import re
import struct
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_URL = "https://maceip.github.io/tee-skills/"


def require(condition, message):
    if not condition:
        raise SystemExit(message)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.resources = []
        self.meta = {}
        self.canonicals = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        for key in ("src", "href"):
            if attrs.get(key):
                self.resources.append(attrs[key])
        for source in attrs.get("srcset", "").split(","):
            if source.strip():
                self.resources.append(source.strip().split()[0])
        if tag == "meta":
            self.meta.setdefault(attrs.get("property", attrs.get("name")), []).append(attrs.get("content"))
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs["href"])
        if tag == "img":
            require("alt" in attrs, f"Image lacks alt: {attrs.get('src')}")
            require(attrs.get("width", "").isdigit() and attrs.get("height", "").isdigit(),
                    f"Image lacks intrinsic dimensions: {attrs.get('src')}")


def check_resource(value, base=ROOT):
    parsed = urlparse(value)
    if parsed.scheme or parsed.netloc:
        return
    require(not value.startswith("/"), f"Use a subdirectory-safe asset path: {value}")
    if parsed.path:
        target = (base / unquote(parsed.path)).resolve()
        require(target.is_relative_to(ROOT) and target.is_file(), f"Missing local resource: {value}")
    elif parsed.fragment:
        require(unquote(parsed.fragment) in page.ids, f"Broken anchor: {value}")


html = (ROOT / "index.html").read_text()
page = Page()
page.feed(html)
require(len(page.ids) == len(set(page.ids)), "Duplicate HTML IDs")
for value in page.resources:
    check_resource(value)
for value in re.findall(r"url\(['\"]?([^)'\"]+)", (ROOT / "assets/article.css").read_text()):
    check_resource(value, ROOT / "assets")
require(page.canonicals == [PUBLIC_URL], "Canonical URL differs from publication URL")
require(page.meta.get("og:url") == [PUBLIC_URL], "og:url differs from canonical")
image_url = PUBLIC_URL + "img/social-preview.png"
for key in ("og:image", "og:image:secure_url", "twitter:image"):
    require(page.meta.get(key) == [image_url], f"Unexpected {key}")
for key in ("og:title", "og:description", "og:type", "og:locale", "og:image:alt", "twitter:image:alt"):
    require(len(page.meta.get(key, [])) == 1 and page.meta[key][0], f"Missing or duplicate {key}")
require(page.meta.get("twitter:card") == ["summary_large_image"], "Wrong X card type")
png = (ROOT / "img/social-preview.png").read_bytes()
require(png[:8] == b"\x89PNG\r\n\x1a\n", "Social image is not PNG")
width, height = struct.unpack(">II", png[16:24])
require(page.meta.get("og:image:width") == [str(width)], "Wrong image width")
require(page.meta.get("og:image:height") == [str(height)], "Wrong image height")
schema = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S).group(1))
require(schema["url"] == PUBLIC_URL and schema["mainEntityOfPage"]["@id"] == PUBLIC_URL, "Wrong article identity")
require(schema["image"]["url"] == schema["image"]["contentUrl"] == image_url, "Wrong structured image URL")
require((schema["image"]["width"], schema["image"]["height"]) == (width, height), "Wrong structured image size")
for skill in (ROOT / ".agents/skills").iterdir():
    entry = skill / "SKILL.md"
    require(entry.is_file(), f"Missing skill entrypoint: {skill.name}")
    text = entry.read_text()
    require(text.startswith("---\n"), f"Missing skill frontmatter: {skill.name}")
    frontmatter = text.split("---", 2)[1]
    require(f"name: {skill.name}\n" in frontmatter and "description: " in frontmatter, f"Invalid skill identity: {skill.name}")
    for doc in skill.rglob("*.md"):
        for link in re.findall(r"\]\(([^)]+)\)", doc.read_text()):
            check_resource(link, doc.parent)
subprocess.run([sys.executable, str(ROOT / "scripts/sync_skills.py"), "--check"], check=True)
print(f"Publication checks passed: {len(page.ids)} IDs, {len(page.resources)} resource/link references, metadata, image dimensions, skills.")
