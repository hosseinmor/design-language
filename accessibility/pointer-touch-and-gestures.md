---
id: design-system.accessibility.pointer-touch-and-gestures
collection: design-system
type: accessibility
title: Pointer, Touch, and Gestures
summary: Defines target-size, cancellation, gesture, dragging, concurrent-input, hover, and motion-actuation accessibility requirements.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.keyboard-navigation
- design-system.accessibility.motion
last_reviewed: '2026-09-02'
---

# Pointer, Touch, and Gestures

This document owns cross-cutting pointer/touch input requirements, including **device/user motion used as an input mechanism**. Visual animation/reduced-motion behavior remains owned by `motion.md`.

## Target Size (Minimum) — WCAG 2.5.8 AA

**MUST** provide pointer targets at least 24×24 CSS px or satisfy a criterion-defined exception.

The visual icon/glyph may be smaller than the target; hit area and visual size are separate.

**SHOULD** use roughly 40–44 CSS px or larger for frequent/important touch-primary controls where practical.

Dense desktop UI does not need every control enlarged to 44 px when the WCAG minimum/exception is satisfied and larger targets would materially harm information density.

Do not invent an exception merely because a toolbar/table is dense.

## Pointer cancellation — WCAG 2.5.2 A

For functionality operable with a single pointer, **MUST** satisfy the applicable down-event/up-event/undo/reversal requirements.

Prefer activating ordinary controls on `up`/click rather than irreversible action on pointer-down.

For high-impact actions, avoid designs where a slight accidental touch immediately commits an irreversible result.

## Pointer gestures — WCAG 2.5.1 A

Functionality using multipoint or path-based gestures **MUST** also be operable with a single pointer without a path-based gesture unless the gesture is essential.

Examples:
- pinch-only zoom → provide controls if functionality depends on the gesture;
- swipe-path action → provide a simple tap/control alternative where required.

## Dragging Movements — WCAG 2.5.7 AA

Functionality that uses dragging **MUST** be achievable by a single pointer without dragging unless dragging is essential or the user agent determines the behavior.

Examples:
- reorder by drag → also provide Move up/Move down or another discrete control;
- slider thumb drag → native/keyboard/pointer alternatives as appropriate.

Keyboard access is separately required where WCAG Keyboard applies; a non-drag single-pointer alternative is not automatically the same as a keyboard alternative.

## Motion Actuation — WCAG 2.5.4 A

This criterion is owned here because it concerns **input mechanism**, not visual animation.

When functionality can be operated by device motion or user motion detected by sensors/camera:

**MUST**
- provide a user-interface component alternative that operates the same functionality; and
- provide a mechanism to disable responding to motion,

unless an explicit WCAG 2.5.4 exception applies (for example motion is supported through an accessibility-supported interface or is essential to the function).

Examples of triggers:
- shake to undo/refresh;
- tilt to navigate/control;
- camera-detected body/head gesture as the operation mechanism;
- sensor motion that triggers a product action.

Do not confuse this with `prefers-reduced-motion`, visual transitions, parallax, or vestibular animation. Those belong to `motion.md`.

## Concurrent input mechanisms — WCAG 2.5.6 AAA

Do not restrict users to one input modality when other supported input mechanisms are available, unless the restriction is essential, required for security, or needed to respect user settings.

This is Level AAA, so it is not a blanket JV MUST. As a **SHOULD**, avoid breaking keyboard/mouse interaction merely because a touch interface exists and vice versa.

## Hover-only interaction

**MUST** provide keyboard/touch-operable access to functionality that would otherwise be available only on hover.

For content appearing on hover/focus, apply WCAG 1.4.13 where relevant: qualifying additional content must be dismissible, hoverable, and persistent under the criterion conditions.

## Touch gestures and system behavior

**SHOULD** avoid custom gestures that conflict with browser/OS/assistive-technology gestures, especially when ordinary controls can achieve the task.

Do not disable pinch zoom or other user-agent zoom behavior as a design convenience.

## Component ownership

Reusable components should document:
- target-size contract;
- hover dependencies;
- drag and non-drag alternatives;
- custom gesture behavior;
- motion-actuation behavior when they actually use sensors/motion;
- pointer-cancellation behavior where high-impact custom handling exists.

Product/Pattern owns whether such an interaction is appropriate in the business context.

## Testing

Test applicable target dimensions, pointer cancellation, simple alternatives to complex gestures, non-drag alternative for dragging, keyboard access where required, touch/hover discovery, and—when motion actuation exists—the UI alternative plus disable mechanism.

Motion Actuation testing **MUST** be separate from reduced-motion animation testing so a pass in one domain cannot mask a failure in the other.

## AI contract

AI **MUST** route shake/tilt/sensor/user-motion operation here, not solely to Motion; must distinguish 24px WCAG minimum from larger JV touch guidance; must not treat a keyboard alternative as automatically satisfying 2.5.7's single-pointer requirement; and must preserve criterion exceptions accurately.

## References

- WCAG 2.2 — 1.4.13 Content on Hover or Focus
- WCAG 2.2 — 2.5.1 Pointer Gestures
- WCAG 2.2 — 2.5.2 Pointer Cancellation
- WCAG 2.2 — 2.5.4 Motion Actuation
- WCAG 2.2 — 2.5.7 Dragging Movements
- WCAG 2.2 — 2.5.8 Target Size (Minimum)
- WCAG 2.2 — 2.5.6 Concurrent Input Mechanisms (AAA)
