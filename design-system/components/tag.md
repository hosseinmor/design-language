---
id: design-system.component.tag
collection: design-system
type: component
title: Tag
summary: TBD Tag component anatomy and behavior; approved categorical Tag Color tokens exist separately from this unverified component scaffold.
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.token.component-tokens
  - design-system.component.chip
  - design-system.component.badge
---

# Tag

> **TBD / Unverified — reserved component topic only.** This is not evidence of a released or approved public component. The linked reviewed documents below retain ownership of existing rules; the remaining component decisions need review.

## Purpose

A possible non-editable categorical label. The **Color contract for Tag is already reviewed**, but no corresponding component anatomy, variants, sizes, content model or runtime API is approved by this scaffold.
## When to Use

> TBD — Validate real product needs and component ownership before recommending this component.
## When Not to Use

Do not treat [Chip](chip.md) (which supports selection, removal, disclosure and actions) as a read-only Tag merely because it looks similar. Do not infer a general Color palette or system severity API from categorical Tag colors.
## Anatomy

> TBD — No approved independent canonical component anatomy is recorded here.
## Variants

> TBD — Do not create an unreviewed variant or family from this heading.
## Sizes

> TBD — No approved public size axis is defined here.
## States

> TBD — Do not infer Hover, Selected, Disabled or Error variants without component-specific review.
## Behavior

Category labels are not inherently interactive. If removal/selection is required, use the approved component/pattern owning that interaction; Tag interaction policy remains TBD.
## Content Guidelines

The [Component Color Tokens](../tokens/color/component-tokens.md) file owns the approved `tag/{color}/*` categorical token vocabulary, including its limits; it does **not** certify a public Tag component.
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

- Is Tag a standalone non-interactive component and which typography/size/shape choices are supported?
- Does it need hover or any click behavior; if so, is that actually Chip?
- How do visual categories, semantic status and accessible labels remain distinct?

**Existing owners and evidence:**

- [Component Color Tokens](../tokens/color/component-tokens.md) — approved Tag-only categorical palette, not full component
- [Chip](chip.md) — approved interactive compact-control family
- [Badge](badge.md) — another reserved, unverified compact-indicator category
