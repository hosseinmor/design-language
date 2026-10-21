---
id: design-system.component.drawer
collection: design-system
type: component
title: Drawer
summary: TBD Drawer component scope and design contract; distinguish modal/non-modal side surfaces from Dialog and responsive pane layouts.
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.component.dialog
  - design-system.foundation.responsive-layout
  - design-system.accessibility.focus-management
---

# Drawer

> **TBD / Unverified — reserved component topic only.** This is not evidence of a released or approved public component. Linked documents have **independent maturity and review status** (some are draft/scaffold). Each source owns only decisions within its stated, evidence-backed scope; follow its metadata and unresolved gaps before treating any rule as approved.

## Purpose

A possible side-attached contextual surface for supplementary content or a task. **No shared Drawer variant, size, dismissal, focus or responsiveness contract is approved in this scaffold.**
## When to Use

> TBD — Validate real product needs and component ownership before recommending this component.
## When Not to Use

Do not introduce a Drawer in place of [Dialog](dialog.md) for blocking task dialogs or a persistent responsive pane merely because the layouts look similar.
## Anatomy

> TBD — No approved independent canonical component anatomy is recorded here.
## Variants

> TBD — Do not create an unreviewed variant or family from this heading.
## Sizes

> TBD — No approved public size axis is defined here.
## States

> TBD — Do not infer Hover, Selected, Disabled or Error variants without component-specific review.
## Behavior

Overlay modality, dismissal, focus containment/restoration and history behavior are **TBD**, not inherited automatically from Dialog. Follow the [Focus Management](../../accessibility/focus-management.md) baseline.
## Content Guidelines

Content hierarchy, actions and inline form composition must follow the owning component/pattern; no Drawer-specific UI copy has been approved.
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

- Is Drawer a distinct reusable component or a page/overlay composition pattern?
- Which scenarios require modal versus non-modal interaction?
- How is it distinguished from Dialog and persistent layout panes on narrow viewports?

**Related sources and scopes (review maturity varies):**

- [Dialog](dialog.md) — approved modal-task design contract
- [Responsive Layout](../../foundations/visual/responsive-layout/guideline.md) — page region ownership
- [Focus Management](../../accessibility/focus-management.md) — normative cross-component accessibility
