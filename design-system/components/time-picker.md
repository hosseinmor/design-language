---
id: design-system.component.time-picker
collection: design-system
type: component
title: Time Picker
summary: One public segmented time field with optional shared Selection Panel and optional seconds.
knowledge_state: verified
document_maturity: draft
owner: Design System team
related:
  - design-system.experience-rule.segmented-field-editing
  - design-system.component.date-picker
  - design-system.component.select
  - design-system.component.text-input
  - design-system.accessibility.forms
  - design-system.accessibility.focus-management
topics:
  - time-picker
  - time-input
  - segmented-time
  - rtl
  - keyboard
  - accessibility
---

# Time Picker

> **HOS-49 — proposed design contract for owner review.** Figma's unified Time Picker source and connected Selection Panel have been inspected after visual changes on 2026-10-24. The HTML prototype validates intended keyboard interactions but is **not** proof of a production runtime API, accessible screen-reader implementation or Storybook parity. Design maturity remains draft until review.

## Purpose and boundary

**Time Picker is the only public Karbon time-field component.** Its segmented Hour/Minute input is always editable unless disabled or read-only.

- **Selection panel On (default)**: the field has an independently operable trailing clock action which opens the existing shared Selection Panel for selecting one allowed time. Direct typing remains available.
- **Selection panel Off**: manual segmented typing only; no clock action, no popup and no activation.
- **Seconds Off (default)**: HH:mm.
- **Seconds On**: HH:mm:ss and a third editable segment; Hour → Minute → Second.

Do not maintain a separate public Time Input. Its previous component source is retained on the existing **Date & Time · Legacy compatibility sources** page for existing consumers, without detaching/replacing them. It is not a source for new instances. Do not use Select itself as an editable time input, or add an independent generic Popover shell around the shared Selection Panel.

Date Picker follows the same single-public-component decision with optional Calendar, but its calendar grid and date parsing remain independent.

## Figma sources

- [Time Picker documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=25067-1359).
- [Public Time Picker Component Set](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24862-46616), stable node `24862:46616`, with 24 variants (`Size=Small|Medium|Large` × eight Field Family States). Original component set identity is preserved.
- [Active Time Segment / Internal](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=25025-455): Hour / Minute / Second; content-hugging selection backdrop with semantic colors.
- [Time Option Content / Internal](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=25021-449) is composed of instances of [Select Option](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=20613-21).
- [Selection Panel](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=20619-306) is a **shared Select source**, reused as an instance with time options in its `Options` Slot.
- [Mobile selection composition](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=25073-45891) uses the shared Dialog mobile variant with `Time Option Content / Internal` in its native Body Slot; it is design evidence, not verified runtime modality.
- [Legacy Time Input](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24861-46139) preserves its earlier master ID and key for migration.

## Figma authoring

| Kind | Property | Semantics |
| --- | --- | --- |
| Variant axis | Size | Small 32px / Medium 40px / Large 48px; Medium default |
| Variant axis | State | Default, Hover, Focus, Error, Error focus, Disabled, Read only, Read only focus |
| Boolean | Selection panel | On by default; controls capability and clock icon; Off means no popup even when Open=True |
| Boolean | Seconds | Off by default; makes the third unit and `:--` placeholder suffix visible |
| Text | Hour / Minute / Second | Sampled segment display strings, not three independently committed values |
| Instance Swap | Active segment | Hour / Minute / Second active highlight preview; Figma-only |
| Boolean | Filled | Value vs placeholder presentation; Figma-only |
| Boolean | Open | Preview popup content only while Selection panel is On and field interactive; Figma-only |
| Field content | Show label, Label, Required, Placeholder, Show helper, Helper, Error text | Shared Field Family authoring conventions |

No `Open`, `Filled`, or seconds-combination Variant axis is needed. The runtime must derive focus/filled/opened from interaction and value.

## Visual and composition

- Field radius 6px, sizes 32/40/48px, shared typography and semantic padding. `focus/default` is a dedicated field ring; `line/error` and error messaging persist with it.
- Active segment: `surface/accent-emphasis` plus `fg/on-color`, with **content-hugging width**, not a fixed two-digit highlight. The preceding/following colon separators never become part of the selection.
- Empty segments show dashes. HH:mm order on the screen is **Hour left, Minute right**, with optional Second further right, including in RTL UI. Keep the whole time value bidi-isolated; clock icon is the trailing action at the left edge of the RTL field.
- The shared Selection Panel is the single floating shell (12px radius, floating elevation and governed spacing). Use **Single / Results / Filterable=False** with instances of shared Option rows. No duplicate Time Option style system. The time picker controls allowed values, step, filtering against min/max, validation and whether a selection commits.
- Figma's source panel and sample option content demonstrate composition, not a fixed menu width, minute interval or maximum option count. Runtime handles viewport collision and scrolling. On narrow viewports, compose the option content in the shared mobile Dialog/Drawer pattern as appropriate, without nesting the floating shell.
- Disabled has no usable popup or typing; Read only stays legible and must not suggest a usable clock action.

## Editing and keyboard behavior

Follow [Segmented Field Editing](../../foundations/interaction/segmented-field-editing.md). Full two-digit entry advances Hour → Minute → optional Second; the final unit retains focus. Backspace removes one digit per press. Support horizontal unit navigation, Up/Down adjustment, localized numeric typing, whole-time paste and an incomplete draft without premature commits.

The time value is **one committed value** (for example `14:30` or `14:30:25`). Panel selection and manual editing update the same value model. If a panel is enabled, the clock trigger is keyboard-operable and separate from the segmented field; editing the value alone does **not** automatically open it. Escape closes without overwriting the last committed value; Enter/click on an enabled option commits and closes. Tab does not cause an unintended commit.

The 24-hour locale default is appropriate for the Persian experience. Twelve-hour display, AM/PM, timezone and seconds availability are format/product decisions; 12-hour and timezone UI are **not** part of the current authored v1. Seconds is supported, but not forced. Product owns permitted time range and selectable suggestion step; don't unnecessarily restrict valid typed values to the suggestion step unless explicitly configured.

## Handoff and acceptance

The Figma sources and HTML prototype are ready for **design review**, not confirmed production implementation. Before development sign-off, validate resizing and `Selection panel=False/Open=True` suppression, `Seconds` toggles for empty and filled values, content-hugging highlight for 1- and 2-digit drafts, keyboard navigation and Backspace, zero/overflow cases, RTL, accessibility, mobile viewport/zoom, selection-list scrolling, and screen reader behavior. Confirm runtime naming and any migration from Time Input against the Storybook/code source; no runtime parity or successful CI is claimed here.
