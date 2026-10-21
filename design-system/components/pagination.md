---
id: design-system.component.pagination
collection: design-system
type: component
title: Pagination
summary: TBD Pagination component anatomy and control states; data-view composition and product paging policy are owned elsewhere.
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.pattern.data-views
  - design-system.component.table
  - design-system.accessibility.structure-and-navigation
---

# Pagination

> **TBD / Unverified — reserved component topic only.** This is not evidence of a released or approved public component. The linked reviewed documents below retain ownership of existing rules; the remaining component decisions need review.

## Purpose

Potential shared visual/navigation control for moving between bounded result pages. **The actual paged-data model, UI composition and public API are not yet decided**.
## When to Use

> TBD — Validate real product needs and component ownership before recommending this component.
## When Not to Use

Do not prescribe Pagination for infinite scroll, cursor-backed APIs or any specific product data view without Product-owned pagination requirements. The [Data Views pattern](../patterns/data-views.md) owns overall placement.
## Anatomy

> TBD — No approved independent canonical component anatomy is recorded here.
## Variants

> TBD — Do not create an unreviewed variant or family from this heading.
## Sizes

> TBD — No approved public size axis is defined here.
## States

> TBD — Do not infer Hover, Selected, Disabled or Error variants without component-specific review.
## Behavior

Unknown page totals, navigation feedback, loading, focus and pagination event semantics remain TBD; do not infer runtime controls from a Table design.
## Content Guidelines

Labels, range summaries and empty last-page messaging remain TBD and must follow Content and accessibility contracts when specified.
## Accessibility

The [Component Accessibility Authoring Contract](../../accessibility/component-accessibility-authoring-contract.md) defines required questions before handoff. **No component-specific accessibility contract is approved here yet.** Do not confuse a general requirement in Accessibility with verified runtime behavior.
## Product Variations

> TBD — No Product-specific variance or approved override is implied.
## Figma Reference

> TBD — Do not infer public component identity, variants or Figma publication from this placeholder. Confirm from the live owner during the final reconciliation.
## Code Reference

> TBD — No registered runtime package, API, Storybook story or executed test evidence is represented here.
## Known Gaps

**Open owner decisions:**

- Which page-based versus load-more/cursor behaviors must the system support?
- Is Pagination a separate public component or a Data Views composition?
- Who owns page-size selection, total counts and URL/history synchronization?

**Existing owners and evidence:**

- [Data Views](../patterns/data-views.md) — choice/placement in page composition
- [Data Table](table.md) — table-specific data presentation, not paging policy
- [Structure and Navigation Accessibility](../../accessibility/structure-and-navigation.md) — shared navigation requirements
