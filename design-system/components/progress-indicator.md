---
id: design-system.component.progress-indicator
collection: design-system
type: component
title: Progress Indicator
summary: Carbon-derived RTL progress indicator for known, ordered multi-step workflows, with explicit current/completed/incomplete/error/disabled states and compositional Figma authoring.
knowledge_state: verified
document_maturity: final
design_status: ready-for-dev
design_maturity: handoff-ready
last_reviewed: '2026-10-15'
related:
  - design-system.component.timeline
  - design-system.component.breadcrumb
  - design-system.component.tabs
  - design-system.accessibility.core
  - design-system.accessibility.forms
  - design-system.reference.component-mapping
---

# Progress Indicator

## Purpose

Progress Indicator shows a user's position in a **known, ordered sequence of workflow steps**.

Use it when:

- the flow has a defined sequence;
- users benefit from knowing what is completed, current, and still ahead;
- validation may block the current step;
- the sequence is part of a task or workflow, not a chronological event history.

Examples include job-posting flows, approval flows, hiring-request workflows, setup flows, and other multi-step product tasks.

The component is primarily **progress/status presentation** in v1. It does not ship with built-in step-navigation interaction.

## Not for

Do not use Progress Indicator for:

- **operation progress or percentage completion** such as upload, loading, installation, or processing; use a Progress Bar/loading pattern;
- **chronological event history**; use Timeline;
- **hierarchical location** in the product; use Breadcrumb;
- **switching between peer views**; use Tabs or Content Switcher;
- **a single binary state**;
- arbitrary milestones that do not form one ordered workflow.

Progress Indicator answers **"where am I in this workflow?"**. Timeline answers **"what happened, and when?"**.

## Verified Figma identity

- Figma file: `[DS] Job Vision NEXT`
- File key: `rROD8ctH9UfPGAMrRrOzHe`
- Page: `Progress indicator`, node `521:16785`
- Canonical documentation frame: `Progress indicator / Documentation`, node `23730:499`
- Item component set: `_Progress indicator item`, node `23704:348`, component key `ebd4a7beb03d58ea243faaed501712880ffa2669`
- Parent component set: `Progress indicator`, node `23704:699`, component key `335d54d47ea28e6329f88a8bb34dc3b2d02e5c77`

Figma review link:
https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23730-499

The component identities above were read directly from the owning Figma source on 2026-10-15. A Figma component key proves design identity; it does **not** by itself prove shared-library publication, Code Connect, or an existing runtime implementation.

## Component architecture

Progress Indicator uses two compositional component sets.

### Progress indicator

The parent component owns direction and an extensible native Figma slot:

| Property | Values | Contract |
|---|---|---|
| `Direction` | `Horizontal`, `Vertical` | Layout orientation |
| `Items` | native `SLOT` | Contains Progress Indicator Item instances |

Variant count: **2 = Horizontal / Vertical**.

Each Direction variant exposes one native `Items` slot with **three default Progress Indicator Item instances**. Designers may add or remove Item instances directly inside the slot when a product flow needs a different step count.

The default three-item composition terminates its connector correctly. When a designer adds a new terminal Item in Figma, they must:

1. set `Show connector=true` on the previous terminal Item;
2. keep `Show connector=false` on the new terminal Item.

This connector adjustment is a Figma authoring responsibility only. Runtime must derive terminal connector visibility from item position automatically.

### Progress indicator item

The Item owns status, content, marker, and connector.

| Property | Values | Contract |
|---|---|---|
| `Direction` | `Horizontal`, `Vertical` | Changes item anatomy/layout |
| `State` | `Incomplete`, `Current`, `Completed`, `Error`, `Disabled` | Workflow step state |
| `Label` | text | Required visible step name |
| `Helper` | text | Optional helper/error content |
| `Show helper` | Boolean; default `true` | Shows Helper directly below Label |
| `Show connector` | Boolean; default `true` | Connector visibility; normally false on terminal Item |

Variant count: **10 = 2 Direction × 5 State**.

The Item owns the visual line between steps. The parent owns **which Item is terminal**.

## Anatomy

Conceptually:

```text
Progress Indicator Item
├── Connector
└── Content
    └── Icon + Label
        ├── Text
        │   ├── Label
        │   └── Helper (optional)
        └── Marker
```

In Vertical orientation, the same contract is arranged vertically while keeping the marker/connector as the step axis and the text block aligned for RTL reading.

The Helper belongs to the step text block and sits **directly below Label**. It is not a separate row below the whole component.

## State model

