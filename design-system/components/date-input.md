---
id: design-system.component.date-input
collection: design-system
type: component
title: Date Input
summary: Segmented manual date entry using shared Field Family anatomy, localized date parsing, one committed date value, and mutually exclusive supporting or error feedback.
knowledge_state: verified
document_maturity: draft
owner: Design System team
related:
  - design-system.component.text-input
  - design-system.component.date-picker
  - design-system.accessibility.forms
  - design-system.accessibility.focus-management
  - design-system.accessibility.keyboard-navigation
  - design-system.accessibility.component-authoring-contract
topics:
  - date-input
  - date-field
  - segmented-date
  - form-field
  - rtl
  - localization
  - accessibility
---

# Date Input

> **HOS-49 — design contract for review.** The live Figma source was verified on 2026-10-22 and its visual authoring design is complete. Keyboard parsing, screen-reader operation, mobile input methods, Karbon/Storybook parity, and executed accessibility tests have **not** been verified. `document_maturity: draft` remains until the Design System owner reviews the normative contract. Figma property names are **not** a confirmed runtime API.

## Purpose and boundaries

Date Input accepts **one date** by manual entry, without opening a calendar. It extends the shared [Text Input](text-input.md) Field Family with date-specific editing and validation.

**Use** when manually entering a known exact date is the primary task, including dates from documents or historical dates where calendar browsing is inefficient. Use [Date Picker](date-picker.md) when users should also browse or select a date from a calendar. Ordinary Text Input is not an adequate replacement when segment rules, validation, accessible date semantics, and locale handling are needed. Date Range, Time Input, Date-Time and timezone selection are separate concerns.

Date Input is a **single public component**, not a product composition of three Number Inputs. Its year, month, and day parts form one accessible date field with one label, one value model, and one validation result.

## Live Figma source and authoring

- [Date Input — canonical component set](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24779-839) — `24779:839`, page **Date Input**.
- [Date Input — presentation and live examples](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24782-1717).
- Shared internal source `Date Field Base / Internal` — `24662:227`. Shared `Date Segment Focus / Internal` — `24809:56070`. Both are internal Figma composition sources, **not** separate public controls.

The public Figma set has **24 variants**: `Size = Small | Medium | Large` × `State = Default | Hover | Focus | Error | Error focus | Disabled | Read only | Read only focus`. **Medium / Default** is the default. Do not add a `Filled` axis or a variant for every possible calendar value.

| Figma authoring property | Purpose |
|---|---|
| `Filled` (Boolean) | Preview empty versus displayed date; **Figma-only** |
| `Placeholder` (Text) | Editable sample format/instruction when empty |
| `Year`, `Month`, `Day` (Text) | Separate editable Figma representations of a **single** date value |
| `Active segment` (Instance Swap) | Year / Month / Day focus-highlight position; **Figma-only** |
| `Show label` (Boolean) | Hides visible label only where an accessible name is otherwise provided |
| `Show supporting` (Boolean) | Displays the shared non-error supporting region |
| `Supporting text` (Text) | Either helper copy **or** a locale-derived format hint |
| `Error text` (Text) | Validation feedback in Error / Error focus |

The nested canonical **Field label** owns `Label`, `Required`, and `Show info`. They are not duplicated as unrelated top-level date properties. `Date Field Base` has a `Show calendar action` Boolean that is **False** for Date Input; Date Input has **no `Open` property** and no calendar overlay. The shared Field Base also owns an internal `Show validation icon` Boolean; it is enabled only for Error and Error focus. That **16px validation icon is at logical End** (left edge in RTL), in the same inline Auto Layout as the editable content with **12px Small / 16px Medium-Large end padding** and **4px Small / 8px Medium-Large tokenized gaps**, consistent with the canonical [Select](select.md) Chevron pattern. It must not be placed as an absolutely positioned icon on the opposite side. Date Input has no Calendar icon; Date Picker, in contrast, places Error immediately to the right of its leftmost Calendar icon in RTL.

