---
id: design-system.overview
collection: design-system
type: overview
title: Design Language Scope
summary: Defines the purpose, scope, boundaries, and operating model of the shared JobVision and Cando Design Language.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.design-language
  - design-system.structure
  - design-system.reference.source-of-truth
---

# Design Language Scope

## Purpose

The shared Design Language gives JobVision and Cando a common visual, content,
interaction, component, and accessibility language so teams can design and
implement consistent product experiences without re-solving common decisions.

## Scope

The Design Language owns reusable experience knowledge that is meaningful across product features, including:
- foundations and token semantics;
- reusable components;
- reusable composition patterns;
- cross-component interaction rules;
- accessibility guidance;
- approved product-level visual variations.

It does **not** own:
- product-specific business rules, permissions, workflows, or domain states;
- temporary feature proposals;
- the complete Figma specification;
- runtime API documentation already available from code/Storybook;
- migration history that is not needed for current use.

## Operating model

Use the smallest source that can answer the task:

```text
Design intent
→ overview/design-language.md

Reusable UI decision
→ Component / Pattern

Cross-cutting rule
→ Foundation / Experience / Accessibility

Exact visual construction
→ Figma

Exact runtime API / behavior / executable example
→ Code / Storybook when available

Product-specific behavior
→ Product Knowledge
```

## Supported products

The system is shared by JobVision and Cando. Shared semantic meaning should remain stable across products. Product-specific Brand values or approved variations may differ without forking the full component model.

## Documentation principle

Documentation is a **decision layer**, not a copy of every live source.

Prefer broad coverage with concise, trustworthy contracts over a small number of exhaustive component manuals. Add detail when it changes a design or implementation decision; query live sources for facts that can be generated or inspected directly.
