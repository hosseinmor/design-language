---
id: design-system.component.skeleton
collection: design-system
type: component
title: Skeleton
summary: Composable content placeholders with Text, Block and Circle primitives, one shared Shimmer motion utility, and region-owned loading feedback.
knowledge_state: canonical
document_maturity: final
design_status: ready-for-dev
design_maturity: handoff-ready
status: reviewed
owner: Design System team
last_reviewed: '2026-10-19'
related:
  - design-system.component.progress-bar
  - design-system.pattern.loading-and-progress
  - design-system.foundation.motion
  - design-system.accessibility.motion
  - design-system.accessibility.dynamic-content-and-feedback
  - design-system.reference.component-mapping
topics:
  - skeleton
  - loading
  - shimmer
  - composition
  - reduced-motion
  - accessibility
---

# Skeleton

> **Final v1 design contract — HOS-47.** The primitive family, composition rules and Shimmer direction are approved for design handoff. Motion values below apply now and carry an explicit **TBD review after shared Design System Motion foundations are completed**. Runtime exports, implementation, browser performance and executed accessibility behavior remain unverified.

## Purpose and classification

Skeleton reserves the recognizable structure of content while its data is loading. It communicates pending content, not a percentage, disabled action, empty result or failure.

- **Component:** the reusable Text, Block and Circle placeholder primitives.
- **Motion behavior:** Shimmer, shared by all primitives through one intended `animate-skeleton` utility.
- **Composition patterns:** card, list and table loading layouts built from the same primitives. These examples are not separate fixed public components for every product screen.

Figma component classification does not require a separate Angular component. A runtime may use the shared utility with ordinary layout/shape utilities, provided this contract is preserved.

## Choose by meaning

| Need | Use |
| --- | --- |
| Data is pending and the expected content layout is known | Skeleton |
| A local action or region is busy without useful content-shaped placeholders | Appropriate Loading / Spinner feedback |
| An ongoing operation has measurable completed work | Progress Bar — Determinate |
| An ongoing operation needs linear busy feedback but reliable progress is unknown | Progress Bar — Indeterminate |
| Loading finished without content, or failed | The owning empty/error/recovery treatment |

Do not invent universal duration thresholds for choosing a loader. Avoid brief distracting flashes, but do not impose an artificial minimum wait, wait for a Shimmer cycle to finish, or withhold already available content. Product-specific scheduling, debounce, timeout and retry policies belong to their owners.

## Primitive contract

| Shape | Meaning and geometry | Radius |
| --- | --- | --- |
| **Text** | One text-line placeholder. The current reference is a 24px Body/SM line box with a centered 12px visible bar. Width follows the expected text measure. | Small |
| **Block** | Media or another non-text content area. Width, height and aspect ratio follow its expected container. | Medium by default; match the actual container where needed |
| **Circle** | Circular avatar/image placeholder. Keep width equal to height when resizing. | Full |

- Width and height are geometry, not Small/Medium/Large variants.
- The Text reference is not a universal typography size. For another text role, adjust the line box and visible-bar geometry to the intended text metrics; do not scale a whole composition to fit.
- Preserve the expected text line boxes, media aspect ratio, columns and row density so content can replace the placeholders without avoidable layout shift.
- Skeleton has no Hover, Focus, Selected, Disabled, Success or Error states and exposes no actions.

## Composition

- **Multiline text:** compose line instances at the target line-height rhythm. A shorter final line may suggest a paragraph; align it to reading start (right in RTL, left in LTR). Lengths are illustrative and must not imply data already known. Do not randomize widths every animation cycle.
- **Avatar/media:** use Circle for a circular avatar and Block for rectangular media. Reserve the actual display geometry.
- **Cards/lists:** replace only pending data. Keep known labels, structural containers, navigation and available content. Use a representative visible count, not a promise about the eventual number of results.
- **Tables:** retain known headers and table structure. Align placeholder values to their columns and preserve the intended row density; selection controls and actions do not become decorative Skeleton controls.
- **Forms:** retain known labels and form structure. Do not replace an entire form or its controls with Skeleton states merely because a dependent value is pending.
- **Incremental loading:** reveal content as it becomes usable. On refresh, retain useful loaded content where practical and communicate the local busy state instead of blanking the whole view.
- **Responsive/RTL:** use the real container widths and reflow rules. Primitives are direction-neutral; text composition follows reading direction. The ornamental Shimmer direction stays the same in RTL.

The Playground examples are generic composition evidence, not canonical product behavior or a comprehensive audit of existing screens.

## Motion — single Shimmer utility

The intended public interface is **one `animate-skeleton` class** on each filled placeholder surface. The class controls the motion; shape, size, radius and layout remain owned by the component/composition. Do not apply a single opaque sweep over a whole card including its gaps or text labels.