`Filled`, `Active segment`, and `State` snapshots support Figma authoring; a runtime implementation derives empty/filled, focus, error, and actual editing state from behavior. Do **not** require consumers to pass three independent Year/Month/Day values to a public runtime component.

## Anatomy and geometry

```text
Date Input
├── Field label (Label / Required? / Info?)
├── Control
│   ├── Segmented date content (Year / Month / Day in localized order)
│   └── No calendar trigger
└── Supporting region
    ├── Helper OR format hint
    └── Error instead, when invalid
```

| Size | Control height | Inline padding |
|---|---:|---:|
| Small | 32px | 12px |
| Medium (default) | 40px | 16px |
| Large | 48px | 16px |

Use the shared control radius `6px · Medium` / Radius Medium; default surface `surface/default`, border `line/default`, content `fg/primary`, placeholder `fg/placeholder`, and label/support `fg/secondary`. Shared Field label, typography, spacing, and Radius tokens apply without date-specific replacements. The control remains one line; resizing must not truncate away the meaning of a focused segment or cause a vertical layout jump. The illustrated `YYYY/MM/DD`-style value is a **sample**, not an approved universal format.

### Focus and validation

The Focus border is **`line/emphasis` 1px**, while its separate visible Focus treatment is **`focus/default` 2px with a 1px offset**, using the two semantic Effects from the canonical Text Input control. **Do not implement Focus as an additional border or an ad-hoc stroke rectangle.**

- `Error`: `line/error` 2px, `fg/error` message, programmatic invalid state.
- `Error focus`: retains both the error border/message and the independent Focus treatment.
- `Disabled`: `surface/disabled`, `line/disabled`, `fg/disabled`; unavailable to edit.
- `Read only`: `line/muted`, readable date; focusable when the chosen runtime semantics permit. `Read only focus` retains the shared Focus treatment.
- Hover changes semantic border role without changing geometry. Focus does **not** change height or padding.

The visible segment highlight is an **inner editing-caret context**, not a replacement for the field's outer keyboard Focus ring.

**Figma anatomy rule:** compose Day / separator / Month / separator / Year in one RTL-aware horizontal **Auto Layout**, using a bound **2px spacing token** between items. Each part has its own text-bound segment wrapper, and the `Active segment` authoring highlight stays **behind** the text. Do not maintain duplicate Date Field Base placeholder layers or manually absolute-position individual date numerals.

## Date model, parsing, and editing behavior

**One date value:** consuming products supply an optional date-only value and the relevant locale/calendar configuration. A valid date must remain the same civil calendar date across timezone or UTC conversion; do not implement Date Input as an unqualified midnight UTC timestamp.

**Separate committed value and editing draft.** While typing, the user may have empty, partial, or temporarily impossible segments. Preserve this recoverable draft; do not emit or silently normalize an invalid committed date. On a complete valid entry, derive one valid date value. When validation should be shown (e.g., blur/submit) follows the Form/Product policy, not an Error on every intermediate keystroke.

**Segmented editing intent:**
- Expose year/month/day as distinguishable, individually editable segments with meaningful accessible labels, while retaining one overall field label and one date value.
- Segment order, separators, numeral rendering and expected segment widths follow the chosen locale/calendar. In the **current RTL Figma demonstration**, the visible order from right to left is Year → Month → Day. Do not assume this demonstration chooses Gregorian for all products.
- Navigate the segments in their logical/displayed order; Left/Right must be checked in RTL with actual browser and screen-reader behavior. Up/Down may increment/decrement the active segment according to calendar semantics. Preserve selection, cursor, editing, and standard keyboard shortcuts.
- Accept Persian, Arabic and Latin numerals in supported input locales; normalize for parsing without silently changing the user's intended date. Backspace/Delete should edit the active segment. Do not force focus changes on every typed digit when the user's intended segment remains ambiguous.
- **Paste** an entire supported date string as one atomic parse-and-validation operation. Do not block paste or silently reinterpret ambiguous formats. Preserve the last valid committed value and offer recoverable feedback when a pasted value cannot be parsed.
- Distinguish **missing/incomplete**, **invalid calendar date**, **out of min/max bounds** and **required** errors. Product-specific rules and exact error copy remain with the consuming form.

