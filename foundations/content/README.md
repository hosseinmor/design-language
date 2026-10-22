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
## Validation

```bash
python tooling/validators/check_content_terminology.py
python tooling/validators/check_content_localization.py
python tooling/validators/check_content_components.py
python tooling/validators/check_content_patterns.py
python tooling/generate_manifest.py check
```
