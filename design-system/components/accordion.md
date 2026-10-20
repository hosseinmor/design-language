---
id: accordion
collection: design-system
type: component
title: Accordion
summary: Accordion groups related disclosure items so users can reveal supporting content in place while keeping the page scannable.
knowledge_state: verified
document_maturity: draft
related: []
design_status: ready-for-dev
design_maturity: handoff-ready
source_figma: https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=22821-129502
source_node: 22821:129502
---

# Accordion

## Purpose

Accordion organizes related supporting content as a vertical group of expandable sections.

Use it when users benefit from scanning section titles before deciding which details to read. Do not use it to hide information required to understand or complete the current task.

## Component boundary

The Figma model contains two related components:

- **Accordion Item** — one disclosure row. It owns Trigger, title, indicator, expanded state, and Panel content.
- **Accordion** — the group wrapper. It owns a native Figma `Items` Slot containing one or more Accordion Item instances.

A single Accordion Item may be used by itself as a **Disclosure / Collapsible section** pattern. Do not create another duplicate component for that standalone case.

Accordion is not navigation. Use Tabs, navigation, Tree, or another navigation pattern when changing sections changes destination/context rather than revealing content in place.

## Canonical Figma sources

Primary Design System file:

- File: `-DS--Job-Vision-NEXT`
- File key: `rROD8ctH9UfPGAMrRrOzHe`

### Accordion

- Component: `Accordion`
- Node ID: `22821:129502`
- Component key: `649891c2bfc1413f60f04011bc71a05576d12738`

### Accordion Item

- Component set: `Accordion Item`
- Node ID: `22794:548`
- Component key: `2728144865f9616dd66228719b4fb71936e3062a`

## Accordion anatomy

Accordion is intentionally only a grouping layer:

1. **Items Slot** — native Figma Slot containing Accordion Item instances.
2. **Accordion Items** — vertically stacked with zero gap.

Accordion adds no card surface, radius, border, or elevation around the group.

The default Figma instance contains three **collapsed** Accordion Items for convenience, but the count is not fixed. Designers may add or remove items through the native `Items` Slot.

### Items Slot contract

- Property: `Items`
- Type: native Figma `SLOT`
- Minimum children: 1
- Maximum children: unrestricted
- Vertical gap: 0
- Children stretch to the Accordion width
- Preferred/allowed content: `Accordion Item` component set

The Slot is constrained to Accordion Item instances so the group cannot accidentally become a generic arbitrary-content container.

## Accordion Item anatomy

Each Accordion Item contains:

1. **Trigger** — the full interactive header row.
2. **Title** — visible and accessible label of the Trigger.
3. **Indicator** — decorative expand/collapse Chevron.
4. **Panel** — disclosed content region.
5. **Content Slot** — native Figma Slot that owns all Panel content.
6. **Bottom divider stroke** — a 1 px structural separator applied to the Accordion Item root; it is not a separate child layer.

The Trigger owns expand/collapse interaction. The Chevron is not a separate control.

Do not put arbitrary interactive controls inside the Trigger. If a persistent action must sit beside the heading, keep it outside the Trigger as a sibling control with its own focus target and semantics.

## Accordion Item Figma API

### Variant properties

| Property | Values | Meaning |
|---|---|---|
| `Size` | `Large / Medium / Small` | Minimum Trigger height and title typography |
| `State` | `Enabled / Hover / Focus / Disabled` | Design-time interaction state |
| `Expanded` | `False / True` | Panel visibility and Indicator direction |
| `Indicator position` | `Start / End` | Places the Indicator at the logical Start or End side of the Trigger |

There are 48 visual variants:

`3 Size × 4 State × 2 Expanded × 2 Indicator position`.

`Skeleton` is intentionally not part of the interactive state matrix.

### Content properties

| Property | Type | Default |
|---|---|---|
| `Title` | Text | `عنوان آکاردئون` |
| `Content` | native Figma Slot | Body/SM sample text |

The expanded Panel is entirely owned by the native `Content` Slot.

Designers may:
- edit the default Body text directly;
- delete or replace the default text;
- add multiple text blocks;
- add Frames;
- add component instances;
- compose richer Panel layouts without changing the Accordion Item API.

The Slot uses vertical Auto Layout with a 12 px gap between multiple children.

Do not reintroduce separate `Body`, `Body text`, `Custom content`, or `Content swap` component properties. Native Slot composition replaces those authoring controls.

## Size and layout

