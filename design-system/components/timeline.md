---
id: design-system.component.timeline
collection: design-system
type: component
title: Timeline
summary: A compositional vertical RTL sequence of chronological events or scheduled time groups, shared by Job Vision My Applications and employee Onboarding.
knowledge_state: verified
document_maturity: draft
design_status: ready-for-dev
design_maturity: handoff-ready
last_reviewed: '2026-10-14'
related:
  - design-system.component.progress-indicator
  - design-system.accessibility.core
---

# Timeline

## Purpose

Timeline presents **what happened** or **what is scheduled at specific points in time**, in a vertical chronological sequence. Event content is variable, and event count is not a fixed workflow stage model (the Figma parent displays 1–6 for composition). It is primarily read-only.

Current pilot supports two verified product use cases:

1. **Onboarding — scheduled task groups:** each relative date/time group is a Timeline Item, with one or more tasks composed inside the Content slot. Examples: «۷ روز قبل از شروع کار» and «روز شروع کار».
2. **Job Vision / My Applications — event history:** each application event is a Timeline Item, usually with a title, timestamp, and event-type icon. Examples: application sent, resume seen, review prioritized, application approved.

Both use the same Figma primitives. Do not create `ScheduleTimeline` or `ApplicationTimeline` variant axes.

## Not for

- **Progress Indicator / Stepper (HOS-31):** fixed sequence of known workflow steps with complete/current/upcoming/blocked statuses (e.g. hiring request approval). Use the Stepper, whether showing a workflow preview or the progress of an actual request.
- **Activity Feed:** comment/mention/reaction-centric interactions and conversations.
- **Audit Log:** technical before/after change records, actor/field-level audit, or immutable compliance history.
- Horizontal, alternating, or two-sided sequences in v1.

The Timeline must not acquire Stepper's completed/current/upcoming state model.

## Verified Figma identity

- Figma file: `[DS] Job Vision NEXT`
- File key: `rROD8ctH9UfPGAMrRrOzHe`
- Page: `Timeline`, node `23509:9`
- Component set: `Timeline Item`, node `23509:48`, Figma key `3d90d9035ecdfe4f210b8602b8d8d93e8f59e7da`
- Parent component set: `Timeline`, node `23609:126914`, Figma key `70716c3cb413b2669f06596426cea18ff7f7c92a` (`Count=1..6`). The original parent master `23509:49` is retained as the `Count=4` variant.
- Canonical presentation frame: `23618:417` (2528px reference-aligned format, matching the Textarea presentation at `22880:132462`), containing Header, variant matrix with both live component sets, side Axes & Properties panel, Internal anatomy cards, and a unified Playground for Onboarding, My Applications and narrow RTL QA. The earlier frame `23576:15065` was archived in a hidden legacy frame.
- Canonical Playground board: `23618:127314`, containing the live product preview cards `23511:13375` (Onboarding) and `23511:13482` (My Applications). The old standalone Playground wrapper `23511:13370` is no longer the canonical review surface.
- Narrow/long-title QA: `23519:121`, verified at 360px width
- Neutral DS marker icon: `Icon/dot`, node `23609:9`, Figma key `e9def3d417c05352d5f86ed6d7553755399fd22d` (24px icon containing a centered filled dot; override semantic color in context).

Figma review link: https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23618-417

Figma component identity keys above were read directly from the owning Figma source on 2026-10-14. Whether these components have been **published to a shared Figma Library** is not verified; do not mistake an identity key for publication. Runtime component identifiers and Figma-to-code mappings remain unregistered.

## Component contract (Figma)

### Timeline

`Timeline` is a vertical auto-layout **component set with one `Count` axis (`1`, `2`, `3`, `4`, `5`, `6`)**. Each variant contains six nested Timeline Item instances, of which the first `Count` items are visible. Default is `Count=4`. This deliberately replaces the fragile `Show item 1–6` Boolean properties, which allowed a broken/disconnected connector chain. In each Count variant, all visible items except the last show their connector; the final item does not. **Switching Count automatically yields the correct connector chain without designer intervention** and preserves matching nested text and Content Slot overrides (tested on the Onboarding task list). Designers edit titles, timestamps and icons by selecting nested items.

Figma is capped at six event items for review/design convenience; a longer list needs a larger explicit composition or a data-driven runtime implementation. This maximum is **not a product/runtime data limit**. The Timeline does not sort input data or carry Stepper-like statuses.

### Timeline Item

Structure:

