"""Offline integrity checks for the public profile."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SOURCES = ROOT / "docs" / "SOURCES.md"
PUBLISH_WORKFLOW = ROOT / ".github" / "workflows" / "publish.yml"

REQUIRED_README_MARKERS = (
    "# Francisco Angulo de Lafuente",
    "## Public research and engineering record",
    "## Literary work",
    "## Contest and award claims",
    "## Evidence policy",
    "## Development",
)

UNSUPPORTED_PROMOTIONAL_PHRASES = (
    "world's most advanced",
    "next giant",
    "revolutionary breakthrough",
    "official winner",
    "first ever",
)


def validate() -> list[str]:
    errors: list[str] = []
    readme = README.read_text(encoding="utf-8")
    sources = SOURCES.read_text(encoding="utf-8")
    publish_workflow = PUBLISH_WORKFLOW.read_text(encoding="utf-8")

    for marker in REQUIRED_README_MARKERS:
        if marker not in readme:
            errors.append(f"README is missing required section: {marker}")

    links = re.findall(r"\[[^\]]+\]\((https?://[^)]+)\)", readme)
    if len(links) < 10:
        errors.append("README must retain at least ten explicit public source links")
    if any(url.startswith("http://") for url in links):
        errors.append("README contains an insecure HTTP source link")

    for phrase in UNSUPPORTED_PROMOTIONAL_PHRASES:
        if phrase in readme.lower():
            errors.append(f"README contains unsupported promotional phrase: {phrase}")

    if "r2cdn.perplexity.ai" in readme.lower():
        errors.append("README must not depend on an embedded third-party branding asset")
    if "## Maintenance rules" not in sources:
        errors.append("Source ledger is missing its maintenance rules")
    if "sha256sum francisco-angulo-de-lafuente-*" not in publish_workflow:
        errors.append("Release workflow must hash only the two source archives")
    if "sha256sum *)" in publish_workflow:
        errors.append("Release workflow must not hash an unconstrained directory glob")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    url_count = len(re.findall(r"https?://", README.read_text(encoding="utf-8")))
    print(f"Profile validation passed: {README.name}, {url_count} URLs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