| Size | Trigger min-height | Title style | Vertical padding |
|---|---:|---|---:|
| Large | 48 px | `Label/MD` — 16/24, 500 | 8 px |
| Medium | 40 px | `Label/SM` — 14/20, 500 | 8 px |
| Small | 32 px | `Label/SM` — 14/20, 500 | 4 px |

Shared Trigger construction:

- horizontal padding: 16 px;
- Title–Indicator gap: 16 px;
- Indicator: 16 px;
- Trigger width: fill container;
- title may wrap;
- listed heights are minimums; multiline titles grow rather than truncate.

The 400 px width shown in the variant set is only an authoring width. Product instances fill their available container.

### Panel

Panel padding follows Indicator position so content stays aligned with the Title.

For `Indicator position=Start` in RTL:
- top: 8 px;
- right / logical Start: 48 px;
- bottom: 16 px;
- left / logical End: 16 px.

For `Indicator position=End` in RTL:
- top: 8 px;
- right: 16 px;
- bottom: 16 px;
- left: 48 px.

The Panel contains only the native Content Slot as its direct content layer.

The default Slot text uses `Body/SM` — 14/24, 400.

## Indicator position

`Indicator position` is a visual geometry property, so it is represented as a Figma variant axis.

Use logical naming rather than physical `Right / Left`:

- **Start** → right in RTL, left in LTR.
- **End** → left in RTL, right in LTR.

In the current Persian/RTL Figma authoring context:
- Start places the Chevron on the right.
- End places the Chevron on the left.
- Panel inset flips with the Indicator so content remains aligned with the Title.

Chevron up/down expresses collapsed/expanded state and does not horizontally mirror.

## Visual treatment

Accordion remains low-decoration:

- no group surface by default;
- no outer border;
- no radius;
- no elevation;
- a 1 px bottom stroke on each Accordion Item root, bound to `line/muted`, separates items;
- expanded is disclosure state, not selection state, so it does not receive Brand, Accent, or Selected treatment.

## States

| State | Trigger treatment | Title / Indicator | Divider |
|---|---|---|---|
| Enabled | transparent | normal semantic foreground | `line/muted` |
| Hover | `surface/transparent-hover` | normal semantic foreground | `line/muted` |
| Active | runtime-only `surface/transparent-active` | normal semantic foreground | `line/muted` |
| Focus | shared Focus treatment on Trigger only | normal semantic foreground | `line/muted` |
| Disabled | transparent | `fg/disabled` | `line/muted` |

Focus uses the shared `Focus/Default` Effect Style bound to `focus/default`. It represents a 2px ring with a 1px gap and must not resize the Trigger or wrap the Panel.

Active is a transient runtime pseudo-state and is intentionally not a Figma variant.

If a Disabled Item is already expanded, its Panel content remains readable. Avoid a collapsed Disabled Item when disabling it would make otherwise necessary content inaccessible.

## Loading

Loading is not an Accordion interaction state.

- If the whole Accordion is unavailable, use the shared loading/skeleton pattern outside the interactive component.
- If only an expanded Panel is loading, place the appropriate Loading/Skeleton component inside the native Content Slot.
- Placeholder headers must not be exposed as operable disclosure controls.

## Expanded and collapsed behavior

Default initial Item state is **collapsed** unless product context clearly benefits from revealing a specific section.

Collapsed:
- Panel hidden;
- Indicator points down;
- accessible expanded state is false.

Expanded:
- Panel visible below the Trigger;
- Indicator points up;
- accessible expanded state is true.

Opening or closing an Item must not change horizontal alignment.

## Group behavior

Accordion supports two runtime policies:

- **Multiple-open — default.** Each Item owns independent expanded state; any number may remain open.
- **Single-open — explicit option.** Opening one Item closes another open Item in the same Accordion.

Both policies allow all Items to be collapsed.

The group policy does not change Figma anatomy and therefore is not a Figma variant on the `Accordion` wrapper.

Use Single-open only when limiting simultaneous expansion is materially useful. Do not use it only to make the interface look tidier.

## RTL and direction

Persian/RTL is the primary authored context.

- Use logical Start/End terminology.
- `Indicator position=Start` places the Indicator on the right in RTL.
- `Indicator position=End` places it on the left in RTL.
- Title remains right-aligned for Persian content.
- Panel inset follows Indicator position so content aligns with Title.
- Runtime implementations should use logical properties rather than physical left/right rules.

## Accessibility contract

