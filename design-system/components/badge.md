---
id: design-system.component.badge
collection: design-system
type: component
title: Badge
summary: TBD Badge component scope and anatomy; distinguish non-interactive Badge from Tag, Chip, counters and status text before approving a public component.
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.component.tag
  - design-system.component.chip
  - design-system.component.tabs
---

# Badge

> **TBD / Unverified — reserved component topic only.** This is not evidence of a released or approved public component. The linked reviewed documents below retain ownership of existing rules; the remaining component decisions need review.

## Purpose

A candidate compact visual indicator associated with a count, classification or short state. **Whether Badge is an independent public component, an internal primitive or an instance of an existing component is not yet decided.**
## When to Use

> TBD — Validate real product needs and component ownership before recommending this component.
## When Not to Use

Use the reviewed owning component contract for an actual interaction (for example [Chip](chip.md)), or the appropriate content/status pattern. Do not invent a Badge API or color taxonomy because another component refers to a badge.
## Anatomy

> TBD — No approved independent canonical component anatomy is recorded here.
## Variants

> TBD — Do not create an unreviewed variant or family from this heading.
## Sizes

> TBD — No approved public size axis is defined here.
## States

> TBD — Do not infer Hover, Selected, Disabled or Error variants without component-specific review.
## Behavior

Badge is not automatically a control. Whether any variant is actionable, announced or decorative remains TBD; interactive behavior must come from an owning action component.
## Content Guidelines

Counts/labels should follow their owning component and Content System rules; truncation, zero-count and overflow remain TBD.
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

- Is Badge a standalone public component, a count adornment owned by Tabs, or a visual subcomponent?
- How does it differ from Tag and Chip in purpose and accessibility?
- What semantics and product scenarios warrant any special state/color treatment?

**Existing owners and evidence:**

- [Chip](chip.md) — interactive compact controls
- [Tag](tag.md) — categorical Tag component, itself still a scaffold
- [Tabs](tabs.md) — existing component-specific counter/badge contract
