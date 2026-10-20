---
id: design-system.accessibility.screen-reader-semantics
collection: design-system
type: accessibility
title: Screen Reader Semantics
summary: Defines native-first semantics, accessible naming, programmatic state and relationship rules, hidden-content behavior, and assistive-technology expectations.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.keyboard-navigation
- design-system.accessibility.focus-management
- design-system.accessibility.dynamic-content-and-feedback
- design-system.accessibility.structure-and-navigation
last_reviewed: '2026-09-02'
---

# Screen Reader Semantics

This document owns cross-cutting semantic rules. Component guidelines own the resolved component-specific contract.

## Native semantics first

**MUST** use native HTML when it correctly expresses the content/control and behavior.

Examples: action → `<button>`; navigation → `<a href>`; text entry → `<input>`/`<textarea>`; headings → native heading elements; data table → native table structure.

**MUST NOT** recreate a native control with generic elements plus ARIA unless a real requirement makes the native control unsuitable.

## Name, role, state, value

For applicable interactive UI, **MUST** expose the correct accessible name, role, relevant state/property, and value. Programmatic state must remain synchronized with actual behavior.

Relevant states include `disabled`, `readonly`, `expanded`, `selected`, `current`, `checked`, `pressed`, `invalid`, `required`, and `busy` only when those concepts actually apply.

Do not add state attributes merely because a visual style exists.

## Accessible names

**MUST** give every interactive control a meaningful accessible name.

**SHOULD** prefer visible native label/text as the naming source; use `aria-labelledby` when visible content should name the control, and `aria-label` when no suitable visible naming source exists.

When a visible text label exists, the accessible name **MUST** contain that visible label text (WCAG 2.5.3 Label in Name).

Do not put role words such as “button” or “link” into the accessible name unless they are genuinely part of product copy.

Icon-only controls **MUST** have a meaningful accessible name. Tooltip does not replace that name.

Placeholder **MUST NOT** be the only label for an input.

## Descriptions and relationships

Use a description for supplementary information such as helper text, instructions, or an error relationship rather than inflating the accessible name.

**SHOULD** prefer native relationships (`label`, `fieldset`/`legend`, table headers, headings/lists) before ARIA relationships. Use `aria-describedby` or similar only when it is the correct semantic relationship.

## ARIA discipline

ARIA changes semantics; it does not implement keyboard, focus, pointer, or application behavior.

**MUST** satisfy applicable WAI-ARIA role/state/property requirements and ARIA-in-HTML constraints when ARIA is used.

**SHOULD** use the established APG pattern as the default semantic/interaction reference for custom composite widgets when an appropriate pattern exists. APG remains guidance; applicable WCAG/WAI-ARIA requirements remain mandatory.

**MUST NOT** choose a role because its screen-reader announcement sounds convenient, or add generic ARIA mechanically.

`role="application"` **SHOULD NOT** be used for ordinary product UI and requires explicit accessibility review if proposed.

## Hidden content

Content that is visually and interactively unavailable should not remain exposed as active UI to assistive technology.

`aria-hidden="true"` removes content from the accessibility tree but does not itself prevent focus or pointer interaction.

**MUST NOT** apply `aria-hidden="true"` to a focusable element or an ancestor of visible/focusable controls that must remain usable.

Do not use `aria-hidden` as a substitute for actual modal background inertness/focus containment.

Visually hidden text may remain available to assistive technology when it provides meaningful non-visual information, but **SHOULD NOT** create a large parallel “screen-reader-only” content experience.

## Reading and structural order

**MUST** preserve meaningful programmatic reading order. **SHOULD** keep DOM order aligned with the meaningful visual sequence. Page-level headings, landmarks, and navigation structure belong to `structure-and-navigation.md`.

## Dynamic content

Not every DOM update needs an announcement.

**MUST** expose important status changes programmatically when required. **SHOULD** use the least interruptive mechanism that communicates the update. Detailed live/status behavior belongs to `dynamic-content-and-feedback.md`.

## Modal and custom widgets

A visual overlay is not automatically a dialog. If exposed as modal, it must actually behave modally, have an accessible name, move/contain/restore focus as defined, and make background content unavailable for interaction.

Before approving a custom widget, define:

```text
Name
Role
States/properties/values
Relationships
Keyboard model
Focus model
Dynamic announcements if any
```

A reusable custom Grid, Combobox, Menu, Tabs, Tree, Listbox, or Modal contract is not complete until those aspects are resolved and tested.

## Exact screen-reader wording

Component documentation defines semantic outcomes—name, role, state/value, description, relationship, status behavior—not an exact phrase one screen reader must speak.

Exact wording is only useful for a targeted interoperability regression/test.

## Ownership

| Design System/component owns | Product/Pattern owns |
|---|---|
| Semantic role/mechanism | Correct component choice |
| Accessible-name mechanism | Actual label/name |
| State/property mechanism | Business state applied |
| Error/helper association mechanism | Actual helper/error content |
| Popup/dialog relationship | Why/when it opens |
| Component status mechanism | Which event deserves announcement |

## Testing

For relevant work, inspect the accessibility tree and verify expected role, name, description, state/property, relationship, and hidden/decorative exposure. For complex/shared widgets, test representative supported screen-reader/browser combinations together with keyboard operation and state updates.

## AI contract

AI **MUST** use native semantics first, preserve visible-label/name consistency, distinguish semantic states, use existing component contracts before inventing ARIA, and mark unresolved semantics as an accessibility gap. AI **MUST NOT** add ARIA for decoration, claim a role alone makes behavior accessible, or invent exact screen-reader speech as a universal contract.

## References

- WCAG 2.2 — 4.1.2 Name, Role, Value
- WCAG 2.2 — 2.5.3 Label in Name
- ARIA in HTML
- WAI-ARIA 1.2
- WAI-ARIA APG
