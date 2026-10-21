#!/usr/bin/env python3
"""Generate and validate the lightweight AI retrieval manifest."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required. Run: python -m pip install -r requirements-dev.txt"
    ) from exc

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "registry" / "manifest.generated.json"
GRAPH_PATH = ROOT / "registry" / "graph.generated.json"
ALIASES_PATH = ROOT / "registry" / "aliases.yaml"
INDEX_ROOTS = (
    ROOT / "overview",
    ROOT / "foundations",
    ROOT / "accessibility",
    ROOT / "design-system",
    ROOT / "product-expression",
    ROOT / "playbooks",
    ROOT / "integrations",
    ROOT / "governance",
    ROOT / "ai",
)
EXCLUDED_FILENAMES = {"README.md"}
EXCLUDED_DIRECTORIES = {"document-templates", "evals"}
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
SLUG_RE = re.compile(r"[^a-z0-9]+")
VALID_STATUS = {"draft", "reviewed"}
GROUP_KINDS = {"product-group-overview"}
PRODUCT_KINDS = {"product-overview", "product-area", "product-area-flow"}
DESIGN_SYSTEM_TEAM = "Design System team"


@dataclass(frozen=True)
class Finding:
    path: str
    message: str

    def render(self) -> str:
        return f"ERROR {self.path}: {self.message}"


@dataclass
class Document:
    path: Path
    relative_path: str
    metadata: dict[str, Any] | None
    body: str
    parse_error: str | None = None


def iter_markdown() -> Iterable[Path]:
    found: set[Path] = set()
    for root in INDEX_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            if path.name in EXCLUDED_FILENAMES:
                continue
            if any(part in EXCLUDED_DIRECTORIES for part in path.relative_to(ROOT).parts):
                continue
            found.add(path)
    yield from sorted(found, key=lambda item: item.as_posix())


def parse_document(path: Path) -> Document:
    raw = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT).as_posix()
    match = FRONTMATTER_RE.match(raw)
    if not match:
        return Document(path, relative, None, raw)

    try:
        loaded = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return Document(path, relative, None, raw[match.end() :], str(exc))

    if loaded is None:
        loaded = {}
    if not isinstance(loaded, dict):
        return Document(
            path,
            relative,
            None,
            raw[match.end() :],
            "Frontmatter must be a YAML mapping.",
        )
    return Document(path, relative, loaded, raw[match.end() :])


def scan_documents() -> list[Document]:
    return [parse_document(path) for path in iter_markdown()]


def slugify(value: str) -> str:
    return SLUG_RE.sub("-", value.lower()).strip("-")


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def as_string_list(value: Any) -> list[str]:
    if value in (None, ""):
        return []
    if not isinstance(value, list):
        raise ValueError("must be a list")
    result: list[str] = []
    for item in value:
        if not nonempty_string(item):
            raise ValueError("must contain only non-empty strings")
        result.append(item.strip())
    return result


def infer_group(path: str, metadata: dict[str, Any]) -> str | None:
    if nonempty_string(metadata.get("group")):
        return str(metadata["group"]).strip()
    parts = Path(path).parts
    return None


def infer_product(path: str, metadata: dict[str, Any]) -> str | None:
    if nonempty_string(metadata.get("product")):
        return str(metadata["product"]).strip()
    parts = Path(path).parts
    return None


def infer_owner(path: str, metadata: dict[str, Any]) -> str | None:
    """Resolve stewardship independently of review and implementation maturity.

    Explicit ownership wins; shared Design Language documents inherit
    maintaining stewardship even while draft or scaffold, not content approval.
    """
    if nonempty_string(metadata.get("owner")):
        return str(metadata["owner"]).strip()

    parts = Path(path).parts
    if parts and parts[0] == "accessibility":
        return DESIGN_SYSTEM_TEAM

    # Stewardship is not review approval, design maturity or code shipment.
    if metadata.get("collection") in {"design-system", "design-language"}:
        return DESIGN_SYSTEM_TEAM

    return None


def infer_kind(path: str, metadata: dict[str, Any]) -> str:
    if nonempty_string(metadata.get("kind")):
        return str(metadata["kind"]).strip()

    collection = metadata.get("collection")
    doc_type = metadata.get("type")
    if nonempty_string(collection) and nonempty_string(doc_type):
        return f"{slugify(str(collection))}-{slugify(str(doc_type))}"
    if nonempty_string(doc_type):
        return slugify(str(doc_type))
    parts = Path(path).parts
    if parts:
        return f"{slugify(parts[0])}-guidance"
    raise ValueError("path is outside the supported manifest structure")


def infer_status(metadata: dict[str, Any]) -> str:
    explicit = metadata.get("status")
    if nonempty_string(explicit) and str(explicit).lower() in VALID_STATUS:
        return str(explicit).lower()

    design_status = str(metadata.get("design_status", "")).lower()
    if design_status in {"reviewed", "stable", "approved", "active"}:
        return "reviewed"
    if design_status:
        return "draft"

    maturity = str(metadata.get("document_maturity", "")).lower()
    knowledge_state = str(metadata.get("knowledge_state", "")).lower()
    if maturity in {"reviewed", "stable"} and knowledge_state == "canonical":
        return "reviewed"
    return "draft"


def normalize_date(value: Any) -> str | None:
    if value in (None, ""):
        return None
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str):
        try:
            return date.fromisoformat(value).isoformat()
        except ValueError as exc:
            raise ValueError("must use YYYY-MM-DD") from exc
    raise ValueError("must use YYYY-MM-DD")


def derive_topics(path: str, metadata: dict[str, Any], kind: str) -> list[str]:
    topics: set[str] = set()
    for field in ("topics", "tags"):
        value = metadata.get(field)
        if value not in (None, ""):
            topics.update(as_string_list(value))

    parts = Path(path).parts
    ignored_parts = {
        "overview",
        "foundations",
        "design-system",
        "product-expression",
        "playbooks",
        "integrations",
        "governance",
        "accessibility",
        "ai",
    }
    for part in parts[:-1]:
        if part not in ignored_parts:
            topics.add(part)
    stem = Path(path).stem
    if stem not in {"overview", "STRUCTURE"}:
        topics.add(stem)
    topics.add(kind)
    return sorted(topics)


def normalize_document(doc: Document) -> tuple[dict[str, Any] | None, list[Finding]]:
    findings: list[Finding] = []
    if doc.parse_error:
        return None, [Finding(doc.relative_path, f"Invalid YAML frontmatter: {doc.parse_error}")]
    if doc.metadata is None:
        return None, [Finding(doc.relative_path, "Missing YAML frontmatter.")]

    metadata = doc.metadata
    for field in ("id", "title", "summary"):
        if not nonempty_string(metadata.get(field)):
            findings.append(Finding(doc.relative_path, f"Missing non-empty `{field}`."))

    if findings:
        return None, findings

    try:
        kind = infer_kind(doc.relative_path, metadata)
    except ValueError as exc:
        findings.append(Finding(doc.relative_path, str(exc)))
        return None, findings

    group = infer_group(doc.relative_path, metadata)
    product = infer_product(doc.relative_path, metadata)

    if kind in GROUP_KINDS and not group:
        findings.append(Finding(doc.relative_path, "Product Group documents require `group`."))
    if kind in PRODUCT_KINDS:
        if not group:
            findings.append(Finding(doc.relative_path, "Product documents require `group`."))
        if not product:
            findings.append(Finding(doc.relative_path, "Product documents require `product`."))

    try:
        related = as_string_list(metadata.get("related", []))
        topics = derive_topics(doc.relative_path, metadata, kind)
        last_reviewed = normalize_date(
            metadata.get("last_reviewed", metadata.get("last_verified"))
        )
    except ValueError as exc:
        findings.append(Finding(doc.relative_path, str(exc)))
        return None, findings

    status = infer_status(metadata)
    if status not in VALID_STATUS:
        findings.append(Finding(doc.relative_path, "Status must be `draft` or `reviewed`."))

    entry: dict[str, Any] = {
        "id": str(metadata["id"]).strip(),
        "kind": kind,
        "title": str(metadata["title"]).strip(),
        "summary": " ".join(str(metadata["summary"]).split()),
        "status": status,
        "owner": infer_owner(doc.relative_path, metadata),
        "last_reviewed": last_reviewed,
        "related": related,
        "topics": topics,
        "path": doc.relative_path,
    }
    if group:
        entry["group"] = group
    if product:
        entry["product"] = product

    return entry, findings


def build_manifest(documents: list[Document]) -> tuple[dict[str, Any], list[Finding]]:
    entries: list[dict[str, Any]] = []
    findings: list[Finding] = []
    ids: dict[str, str] = {}

    for doc in documents:
        entry, document_findings = normalize_document(doc)
        findings.extend(document_findings)
        if entry is None:
            continue
        doc_id = entry["id"]
        if doc_id in ids:
            findings.append(
                Finding(doc.relative_path, f"Duplicate ID `{doc_id}` also used by {ids[doc_id]}.")
            )
        else:
            ids[doc_id] = doc.relative_path
        entries.append(entry)

    for entry in entries:
        for related_id in entry["related"]:
            if related_id == entry["id"]:
                findings.append(Finding(entry["path"], "A document cannot relate to itself."))
            elif related_id not in ids:
                findings.append(
                    Finding(entry["path"], f"Related ID `{related_id}` does not exist.")
                )

    entries.sort(key=lambda item: item["id"])
    by_kind = Counter(entry["kind"] for entry in entries)
    by_group = Counter(entry["group"] for entry in entries if "group" in entry)
    by_product = Counter(
        f"{entry['group']}/{entry['product']}"
        for entry in entries
        if "group" in entry and "product" in entry
    )

    manifest = {
        "schema_version": 1,
        "documents": entries,
        "summary": {
            "documents": len(entries),
            "by_kind": dict(sorted(by_kind.items())),
            "by_group": dict(sorted(by_group.items())),
            "by_product": dict(sorted(by_product.items())),
        },
    }
    return manifest, findings


def serialized_manifest(manifest: dict[str, Any]) -> str:
    return json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"


def load_aliases(document_ids: set[str]) -> tuple[dict[str, str], list[Finding]]:
    findings: list[Finding] = []
    if not ALIASES_PATH.exists():
        return {}, [Finding("registry/aliases.yaml", "Alias registry is missing.")]
    try:
        data = yaml.safe_load(ALIASES_PATH.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        return {}, [Finding("registry/aliases.yaml", f"Invalid YAML: {exc}")]
    aliases = data.get("aliases", {})
    if not isinstance(aliases, dict):
        return {}, [Finding("registry/aliases.yaml", "`aliases` must be a mapping.")]
    normalized: dict[str, str] = {}
    for alias, target in aliases.items():
        if not nonempty_string(alias) or not nonempty_string(target):
            findings.append(Finding("registry/aliases.yaml", "Aliases and targets must be non-empty strings."))
            continue
        alias_text = str(alias).strip()
        target_text = str(target).strip()
        if alias_text in document_ids:
            findings.append(Finding("registry/aliases.yaml", f"Alias `{alias_text}` conflicts with a document ID."))
        if target_text not in document_ids:
            findings.append(Finding("registry/aliases.yaml", f"Alias `{alias_text}` points to missing ID `{target_text}`."))
        normalized[alias_text] = target_text
    return dict(sorted(normalized.items())), findings


def enrich_manifest(manifest: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], list[Finding]]:
    ids = {entry["id"] for entry in manifest["documents"]}
    aliases, findings = load_aliases(ids)
    manifest["aliases"] = aliases
    edges = sorted(
        (
            {"from": entry["id"], "to": related_id, "type": "related"}
            for entry in manifest["documents"]
            for related_id in entry["related"]
        ),
        key=lambda edge: (edge["from"], edge["to"]),
    )
    graph = {
        "schema_version": 1,
        "nodes": sorted(ids),
        "edges": edges,
    }
    return manifest, graph, findings


def print_findings(findings: list[Finding]) -> None:
    for finding in sorted(findings, key=lambda item: (item.path, item.message)):
        print(finding.render())
    if findings:
        print(f"\n{len(findings)} error(s)")


def command_generate(_: argparse.Namespace) -> int:
    manifest, findings = build_manifest(scan_documents())
    manifest, graph, alias_findings = enrich_manifest(manifest)
    findings.extend(alias_findings)
    if findings:
        print_findings(findings)
        return 1
    MANIFEST_PATH.write_text(serialized_manifest(manifest), encoding="utf-8")
    GRAPH_PATH.write_text(serialized_manifest(graph), encoding="utf-8")
    print(
        f"Generated {MANIFEST_PATH.relative_to(ROOT)} and {GRAPH_PATH.relative_to(ROOT)} "
        f"with {manifest['summary']['documents']} documents."
    )
    return 0


def command_check(_: argparse.Namespace) -> int:
    manifest, findings = build_manifest(scan_documents())
    manifest, graph, alias_findings = enrich_manifest(manifest)
    findings.extend(alias_findings)
    if findings:
        print_findings(findings)
        return 1
    expected = serialized_manifest(manifest)
    expected_graph = serialized_manifest(graph)
    if not MANIFEST_PATH.exists():
        print("ERROR registry/manifest.generated.json: file is missing. Run `python tooling/generate_manifest.py generate`.")
        return 1
    actual = MANIFEST_PATH.read_text(encoding="utf-8")
    if actual != expected:
        print("ERROR registry/manifest.generated.json: file is stale. Run `python tooling/generate_manifest.py generate`.")
        return 1
    if not GRAPH_PATH.exists():
        print("ERROR registry/graph.generated.json: file is missing. Run `python tooling/generate_manifest.py generate`.")
        return 1
    if GRAPH_PATH.read_text(encoding="utf-8") != expected_graph:
        print("ERROR registry/graph.generated.json: file is stale. Run `python tooling/generate_manifest.py generate`.")
        return 1
    print(f"Manifest and graph are current with {manifest['summary']['documents']} documents.")
    return 0


def command_report(_: argparse.Namespace) -> int:
    manifest, findings = build_manifest(scan_documents())
    print(json.dumps(manifest["summary"], ensure_ascii=False, indent=2))
    if findings:
        print_findings(findings)
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("generate").set_defaults(handler=command_generate)
    subparsers.add_parser("check").set_defaults(handler=command_check)
    subparsers.add_parser("report").set_defaults(handler=command_report)
    args = parser.parse_args()
    return args.handler(args)


if __name__ == "__main__":
    sys.exit(main())
