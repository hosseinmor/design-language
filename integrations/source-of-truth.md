---
id: design-system.reference.source-of-truth
collection: design-system
type: reference
title: Sources of Truth
summary: Defines which source owns design meaning, visual construction, runtime implementation, product behavior, and temporary change history.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.overview
  - design-system.structure
  - design-system.reference.figma
  - design-system.reference.code
  - design-system.reference.storybook
  - design-system.reference.component-mapping
  - design-language.integration.karbon
---

# Sources of Truth

No single tool is the source of truth for every Design System fact.

Use ownership by question:

| Question | Primary source |
|---|---|
| Why does this component/pattern exist? | Design Language |
| When should it be used or avoided? | Design Language |
| What does a semantic token/state mean? | Design Language |
| What is the approved design intent, semantic meaning, or a component state model? | Design Language (reviewed decisions and marked draft gaps) |
| What are the current editable visual properties/layouts? | Figma |
| Which component properties, code APIs, events and defaults are **implemented**? | Versioned Karbon code and its implementation docs |
| Which rendered examples actually run? | Karbon Storybook at a verified build/version |
| Which interaction/accessibility checks actually pass? | Executed Karbon tests / CI evidence, not a written promise |
| What cross-product accessibility requirements apply? | Design Language Accessibility corpus |
| What is a feature's eligibility, persistence or business workflow? | Product Knowledge / Product Walkthrough |
| What changed during migration? | Migration/change artifact |

## Conflict rule

When sources disagree, do not silently merge them.

```text
Meaning / usage conflict
→ Design Language owner reviews

Visual construction conflict
→ Figma implementation is inspected and reconciled

Runtime/API conflict
→ Code implementation is inspected and reconciled

Product-behavior conflict
→ Product Knowledge owner resolves
```

A mismatch is a maintenance gap, not permission for AI to invent a compromise.

## Duplication rule

Do not manually duplicate facts that another live source can provide reliably.

Examples that normally belong outside general prose documentation:
- generated component props and defaults;
- every Figma property/value combination;
- raw exported variable dumps or unreviewed snapshots (the **reviewed** token contracts and declared values in `design-system/tokens/` remain valid canonical Design Language references);
- exhaustive rendered state permutations;
- test implementation details;
- historical token/component migration mappings after migration is complete.

Design Language should retain durable semantic decisions, decision rules, important constraints, and known gaps.

## Live-source availability rule

A source-of-truth role does not prove that the live source is currently registered or accessible.

```text
source registered and accessible
→ query it for exact facts

source role known but source unregistered/unavailable
→ use Design Language only for the semantic contract
→ explicitly mark exact live fact as unverified
→ do not infer it from another source
```

Examples:

- Figma property name does not prove a runtime prop name.
- Figma component presence does not prove code shipment.
- Markdown state lists do not prove a runnable Storybook story or test.
- Code implementation does not override Design System semantic meaning merely because it currently differs; the mismatch must be reconciled.

Use [Component Mapping Index](component-mapping-index.md) to locate the relevant part of the [Component Mapping evidence registry](component-mapping.md). A Figma-only identity is **not** a verified Figma ↔ Code ↔ Storybook match.

## Documentation authority by repository

**Design Language** owns reusable intent, foundations, token meaning and reviewed design token contracts, component and pattern **usage and design decisions**, content guidance, and normative cross-component accessibility guidance.

**Figma** owns the live, editable visual construction, component/variable/style identities and authoring composition. Figma documentation-frame details belong to the focused [Figma Component Presentation](figma-component-presentation.md), not a duplicate layout definition in this reference.

**Karbon code and accompanying Storybook documentation** own executable implementation details: exported component APIs/defaults, framework and DOM/ARIA behavior, install/build/runtime usage, actual states, test coverage and versioned release facts. A Storybook documentation page can **display or link** Design Language usage and accessibility rules, but that copy is not an independent semantic policy source. Runtime a11y tests are evidence of implementation, not a replacement for normative accessibility requirements.

**Product Knowledge and Product Walkthrough** own domain rules and actual user flows. Neither component documentation nor visual examples may fabricate those details.

## Cross-source change and drift rule

A design decision changing component meaning, usage or shared accessibility guidance starts with its owning Design Language contract and a Design System owner review. A change to implemented props, rendering or behavior starts with Karbon code and its owning engineering review. A visual source change starts with Figma. All changes that affect another source create a corresponding update/reconciliation task **in the same change workflow**, but independent repositories do not need fictional atomic commits.

Until both sides are verified, record a gap such as `design-approved / implementation-unverified` or `runtime-implemented / design-reconciliation-needed`. Do not label the component `shipped`, `ready`, or `in parity` merely because one source is updated.

Mapped links, source revision/build IDs, Design Language document IDs, and outstanding mismatches belong in the component mapping registry. The detailed drift process lives in [Karbon Integration](karbon.md).

## AI use

AI should retrieve the smallest relevant knowledge set, then query the owning registered live source for exact facts. If a required source is unavailable, unregistered, or the mapping is incomplete, surface the gap rather than guessing.
