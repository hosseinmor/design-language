---
id: design-system.foundation.iconography
collection: design-system
type: foundation
title: Iconography
summary: Documents the verified icon-instance semantic color override guard; icon library, sizing, stroke/fill and accessibility guidelines remain TBD.
knowledge_state: verified
document_maturity: draft
related:
  - design-system.accessibility.images-icons-and-media
  - design-system.component.icon-button
---

# Iconography

> **Partially reviewed / Draft.** Only the Consumer Color Override Guard below is verified for current Figma authoring. Icon library choices, naming, sizes, stroke/fill and shared asset governance are **TBD**, not approved by this draft.

## Icon Library

> TBD — Define the canonical asset library, icon naming and governance only after the shared icon-system source is reviewed.

## Sizes

> TBD — Component-specific icon sizes remain in their owning component specifications; do not invent a universal icon-size token scale.

## Stroke and Fill

> TBD — Do not infer stroke widths, fill style or library construction from this incomplete document.

## Usage Rules

### Consumer color override guard

Shared icon components intentionally keep a fixed base color instead of automatically inheriting a semantic foreground token.

Every component or screen that consumes an icon must explicitly override the icon color to the semantic token appropriate for that context. This is an authoring guard: a newly placed or swapped icon should look obviously unfinished until the designer chooses the correct semantic color.

Rules:

- do not change the shared icon component's base color to solve a consumer-specific color need;
- apply the semantic foreground token at the icon instance usage;
- after swapping an icon, verify that the color override is still present;
- disabled, danger, inverse, accent, and other contextual treatments must use their corresponding semantic foreground token rather than a literal color;
- component documentation should state the required icon-color mapping when the mapping is deterministic.

This rule is verified for current component authoring even though the rest of this Iconography foundation document remains a scaffold.

## Accessibility

The [Images, Icons and Media accessibility contract](../../accessibility/images-icons-and-media.md) owns accessible naming and decorative/informational icon behavior. The [Icon Button](../../design-system/components/icon-button.md) owns its own anatomy and operation labeling. Further icon-system-level guidance remains TBD.