| State | Meaning | Visual role |
|---|---|---|
| `Incomplete` | Future/upcoming step not yet reached | Outline marker, neutral connector, secondary label |
| `Current` | Current active step | Filled marker, accent connector, primary label |
| `Completed` | Successfully completed step | Check-circle marker, accent connector, primary label |
| `Error` | Current step has a validation/problem state requiring correction | Error marker, neutral connector, primary label, error Helper |
| `Disabled` | Step is genuinely unavailable/disabled | Muted marker and disabled text |

### State rules

- **Error replaces Current** for the affected step. Do not render a separate Current step and a second Error step for the same position.
- Do not mark a future step Disabled merely because it has not been reached. Use Incomplete for ordinary future steps.
- Completed means the step has been successfully passed; do not use it as a general "seen" state.
- Current and Error are mutually exclusive visual states for one step.
- A sequence may contain multiple Completed steps before the Current/Error step and multiple Incomplete steps after it.
- Product logic owns whether Disabled is valid for a particular workflow.

## Visual contract

The final visual direction deliberately preserves Carbon-like progress-indicator anatomy while using Job Vision's approved marker assets and tokens.

### Marker assets

All marker instances are **20×20px**.

| State | Marker |
|---|---|
| Incomplete | `Icon / dot mark outline`, key `47cb7ef73c7f7b92cf2c75417bd7127caad65dd5` |
| Current | `Icon / dot mark`, key `e21ceabe6cd6cb4e516aa85d1b0da9042292a393` |
| Completed | `Icon/check_circle_outline`, key `a39add6efe2e57f5725795447e3341f9226ee319` |
| Error | `Icon/error_outline`, key `8a13f550e18df97ee7ccfa5b5369f774fc37c797` |
| Disabled | Incomplete outline marker at reduced opacity |

Do not redraw equivalent markers inside Progress Indicator. Use the approved DS Icon components.

### Connector

- thickness: **3px**;
- Current / Completed connector: `line/accent`;
- Incomplete / Error / Disabled connector: `line/default`;
- terminal Item: connector hidden;
- connector is decorative and must not carry the only representation of state.

### Typography

- Label: `Label/SM`;
- Helper: `Body/Compact/XS`;
- Label-to-Helper gap: **4px**;
- `Show helper` currently defaults to `true` in the Figma master; turn it off when a step has no supporting or validation copy.

State foregrounds:

- Incomplete Label: `fg/secondary`;
- Current / Completed / Error Label: `fg/primary`;
- Disabled Label: `fg/disabled`;
- normal Helper: `fg/secondary`;
- Error Helper: `fg/error`;
- Disabled Helper: `fg/disabled`.

### Text limits

Horizontal:

- Label: maximum **1 line**, ending truncation;
- Helper: maximum **2 lines**, ending truncation.

Vertical:

- Label: maximum **2 lines**, ending truncation;
- Helper: maximum **3 lines**, ending truncation.

If meaningful step copy cannot fit these limits, prefer rewriting the label, moving supplementary information to Helper, or using Vertical. Do not keep expanding a horizontal step until it becomes unreadable.

### Geometry

Current canonical authoring geometry:

- marker: **20px**;
- connector: **3px**;
- Horizontal Item minimum width: **128px**;
- Horizontal content begins **8px** below the connector;
- marker-to-label row spacing: **8px**;
- Label-to-Helper: **4px**;
- component has no card, shadow, or independent surface.

The fixed widths used by Figma masters are authoring examples, not runtime page-width requirements.

## Horizontal and Vertical usage

### Horizontal

Use Horizontal when:

- there are roughly 3–6 concise steps;
- the available width can preserve at least the component's intended minimum step width;
- helper/error content is short;
- seeing the whole workflow at once is useful.

Do **not** squeeze Horizontal below a readable width only to keep every step visible.

### Vertical

Prefer Vertical when:

- step labels are longer;
- helper/error content is likely;
- the container is narrow;
- the number of steps or content density makes Horizontal hard to scan.

Vertical order stays top-to-bottom in RTL.

## Responsive boundary

There is **no Compact/mobile Progress Indicator variant in v1**.

**Mobile / narrow-width breakpoint and minimum supported size: TBD.**

Until that size is defined, use the following boundary:

1. do not compress the full Horizontal component below its usable width;
2. prefer Vertical when the product still needs to show the whole sequence;
3. a product may choose a separate mobile composition if required, but that is **not currently part of the shared component contract**.

A progress bar or segmented mobile track is not part of v1. Add one only after a validated product need and a separate design-system decision.

## Error and Helper behavior

Helper provides supplementary step information and validation feedback.

