---
id: design-system.component.notification
collection: design-system
type: component
title: Notification
summary: Defines the canonical design contracts for Inline Notification and Toast, including severity, anatomy, composition, and current runtime gaps.
knowledge_state: verified
document_maturity: draft
last_reviewed: 2026-09-19
related:
  - design-system.pattern.notifications
  - design-system.component.icon-button
  - design-system.component.link
---

# Notification

> Status: the current Figma anatomy, visual variants, token mapping, RTL geometry, and composition rules are verified. Runtime timing, stacking, placement, and executable announcement behavior remain open until the runtime source is registered.

## Purpose

The feedback system has two independent component identities that share one severity model:

- **Inline Notification** — persistent contextual feedback placed in the layout near the affected content.
- **Toast** — transient floating feedback placed in a viewport-level toast region.

They are not visual variants of one Figma component. Do not add a shared `Type=Inline|Toast` axis.

## Severity Model

Standard system-feedback severities are:

```text
Info
Success
Warning
Error
```

Danger is not a fifth Notification severity. Danger represents destructive intent/action; Error represents validation failure or a system/problem state.

## Inline Notification

### Anatomy

```text
Status icon
Content
  Text content
    Message      required
    Description  optional
  Action content optional; native Slot; always below text
Dismiss          optional; absolute, independent from Content
```

A short one-line notification is the same component with Description omitted. Do not create a separate one-line or `Inline Long` variant.

### Figma properties

```text
Status
Message
Description
Show description
Action
Action content    native SLOT
Dismissible
```

`Status` is the only visual variant axis: Info / Success / Warning / Error.

`Action=False` hides the Action Slot. `Action content` owns the inserted control and accepts one child.

### Action composition

Notification does not create a local action style.

Use:

- shared Link for navigation / destination change;
- shared Button for an operation / state change in the current context.

The native `Action content` Slot preserves the real geometry and properties of the inserted component. Keep at most one action.

Current preferred Figma compositions are:

- Link / Default / Medium / Enabled / Underline=False;
- Button / Tertiary / Small / Enabled as the low-emphasis operational option.

### Typography and foreground

```text
Message      → Heading/SM          14/20, 700, fg/primary
Description  → Body/Compact/SM     14/20, 400, fg/primary
Action       → shared Link or Button component
```

Description is part of the primary feedback message, not helper metadata, so it uses `fg/primary`.

Body/Compact is appropriate because Notification description is short component copy. One or two wrapped lines are valid. Paragraph-like or reading-oriented content should use regular Body or a different pattern.

### Color and elevation

```text
Container    → surface/{severity}-muted
Status icon  → fg/{severity}
Message      → fg/primary
Description  → fg/primary
Border       → none
Shadow       → none
```

Only muted Support surfaces are approved globally. A Notification does not justify a strong `surface/{severity}-emphasis*` matrix.

### Width

Inline Notification has no intrinsic component-level max width. It fills the available width of the related content container and must not exceed that container.

Page-level readability is controlled by the page/grid/form/card/drawer/modal content container, not by Notification.

The 560px width used in the Figma component set is an authoring/example width, not a maximum.

## Toast

### Anatomy

```text
Body
  Status icon
  Content
    Text content
      Title      optional
      Message    required
    Action content optional; native Slot
  Dismiss        optional; absolute
Timeout indicator optional
```

Title and Message stay vertically stacked. There is no separate one-line or responsive-layout variant.

### Figma properties

```text
Status
Contrast
Title
Message
Show title
Action
Action content    native SLOT
Dismissible
Timeout indicator
```

Visual axes:

```text
Status   = Info | Success | Warning | Error
Contrast = Normal | High
```

This produces 8 visual variants.

### Typography

```text
Title    → Heading/SM          14/20, 700
Message  → Body/Compact/SM     14/20, 400
```

Toast copy is concise component feedback, so both recipes use the shared 20px line-height rhythm.

### Contrast treatments

```text
Contrast = Normal
Container    → surface/default
Title        → fg/primary
Message      → fg/secondary
Status icon  → fg/{severity}
Action Link  → Link / Default
Elevation    → Shadow/Floating

Contrast = High
Container    → surface/inverse
Title        → fg/on-inverse
Message      → fg/on-inverse
Status icon  → fg/{severity}-inverse
Action Link  → Link / Inverse
Elevation    → Shadow/Floating
```

`Normal` is the default treatment. `High` is an alternate high-contrast treatment; it is not a severity.

Approved inverse Support foregrounds:

```text
fg/info-inverse
fg/success-inverse
fg/warning-inverse
fg/error-inverse
```

### Action composition

Toast uses the same native `Action content` Slot as Inline Notification.

- Normal Toast defaults to the current Link / Default / Medium composition.
- High Toast defaults to the current Link / Inverse / Medium composition.
- Button may be inserted when semantics require an operation and the selected Button treatment is valid on the Toast surface.

