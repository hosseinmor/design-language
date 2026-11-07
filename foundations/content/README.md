# Content foundation

This directory contains reusable language decisions for JobVision and Cando:

```text
content-guidelines.md     Human entry point and routing
product-voice.*           Shared voice and machine-readable contract
localization.*            Persian, RTL, formatting, and localization rules
terminology/              Shared semantic lexicon
components/               Copy contracts for reusable UI components
patterns/                 Reusable message and interaction-language patterns
```

Semantic regression cases live under `ai/evals/content/`. Product- and
audience-specific business terminology stays in Product Knowledge; it is loaded
at use time and is not mirrored here.

## Source boundary

```text
Product Knowledge
→ What a product concept means and how it behaves

Content foundation
→ How shared interface concepts are named and communicated

Karbon / Storybook
→ Exact runtime behavior and rendered implementation
```

## Registered Product Knowledge sources

- JobVision: https://docs-jv.jvoffice.ir/
- Cando / HrCando: https://docs-cd.jvoffice.ir/

These are separate product sources. Retrieve the source for the product in scope;
do not transfer a concept, lifecycle rule, permission, or preferred product term
from one product to the other without explicit shared-source evidence.

## Product-knowledge boundary

Content owns reusable naming, writing, localization, component-copy, and
interaction-language rules. Product Knowledge owns product concepts, business
rules, lifecycle, permissions, eligibility, validation, and feature behavior.
Product Walkthrough owns observed end-to-end product flows.

A content rule may reference a product concept or preferred label, but it must
not become a second source for the concept definition, behavior, or
implementation binding. Existing product-specific definitions and code bindings
inside the terminology data are migration debt: use them as discovery evidence,
not as canonical product truth. New product-specific entries must point to the
owning Product Knowledge source instead of copying it.

## Current maturity and stewardship

The content corpus is still `draft`. Most deterministic contracts and fixtures
exist, but explicit content stewardship is not yet assigned by
`governance/ownership.md`. Do not promote a document to `reviewed`, set
`last_reviewed`, or describe the foundation as production-approved until a
named owner reviews it.

`knowledge_state: verified` means that cited evidence was checked; it does not
mean the document has completed owner review, model evaluation, product pilot,
or runtime verification.

## Quality model

The current validators check schemas, identifiers, references, rule coverage,
and fixture consistency. The semantic cases under `ai/evals/content/` are
fixtures only; they are not currently executed against an AI model. Therefore,
the repository has deterministic validation coverage but no model pass rate.

Promote a content document only after:

1. its owner and source boundary are explicit;
2. deterministic validators pass;
3. relevant semantic fixtures have been executed by a reviewed evaluator;
4. unresolved product or runtime claims remain explicit; and
5. the rule has been piloted on representative product copy.

## Rule contract schema

The YAML contract is the canonical source of every content rule; its paired
Markdown document explains the rules for people. The rule list inside each
Markdown contract section (`## قرارداد قطعی`, or `## قواعد همیشگی` in product
voice) is generated from YAML with rule IDs. Do not edit it by hand: change the
YAML contract, then run `python tooling/generate_content_rule_sections.py
generate`.

Every rule in `product-voice.yml`, `patterns/*.yml` and `components/*.yml` has:

| Field | Meaning |
|---|---|
| `id` | Stable ID with one prefix per contract, such as `ERR-001`. |
| `obligation` | `must`, `must_not` or `should`. |
| `dimension` | One value from the closed vocabulary below. |
| `key` | Stable snake_case name; not required for product-voice rules. |
| `statement` | The Persian rule text. |

`dimension` classifies what kind of failure a violation is, so evaluations and
copy audits can be aggregated across contracts:

| Dimension | Covers |
|---|---|
| `classification` | Identifying the situation, text role or component before writing. |
| `product_truth` | Claims that match verified product behavior and real system state. |
| `clarity` | Naming what happened, to what, and what it means. |
| `structure` | Distributing content across anatomy roles without repetition. |
| `action` | Action labels, available actions, safe exit and recovery. |
| `terminology` | Canonical labels for the audience and surface. |
| `tone` | Voice, register and brand expression. |
| `localization` | Numbers, dates, variables, units and bidirectional text. |
| `accessibility` | Programmatic meaning, names, relationships and announcements. |
| `disclosure` | AI involvement, provenance, limits and status of generated output. |
| `presentation` | Visual severity, hierarchy or display choice. A content rule with this dimension marks a Design System boundary to review. |
| `interaction` | Interactive behavior such as data preservation and input handling. |

## Validation

```bash
python tooling/generate_content_rule_sections.py check
python tooling/validators/check_content_contracts.py
python tooling/validators/check_content_terminology.py
python tooling/validators/check_content_localization.py
python tooling/validators/check_content_components.py
python tooling/validators/check_content_patterns.py
python tooling/generate_manifest.py check
```