- Helper appears directly below the Label.
- `Show helper` currently defaults to `true` in Figma; disable it when no supporting or validation copy is needed.
- Error Helper uses `fg/error`.
- An Error step should contain enough text to explain what needs attention; do not rely only on the Error icon or color.
- Validation belongs to the current workflow step. Do not style unrelated future steps as Error.
- Helper may be used outside Error when product copy genuinely adds useful context, but avoid repeating what the Label or marker already communicates.

## Interaction

The v1 Progress Indicator is **noninteractive by default**.

It does not define:

- hover;
- pressed/active interaction;
- focus;
- click-to-navigate behavior;
- keyboard step switching.

Do not infer that a step is clickable because it visually resembles a navigation item.

If a product needs navigation to previous steps, define that behavior deliberately at the product/pattern level or through a future shared interactive extension. Do not make future steps implicitly clickable.

## Figma designer workflow

1. Insert `Progress indicator`.
2. Select `Direction`.
3. The native `Items` slot starts with three default Progress Indicator Items.
4. Select nested Items and set `State`, `Label`, and optional `Helper`.
5. To add a step, place another Progress Indicator Item inside the `Items` slot in sequence order.
6. When adding a new terminal Item, enable `Show connector` on the previous terminal Item and disable it on the new terminal Item.
7. `Show helper` currently defaults to `true`; disable it when the step has no supporting or validation copy.
8. Use Vertical instead of forcing dense or long content into Horizontal.

The three default Items are an **authoring starting point**, not a product-data limit. Runtime sequence length remains data-driven.

## RTL

RTL is the default Job Vision presentation.

- Horizontal visual progression is mirrored for RTL without reversing the workflow's semantic order.
- Runtime should preserve source/data step order and use logical layout/direction to render the visual sequence.
- Vertical progression remains top-to-bottom.
- Labels and Helper text are right-aligned in RTL.
- Mixed Persian/English labels must preserve readable bidi behavior.
- Do not encode sequence order only through physical left/right assumptions.

## Accessibility

Progress Indicator exposes ordered workflow position and state; decorative geometry alone is insufficient.

Runtime implementation **SHOULD**:

- expose the steps as an ordered sequence, for example an `<ol>` with one `<li>` per step;
- mark the current step with `aria-current="step"` or an equivalent supported semantic;
- expose Completed / Current / Incomplete / Error / Disabled meaning in accessible text or state, not color alone;
- associate Error Helper content with the affected step;
- hide decorative connectors from assistive technology;
- avoid announcing both a decorative marker icon and identical redundant status text;
- preserve meaningful reading order in RTL.

Because v1 is noninteractive, the base Progress Indicator should not create unnecessary focus stops.

If a future interactive version is introduced, it requires a separate keyboard/focus contract rather than inheriting semantics from the passive component.

## Development implementation contract

This section defines required behavior; it does **not** claim that a runtime API already exists.

### Runtime data model

A runtime implementation should accept a dynamic ordered sequence of workflow steps.

Conceptually, each step needs:

- stable identity;
- visible label;
- workflow state;
- optional helper/validation content.

These are conceptual fields, not verified TypeScript/Angular prop names.

### Runtime rules

- Do not treat Figma's three default slot Items as a runtime data limit.
- Derive the number of Items from the supplied step data.
- Derive terminal connector visibility from array position; consumers should not coordinate the final connector manually.
- Render exactly one Item per workflow step.
- Preserve the supplied semantic order.
- The component does not sort or reorder steps.
- Error is a state of the current step, not an extra workflow step.
- Responsive layout choice should preserve readability; do not automatically shrink step geometry below the visual contract.
- Runtime may render any validated step count required by the product flow, but product design must choose an appropriate layout rather than assuming a longer horizontal sequence is always usable.

### Suggested semantic shape

A framework may use a structure equivalent to:

```text
ProgressIndicator
└── ordered list
    ├── ProgressIndicatorItem
    ├── ProgressIndicatorItem
    └── ...
```

Exact component names, Angular inputs, DOM wrappers, event names, and TypeScript types remain unverified until the owning runtime Design System source is registered.

## Acceptance tests — Storybook bypass

