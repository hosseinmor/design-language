---
id: design-system.accessibility.motion
collection: design-system
type: accessibility
title: Motion and Reduced Motion
summary: Defines animation, reduced-motion, flashing, moving/auto-updating content, timing, autoplay, and vestibular-safety guidance.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.pointer-touch-and-gestures
last_reviewed: '2026-09-02'
---

# Motion and Reduced Motion

This document owns **visual motion, animation, time, flashing, and moving/auto-updating content**.

Device/user motion used to operate functionality (shake, tilt, sensor/body motion) is an input-mechanism requirement owned by `pointer-touch-and-gestures.md` under WCAG 2.5.4 Motion Actuation.

## Seizures and flashing

**MUST** meet applicable WCAG 2.3.1 Three Flashes or Below Threshold (Level A). Do not create content that flashes more than the allowed threshold unless the criterion's thresholds are satisfied.

Avoid unnecessary flashing even when technically below the threshold.

## Pause, Stop, Hide — WCAG 2.2.2 A

Moving, blinking, scrolling, or auto-updating content that starts automatically and meets the criterion conditions **MUST** provide the required mechanism to pause, stop, hide, or control update frequency unless an exception applies.

Examples can include auto-advancing carousels, live feeds, or persistent motion that competes with other content.

Do not assume a short one-time state transition falls under the same requirement.

## Timing Adjustable — WCAG 2.2.1 A

Where the product sets a time limit, **MUST** satisfy the applicable WCAG timing-adjustability requirements and exceptions.

Session/security time limits require explicit analysis; do not silently exempt them because they are common.

## Animation from Interactions — WCAG 2.3.3 AAA

WCAG 2.3.3 is Level AAA, not a JV AA baseline requirement.

As a JV **SHOULD**, motion animation triggered by interaction should be disableable when it is not essential and could create vestibular discomfort.

## Reduced-motion preference

**SHOULD** respect `prefers-reduced-motion` or the equivalent supported platform preference for non-essential motion.

Reduced-motion mode should preserve information and task completion. Prefer removing/reducing movement rather than merely making the same movement faster.

Examples to reduce/replace:
- large parallax movement;
- dramatic zoom/pan;
- unnecessary sliding across large distances;
- repeated attention-grabbing animation.

Small state transitions may remain when they do not create material motion risk and still improve comprehension.

## Autoplay media

Audio/video autoplay has separate media/timing requirements. If audio automatically plays for more than the WCAG threshold, provide the required independent mechanism to pause/stop/control volume.

Use `images-icons-and-media.md` for media alternatives/captions/audio-description requirements.

## Loading and progress

Loading indicators may animate, but **SHOULD** avoid large or continuous motion that becomes distracting. Reduced-motion mode may use a static/progress treatment when practical.

Important progress/status meaning must not depend on motion alone; expose programmatic status where required through `dynamic-content-and-feedback.md`.

## Motion is not Motion Actuation

Do not conflate:

```text
visual animation / reduced motion
→ this document

shake / tilt / body-motion input that operates functionality
→ pointer-touch-and-gestures.md → WCAG 2.5.4
```

A reduced-motion implementation does not satisfy Motion Actuation, and a Motion Actuation alternative does not satisfy visual-motion requirements.

## Ownership

Component/Pattern owns its supported transition/autoplay/timing behavior. Product owns whether and when that behavior is used in the flow. Pointer/Touch owns sensor-based motion input.

## Testing

Test applicable flashing thresholds, moving/auto-updating pause/stop behavior, product-set time limits, autoplay, reduced-motion preference, and information retention when motion is reduced.

If the feature also uses device/user motion as input, run the separate Motion Actuation checks in `pointer-touch-and-gestures.md`.

## AI contract

AI **MUST** label AAA criteria accurately, preserve A/AA timing/flashing requirements, distinguish visual motion from motion-actuated input, and avoid turning reduced-motion best practice into an invented WCAG AA rule.

## References

- WCAG 2.2 — 2.2.1 Timing Adjustable
- WCAG 2.2 — 2.2.2 Pause, Stop, Hide
- WCAG 2.2 — 2.3.1 Three Flashes or Below Threshold
- WCAG 2.2 — 2.3.3 Animation from Interactions (AAA)
- WCAG 2.2 — 2.5.4 Motion Actuation (owned by Pointer/Touch)
