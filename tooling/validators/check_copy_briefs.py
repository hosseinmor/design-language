#!/usr/bin/env python3
"""Validate copy briefs in generation eval fixtures against the copy-brief contract.

A brief may only reference what Design Language already owns: a content
contract and its anatomy, terminology entries and registered sources. The
validator also checks that each case's expectations are consistent with its
brief and that every blocking `BRF` rule is covered by at least one case.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tooling.content_rule_index import (  # noqa: E402
    active_rule_ids,
    contracts_by_id,
    inherited_rule_ids,
)

BRIEF_CONTRACT = ROOT / "foundations" / "content" / "copy-brief.yml"
TERMS = ROOT / "foundations" / "content" / "terminology" / "terms.yml"
GENERATION_DIR = ROOT / "ai" / "evals" / "content" / "generation"

ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")
AUDIENCE_KINDS = {"role", "persona", "internal_role"}
FACT_STATUSES = ("unknown", "draft", "verified")
FIXTURE_SOURCE = "eval_fixture"
OUTCOMES = {"copy", "blocked"}
BRIEF_KEYS = {
    "id", "product", "audience", "surface", "contract", "states",
    "concepts", "product_facts", "context", "constraints",
}
EXPECTED_KEYS = {
    "outcome", "checked_rules", "required_slots", "empty_slots",
    "required_questions", "draft_dependencies", "must_use_labels",
    "forbidden_labels",
}


def load(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def _labels(value: Any) -> set[str]:
    if isinstance(value, str):
        return {value}
    if isinstance(value, dict):
        return {s for item in value.values() for s in _labels(item)}
    if isinstance(value, list):
        out: set[str] = set()
        for item in value:
            out |= _labels(item.get("label") if isinstance(item, dict) else item)
        return out
    return set()


def anatomy_roles(anatomy: Any) -> tuple[set[str], set[str]]:
    """Return (all roles, required roles) named under required/conditional/sequence keys."""
    roles: set[str] = set()
    required: set[str] = set()

    def walk(node: Any) -> None:
        if not isinstance(node, dict):
            return
        for key, value in node.items():
            if isinstance(value, list) and key.startswith(("required", "conditional", "sequence")):
                names = {v for v in value if isinstance(v, str)}
                roles.update(names)
                if key == "required":
                    required.update(names)
            else:
                walk(value)

    walk(anatomy)
    return roles, required


@dataclass
class Context:
    terms: dict[str, dict[str, Any]]
    visibility: set[str]
    sources: dict[str, str]
    contracts: dict[str, dict[str, Any]]
    layers: dict[str, dict[str, Any]]
    brief_rules: dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_repository(cls) -> "Context":
        terms_data = load(TERMS)
        terms = {t["id"]: t for t in terms_data.get("terms") or [] if isinstance(t, dict)}
        contract = load(BRIEF_CONTRACT)
        return cls(
            terms=terms,
            visibility={v for t in terms.values() for v in t.get("visibility") or []},
            sources={
                s["id"]: s.get("state", "")
                for s in terms_data.get("sources") or []
                if isinstance(s, dict) and "id" in s
            },
            contracts=contracts_by_id(),
            layers=contract.get("product_layers") or {},
            brief_rules={
                r["id"]: r["obligation"]
                for r in contract.get("rules") or []
                if isinstance(r, dict) and "id" in r
            },
        )

    def forbidden(self, term_id: str) -> set[str]:
        term = self.terms.get(term_id, {})
        return _labels(term.get("forbidden")) | _labels(term.get("legacy_labels"))

    def preferred(self, term_id: str) -> set[str]:
        term = self.terms.get(term_id, {})
        return _labels(term.get("preferred")) | _labels(term.get("allowed"))


def _string_list(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(v, str) and v.strip() for v in value)


def validate_brief(brief: Any, ctx: Context, where: str, allow_fixture_source: bool) -> list[str]:
    if not isinstance(brief, dict):
        return [f"{where}: brief must be a mapping"]
    errors: list[str] = []
    if unknown := sorted(set(brief) - BRIEF_KEYS):
        errors.append(f"{where}: unknown brief keys {unknown}")
    for key in ("id", "product", "audience", "surface", "contract", "states"):
        if key not in brief:
            errors.append(f"{where}: missing `{key}`")
    if "id" in brief and not (isinstance(brief["id"], str) and ID_RE.fullmatch(brief["id"])):
        errors.append(f"{where}: id must be snake_case")
    if "product" in brief and brief["product"] not in ctx.layers:
        errors.append(f"{where}: product `{brief['product']}` is not a product layer")

    audience = brief.get("audience")
    if "audience" in brief:
        if not _string_list(audience) or not audience:
            errors.append(f"{where}: audience must be a non-empty list of term ids")
        else:
            for item in audience:
                kind = ctx.terms.get(item, {}).get("concept_kind")
                if kind not in AUDIENCE_KINDS:
                    errors.append(f"{where}: audience `{item}` is not a role, persona or internal_role term")
    if "surface" in brief and brief["surface"] not in ctx.visibility:
        errors.append(f"{where}: surface `{brief['surface']}` is not a terminology visibility value")

    contract_id = brief.get("contract")
    contract = ctx.contracts.get(contract_id) if isinstance(contract_id, str) else None
    if "contract" in brief and (
        contract is None or not contract_id.startswith(("content.pattern.", "content.component."))
    ):
        errors.append(f"{where}: contract `{contract_id}` is not a content pattern or component")
        contract = None
    roles, required = anatomy_roles(contract.get("anatomy")) if contract else (set(), set())

    states = brief.get("states")
    if "states" in brief:
        if not isinstance(states, list) or not states:
            errors.append(f"{where}: states must be a non-empty list")
            states = []
        seen: set[str] = set()
        for index, state in enumerate(states):
            at = f"{where}: states[{index}]"
            if not isinstance(state, dict) or not isinstance(state.get("id"), str):
                errors.append(f"{at}: must be a mapping with an id")
                continue
            if state["id"] in seen:
                errors.append(f"{at}: duplicate state `{state['id']}`")
            seen.add(state["id"])
            slots = state.get("slots")
            if not _string_list(slots) or not slots:
                errors.append(f"{at}: slots must be a non-empty string list")
                continue
            if roles:
                if bad := sorted(set(slots) - roles):
                    errors.append(f"{at}: slots {bad} are not anatomy roles of `{contract_id}`")
                if missing := sorted(required - set(slots)):
                    errors.append(f"{at}: required anatomy roles {missing} are missing")
            elif bad := sorted(s for s in slots if not ID_RE.fullmatch(s)):
                errors.append(f"{at}: slots {bad} must be snake_case")

    concepts = brief.get("concepts", [])
    if not isinstance(concepts, list):
        errors.append(f"{where}: concepts must be a list")
        concepts = []
    seen_concepts: set[str] = set()
    for index, item in enumerate(concepts):
        at = f"{where}: concepts[{index}]"
        errors += [f"{at}: {e}" for e in concept_errors(item, brief.get("product"), ctx)]
        cid = concept_id(item)
        if cid in seen_concepts:
            errors.append(f"{at}: duplicate concept `{cid}`")
        seen_concepts.add(cid)

    facts = brief.get("product_facts", [])
    if not isinstance(facts, list):
        errors.append(f"{where}: product_facts must be a list")
        facts = []
    fact_ids: set[str] = set()
    for index, fact in enumerate(facts):
        at = f"{where}: product_facts[{index}]"
        if not isinstance(fact, dict):
            errors.append(f"{at}: must be a mapping")
            continue
        fid = fact.get("id")
        if not (isinstance(fid, str) and ID_RE.fullmatch(fid)) or fid in fact_ids:
            errors.append(f"{at}: id must be unique snake_case")
        fact_ids.add(fid)
        if not (isinstance(fact.get("statement"), str) and fact["statement"].strip()):
            errors.append(f"{at}: missing statement")
        status = fact.get("status")
        if status not in FACT_STATUSES:
            errors.append(f"{at}: status must be one of {list(FACT_STATUSES)}")
            continue
        source = fact.get("source")
        if status == "unknown":
            if source is not None:
                errors.append(f"{at}: unknown fact must not cite a source")
            if not (isinstance(fact.get("question"), str) and fact["question"].strip()):
                errors.append(f"{at}: unknown fact requires a question")
            continue
        if source == FIXTURE_SOURCE:
            if not allow_fixture_source:
                errors.append(f"{at}: `{FIXTURE_SOURCE}` is only allowed in eval fixtures")
            continue
        state, source_errors = source_maturity(source, brief.get("product"), ctx)
        errors += [f"{at}: {e}" for e in source_errors]
        if state is None:
            if not source_errors:
                errors.append(f"{at}: source `{source}` is not a registered terminology source")
            continue
        if status == "verified" and state != "verified":
            errors.append(f"{at}: status `verified` exceeds source maturity `{state}`")
    return errors


def concept_id(item: Any) -> str:
    if isinstance(item, dict):
        return str(item.get("page") if item.get("kind") == "product_knowledge" else item.get("id"))
    return str(item)


def concept_errors(item: Any, product: Any, ctx: Context) -> list[str]:
    if isinstance(item, str):
        return [] if item in ctx.terms else [f"concept `{item}` is not a terminology entry"]
    if not isinstance(item, dict):
        return ["concept must be a term id or a mapping"]
    kind = item.get("kind")
    if kind == "product_knowledge":
        errors = [
            f"product_knowledge concept needs `{key}`"
            for key in ("product", "page", "label")
            if not (isinstance(item.get(key), str) and item[key].strip())
        ]
        if item.get("product") and item["product"] != product:
            errors.append(f"concept from `{item['product']}` Product Knowledge cannot label a `{product}` brief")
        return errors
    if kind == "new_concept":
        errors = [] if isinstance(item.get("id"), str) and ID_RE.fullmatch(item["id"]) else ["new_concept needs a snake_case id"]
        if item.get("id") in ctx.terms:
            errors.append(f"new_concept `{item['id']}` already has a terminology entry")
        source = item.get("source")
        if not (isinstance(source, dict) and source.get("kind") == "prd"):
            errors.append("new_concept source must be a prd reference")
        else:
            errors += source_maturity(source, product, ctx)[1]
        return errors
    return [f"unknown concept kind `{kind}`"]


def source_maturity(source: Any, product: Any, ctx: Context) -> tuple[str | None, list[str]]:
    """Return the highest fact status a source supports, plus shape errors."""
    if isinstance(source, str):
        return ctx.sources.get(source), []
    if not isinstance(source, dict):
        return None, ["source must be a registered id or a mapping"]
    kind = source.get("kind")
    if kind == "product_knowledge":
        errors = [
            f"product_knowledge source needs `{key}`"
            for key in ("product", "page", "state")
            if not (isinstance(source.get(key), str) and source[key].strip())
        ]
        if source.get("product") and source.get("product") != product:
            errors.append(
                f"product_knowledge source of `{source.get('product')}` cannot support a `{product}` brief"
            )
        if source.get("state") not in {"verified", "draft"}:
            errors.append("product_knowledge source state must be verified or draft")
        return (None if errors else source["state"]), errors
    if kind == "prd":
        errors = []
        if not (isinstance(source.get("ref"), str) and source["ref"].strip()):
            errors.append("prd source needs `ref`")
        if source.get("decision") not in {"accepted", "proposed"}:
            errors.append("prd source decision must be accepted or proposed")
        return (None if errors else ("verified" if source["decision"] == "accepted" else "draft")), errors
    return None, [f"unknown source kind `{kind}`"]


def validate_case(case: Any, ctx: Context, where: str) -> tuple[list[str], set[str]]:
    if not isinstance(case, dict) or not isinstance(case.get("id"), str):
        return [f"{where}: case must be a mapping with an id"], set()
    where = f"{where} `{case['id']}`"
    brief = case.get("brief")
    errors = validate_brief(brief, ctx, where, allow_fixture_source=True)
    expected = case.get("expected")
    if not isinstance(expected, dict) or not isinstance(brief, dict):
        return errors + [f"{where}: expected must be a mapping"], set()
    if unknown := sorted(set(expected) - EXPECTED_KEYS):
        errors.append(f"{where}: unknown expected keys {unknown}")

    layer = ctx.layers.get(brief.get("product"), {})
    should_block = layer.get("status") != "available"
    outcome = expected.get("outcome")
    if outcome not in OUTCOMES:
        errors.append(f"{where}: outcome must be one of {sorted(OUTCOMES)}")
    elif (outcome == "blocked") != should_block:
        errors.append(f"{where}: outcome `{outcome}` contradicts product layer status")

    checked = expected.get("checked_rules")
    contract_id = brief.get("contract", "")
    known = set(ctx.brief_rules) | inherited_rule_ids(contract_id)
    if contract_id in ctx.contracts:
        known |= active_rule_ids(ctx.contracts[contract_id])
    if not _string_list(checked) or not checked:
        errors.append(f"{where}: checked_rules must be a non-empty list")
        checked = []
    elif bad := sorted(set(checked) - known):
        errors.append(f"{where}: checked_rules {bad} are not BRF rules or rules of `{contract_id}`")

    state_slots = {
        s["id"]: set(s.get("slots") or [])
        for s in brief.get("states") or []
        if isinstance(s, dict) and isinstance(s.get("id"), str)
    }
    for key in ("required_slots", "empty_slots"):
        value = expected.get(key, {})
        if not isinstance(value, dict):
            errors.append(f"{where}: {key} must map state to slots")
            continue
        if value and outcome == "blocked":
            errors.append(f"{where}: blocked case must not expect {key}")
        for state, slots in value.items():
            if state not in state_slots or not _string_list(slots) or set(slots) - state_slots[state]:
                errors.append(f"{where}: {key}.{state} must name slots of that brief state")
    required, empty = expected.get("required_slots") or {}, expected.get("empty_slots") or {}
    if isinstance(required, dict) and isinstance(empty, dict):
        for state in set(required) & set(empty):
            if set(required[state]) & set(empty[state]):
                errors.append(f"{where}: a slot cannot be both required and empty in `{state}`")

    facts = [f for f in brief.get("product_facts") or [] if isinstance(f, dict)]
    new_concepts = {
        concept_id(c) for c in brief.get("concepts") or []
        if isinstance(c, dict) and c.get("kind") == "new_concept"
    }
    for key, status in (("required_questions", "unknown"), ("draft_dependencies", "draft")):
        listed = expected.get(key, [])
        wanted = {f.get("id") for f in facts if f.get("status") == status}
        if key == "draft_dependencies":
            wanted |= new_concepts
        if outcome == "blocked":
            wanted = set()
        if not _string_list(listed) or set(listed) != wanted:
            errors.append(f"{where}: {key} must list exactly {sorted(wanted)}")

    by_id = {concept_id(c): c for c in brief.get("concepts") or []}
    concepts = set(by_id)

    def preferred(cid: str) -> set[str]:
        item = by_id.get(cid)
        if isinstance(item, dict):
            return {item["label"]} if item.get("kind") == "product_knowledge" and item.get("label") else set()
        return ctx.preferred(cid)

    def forbidden(cid: str) -> set[str]:
        return ctx.forbidden(cid) if isinstance(by_id.get(cid), str) else set()

    must_use: list[str] = []
    for key, allowed in (("must_use_labels", preferred), ("forbidden_labels", forbidden)):
        items = expected.get(key, [])
        if not isinstance(items, list):
            errors.append(f"{where}: {key} must be a list")
            continue
        for item in items:
            if not isinstance(item, dict) or item.get("concept") not in concepts:
                errors.append(f"{where}: {key} item must name a concept of the brief")
                continue
            if item.get("label") not in allowed(item["concept"]):
                errors.append(
                    f"{where}: {key} `{item.get('label')}` is not a terminology "
                    f"{'preferred' if key == 'must_use_labels' else 'forbidden'} label of `{item['concept']}`"
                )
            elif key == "must_use_labels":
                must_use.append(item["label"])
    for item in expected.get("forbidden_labels") or []:
        if isinstance(item, dict) and any(item.get("label", "") in label for label in must_use):
            errors.append(f"{where}: forbidden label `{item.get('label')}` occurs inside a required label")
    return errors, set(checked)


def validate_fixture(path: Path, ctx: Context) -> tuple[list[str], set[str]]:
    data = load(path)
    label = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
    errors: list[str] = []
    for key in ("schema_version", "id", "foundation_id", "language"):
        if not isinstance(data.get(key), str):
            errors.append(f"{label}: missing `{key}`")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + [f"{label}: cases must be a non-empty list"], set()
    covered: set[str] = set()
    seen: set[str] = set()
    for index, case in enumerate(cases):
        case_errors, checked = validate_case(case, ctx, f"{label}: cases[{index}]")
        errors.extend(case_errors)
        covered |= checked
        case_id = case.get("id") if isinstance(case, dict) else None
        if case_id in seen:
            errors.append(f"{label}: duplicate case id `{case_id}`")
        seen.add(case_id)
    return errors, covered


def main() -> int:
    ctx = Context.from_repository()
    errors: list[str] = []
    if ctx.layers.keys() and not any(v.get("status") == "available" for v in ctx.layers.values()):
        errors.append("copy-brief.yml: at least one product layer must be available")
    for name, layer in ctx.layers.items():
        if layer.get("status") == "available" and layer.get("verbal_identity") not in ctx.contracts:
            errors.append(f"copy-brief.yml: product layer `{name}` must name an existing voice contract")
        if layer.get("status") not in {"available", "missing"}:
            errors.append(f"copy-brief.yml: product layer `{name}` status must be available or missing")
    paths = sorted(GENERATION_DIR.glob("*-cases.yml"))
    if not paths:
        errors.append(f"{GENERATION_DIR.relative_to(ROOT)}: no generation fixtures")
    covered: set[str] = set()
    cases = 0
    for path in paths:
        fixture_errors, fixture_covered = validate_fixture(path, ctx)
        errors.extend(fixture_errors)
        covered |= fixture_covered
        cases += len(load(path).get("cases") or [])
    blocking = {rid for rid, ob in ctx.brief_rules.items() if ob in {"must", "must_not"}}
    if missing := sorted(blocking - covered):
        errors.append(f"generation fixtures do not cover blocking rules: {', '.join(missing)}")
    if errors:
        print("Copy brief validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        f"Copy briefs are valid: {cases} generation cases, "
        f"{len(blocking)} blocking BRF rules covered."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
