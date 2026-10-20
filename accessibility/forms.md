---
id: design-system.accessibility.forms
collection: design-system
type: accessibility
title: Accessible Forms
summary: Defines form labeling, instructions, validation, errors, input purpose, authentication, redundant-entry, multi-step, and submission requirements.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.focus-management
- design-system.accessibility.dynamic-content-and-feedback
- design-system.accessibility.content
- design-system.accessibility.structure-and-navigation
last_reviewed: '2026-09-02'
---

# Accessible Forms

This document owns form-level accessibility behavior. Atomic field components own their mechanism; the Product/Pattern owns business validation, actual copy, and flow policy.

## Labels and instructions

**MUST** give form controls a meaningful accessible name/label. Placeholder **MUST NOT** be the only label.

**MUST** provide labels or instructions when user input requires them. Instructions needed to complete the field should be available before the user needs them.

For related control groups, use an appropriate programmatic group label such as native `fieldset`/`legend` where it fits.

## Required, optional, readonly, disabled

Requiredness **MUST** be communicated programmatically and visibly enough to be understood. Do not rely on color or an asterisk with no explanation when ambiguity remains.

Readonly and Disabled are different states. Preserve native semantics when available; do not use Disabled as a substitute for immutable but useful/readable data.

## Input purpose and autofill

Where WCAG 1.3.5 applies, **MUST** identify common user-information input purpose programmatically (typically with appropriate `autocomplete` values).

**SHOULD** allow browser/password-manager autofill and paste unless there is a specific, justified constraint.

Do not globally add `autocomplete="off"` or disable paste as a default security pattern.

## Validation and errors

When an input error is detected:
- **MUST** identify the item in error and describe the error in text when WCAG 3.3.1 applies;
- **MUST** provide a correction suggestion when known and WCAG 3.3.3 applies, unless it would jeopardize security/purpose;
- **MUST** associate the error programmatically with the relevant control where applicable;
- **MUST NOT** communicate the error only by color.

**SHOULD** keep error copy actionable: what is wrong + how to correct it when known.

Do not clear unrelated valid data after a recoverable validation failure.

## Validation timing

A reliable baseline is submit-attempt validation plus clear field relationships/recovery.

**SHOULD NOT** announce errors assertively on every keystroke or move focus away while the user is still editing unless immediate feedback materially helps the task.

On failed submission, users **MUST** have a logical way to discover and reach errors. For small forms, focusing the first invalid field may be appropriate. For large/multi-error forms, an error summary near the beginning of the relevant step that receives programmatic focus is often preferable.

Focus strategy belongs jointly to the Form Pattern/Product and `focus-management.md`; dynamic announcement mechanism belongs to `dynamic-content-and-feedback.md`.

## Predictable changes on focus/input

Form controls **MUST** comply with WCAG 3.2.1 On Focus and 3.2.2 On Input.

Receiving focus must not itself initiate an unexpected change of context.

Changing a value/setting must not automatically cause navigation, open a new window, move focus, or otherwise change context unless the user was advised of that behavior before using the control.

Ordinary local UI updates that do not meet the WCAG definition of change of context are not automatically prohibited.

`structure-and-navigation.md` owns the cross-cutting predictable-context policy; Forms owns form-specific implementation/recovery.

## Submit actions

**SHOULD** avoid disabling Submit/Continue when doing so hides why the user cannot proceed. If a disabled action is used, the reason must be understandable and all required information available without guessing.

During submission, **MUST** prevent accidental duplicate submission. Preserve focus when the trigger remains conceptually present; do not move focus to a spinner by default.

On server/network failure, preserve entered data where safe, explain what happened, and provide a recovery/retry path.

## Redundant Entry — WCAG 3.3.7 A

Within the same process, information the user previously entered and that must be entered again **MUST** be auto-populated or available for selection unless a criterion exception applies.

Do not treat Back navigation in a multi-step flow as a reason to erase valid data.

## Accessible Authentication — WCAG 3.3.8 AA

Authentication **MUST NOT** rely on a cognitive function test unless a WCAG exception/assistive mechanism applies.

Practical consequences include supporting password managers and paste, and avoiding authentication designs that require users to memorize/transcribe information when a compliant alternative is available.

## Error Prevention — WCAG 3.3.4 AA

For pages that create legal commitments, perform financial transactions, modify/delete user-controllable stored data, or submit user test responses, **MUST** provide at least one qualifying protection: reversible action, checked opportunity to correct, or review/confirm/correct before finalization.

Do not apply 3.3.4 merely because a flow is important or is a job application. Determine whether the actual submission falls within the criterion scope.

## Multi-step forms

Each step **MUST** have a clear purpose, expose its own fields/errors accessibly, preserve relevant valid data, and avoid redundant re-entry.

**SHOULD** communicate progress when it helps users understand position/remaining effort.

On step transition, focus **SHOULD** move to the most useful beginning point when needed for orientation; do not enforce a universal target.

Conditional fields **MUST** appear in logical DOM/focus order, have labels/instructions, and must not become hidden required fields that block submission. Do not automatically focus every newly revealed field.

A generic `multi-step-flow` Design System pattern does not by itself define product-specific Apply/Screening Questions policy. If such flow-level behavior is missing, record an explicit Pattern/Product gap rather than inventing it here.

## Ownership

| Component/Design System owns | Form/Product owns |
|---|---|
| Label/helper/error association mechanism | Actual label/helper/error copy |
| Required/invalid/readonly/disabled support | Which state applies |
| Input-purpose/autocomplete pass-through | Correct field purpose/token |
| Component focus/error visuals | Validation and recovery strategy |
| Button loading mechanism | Result after submission |
| Group semantics mechanism | Actual group question |

## Testing

Test applicable labels/names, required/readonly/disabled/invalid semantics, keyboard completion, multiple-error recovery, error associations, autofill/paste, authentication, Back/data preservation, redundant-entry behavior, zoom/reflow, and submit success/failure recovery.

## AI contract

AI **MUST** separate component mechanism from business validation policy, preserve input-purpose semantics, expose errors correctly, avoid redundant entry, apply 3.3.4 only to qualifying submissions, and apply authentication requirements to actual authentication. AI **MUST NOT** invent Apply-specific policy or unresolved ARIA/focus behavior.

## References

- WCAG 2.2 — 1.3.1, 1.3.5, 2.5.3
- WCAG 2.2 — 3.2.1 On Focus
- WCAG 2.2 — 3.2.2 On Input
- WCAG 2.2 — 3.3.1–3.3.4, 3.3.7, 3.3.8
- WCAG 2.2 — 4.1.2, 4.1.3