| Test | Required result | Status |
|---|---|---|
| Figma Direction × State matrix | 10 Item variants render correctly | **Verified in Figma** |
| Figma parent Direction variants | 2 parent variants: Horizontal / Vertical | **Verified in Figma** |
| Native Items slot | One shared SLOT property in both Direction variants | **Verified in Figma** |
| Default slot content | 3 Progress Indicator Item instances in each Direction variant | **Verified in Figma** |
| Add-item authoring | A fourth Item can be added successfully inside an instance slot | **Verified in Figma** |
| Default terminal connector | No connector after the default terminal Item | **Verified in Figma** |
| Helper default | `Show helper=true` in the finalized Figma master | **Verified in Figma** |
| Helper placement | Directly below Label | **Verified in Figma** |
| Typography | Label = Label/SM; Helper = Body/Compact/XS | **Verified in Figma** |
| Horizontal text limits | Label 1 line; Helper 2 lines; ending truncation | **Verified in Figma** |
| Vertical text limits | Label 2 lines; Helper 3 lines; ending truncation | **Verified in Figma** |
| Error scenario | Error replaces Current; Error Helper visible | **Verified in Figma** |
| RTL presentation | Horizontal/Vertical examples read correctly in RTL | **Verified in Figma** |
| Runtime dynamic count | Correct rendering from product step data without a 3–6 API cap | **Required in development** |
| Runtime connector termination | Exactly one connector between adjacent steps, none after final step | **Required in development** |
| Runtime semantics | Ordered sequence, current-step semantics, non-color status communication | **Required in development** |
| Runtime responsive behavior | No unreadable horizontal compression; layout choice preserves text/state meaning | **Required in development** |
| Mobile size / breakpoint | Define the narrow-width breakpoint/minimum supported size | **TBD** |

Storybook is **not required** for this design handoff phase. Runtime tests and accessibility QA remain development responsibilities.

## Benchmark rationale

The final direction uses **Carbon Progress Indicator** as the primary visual/anatomy reference:

- dedicated marker row / axis;
- distinct Completed, Current, and future states;
- label/helper content separated from the connector;
- Horizontal and Vertical forms.

JV intentionally modifies the marker language and component architecture rather than copying Carbon implementation details.

Other benchmark findings informed boundaries:

- USWDS and MUI demonstrate compact/mobile alternatives, but JV deliberately leaves a Compact mode out of v1;
- Atlassian Progress Tracker reinforces the known-stage/workflow use case;
- continuous Progress Bar patterns are treated as operation/proportion progress, not a substitute for discrete workflow steps.

External design systems are references, not runtime sources for Job Vision.

## Figma QA performed

- [x] Canonical Item set reduced to `Direction × State`.
- [x] Canonical Parent set reduced to `Direction` only.
- [x] One native shared `Items` SLOT property exists in Horizontal and Vertical variants.
- [x] Each slot contains three default Items.
- [x] Adding a fourth Item to an instance slot was structurally verified.
- [x] Carbon-like anatomy retained while JV marker assets replace Carbon iconography.
- [x] 20px marker assets verified.
- [x] 3px connectors verified.
- [x] Connector semantic tokens verified: Current/Completed accent; future/error/disabled neutral.
- [x] Default three-item terminal connector behavior verified; Figma add/remove workflow documents the required previous/new terminal connector adjustment.
- [x] Label/SM and Helper Body/Compact/XS verified.
- [x] Finalized Figma default verified: `Show helper=true`.
- [x] Helper sits directly below Label.
- [x] Horizontal and Vertical text-line constraints verified.
- [x] Current-step Error scenario verified in Playground.
- [x] RTL layout visually reviewed.
- [x] Legacy/Expressive explorations archived/hidden from the canonical review surface.
- [x] Compact/mobile experiment removed from the v1 component contract.
- [x] Canonical documentation presentation rebuilt using the shared component-page presentation pattern.
- [x] Final Figma structural/visual audit completed 2026-10-15.
- [ ] Runtime implementation tests and accessibility review after development.
- [ ] Shared-library publication status / Code Connect if required later.

## Runtime / Storybook status

Code repository/package: **Unregistered**

Runtime component/API: **Unverified**

Figma parent authoring: **Direction + native Items SLOT with 3 default Items**

Storybook: **Bypassed for current handoff**

Figma property → runtime prop mapping: **Unverified**

Code Connect: **No registered mapping**

Do not infer production Angular inputs, event names, DOM structure, or state enums from Figma property labels alone.

## Migration notes

The previous Carbon-derived assets and Expressive exploration were retained only as hidden/archive material during design reconciliation.

Canonical v1 now uses:

- `_Progress indicator item` — node `23704:348`;
- `Progress indicator` — node `23704:699`;
- documentation frame `23730:499`.

Removed from the canonical contract:

- legacy Count-axis / fixed-count composition;
- Expressive duplicate;
- Skeleton state;
- Compact/mobile variant;
- step-number property experiment;
- visual explorations that were not part of the final component.

The canonical contract is intentionally small: workflow state and item content live on the Item; Direction and the native extensible Items slot live on the Parent; runtime sequence length remains data-driven.
