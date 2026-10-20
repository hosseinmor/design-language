---
id: design-system.foundation.iconography
collection: design-system
type: foundation
title: Iconography
summary: '> Status: structure only'
knowledge_state: unverified
document_maturity: scaffold
related: []
---

# Iconography

> Status: structure only

## Icon Library
## Sizes
## Stroke and Fill
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
