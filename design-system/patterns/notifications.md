---
id: design-system.pattern.notifications
collection: design-system
type: pattern
title: Notifications
summary: Defines shared feedback severity and when feedback appears inline or as a transient Toast.
knowledge_state: verified
document_maturity: draft
last_reviewed: 2026-09-19
related:
- design-system.accessibility.dynamic-content-and-feedback
- design-system.component.notification
---

# Notifications

## Problem and Use

Notifications communicate system feedback without turning every success, warning, or failure into a different interaction model.

Use this pattern when the interface needs to communicate a system state or result such as:
- information;
- success;
- warning;
- error.

Standard feedback severities are:

```text
Info
Success
Warning
Error
```

`Danger` is **not** a fifth notification severity. Danger describes destructive intent before an action; Error describes a failure/problem state.

## Component Model

The pattern has two independent component presentations that share severity semantics:

### Inline Notification

Use when the message should remain visible near the affected content or when users may need time to read or act on it.

Baseline visual semantics:
- muted severity surface;
- readable neutral message content;
- severity cue through the status icon;
- no elevation shadow.

Inline Notification remains in the content flow and follows the width of its related content region.

### Toast

Use for short transient feedback that does not need to remain in the layout, such as routine confirmation after an action.

Toast is a floating component and uses `Shadow/Floating`.

Normal is the default neutral-surface treatment. High is the approved inverse-surface treatment.

Toast is a visual presentation, not a semantic role and not another severity.

Do not combine Inline Notification and Toast into a single Figma `Type` axis. Their placement, persistence, elevation, timing, and responsive behavior are different enough to keep separate component identities.

## Rules and States

### Severity is not urgency

Visual severity and assistive-technology announcement urgency are separate decisions.

For example:
- an Error does not automatically require an assertive announcement;
- a Success does not automatically need a live announcement if focus/context already communicates the result.

Use the least interruptive mechanism that still communicates the change.

### Destructive warning vs Error

```text
“This action permanently deletes the job.”
→ Danger / destructive pattern

“Deleting the job failed.”
→ Error Notification
```

Do not use Error merely because destructive actions and errors may share a red hue.

### Actions

Notification actions reuse existing Button/Link semantics. Do not create notification-specific action styles only because an action appears inside feedback.

The Figma components expose a native Action Slot so Link/Button keep their own geometry and properties.

Use:
- Link for navigation;
- Button for an operation in the current context.

Keep at most one action.

High Toast currently has a verified Inverse Link composition; operational Button treatment on High Toast remains blocked on a shared inverse Button decision.

If a transient Toast includes an action, users must have enough opportunity to perceive and operate it. A Toast should not steal focus merely because it appeared.

### Close / dismissal

Dismiss uses the shared Icon Button rather than a locally styled close glyph.

Dismissibility and timing belong to the concrete component/runtime contract. Users should be able to predict whether a message persists, disappears, or can be manually dismissed.

The dismiss Icon Button inherits the shared accessible-name and Tooltip contract.

## Components

This pattern composes:
- `Inline Notification`;
- `Toast`;
- existing Link / Button for the optional action;
- existing Icon Button for dismissal;
- semantic Support/Danger tokens according to message meaning.

The components own anatomy and implementation mechanics; this pattern owns severity meaning and presentation choice.

## Accessibility

- Severity must not rely on color alone when the distinction affects understanding.
- A Toast is a visual pattern; choose status/live semantics from message importance, not from the fact that it is a Toast.
- Routine confirmation should normally be non-interruptive.
- Do not move focus to a Toast or spinner merely to announce it.
- Interactive Toast controls must be keyboard accessible without automatic autofocus.
- If a message disappears automatically, applicable timing requirements must still be met.
- Avoid duplicate feedback such as focus movement + alert + Toast for the same event unless deliberately justified and tested.

Programmatic status/alert behavior is owned by `accessibility/dynamic-content-and-feedback.md`.

## Variations and Gaps

Current reusable decisions still needed before this pattern is `reviewed`:
- Toast timing and persistence policy;
- stacking/queue behavior;
- maximum simultaneous Toasts;
- actionable Toast persistence/fallback;
- responsive placement;
- executable announcement/focus tests;
- shared inverse Button/Icon Button treatments needed to remove High-Toast composition exceptions.

Do not invent a full matrix of strong severity surfaces or notification-specific token families to fill these gaps.

## Live References

- Figma Inline Notification: node `22838:3046`
- Figma Toast: node `22839:3058`
- Storybook / Code: unregistered
- Related component: `../components/notification.md`
- Destructive behavior: `destructive-actions.md`
