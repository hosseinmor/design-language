---
id: design-system.component.tree-view
collection: design-system
type: component
title: Tree View
summary: TBD Tree View scope for viewing and managing hierarchical structures; not a form-field replacement for choosing a value from a hierarchy.
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.component.select
  - design-system.pattern.hierarchical-selection
---

# Tree View

> **TBD / Unverified — reserved component topic only.** This is not evidence of a released or approved public component. Linked documents have **independent maturity and review status**. Each source owns only decisions within its stated, evidence-backed scope; follow its metadata and unresolved gaps before treating any rule as approved.

## Purpose

A candidate component for **viewing and managing** a hierarchy in place, such as an organization's branch structure: expanding and collapsing levels, and possibly adding, moving or renaming nodes.

## When to Use

> TBD — Validate real product needs (for example a branch-structure management surface) before recommending this component.

## When Not to Use

Do not use Tree View as a form field for **choosing** a value from a hierarchy. That task is owned by [Select › Hierarchical options](select.md#hierarchical-options) and the [Hierarchical Selection pattern](../patterns/hierarchical-selection.md): an always-expanded indented list with structure-preserving search, one select target per row, and cascade selection in Multiple.

## Anatomy

> TBD — No approved canonical anatomy. If approved, row indentation and indent guides should reuse the hierarchical Option measurements (24px step derived from indicator + gap, guides centred under the ancestor indicator) rather than define a second indent scale.

## Variants

> TBD — Do not create an unreviewed variant family from this heading.

## States

> TBD — Expanded/collapsed, selected, focused and disabled states are not yet defined here.

## Behavior

> TBD — Keyboard model (WAI-ARIA tree pattern), expand/collapse rules, selection model and any editing actions remain undecided.

## Accessibility

The [Component Accessibility Authoring Contract](../../accessibility/component-accessibility-authoring-contract.md) defines required questions before handoff. **No component-specific accessibility contract is approved here yet.**

## Figma Reference

> TBD — The Figma file contains a `Tree view` page; it is not confirmed as an approved canonical source for this contract.

## Code Reference

> TBD — No registered runtime package, API, Storybook story or executed test evidence is represented here.

## Known Gaps

**Open owner decisions:**

- Is Tree View needed as a public component, and for which product surfaces?
- Which selection model does it support (none, single, multiple with cascade)?
- Does it include in-place editing, or only display and navigation?

**Related sources and scopes (review maturity varies):**

- [Select](select.md) — hierarchical options for choosing values
- [Hierarchical Selection](../patterns/hierarchical-selection.md) — cross-component choice between Select, Tree View and other controls
