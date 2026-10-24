---
id: design-system.experience-rule.segmented-field-editing
collection: design-system
type: experience-rule
title: Segmented Field Editing
summary: Shared editing, active-segment presentation, and keyboard model for date and time fields.
knowledge_state: verified
document_maturity: reviewed
last_reviewed: '2026-10-24'
owner: Design System team
related:
  - design-system.component.date-picker
  - design-system.component.time-picker
  - design-system.accessibility.focus-management
  - design-system.accessibility.keyboard-navigation
topics:
  - segmented-editing
  - keyboard
  - date-field
  - time-field
  - rtl
  - accessibility
---

# Segmented Field Editing

> **Reviewed shared design rule — HOS-49.** The Design System owner accepted this segmented-editing model for Date Picker and Time Picker and requested development handoff on 2026-10-24. The Time Picker HTML was interactively prototyped and Figma demonstrates the reviewed visual authoring; neither is evidence of tested Karbon behavior. Date Picker retains its date-specific validation and localization contract. This foundation does not assert that the two runtime implementations already share code.

## Scope and ownership

A segmented field edits one compound value through separately editable numeric units. The outer field remains one form control in terms of value, validation, label, helper/error precedence, and committed state. **Date Picker** and **Time Picker** apply this shared model. Do not create a separate public Segmented Input product component solely for this behavior.

The owning date/time component decides ordering according to its format/locale, allowed ranges, calendar system, whether seconds exist, and how its optional selection surface is activated. Accessibility foundations own general focus and keyboard requirements.

## Active segment vs field focus

- The **active editing segment** uses `surface/accent-emphasis` for the filled highlight and `fg/on-color` for its glyph. Use semantic tokens, never a fixed blue/white hex pair.
- The highlighted background hugs **actual rendered segment content**, including a one-digit draft or a two-dash placeholder. It must not keep a fixed two-digit width. Include only the segment's small governed inline padding, not the separators.
- The field's independent Focus ring uses `focus/default`; error retains its `line/error` boundary and error text while the active segment remains readable. An active segment is **not** the persistent selected value of a selection list.
- Separator characters remain visible and are not editable units. Empty units show individual dashes (e.g. `--:--`, optionally `--:--:--`).
- For a time value displayed as HH:mm or HH:mm:ss in the current Karbon decision, **Hour is physically left of Minute**, and optional Second follows on the right. Isolate digit-run direction so the RTL form container cannot reverse the unit sequence. Date ordering remains date-locale-specific.

## Keyboard and input contract

- Each unit can be selected and typed into directly; typed digits replace the selected value with an in-progress draft. Normalize Persian, Arabic and Latin digits for parsing without forcing one display digit set.
- After a unit receives its expected number of digits, move the active editing context to the next available unit (Hour → Minute → optional Second for Time Picker). The last unit does not automatically leave the field.
- `Backspace` removes **one digit at a time** in the current unit. If already empty, an additional Backspace may move to the preceding unit; do not clear an entire date/time or every unit on one press. `Delete` has a corresponding local, non-destructive behavior.
- Horizontal Arrows move between **physical adjacent** editable units, respecting their actual visual order; Up/Down adjust the current unit according to the owning field's numeric validation and wrapping rules. Do not interpret left/right from an accidental bidi reorder.
- Keep the segmented value reachable as one logical field Tab stop using a predictable roving/managed focus model; Tab/Shift+Tab exit the segment group. Optional Calendar/Selection Panel action is a separate keyboard-operable control.
- Pasting a complete supported date/time updates a **single recoverable draft** and only commits when valid. Incomplete or temporarily invalid unit drafts remain editable and do not corrupt the previously committed compound value.
- Expose a meaningful accessible label, current unit name/value/range, required/invalid relationships and helper/error association. Test keyboard, high contrast, zoom/reflow, RTL, screen reader and mobile virtual keyboard explicitly.

## Boundaries

Date Picker owns calendar/locale-specific field order, day/month/year digit lengths, Jalali/Gregorian limits and Calendar popup. Time Picker owns 24-hour/12-hour presentation, seconds, allowed hours/minutes/seconds, step suggestions and its optional Selection Panel. The shared contract is a design rule, not a shipping React Aria API or promise of runtime parity.

## Live design evidence

- [Time Picker Figma source](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24862-46616).
- [Time Segment Focus source](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=25025-455).
- [Date Picker Figma source](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24703-8942).
