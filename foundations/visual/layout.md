---
id: design-system.foundation.layout
collection: design-system
type: foundation
title: Layout
summary: Routes layout design principles to the reviewed Responsive Layout guidance and the Layout Token Catalog; remaining global grid, density and alignment rules are TBD.
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.foundation.responsive-layout
  - design-system.foundation.responsive-layout-spec
  - design-system.pattern.responsive-layout
  - design-system.token.layout.catalog
---

# Layout

> Status: structure in progress

Layout foundations define how pages and components organize, align, size, and adapt content.

## Responsive layout

**Reviewed layout scope:** responsive page types, viewport ranges, logical regions, container usage, and breakpoint decision rules are maintained under [`responsive-layout/`](responsive-layout/README.md):

- [`responsive-layout/guideline.md`](responsive-layout/guideline.md): human-facing guideline and core decisions.
- [`responsive-layout/spec.md`](responsive-layout/spec.md): atomic rules and decision tables for AI retrieval and implementation.
- [`responsive-layout/patterns.md`](responsive-layout/patterns.md): adaptive behavior for common product patterns.
- [`responsive-layout/examples/`](responsive-layout/examples/README.md): reserved example templates (currently no reviewed product examples).
- [Layout Token Catalog](../../design-system/tokens/layout/catalog.md): canonical reviewed breakpoint, container and layout-padding names/values. The catalog is the only Markdown owner of those numeric declarations.

## Remaining sections

The following **design-principle extensions** remain TBD. Do not infer global constraints from their names:

- Global grid conventions beyond the reviewed responsive baseline (no approved universal column/gutter grid)
- Density choices across product layouts
- General alignment and visual rhythm beyond the documented logical RTL/LTR region rules

Container token identifiers and approved numeric values are **not** TBD: they are already owned by the [Layout Token Catalog](../../design-system/tokens/layout/catalog.md). Page-type rules live in the [Responsive Layout Guideline](responsive-layout/guideline.md), not here.