```
Timeline Item
├── Content (vertical, RTL right-aligned)
│   ├── Header (4px vertical gap)
│   │   ├── Title (TEXT property)
│   │   └── Timestamp (TEXT property, optional via BOOLEAN)
│   └── Content slot (native Figma SLOT, optional and hidden by default)
└── Axis (24px, right-hand side in RTL)
    ├── Marker (DS Icon instance; no Marker variant)
    └── Connector (BOOLEAN visibility)
```

| Property | Contract |
|---|---|
| `Density` | `Default`, `Compact` |
| `Icon` | DS Icon instance swap, default `Icon/dot`. The marker is not a Radio Button, and should not use radio selection semantics |
| `Title` | Editable string |
| `Timestamp` | Editable display string |
| `Show timestamp` | Boolean |
| `Show connector` | Boolean. Normally false on last visible item |
| `Show content` | Boolean; default false. Enable only when the Content slot is needed. Empty history events do not reserve slot space |
| `Content slot` | Native Figma SLOT for optional descriptions, task lists, metadata, links, or actions |

Exactly two Timeline Item variants: `Density=Default` and `Density=Compact`. Marker is **not** a variant axis; all marker shapes are chosen via Icon instance swap. Icon identity, task count, event count, content presence, semantic status, and ordering are not variant axes.

### Anatomy, tokens, and geometry

- Axis: fixed 24px wide, on the **right** of content in RTL.
- Neutral markers use `Icon/dot` in the DS Icons library (24px icon canvas with centered solid dot), never `Icon/radio_button_checked`. Dot-like and semantic icon markers share the same instance-swap API.
- Icon: **24×24px DS Icon instance within the 24px Axis**. Individual icon artwork occupies its intrinsic inner bounds; `Icon/dot` contains a centered 10px solid circle. Use the approved DS Icon component and override its fixed source color to `fg/secondary` unless a validated event meaning calls for another semantic role. Do not assume a 20px instance.
- Connector: 1px, `line/default`; **Axis must stretch to exactly the Timeline Item height**, including wrapped titles and multi-task Content slots. Connector itself flexes within that axis, hidden on the final visible item. Its start is separated from the 24px marker container by 8px, and the axis reserves 8px beneath the connector. Never attach the line directly to an icon.
- Text: title uses `Label/SM`; timestamp uses `Body/XS`; both use Vazirmatn text styles.
- Foreground: `fg/primary` for title, `fg/tertiary` for timestamp, `fg/secondary` for the default marker/icon.
- Spacing: axis–content gap 12px Default / 8px Compact. Inside Header, Title-to-Timestamp = **4px in both densities**. Header-to-optional-Content Slot gap = **16px Default / 12px Compact**. Marker-to-connector gap = 8px, with 8px axis bottom padding. Derive these from existing Spacing variables.
- The fixed Figma master example width is for presentation only, not a required runtime width; content, title, timestamp and slots support fill and wrap.
- Use the DS radius variables for any surrounding cards. Timeline itself has no card surface or border.

Avoid a color scale tied to relative timing ("before / starting day / after") as generic Timeline state; those distinctions belong to the use case/content semantics, not the Timeline component contract.

## Figma designer workflow

1. Insert `Timeline`; set `Count` to the number of chronological events (1–6; default 4).
2. Select `Item 1` through `Item N` in the layer tree, and customize the text, timestamp, icon instance swap, and any optional item details. No per-item visible Boolean is required.
3. For a plain event, leave `Show content=false`. For a task group or additional details, set `Show content=true`, and compose tasks or metadata in the Item's native Content Slot. Do not add an extra empty Slot.
4. The last visible item's connector is already hidden by the selected Count variant; **do not manually patch the connector when adding/removing items**.
5. For more than six event records, use an extended composition or a real dynamic runtime list; do not claim the design-time Count cap is the API constraint.

The parent Count variants are a **Figma authoring optimization**, not a prescription for a runtime `count` prop. A renderer should derive children/connector termination from the event data order.

## Use case composition

### Onboarding — Schedule Timeline

Each time bucket such as `۷ روز قبل از شروع کار` is one item. Date goes in Timestamp; related scheduled tasks are a list inside Content slot with `Show content=true`. A time bucket with three tasks still has **one** marker. Task rows do not get Timeline connectors or individual Timeline markers.

The task list, status of individual tasks, task type icons, navigation targets and whether a task is completed are the responsibility of the composed task content, not the Timeline Item.

### My Applications — Event History

