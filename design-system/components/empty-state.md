---
id: design-system.component.empty-state
collection: design-system
type: component
title: Empty State
summary: TBD Empty State component anatomy; composition belongs to the Empty States pattern and messaging to the Content System.
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.pattern.empty-states
  - content.pattern.empty-states
  - design-system.pattern.data-views
---

# Empty State

> **TBD / Unverified — reserved component topic only.** This is not evidence of a released or approved public component. Linked documents have **independent maturity and review status** (some are draft/scaffold). Each source owns only decisions within its stated, evidence-backed scope; follow its metadata and unresolved gaps before treating any rule as approved.

## Purpose

Potential **reusable visual component anatomy** for empty collections or views; component-level slot/asset specification and its need as a separate public component are **not approved yet**.
## When to Use

> TBD — Validate real product needs and component ownership before recommending this component.
## When Not to Use

Do not substitute an Empty State component for Loading, Error, Permission or Eligibility; content classification is governed by [Empty State Content](../../foundations/content/patterns/empty-states.md). Do not copy pattern-level composition policy into component anatomy.
## Anatomy

> TBD — No approved independent canonical component anatomy is recorded here.
## Variants

> TBD — Do not create an unreviewed variant or family from this heading.
## Sizes

> TBD — No approved public size axis is defined here.
## States

> TBD — Do not infer Hover, Selected, Disabled or Error variants without component-specific review.
## Behavior

Feature-specific recovery and action eligibility remain Product Knowledge-owned. [Empty States pattern](../patterns/empty-states.md) owns future cross-component composition, not this scaffold.
## Content Guidelines

Use [Empty State Content](../../foundations/content/patterns/empty-states.md) for message type, copy and recovery. This file does not create an alternate empty-state content rule.
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

- Is one public Empty State component needed or should Patterns compose Heading, Body and Button directly?
- Which illustration/icon/action slots are actually reusable and reviewed?
- What is component-owned anatomy versus page-context positioning?

**Related sources and scopes (review maturity varies):**

- [Empty States pattern](../patterns/empty-states.md) — intended shared composition, currently TBD
- [Empty State Content](../../foundations/content/patterns/empty-states.md) — verified-in-part copy guidance
- [Data Views](../patterns/data-views.md) — composition of empty data presentations
