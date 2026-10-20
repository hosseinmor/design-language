---
id: design-system.pattern.loading-and-progress
collection: design-system
type: pattern
title: Loading and Progress
summary: Loading usage pattern using Progress Circle Indeterminate directly, with measured progress, Skeleton boundaries, stable Button composition and announcement ownership.
knowledge_state: verified
document_maturity: final
design_status: ready-for-dev
status: reviewed
owner: Design System team
last_reviewed: '2026-10-19'
related:
  - design-system.component.progress-circle
  - design-system.component.progress-bar
  - button
  - design-system.accessibility.dynamic-content-and-feedback
  - content.pattern.loading-and-progress
  - design-system.reference.component-mapping
topics: [loading, progress, busy, spinner, skeleton, feedback]
---

# Loading and Progress

**Loading is a usage pattern, not a separate component.** Compose [Progress Circle](../components/progress-circle.md) in **Indeterminate / Active** mode directly with the action or region's task context. Button consumes the same component directly; no Loading wrapper is required.

## Problem

Users need to understand which operation is pending, whether useful progress can be measured, and which actions remain available. An activity indicator must not imply an invented percentage or automatically block the whole interface.

## When to Use

| Available information / context | Feedback |
|---|---|
| Local busy action, no reliable total | Progress Circle / Indeterminate |
| Known completed work and reliable total | Progress Circle / Determinate or Progress Bar / Determinate |
| Operation already represented by a linear track, progress unknown | Progress Bar / Indeterminate |
| Expected content structure is useful while initial data is pending | Skeleton |
| Ordered workflow steps | Progress Indicator / Stepper |

Choose by useful context and the affected area. No universal time threshold is defined. Static capacity, ratings and scores are not operation progress.

## Structure

The pattern consists of an indicator, understandable task context and a clear busy scope. The context can be the existing Button name, adjacent status text, or the labelled content region; every spinner does not require a new message or live region.

## Behavior

- Use Indeterminate for unknown or unreliable progress; expose no guessed percentage or ETA. Switch to Determinate when a trustworthy value and total become available.
- Keep known zero distinct from unknown work. Fill and visible percentage must share the same real source. Measured completion stays blue at 100%. Only after the real result is known may the consuming flow optionally show a complete, static Determinate Success/Error ring. A complete Error ring describes an outcome, not 100% successful transfer; never fabricate progress to enter it.
- Block only dependent interactions and prevent duplicate activation. The flow owns whether other actions are blocked; the indicator does not define that policy.
- Preserve keyboard focus and the operation's accessible name. Loading must not itself move focus.
- Rotation remains clockwise in RTL and LTR. Respect reduced-motion preferences while keeping readable busy context. Figma's four-phase reference does not establish validated production animation or final shared motion timing.

## Component Composition

- **Button:** directly nest Progress Circle / Indeterminate / Active / Small, 16px at every Button size. Preserve width, height and label/icon layout space while visually hiding the replaced content. Keep the ring centered when labels and optional icons change.
- **Inline status:** Small ring at logical start, with an 8px gap to text. In RTL it appears to the right. Let long text wrap without shrinking the ring or changing its position.
- **Local content region:** Medium is the normal choice; Large fits an appropriately large area. Center feedback within the affected region and identify the pending operation.
- Use `line/default` for the track and `line/accent` for the arc, at full opacity with flat endpoints. There is one activity treatment. No Loading-specific color tokens, Color axis, LoopState property, Inline size or outcome family is introduced.
- Every Loading Button uses the neutral `surface/disabled` background with no style border, keeping the canonical blue activity arc and neutral track. This replaces Brand/Primary/Danger backgrounds while busy. Preserve dimensions and keyboard focus treatment. Loading takes visual precedence over interaction tone, including authored Loading + Disabled combinations; it does not change the operation into an unavailable/Disabled semantic state.

## Variations

Choose the Circle size for the local scope. Loading uses **Indeterminate / Active only**. Success/Error are complete static Determinate outcomes after the operation ends; they are not Loading variations. Loading adds no public component API or wrapper.

## Accessibility

The consuming action or region owns its accessible name, busy state and announcements. Treat its nested ring as decorative when that context already communicates the operation. Avoid duplicate status messages or competing live regions. When exposing progressbar semantics, provide a truthful numeric value/range for determinate work and omit the current value for indeterminate work. Do not announce animation frames. Follow [dynamic content and feedback](../../accessibility/dynamic-content-and-feedback.md) and [Loading and Progress content](../../foundations/content/patterns/loading-and-progress.md).

## Product Examples

The [Figma Loading · Pattern page](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24144-128998) demonstrates RTL inline status, local regions, larger areas, neutral busy Button compositions and long mixed-script text on ordinary light surfaces. These are design compositions, not evidence of product-specific behavior.

## Anti-Patterns

- Fabricated progress or a percentage on indeterminate activity.
- A separate Loading wrapper duplicating Progress Circle.
- Success/Error/Inactive variants on the activity indicator.
- Layout shifts or loss of the Button's operation name/focus.
- One live region for the Button and another announcing the same nested ring.

## Verification and Live Sources

HOS-46: all 160 loading Button masters and three File Uploader spinner sources directly use Progress Circle; current examples were migrated. Old Loading masters were removed after their instance count reached zero. The unused legacy Inline status family was also removed. All Loading Button masters now have neutral busy backgrounds and the shared line-token activity treatment; Circle has 12 valid variants with complete static Determinate outcomes. Figma geometry and semantic bindings are verified; runtime/Storybook identities, production motion, reduced motion and executed assistive-technology behavior remain unregistered or untested.

- [Progress Circle / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24203-116)
- [Loading · Pattern](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24144-128998)
- Stable source identities: [component mapping](../../integrations/component-mapping.md).