Each actual event is one item. Keep `Show content=false` unless a real explanation, action, or additional metadata is needed; no empty placeholder space should appear. Keep the event title primary and date/time secondary; type-appropriate icons may replace the neutral dot. The icon must not be the sole carrier of meaning. The title should describe the event in words. These event records are not fixed process steps.

## Ordering and grouping

- The product passes items in the intended order; Figma and runtime Timeline do **not** automatically reverse or sort. Choose `Count` for a contiguous sequence only; the component cannot represent noncontiguous visibility with holes.
- History may be oldest-first or newest-first depending on consumer context; the application must choose deliberately.
- Onboarding is ordered by scheduled relative time.
- Grouping by date is composition (group heading or time-bucket item), not a `Grouped=true` variant.
- One empty date group must not produce a false event. Empty states and loading skeletons are owned by the product container, not the Timeline primitive.

## Interaction

- Timeline Item is noninteractive by default; do not turn the full item into a generic clickable surface.
- Interactive links/buttons may be composed in Content slot and must keep native focus, accessible names and keyboard behavior.
- Markers and connectors are decorative unless additional programmatically exposed meaning is explicitly designed.
- No built-in approval decision, task completion action, status transition, or navigation API.

## Accessibility and RTL

- Preserve a meaningful chronological reading order independent from the visuals.
- In implementation, prefer ordered sequence semantics such as an ordered list of events, with a machine-readable date/time when available. Exact HTML, props and event schema are **unverified runtime implementation recommendations**, not registered API facts.
- Ensure relative date labels have an understandable absolute date for assistive technology where meaningful.
- Hide decorative connector from screen readers; avoid announcing both marker icon and redundant title.
- In RTL, axis is on the right, content is right-aligned, vertical order is unchanged.
- Long event titles wrap rather than truncate; markers align to the beginning/first line of each item. Text and Content slot fill available width.

## Development implementation contract (framework-agnostic)

This section specifies **required behavior**, not a claim that an existing API has been implemented. Choose component names/props to fit the owning frontend repository. Do not copy Figma-only `Count` into a hard runtime limit.

### Runtime content model

Each entry in the input sequence must have a stable identity, a meaningful visible title, and may include a machine-readable timestamp, an icon semantic identifier, or extra content. These are conceptual fields, **not verified TypeScript property names**.

- The product owns the array of events or scheduled groups, their chronological order, and relative/absolute date formatting.
- The renderer handles **zero or any number of entries**; zero follows the product empty-state contract. The Figma `Count=1..6` selector exists **only for authoring**.
- One array entry maps to one Timeline Item. A scheduled date containing multiple tasks is **one Item with a nested task list**, not multiple events.
- Title is required for a visible event. Timestamp is optional; if present and representable as a date/time, pair the readable Persian text with machine-readable metadata.
- Event-type icon is optional and defaults to a decorative neutral dot. Never encode an event's meaning solely with an icon or color.
- Optional details, tasks, metadata, and interactive actions render in the Item's secondary content area. Do not expose an empty content area when there is no secondary content.
- The component never sorts or reverses its data automatically. Consumers select newest-first or oldest-first per scenario.

### Layout and visual rules

- RTL is the default: the **24px Axis is on logical inline-start (right)**, content occupies remaining inline width, and Title / Timestamp align to the right.
- Marker is a 24px DS Icon instance. `Icon/dot` shows a centered 10px dot within that icon. Default marker color: `fg/secondary`. Icons swapped from the common icon library must have their fixed source color overridden to the contextually appropriate semantic foreground.
- Connector is **1px `line/default`**, starting after an 8px Marker-to-Connector gap; allow 8px bottom spacing. It stretches as the Item grows with wrapped text or secondary content.
- Exactly **one connector between consecutive visible Items**. There is **no connector after the last Item**. Derive this from each Item's array index/last-item status; do not introduce separate connector states that a product consumer must coordinate.
- Title style: `Label/SM`, `fg/primary`; timestamp: `Body/XS`, `fg/tertiary`. Both are Vazirmatn. Gap between them: 4px.
- The optional secondary content sits **16px after the Header in Default** and **12px in Compact**. Axis-to-Content gap: 12px Default / 8px Compact. Use existing spacing tokens, not newly hardcoded ad-hoc color tokens.
- The component has no independent border, card surface, hover state, or item-wide click target by default. Surrounding cards are the consumer's responsibility.
- Text wraps; no imposed single-line ellipsis for event titles. Axis height tracks Item height. Do not assume the 480px / 420px Figma master widths at runtime.

