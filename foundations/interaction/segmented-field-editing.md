---
id: design-system.experience-rule.segmented-field-editing
collection: design-system
type: experience-rule
title: Segmented Field Editing
summary: Draft shared editing behavior for segmented date/time values, including active-segment visuals, character-level deletion, directional navigation, incomplete drafts and accessible focus.
knowledge_state: unverified
document_maturity: draft
owner: Design System team
related:
  - design-system.component.date-picker
  - design-system.accessibility.keyboard-navigation
  - design-system.accessibility.focus-management
  - design-system.accessibility.forms
topics:
  - segmented-field
  - segmented-editing
  - date-input
  - time-input
  - keyboard
  - rtl
  - localization
---

# Segmented Field Editing

> **Draft for owner review — HOS-49 / 2026-10-24.** Shared design proposal based on the approved Time Picker HTML exploration and the live Date Picker Figma states. **Not a runtime API, test certification, or accessibility exception.** This document intentionally owns only the cross-component behavior; Date Picker and future Time Picker documents own their value models and constraints.

## Boundary

A **segmented field** presents one logical value as consecutive editable units (for example, year/month/day or hour/minute/second). It must have **one committed value** and a **separate, recoverable draft** while one or more units are being edited. Literal separators are not editable segments.

A picker popup is **orthogonal** to this editing model. Date Picker retains one public component and its `Calendar` Boolean; the Time Picker owns its optional selection UI separately. Do not introduce a generic public Segmented Field component solely because the behavior is shared.

## Visual states

- The currently active editable segment uses `surface/accent-emphasis` and `fg/on-color`. **Only one segment may be active at once.** Inactive segments retain their ordinary Field typography and semantic foreground.
- The selected surface **hugs the rendered segment characters**: zero fixed minimum character-box width for a partial value. It grows or shrinks when the displayed character count or localized digit glyph widths change, including one digit, two digits, four digits, and a dash placeholder. Keep separators outside the selected background.
- An unset unit displays dash glyphs according to that unit's localized placeholder convention; literal separators stay visible. The exact number and order of units are component/locale-owned.
- The outer Field `focus/default` ring remains a **separate focus-visible effect** (2px with 1px offset), independent of internal selected-segment color. Do not replace Focus with a blue border or let the internal selection change control width.
- Use canonical Typography, Spacing and Radius tokens; layout follows locale writing order, including RTL, without mirroring numeric glyphs or non-directional icons. A high-contrast selected fill must not rely on brand-specific raw colors.
- Disabled and read-only behavior follows the owning component; a read-only field must not imply numeric editing simply because it can receive focus.

## Shared keyboard editing model (proposed)

| Input | Behavior |
|---|---|
| Digit key | Insert/replace one normalized numeric character in the active unit's **draft**, subject to that unit's digit capacity |
| Completing the unit | Move active focus to the **next editable unit** when its required digit count has been entered; do not wait for the entire date/time value to commit |
| Backspace with characters | Remove **one character per keypress** (e.g. `25 → 2 → --`); preserve the remaining prefix and keep focus on that unit |
| Backspace on already empty unit | Move to the previous editable unit, without deleting its whole value; a following Backspace may delete one of its characters |
| ArrowLeft / ArrowRight | Move between adjacent editable units according to the **actual visual order** for the current locale/RTL presentation; separators are skipped |
| ArrowUp / ArrowDown | Increment/decrement the focused unit according to the component's allowed values and boundary policy; do not silently commit an invalid whole value |
| Paste full value | Parse localized full-date/full-time input into a single proposed draft; apply atomically only if the paste format can be parsed, rather than distributing arbitrary characters |
| Partial / invalid draft | Remain visibly editable and recoverable; **only commit a complete valid logical value** under the owning component's commit policy |
| Tab / Shift+Tab | Proposed group entry/exit navigation without a trap; **final DOM focus model is an accessibility/runtime review item**, not dictated by this Figma document |

Digit normalization must accept supported local numeral systems (including Persian, Arabic and Latin when the product permits) without conflating display digits and the canonical committed value. A multi-character pasted date/time, locale calendar conversion, overflow/wrapping, min/max and unavailable values are **owned by Date Picker/Time Picker**, not invented at the shared layer.

## Accessibility and authoring acceptance

- Expose an overall accessible Field name plus a **meaningful segment name** (year, month, day; hour, minute, second, etc.) and current/empty state. Literal separators must not create keyboard stops.
- Follow [Keyboard Navigation](../../accessibility/keyboard-navigation.md), [Focus Management](../../accessibility/focus-management.md), and [Accessible Forms](../../accessibility/forms.md) rather than inventing new ARIA semantics.
- A segment-based control should offer a coherent focus strategy and predictable Tab sequence. **Do not assume** every segment is a Tab stop or that one roving Tab stop is universally correct; benchmark the chosen accessible implementation (e.g., React Aria DateSegment) with actual browser/assistive technology before finalizing.
- Preserve composition with Field Label, Required, Info, Helper/Error associations, `focus-visible`, disabled/read-only semantics and optional picker triggers. Verify RTL navigation, Persian and mixed numerals, screen-reader announcement and keyboard-only workflows in Runtime.
- Figma authoring may show a highlight preview for each unit, but **Figma variants and Boolean preview controls do not prove working keyboard handlers, clipboard parsing or commit logic**.

## Component-owned details / review items

- **Date Picker:** current locale date ordering, year/month/day capacity, leap days, minimum/maximum dates, calendar-system choice, date-only commit and optional Calendar popup remain in [Date Picker](../../design-system/components/date-picker.md).
- **Time Picker:** hour-cycle, minutes/seconds optionality, meridiem, allowed time ranges and any time selection surface belong in the Time Picker contract when published. This proposal does not assert that a Time Picker Markdown component contract or runtime implementation already exists.
- **Before owner approval:** verify whether automatic advance on a valid short prefix (e.g., a constrained unit) is desirable in addition to the full-digit rule; choose a tested DOM/ARIA/Tab model and test Backspace, partial drafts and paste with RTL/locale variants.

## Evidence / status

The Date Picker [live Figma master](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24703-8942) shows token-bound, character-hugging selected segments; the [Figma editing review](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24814-290) shows Year/Month/Day, one-/four-digit examples and empty units. The previously tested **Time Picker HTML v5** is interaction-prototype evidence, **not** runtime or screen-reader validation.

**Review status: Draft.** No normatively approved shared keyboard implementation, shipped Storybook parity or merge is claimed.
