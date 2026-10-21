---
id: design-system.component.dropdown-menu
collection: design-system
type: component
title: Dropdown Menu
summary: TBD legacy Dropdown Menu naming/scope; Menu currently owns action surfaces and Menu Button/Combo Button own their respective triggers.
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.component.menu
  - design-system.component.menu-button
  - design-system.component.combo-button
---

# Dropdown Menu

> **TBD / Unverified — reserved component topic only.** This is not evidence of a released or approved public component. Linked documents have **independent maturity and review status** (some are draft/scaffold). Each source owns only decisions within its stated, evidence-backed scope; follow its metadata and unresolved gaps before treating any rule as approved.

## Purpose

A reserved name associated with a dropdown menu. **Do not assume this is a second implemented component or an approved alias** of [Menu](menu.md).
## When to Use

> TBD — Validate real product needs and component ownership before recommending this component.
## When Not to Use

For an existing action menu, read [Menu](menu.md). For a trigger, use [Menu Button](menu-button.md) or [Combo Button](combo-button.md). Selection dropdowns belong to [Select](select.md), not automatically to this scaffold.
## Anatomy

> TBD — No approved independent canonical component anatomy is recorded here.
## Variants

> TBD — Do not create an unreviewed variant or family from this heading.
## Sizes

> TBD — No approved public size axis is defined here.
## States

> TBD — Do not infer Hover, Selected, Disabled or Error variants without component-specific review.
## Behavior

Action-menu keyboard/focus/item behaviors are owned by Menu. No distinct Dropdown Menu state model or API is approved.
## Content Guidelines

Menu item semantics and composition come from Menu; selection content comes from Select.
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

- Is this obsolete terminology that should become a redirect, or an independently justified component?
- Do any verified Figma or runtime consumers still use this exact public name?
- Which alias/legacy migration would preserve stable IDs without inventing two competing APIs?

**Related sources and scopes (review maturity varies):**

- [Menu](menu.md) — canonical command/action surface
- [Menu Button](menu-button.md) — peer-action trigger
- [Combo Button](combo-button.md) — primary action plus alternatives
- [Select](select.md) — predefined-value selection
