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
| Why does this component/pattern exist? | Design System Knowledge |
| When should it be used or avoided? | Design System Knowledge |
| What does a semantic token/state mean? | Design System Knowledge |
| What are the current editable visual properties/layouts? | Figma |
| What is the runtime API/default/implemented behavior? | Registered Karbon code source |
| Which rendered examples actually run? | Registered Karbon Storybook source |
| Which interaction/accessibility tests actually pass? | Registered Karbon Storybook/test source |
| What business rule or product workflow applies? | Product Knowledge |
| What changed during migration? | Migration/change artifact |

## Conflict rule

When sources disagree, do not silently merge them.

```text
Meaning / usage conflict
→ Design System Knowledge owner reviews

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

Examples that normally belong outside prose documentation:
- generated component props and defaults;
- every Figma property/value combination;
- raw token-value catalogs;
- exhaustive rendered state permutations;
- test implementation details;
- historical token/component migration mappings after migration is complete.

Design System Knowledge should retain durable semantic decisions, decision rules, important constraints, and known gaps.

## Live-source availability rule

A source-of-truth role does not prove that the live source is currently registered or accessible.

```text
source registered and accessible
→ query it for exact facts

source role known but source unregistered/unavailable
→ use Knowledge only for the semantic contract
→ explicitly mark exact live fact as unverified
→ do not infer it from another source
```

Examples:

- Figma property name does not prove a runtime prop name.
- Figma component presence does not prove code shipment.
- Markdown state lists do not prove a runnable Storybook story or test.
- Code implementation does not override Design System semantic meaning merely because it currently differs; the mismatch must be reconciled.

Use `component-mapping.md` for verified Figma ↔ Code ↔ Storybook identities.

## AI use

AI should retrieve the smallest relevant knowledge set, then query the owning registered live source for exact facts. If a required source is unavailable, unregistered, or the mapping is incomplete, surface the gap rather than guessing.
