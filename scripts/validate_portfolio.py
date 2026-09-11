from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml
except ImportError:
    print("Install PyYAML with: python -m pip install pyyaml")
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "_data"
PROJECTS = ROOT / "projects"

YAML_FILES = [
    DATA / "profile.yml",
    DATA / "experience.yml",
    DATA / "education.yml",
    DATA / "coursework.yml",
    DATA / "projects.yml",
    DATA / "skills.yml",
]


def load_yaml(path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


errors = []

# YAML parsing
for path in YAML_FILES:
    if not path.exists():
        errors.append(f"Missing: {path.relative_to(ROOT)}")
        continue

    try:
        load_yaml(path)
    except Exception as exc:
        errors.append(f"YAML error in {path.relative_to(ROOT)}: {exc}")


# Project metadata / assets
projects_file = DATA / "projects.yml"

if projects_file.exists():
    projects = load_yaml(projects_file) or []
    seen_slugs = set()

    for project in projects:
        slug = project.get("slug")
        title = project.get("title", slug)

        if not slug:
            errors.append(f"Project missing slug: {title}")
            continue

        if slug in seen_slugs:
            errors.append(f"Duplicate project slug: {slug}")

        seen_slugs.add(slug)

        page = PROJECTS / f"{slug}.md"
        if not page.exists():
            errors.append(f"Missing project page: {page.relative_to(ROOT)}")

        image = project.get("image")
        if image:
            target = ROOT / unquote(image).lstrip("/")
            if not target.exists():
                errors.append(f"Missing image for {title}: {image}")

        for document in project.get("documents") or []:
            url = document.get("url")
            if url:
                target = ROOT / unquote(url).lstrip("/")
                if not target.exists():
                    errors.append(
                        f"Missing document for {title}: {url}"
                    )


# Liquid include targets
include_pattern = re.compile(r"{%\s*include\s+([^\s%]+)")

scan = (
    list(ROOT.glob("*.md"))
    + list((ROOT / "_layouts").glob("*.html"))
    + list((ROOT / "_includes").glob("*.html"))
    + list(PROJECTS.glob("*.md"))
)

for path in scan:
    text = path.read_text(encoding="utf-8")

    for include in include_pattern.findall(text):
        target = ROOT / "_includes" / include
        if not target.exists():
            errors.append(
                f"Missing include {include} referenced by "
                f"{path.relative_to(ROOT)}"
            )


# Old username / debug text
for path in ROOT.rglob("*"):
    if not path.is_file():
        continue

    if ".git" in path.parts or "scripts" in path.parts:
        continue

    if path.suffix.lower() not in {
        ".md", ".html", ".yml", ".yaml", ".css", ".py"
    }:
        continue

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue

    if "kyledavid36" in text:
        errors.append(
            f"Old GitHub username found in {path.relative_to(ROOT)}"
        )

    if "Trigger GitHub Pages deployment" in text:
        errors.append(
            f"Deployment debug text found in {path.relative_to(ROOT)}"
        )


if errors:
    print("\nPortfolio validation FAILED:\n")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("Portfolio static validation PASSED.")
print(
    "Checked YAML, project pages/assets, include targets, "
    "legacy username references and deployment debug text."
)