| Parameter | Approved v1 design value |
| --- | --- |
| Complete cycle | **1800ms**, repeating while the surface is loading |
| Easing | **linear** |
| Direction | Left to right, independent of RTL |
| Band | **60%** of the individual surface width; feathered transparent edges |
| Intensity | Existing Shimmer color at **50% opacity** over Base at the band center; equivalent to a 50/50 blend |
| Loop boundary | Band starts fully outside the left edge and ends fully outside the right edge, hiding the reset |
| Rhythm | Shared duration; no deliberate random stagger; global synchronization across separately mounted regions is not required |
| Geometry | Stationary shape; no scaling, translation or layout change of the placeholder itself |
| Ready content | Immediate replacement with a **150ms ease-out opacity fade**, without slide/scale |
| Reduced motion | Static Base placeholders and direct replacement, without Shimmer or reveal fade |

The owning loading region triggers the ready-content transition; a shape utility cannot infer data readiness. Stop unnecessary animation when the loading surface is removed/hidden. Do not invent a public Pulse option or per-product timing overrides.

### Semantic tokens

Use existing `utility/skeleton-base` for the placeholder surface and `utility/skeleton-shimmer` for the moving highlight. Transparent gradient edges and the 50% center opacity are derived treatment, not new color tokens.

No new color, component or motion tokens were created for v1. Older `skeleton-element` and `skeleton-background` roles are not required by this recipe; this pilot does not delete or migrate them.

### TBD — reconcile with shared Motion foundations

**Owner: Design System team. Trigger: shared Design System Motion rules are completed/reviewed.**

Revisit:

- the 1800ms Shimmer cycle and linear easing;
- the 150ms reveal duration and ease-out curve;
- highlight width/intensity and repetition guidance;
- whether approved shared motion tokens should replace locally defined recipe values.

Until that review, the v1 values above remain the approved implementation target. This planned maintenance is not an unresolved choice between Pulse and Shimmer and is not a handoff blocker. Preserve immediate content delivery, stable geometry and reduced-motion support when revising values. Update this contract, Figma notes/preview and any registered runtime recipe together.

## Accessibility

- Skeleton shapes are decorative and non-interactive: hide them from assistive technology, normally with `aria-hidden="true"`. They must not enter the tab order or present themselves as unavailable real controls.
- The **owning region** communicates loading. When appropriate to that region's semantics, set `aria-busy` from the actual loading state and clear it when the relevant update completes. Busy state is not itself a guaranteed spoken announcement.
- Provide one concise, contextual loading/status announcement when necessary, usually with polite status semantics. Do not announce every bar, avatar, row or animation cycle. Keep the status mechanism outside a busy region when deferring that region would suppress the intended message.
- Preserve keyboard focus during replacement. Do not focus Skeletons or move focus solely to announce loading. If content replacement removes the focused element, follow the owning component's focus-management contract.
- Honor the platform reduced-motion preference using the static/direct treatment above. Loading meaning must remain available without motion.
- On completion, empty results or failure, clear the busy state and expose the appropriate outcome/recovery feedback. Do not leave a perpetual Skeleton as the error treatment.

See [Dynamic Content and Feedback](../../accessibility/dynamic-content-and-feedback.md) and [Motion and Reduced Motion](../../accessibility/motion.md) for shared standards. Figma visuals and an animated specimen do not establish runtime accessibility conformance.

## Figma source and presentation

File: `rROD8ctH9UfPGAMrRrOzHe` — **[DS] Job Vision NEXT**.

- [Skeleton / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24146-47) — page `24146:46`, presentation `24146:47`.
- Public **Skeleton** set: node `24146:62`, key `d38438dc508671b18e814db895f0cab0cc13b95e`; one Shape axis and three variants. Public masters retain their original identities.
- [Shimmer visual sequence](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24212-63) — node `24212:63`, inside Playground.
- [Native Motion preview](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24212-110) — frame `24212:110`, beside the documentation. Play its timeline for the illustrative sweeps/reveal.

The presentation uses **00 Header → 01 Component set → 02 Playground → 04 Usage & handoff**. Section 01 contains the actual public master set; Playground uses connected instances. No internal-source section or extra public animation-state variants are needed.

The native timeline illustrates two loading cycles and a reveal; its fixed wait is demonstration choreography, not an application loading-delay requirement. The rest-state master family remains simple/static for authoring. Motion-preview gradients are derived from the existing Semantic highlight at creation; production must resolve live theme tokens. Component mapping owns individual variant keys and runtime registration gaps.

## Handoff and verification

**Design handoff:** primitive construction, semantic bindings, source-linked composition examples, native motion reference and the explicit Motion-review TBD.

**Runtime implementation must verify:** text/media geometry at narrow and wide widths; Light/Dark token resolution; clipping and loop reset; the 1800ms/150ms behavior; immediate readiness/empty/error transitions; reduced motion; no focusable decorative elements; one appropriate region-level status mechanism; focus preservation; and performance with many visible rows.

Runtime repository/package exports, class availability, API and Storybook are **unregistered/unverified for this component**. The intended utility name is a design contract, not proof it is already exported. Existing product consumers have not been exhaustively audited; migration remains a separate check.