No hard-coded Gregorian/Jalali conversion, locale, minimum/maximum year, month ordering, or date-storage format may be inferred from the Figma example. A consuming product or pattern supplies these constraints. Unsupported ambiguous locale formats should require clarification in the interaction rather than guesswork.

## Supporting content and copy

Use **one** supporting region below the Control. Priority is:

1. Active Error message (replaces all ordinary supporting content).
2. Explicit contextual helper supplied by the consuming form.
3. Optional format hint generated from the **actual localized display format**.
4. Otherwise no supporting content.

Figma's `Show supporting` + `Supporting text` is one authoring slot. It is **not** permission to stack Helper and Format Hint as two rows. Required instructions must not exist only inside a placeholder or hidden Info affordance. Prefer concrete, correct localized format guidance over an unrelated example. An error should say what failed and how to recover where known.

## Accessibility and runtime acceptance

This is a **stateful segmented field**; using several custom editable parts demands deeper accessibility review than a plain text box. Start from [Accessible Forms](../../accessibility/forms.md), [Focus Management](../../accessibility/focus-management.md), [Keyboard Navigation](../../accessibility/keyboard-navigation.md), and the [Component Accessibility Authoring Contract](../../accessibility/component-accessibility-authoring-contract.md).

Implementation MUST:
- Have one clear field/group accessible name; meaningfully name each edit segment. Associate relevant `required`, invalid state, supporting copy, and error description programmatically; placeholder is never the sole label.
- Allow keyboard-only completion, correction, paste, and focus movement without traps. Keep the user’s draft and cursor/segment location predictable after updates and errors.
- Provide a visible outer `:focus-visible` indicator and a perceivable active editing segment. Error and Focus remain simultaneous when necessary.
- Announce validation without aggressively interrupting every keystroke; communicate incomplete and incorrect entries in text, not only by Color.
- Verify logical Tab/Shift+Tab behavior for the chosen native/segmented implementation; do not blindly reproduce Figma authoring `Active segment` as a runtime prop.
- Test with RTL/LTR, mixed scripts, keyboard-only usage, screen readers, paste/IME, mobile keyboards, reflow/zoom and Product × Appearance combinations.

**Execution status:** these are intended behavior and acceptance requirements. No executed browser, screen-reader, date parser, or Storybook tests are established by this document.

## Known gaps and intentionally deferred scope

- Confirm the product's Gregorian/Jalali choice, locale parsing order, accepted paste formats and date-only data representation.
- Verify the chosen accessible segmented-editing implementation and its Tab/arrow behavior in real browsers and screen readers.
- Define any form-level `min/max`, unavailable-date or `clearable` policy in the consuming Product/Pattern; do not multiply Figma variants for numeric limits.
- No Calendar, Date Range, Time Picker, Time Zone or combined Date-Time Picker in Date Input.
- The illustrated Figma `Filled`/segment text controls are design authoring, not verified Karbon component selectors, inputs/outputs or browser interactions.

## Source and implementation status

**Figma:** live component `24779:839` on the **Date Input** page, verified 2026-10-22.

**Karbon / Storybook:** the existing Storybook site is [karbon.jvoffice.ir](https://karbon.jvoffice.ir/). No matching runtime export, API or executed acceptance suite was verified for this Date Input component. Do not claim visual or behavioral parity solely from the Figma source.

**Review requirement:** Design System owner review, registry and link validation, and applicable accessibility-domain checks are required before this proposed normative contract is merged or promoted in maturity.