### Accessibility and interactions

- Use an ordered sequence in the DOM (e.g. `<ol>` with each event in an `<li>`) so event chronology is exposed independently of decorative positioning. This is a **target implementation contract**, not a verified existing DOM.
- Render valid dates in `<time datetime="...">` where applicable. When a relative display label is used (e.g. «۲ روز پیش»), preserve the associated absolute time in an accessible/machine-readable form.
- Hide decorative Axis, Connector and neutral Marker from assistive technology. If icons convey event category, supply that category in readable text as well.
- Do not put focus or button semantics on a whole passive Item. Links/actions inside content are independently keyboard reachable, with visible focus and proper accessible names.
- Preserve correct reading order in RTL and with mixed Persian/English text. Visual mirroring must not reverse chronology.
- Do not invent step statuses (`completed/current/upcoming`); those belong to Stepper HOS-31.

### Acceptance tests — Storybook bypass

| Test | Required result | Status |
|---|---|---|
| Figma `Count=1..6` visual instances | Correct visible Item number; only adjacent visible Items have a connector | **Verified in Figma** |
| Figma Onboarding (1/2/3 tasks per date) | Each date stays one Item; task slots and matching Axis heights preserved across Count changes | **Verified in Figma** |
| Figma My Applications | 4 event records, icon swaps, neutral semantic colors and last connector hidden | **Verified in Figma** |
| Figma responsive RTL at 360px | Long title wraps, timestamp remains below title, Axis stretches with content | **Verified in Figma** |
| Runtime list length 0, 1, 2, 4, 6, 7+ | Correct dynamic rendering, including >6 events, without authoring `Count` limit | **Required in development** |
| Runtime last connector / variable text | No trailing connector; connector stretches with variable-height content | **Required in development** |
| Runtime semantic dates / RTL / keyboard | Accessible ordered list, meaningful time, decorative marker hidden, nested links operable | **Required in development** |
| Runtime theme and semantics | Semantic tokens resolve in supported themes, no hardcoded icon guard color leaks | **Required in development** |

The implementation must be validated via the owning team's code tests/manual QA. **Do not require Storybook** for this phase.

## Figma QA performed

- [x] Two Timeline Item variants (`Density=Default/Compact`), without a Marker variant axis.
- [x] Parent Timeline `Count=1..6` variants replace Boolean per-item visibility; default Count=4.
- [x] `Icon/dot` added to DS Icons and used for neutral markers.
- [x] Native optional `Content slot` on Timeline Item; **no Items Slot** on Timeline parent.
- [x] Connector auto-termination verified when switching Count=1, 2, 4, 5, 6; no trailing or broken connector.
- [x] Real Onboarding time groups with 1–3 tasks per item.
- [x] Real My Applications event types with icon swapping.
- [x] Last-item connector hidden in both product examples.
- [x] Vazirmatn styles and semantic color/spacing bindings.
- [x] Responsive 360px example with a two-line event title and correctly stretching connector at `Count=2`.
- [x] Slot-preservation tests after switching Onboarding Count across 1, 2, 4, 5, 6: custom task list survives and Axis stays equal to item height.
- [x] Title–Timestamp gap 4px; Header–Content gap 16px Default / 12px Compact.
- [x] Orphan experiments moved to a hidden archive frame on the Figma page (not deleted).
- [x] RTL alignment and variable-height item composition visually reviewed.
- [x] Design-source audit and final review across both product examples, Count variants, optional content, tokens, and 360px RTL layout (2026-10-14).
- [x] Figma component identity keys verified and registered in `../../integrations/component-mapping.md`.
- [x] Development acceptance criteria documented without Storybook dependency.
- [ ] Product-owner final visual sign-off, if required by the team's handoff process.
- [ ] Runtime implementation tests and accessibility review **after** development.
- [ ] Shared-library publication status and Code Connect, if required later (not release blockers for design handoff).

## Status of runtime and sources

This document is a **Figma-verified design contract, ready for development handoff**. No owning runtime Timeline component has been registered or inspected in this task, so exact production TypeScript prop names, current DOM hierarchy and event payloads are **unverified**, not pre-existing facts. Developers should implement against the behavior and acceptance criteria below, choose framework-appropriate APIs, and validate against the real code. **Storybook is explicitly bypassed for this handoff by product decision; a Storybook entry is neither required nor evidence of correctness.** Runtime tests and accessibility QA remain implementation responsibilities, not design blockers.