Follow the WAI-ARIA Accordion pattern.

### Semantics

- Use a native `button` for each Accordion Item Trigger.
- Place the Trigger in the appropriate heading level when Items represent document sections.
- Keep the heading limited to the Trigger.
- Reflect Panel visibility with `aria-expanded`.
- Associate Trigger and Panel with `aria-controls` and a stable Panel ID.
- Indicator is decorative and hidden from assistive technology.
- Add `role="region"` + `aria-labelledby` only when the extra landmark structure is useful; avoid landmark proliferation where many Panels may be open.

### Keyboard

- `Enter` and `Space` toggle the focused Trigger.
- `Tab` and `Shift+Tab` follow normal focus order.
- Focus remains on the Trigger after expand/collapse.
- Do not move focus into the Panel automatically.
- Do not add Arrow/Home/End navigation or roving focus to the base contract.

### Disabled

Disabled suppresses Trigger operation but must not make required explanatory content unreadable. If only controls inside the Panel are unavailable, keep the Accordion Item operable and disable those inner controls instead.

External reference: https://www.w3.org/WAI/ARIA/apg/patterns/accordion/

## Motion

Motion should explain disclosure, not delay access to content.

The shared Motion foundation does not yet define a verified duration/easing contract, so Accordion does not invent component-specific timing.

When runtime motion is implemented:
- animate only disclosure change;
- keep the transition short;
- do not use motion as the only state cue;
- respect reduced-motion preferences.

Exact duration, easing, DOM measurement, and animation implementation remain runtime-owned and unverified until the shared Motion/runtime source is registered.

## Usage

Use Accordion for:
- FAQs;
- supporting information divided into clear sections;
- settings/details users may inspect selectively;
- secondary content where simultaneous comparison may be useful.

Do not use Accordion for:
- small content clearer when shown directly;
- primary page messaging or critical task requirements;
- sequential step flows;
- navigation between destinations;
- content whose collapsed state hides an error or required action;
- deeply nested disclosure structures.

## Content guidance

- Titles should be short, specific, and unique within a group.
- Avoid generic repeated titles such as “More information”.
- Keep essential status/error information outside collapsed Panels.
- Rich Slot content follows the normal rules of the components placed inside it.
- Nested interactive content follows ordinary focus order.
- Avoid nested Accordions unless the information architecture clearly requires another disclosure level.

## Semantic token mapping

Accordion introduces no component-specific Color tokens.

| Need | Semantic role |
|---|---|
| Title | `fg/primary` |
| Indicator | `fg/secondary` |
| Default Panel text | `fg/primary` |
| Disabled Trigger content | `fg/disabled` |
| Divider | `line/muted` |
| Hover | `surface/transparent-hover` |
| Active | `surface/transparent-active` |
| Focus | `focus/default` |

Content inserted into the native Slot owns its own semantic/component token contract.

## Runtime boundary

Current Code and Storybook sources are not registered.

Therefore this document does not assert:
- exact Angular component names;
- runtime prop/input names;
- exact DOM wrapper structure beyond accessibility requirements;
- animation library or implementation;
- class names;
- Storybook story IDs.

Conceptually, runtime must support Item expanded/disabled state, Indicator Start/End geometry, and group Multiple/Single policy, but exact API naming is implementation-owned.

## QA checklist

Verify:
- Accordion Item has 48 variants: `Size × State × Expanded × Indicator position`;
- every variant contains one native Figma `Content` Slot;
- Content Slot contains editable default Body text and accepts arbitrary frames/text/component instances;
- no legacy Body/Body text/Custom content/Content swap properties remain;
- Start places Indicator right in RTL and End places it left;
- Panel inset flips correctly with Indicator position;
- Trigger fills available width;
- Large/Medium/Small min-heights are 48/40/32;
- multiline titles grow rather than truncate;
- Expanded changes Indicator and Panel visibility without horizontal shift;
- Focus appears on Trigger only;
- Accordion group exposes one native `Items` Slot;
- Items Slot accepts one or more Accordion Item instances with zero gap;
- the default Accordion authoring instance contains three collapsed Items;
- the Item separator is a 1 px bottom stroke on the Item root bound to `line/muted`;
- grouped Items can show multiple expanded Panels.

## Open implementation items

- Register runtime Design System repository/package and Storybook.
- Verify Figma ↔ runtime property mapping from the real implementation source.
- Adopt shared Motion timing/easing when the Motion foundation is finalized.
