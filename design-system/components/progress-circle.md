---
id: design-system.component.progress-circle
collection: design-system
type: component
title: Progress Circle
summary: Shared circular progress component for measured work and unknown activity; Button and loading patterns consume its indeterminate mode directly.
knowledge_state: verified
document_maturity: final
design_status: ready-for-dev
status: reviewed
owner: Design System team
last_reviewed: '2026-10-19'
related:
  - design-system.pattern.loading-and-progress
  - design-system.component.progress-bar
  - design-system.accessibility.dynamic-content-and-feedback
  - content.pattern.loading-and-progress
  - design-system.reference.component-mapping
topics: [progress, progress-circle, determinate, indeterminate, feedback]
---

# Progress Circle

> **Design contract: Final — HOS-46.** Figma sources and presentation are ready for development handoff. Runtime identity, production motion and executed accessibility tests remain unverified.

## Purpose and Use

Progress Circle is the compact circular form of operation progress. Use **Determinate / Active** for a reliable completed/total ratio and **Indeterminate / Active** for unknown activity. Prefer [Progress Bar](progress-bar.md) when a horizontal track supports reading or comparison. Workflow steps belong to Progress Indicator / Stepper; capacity, scores and ratings are not operation progress.

Button and [Loading compositions](../patterns/loading-and-progress.md) directly use Indeterminate / Active. Loading is a usage pattern, not another component or wrapper.

## Choices

Choose Small 16px, Medium 32px or Large 64px. Stroke widths are 2px, 3px and 4px respectively. There is one line-color treatment, with no Color, Neutral, On color or inverse axis.

| Situation | Mode / State | Appearance |
|---|---|---|
| Ongoing work, reliable value | Determinate / Active | Blue measured arc, including blue 100% |
| Ongoing work, value unknown | Indeterminate / Active | Blue activity arc; no percentage |
| Operation ended, confirmed success worth retaining | Determinate / Success | Complete, static green ring |
| Operation ended, confirmed failure worth retaining | Determinate / Error | Complete, static red ring |

The matrix contains **12 valid variants**: three sizes × four combinations above. Indeterminate Success/Error is unsupported. Terminal states have no editable Progress value, rotation, message slot or built-in status icon.

Only **Active Determinate** exposes the nested Progress value, with 0, 25, 50, 75 and 100% illustrative snapshots. Runtime must accept actual validated intermediate values; Figma presets do not constrain precision. Put any operation name and visible value outside the ring.

## Behavior and States

- Derive the arc and visible value from the same trustworthy completed/total source. Unknown work stays indeterminate; zero is a known value.
- At 0%, show only the neutral track. At 100%, show a complete **blue Active** ring. Full advancement alone does not establish success.
- The normal measured sequence is **Active partial → Active 100% → optional settled Success or Error**, after the real result is known. Do not automatically turn green at 100%, and do not add a fabricated completion delay or confirmation timer.
- Success/Error are stable terminal results, not colored in-flight progress. Their complete ring is an outcome treatment, not a claim that a failed operation transferred 100% of its data. If a task fails before completion, stop its activity and provide honest surrounding failure/recovery feedback; do not animate its numeric value to 100% to enter Error.
- Partial arcs start at the top and advance clockwise in RTL and LTR. Endpoints stay flat; layer and paint opacity remain full.
- Figma uses editable Stroke geometry; runtime may use SVG circles and stroke dashes. No new token, scope change, LoopState or component-specific color role is required.
- The four-phase Figma loop is a reference only. Only Indeterminate / Active rotates. Production timing and reduced-motion behavior require runtime validation.

### Shared progress color contract

| Role | Existing semantic token |
|---|---|
| Track / unfilled path | `line/default` |
| Active arc, including measured 100% | `line/accent` |
| Complete Success ring | `line/success` |
| Complete Error ring | `line/error` |

Progress Circle and Progress Bar share these line roles. Do not substitute foreground or surface tokens for a different visual shade, and do not use `line/inverse` away from an inverse surface. Presentation examples use the ordinary light surface; this does not remove theme support.

## Composition and Content

Loading always uses Indeterminate / Active. Button directly nests the Small 16px ring on a neutral `surface/disabled` busy background; it suppresses the original Brand/Danger tone while preserving its dimensions, focus and accessible operation name. Busy and Disabled remain different semantics, even though they share a neutral background role. Do not replace the blue activity arc with `fg/disabled`.

Success/Error only color the complete ring. The consuming task owns result meaning, visible context, any error explanation and recovery action; the base Circle adds no error-message slot. See [Loading and Progress content](../../foundations/content/patterns/loading-and-progress.md).

## Accessibility

Name the operation. When exposing progressbar semantics, supply truthful current value/range for Active Determinate and omit the current value for unknown activity. Do not announce animation frames. A decorative ring inside an already accessible busy Button/region must not create a duplicate announcement owner.

A terminal Error ring must not expose a fabricated numeric 100% to assistive technology. Announce the actual result with task context; color alone is insufficient. Use stable status semantics for settled outcomes where appropriate rather than leaving a completed result described as ongoing progress. Preserve focus and readable reduced-motion context. See [dynamic content and feedback](../../accessibility/dynamic-content-and-feedback.md) and [color and contrast](../../accessibility/color-and-contrast.md).

## Known Gaps

Figma variants, fixed complete terminal geometry, editable strokes and semantic bindings are verified. Arbitrary numeric authoring in Figma is unsupported. Runtime/Storybook identities, production motion, reduced motion, forced colors and executed assistive-technology tests remain unregistered or untested. Design handoff readiness does not establish runtime release readiness.

## Live References

- [Progress Circle / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24203-116)
- Stable source identities: [component mapping](../../integrations/component-mapping.md).
- Storybook / code: unregistered.
