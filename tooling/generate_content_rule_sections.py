#!/usr/bin/env python3
"""Generate the rule section of each human content document from its YAML contract.

The YAML contract is the canonical, machine-readable source of content rules.
Each paired Markdown document shows the same rules, with their IDs, inside a
generated block. Run `generate` after changing rules and `check` in CI.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "foundations" / "content"

BEGIN = "<!-- generated:content-rules"
END = "<!-- /generated:content-rules -->"
DEFAULT_HEADING = "## قرارداد قطعی"
HEADINGS = {"product-voice.yml": "## قواعد همیشگی"}
GROUPS = (
    ("must", "### باید"),
    ("should", "### بهتر است"),
    ("must_not", "### نباید"),
)
# Retired IDs stay reserved; each points to the rule or document that owns it now.
RETIRED_HEADING = "### بازنشسته (مالک فعلی)"


def contract_paths() -> list[Path]:
    return sorted(
        [CONTENT / "product-voice.yml", CONTENT / "copy-brief.yml", CONTENT / "copy-audit.yml"]
        + list((CONTENT / "patterns").glob("*.yml"))
        + list((CONTENT / "components").glob("*.yml"))
    )


def render(yml_path: Path) -> str:
    data = yaml.safe_load(yml_path.read_text(encoding="utf-8"))
    rules = data.get("rules") or []
    lines = [
        f"{BEGIN} source={yml_path.name} -->",
        "<!-- این بخش از فایل YAML تولید می‌شود؛ دستی ویرایش نکنید. "
        "پس از تغییر قواعد اجرا کنید: python tooling/generate_content_rule_sections.py generate -->",
    ]
    for obligation, heading in GROUPS:
        group = [rule for rule in rules if rule.get("obligation") == obligation]
        if not group:
            continue
        lines += ["", heading, ""]
        for rule in group:
            statement = " ".join(str(rule["statement"]).split())
            lines.append(f"- `{rule['id']}` {statement}")
    retired = [item for item in data.get("retired_rules") or [] if isinstance(item, dict)]
    if retired:
        lines += ["", RETIRED_HEADING, ""]
        for item in retired:
            owners = "، ".join(f"`{owner}`" for owner in item.get("superseded_by") or [])
            reason = " ".join(str(item.get("reason", "")).split())
            lines.append(f"- `{item['id']}` → {owners}: {reason}")
    lines += ["", END]
    return "\n".join(lines)


def section_bounds(text: str, heading: str) -> tuple[int, int]:
    match = re.search(rf"^{re.escape(heading)}\n", text, re.M)
    if not match:
        raise ValueError(f"missing heading `{heading}`")
    start = match.end()
    following = re.search(r"^## ", text[start:], re.M)
    end = start + following.start() if following else len(text)
    return start, end


def expected_text(md_path: Path, yml_path: Path) -> str:
    text = md_path.read_text(encoding="utf-8")
    heading = HEADINGS.get(yml_path.name, DEFAULT_HEADING)
    start, end = section_bounds(text, heading)
    return text[:start] + "\n" + render(yml_path) + "\n\n" + text[end:]


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    if mode not in {"generate", "check"}:
        print("usage: generate_content_rule_sections.py [generate|check]")
        return 2
    stale: list[str] = []
    for yml_path in contract_paths():
        md_path = yml_path.with_suffix(".md")
        if not md_path.is_file():
            stale.append(f"{md_path.relative_to(ROOT)}: missing paired Markdown")
            continue
        try:
            expected = expected_text(md_path, yml_path)
        except ValueError as error:
            stale.append(f"{md_path.relative_to(ROOT)}: {error}")
            continue
        if md_path.read_text(encoding="utf-8") != expected:
            if mode == "generate":
                md_path.write_text(expected, encoding="utf-8")
                print(f"updated {md_path.relative_to(ROOT)}")
            else:
                stale.append(f"{md_path.relative_to(ROOT)}: rule section is stale")
    if stale:
        print("Content rule sections are not current:")
        for item in stale:
            print(f"- {item}")
        print("Run: python tooling/generate_content_rule_sections.py generate")
        return 1
    if mode == "check":
        print(f"Content rule sections are current for {len(contract_paths())} contracts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