Current limitation: the shared Button primitive does not yet expose a verified inverse-surface treatment. Therefore a Button action in High Toast is **not handoff-ready** yet; use the verified Inverse Link composition until that shared Button gap is resolved.

### Timeout indicator

Timeout indicator represents remaining auto-dismiss lifetime, not operation/task progress.

```text
Normal → fg/secondary, opacity .32
High   → fg/on-inverse, opacity .48
```

It is optional and off by default.

```text
Timed Toast
  → Auto-dismiss
  → Pause on hover/focus
  → Timeout indicator: Optional

Persistent Toast
  → No auto-dismiss
  → No timeout indicator
```

Exact timeout duration is runtime-owned and remains unverified.

## Dismiss Control

Inline Notification and Toast do not create a local close control. Dismiss reuses the canonical Icon Button:

- Style: `Ghost`;
- Size: `Medium` — 40×40px;
- Icon: `close` at the shared 18px Icon Button visual size.

For the canonical RTL layout, Dismiss is absolutely positioned at the physical top-left of the feedback surface:

```text
top = 0
left = 0
size = 40 × 40
```

Equivalent logical runtime intent:

```css
dismiss {
  inset-block-start: 0;
  inset-inline-end: 0;
}
```

Content reserves 32px of left-side internal space. With the surface's 16px outer padding, readable content begins at x=48 while the 40px Dismiss target ends at x=40, preserving an 8px safe gap.

`Dismissible=False` hides the Icon Button without changing content geometry.

Dismiss inherits the full Icon Button accessibility/discoverability contract:

- meaningful accessible action name;
- visible Tooltip on hover and keyboard focus;
- Tooltip does not replace the accessible name;
- no additional tab stop from Tooltip.

For Persian UI, the expected action label / Tooltip text is `بستن`.

High Toast currently applies the required inverse foreground to the nested canonical Icon Button while the shared Icon Button component itself lacks an explicit inverse-surface treatment.

For visible Focus on High Toast:
- Link / Inverse follows the shared Focus Management inverse-context treatment;
- the Dismiss Icon Button must also use the inverse-context Focus treatment when it becomes visibly focused;
- do not silently fall back to the default Focus treatment on surface/inverse.

The Dismiss case remains part of the existing shared inverse-surface Icon Button gap; this Notification contract does not introduce a local Icon Button variant or local Focus token.

## Behavior and Accessibility

Severity and announcement urgency are separate decisions.

- Do not use `role="alert"` merely because Status=Error.
- Routine confirmation should be non-interruptive.
- Do not move focus to a Toast merely because it appeared.
- Interactive controls remain keyboard accessible without automatic autofocus.
- Severity must not rely on color alone.
- If a Toast disappears automatically, users must have sufficient opportunity to perceive and operate it.

Programmatic status/alert behavior is owned by `../../accessibility/dynamic-content-and-feedback.md`.

## Destructive Warning

A pre-action destructive callout uses Danger rather than Error:

```text
surface/danger-muted
fg/danger
fg/primary
line/danger only when anatomy requires it
```

Example distinction:

```text
“This action permanently deletes the job.” → Danger
“Deleting the job failed.”                 → Error
```

## Current Contrast Validation

The current semantic pairings were regression-checked in Figma for JobVision and Cando across Light and Dark on 2026-09-19.

Verified text/action/status foreground pairings used by these components meet at least 4.5:1 in the current token values. Re-run this check when semantic aliases change.

## Figma Reference

### Inline Notification

- Figma file: `rROD8ctH9UfPGAMrRrOzHe`
- Component set: `Inline Notification`
- Node: `22838:3046`
- Component key: `eb09e1db167646902904f70dfd4e3a194a8a265d`
- Matrix: 4 Status variants
- Action composition: native `Action content` Slot

### Toast

- Figma file: `rROD8ctH9UfPGAMrRrOzHe`
- Component set: `Toast`
- Node: `22839:3058`
- Component key: `5c164a8b212650d4e9e322a9088fbc4fc4e7628f`
- Matrix: 4 Status × 2 Contrast = 8 variants
- Action composition: native `Action content` Slot

## Code Reference

Runtime source, Storybook identity, exact prop names, timing constants, and Figma-to-code mapping are unregistered / unverified.

Do not infer runtime props from Figma property names.

## Known Gaps

- exact Toast timeout duration;
- stacking / queue behavior and maximum simultaneous Toasts;
- responsive Toast placement;
- default dismissibility / persistence policy for specific feedback classes;
- actionable Toast persistence/fallback behavior;
- executable live-region / screen-reader tests;
- shared inverse-surface Button treatment for High Toast actions;
- shared inverse-surface Icon Button treatment so High Toast no longer needs a nested foreground override;
- final product-writing guideline and examples.

## Related Documents

- `../patterns/notifications.md`
- `icon-button.md`
- `link.md`
- `../../accessibility/dynamic-content-and-feedback.md`
- `../../foundations/visual/elevation.md`
- `../tokens/color/semantics.md`
- `../tokens/color/usage.md`
