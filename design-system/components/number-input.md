---
id: design-system.component.number-input
collection: design-system
type: component
title: Number Input
summary: RTL-first numeric input with an optional persistent non-editable unit, field-family validation, and shared Secondary Icon Button steppers.
knowledge_state: verified
document_maturity: draft
owner: Design System team
related:
  - design-system.component.text-input
  - design-system.component.icon-button
  - design-system.accessibility.forms
  - design-system.accessibility.component-authoring-contract
topics:
  - number-input
  - currency
  - unit
  - prefix
  - stepper
  - rtl
  - accessibility
---

# Number Input — HOS-48

> **Design decision approved for Figma; implementation is not yet certified.** The accepted interaction was evaluated in an in-chat HTML prototype and transferred to the live Figma source. It has **not** been verified in Karbon/Storybook or tested with a screen reader. Figma property names below describe design authoring, not a confirmed runtime API.

## Purpose

Number Input captures a numeric value when the user may type directly or change it in steps. It reuses the **Text Input Field Family** shell: label, optional required/info affordance, helper/error feedback, border, hover, focus, disabled and read-only behavior. It adds optional increment/decrement actions and a contextual unit display.

**Use** for counts, percentages, durations, dimensions and monetary amounts where the product needs numeric validation, localized digits or stepping. Prefer Text Input for phone numbers, postal codes and identifiers that are not mathematical quantities. A discrete quantity chooser with removal and special minimum behavior may require a separate product Pattern, not a modified Number Input.

## Core value versus visible unit

**A unit is part of the displayed meaning but not of the numeric data.** For example:

| Raw numeric value | Visible field display | Unit |
|---|---|---|
| 125000 | ۱۲۵٬۰۰۰ تومان | تومان |
| 15 | ۱۵٪ | ٪ |
| 120 | ۱۲۰ px | px |
| empty / null | تومان | تومان |

The editable region contains the **number only**. The **Unit** is a non-editable inline text element immediately beside it, not a second input, a Select, a button, or a generic trailing Suffix. This Figma anatomy implements the chosen Spectrum-inspired **formatted-value appearance** while preserving a practical native input caret.

A separate, optional **Prefix** (for example W for width) identifies the meaning of the value; it is not the unit. Prefix can coexist with Unit. The overall RTL control reads **Prefix → editable number → Unit → flexible space → decrement → increment**, with **+** at the far-left edge. **RTL visual order is mandatory: the editable number is on the right and Unit appears immediately to its left.** Within Figma's horizontal Auto Layout group, the physical left-to-right child order must therefore be **Unit, then Content**; do not accidentally render Unit to the right of the number. Preserve this rule for empty, filled, focused, disabled and read-only states, including mixed Persian numerals and Latin units.

### Empty, editing and filled

- When **Show unit** is enabled, Unit is visible **before typing**, **while focused and editing**, **after the last digit has been deleted**, and **after blur**. Clearing the value does not erase its contextual unit.
- With an empty numeric value, Unit uses **fg/secondary** and is still visible. The input's raw value remains empty/null, **not zero**.
- Once a numeric value exists (including the legitimate number zero), Value and Unit both use **fg/primary**. Disabled uses **fg/disabled** for both. Read only preserves readable foreground.
- Hiding the unit during editing, showing the unit only on blur, or suppressing it when empty are **not the selected default**.
- **Show unit = False** means a plain numeric field with no unit, not a different visual Field style.
- Group spacing is **4 px** by default for short units such as تومان, سال and px; percentage may be shown without additional inter-token gap. Format/localization rules may override typographic spacing, but do not introduce a second user-facing visual-style variant.

### Initial value, empty state and Placeholder

Number Input **does not supply a numeric default value by itself**. The consuming product owns any initial value. Do not substitute zero, a dash, or an example number merely because a field is empty.

| Scenario | Numeric model | Editable display | Unit when configured |
|---|---|---|---|
| Product supplies no initial value | `null` / empty | **Blank** numeric area | Still visible, `fg/secondary` |
| Product explicitly supplies zero | `0` | `۰` | Visible, `fg/primary` |
| Product supplies a meaningful default (e.g. 100000) | `100000` | `۱۰۰٬۰۰۰` | Visible, `fg/primary` |
| User deletes every digit | `null` / empty | **Blank** numeric area | Still visible, `fg/secondary` |

- **Default Placeholder is empty (`""`).** There is no default em dash (`—`), hyphen (`-`), or zero in the editable field. A dash often means unavailable data in read-only display contexts; it is not the empty-state instruction of an editable input.
- Preserve the optional `Placeholder` authoring property for a *specific justified example*, but prefer Label or Helper for instructions, unit meaning, expected range and constraints. Placeholder must never be the accessible label.
- **Value and Placeholder are different concepts.** `Filled=False` in Figma is a design-only authoring switch that displays the optional Placeholder; it does not assign or clear a runtime numeric value. `Value="۱۲"` currently exists as a **Figma authoring example default only**, not as a product or code default.
- Numeric `0` must use the **Filled** representation in Figma; it must not be inferred from an empty field. Apply this distinction to validation, saving, accessibility and stepping behavior. An empty amount and a zero amount can have different product meanings.
- **Clearing** all digits returns to the same empty representation as an initially blank field. Configured Unit remains visible; pressing Backspace does not insert a dash or automatically restore zero. The first subsequent typed digit produces a numeric value.

## Click / focus / text-editing behavior

The entire editable side of the Control is a **focusable click region**, excluding the independent Stepper action hit targets:

| Pointer location | Expected behavior |
|---|---|
| Numeric text | Focus input and place caret at clicked text position |
| Unit text (e.g. تومان) | Focus the **same** numeric input and position caret at the **end of the numeric part** |
| Empty space inside the field (outside steppers) | Focus numeric input and place caret at numeric end |
| Increment/decrement Icon Button | Change numeric value; do not place or move a caret merely because an action was clicked |

The Unit itself does **not** introduce another tab stop or semantic button. It is a contextual affordance whose click delegates focus to the numeric input. The native input must retain selection, Delete/Backspace, copy/paste, keyboard shortcuts, input methods and horizontal scrolling for long numbers. Group separators should not cause the caret to jump during insertion or deletion; prefer delaying aggressive presentation formatting while editing if necessary.

Test the specific transition: **۱۲۵ تومان → ۱۲ تومان → ۱ تومان → (numeric value empty, Unit still visible) → typing ۵ gives ۵ تومان**. Clearing an empty field does not create a zero. Clicking the visible Unit while empty must bring the caret to the editable numeric area.

The value data and the displayed unit are distinct even where the visual display appears to be one string. Locale formatting, Persian/Arabic/Latin numeral normalization, precision and unsupported custom units such as تومان are runtime responsibilities; do not derive a serialized numeric value from the entire visible text.

## Design states and Figma authoring

Canonical source: [Number Input, 24 variants](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24570-743). [Component presentation and examples](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24605-40344).

**Size:** Small, Medium (default), Large. **State:** Default, Hover, Focus, Error, Error focus, Disabled, Read only, Read only focus. No Filled/Outline visual-style axis: there is only the shared border-based Field style.

**Top-level Figma properties:**

| Property | Role |
|---|---|
| Filled | Figma-only boolean showing numeric Value versus Placeholder. Not a runtime filled-background style. |
| Value | Numeric **display** text; do not include Unit in this Property. |
| Placeholder | Optional numeric hint; not a substitute for Label. |
| Show unit | Boolean; default False for general-purpose number entry. |
| Unit | Editable **non-interactive** unit text; Figma example defaults to تومان. |
| Show prefix, Prefix | Optional contextual text preceding the numeric value. |
| Show stepper | Boolean; exposes shared +/− controls, default True. |
| Show label, Show helper | Field Family controls; Required, Info and feedback remain nested. |

**Important:** Unit visibility is independent of Filled. Filled=False does not hide Unit. The approved **default behavior when a unit is configured** is to show it even when the numeric value is empty. The general Number Input's **Show unit default is False**, because not every number has a unit.

### Geometry and shared controls

| Field size | Control height | Reused Secondary Icon Button | Top/bottom/left inset |
|---|---:|---:|---:|
| Small | 32 px | Extra Small 28×28 px | 2 px |
| Medium | 40 px | Extra Small 28×28 px | 6 px |
| Large | 48 px | Small 32×32 px | 8 px |

Control corner radius is 6 px. Both + and − are actual **Icon Button / Secondary** instances, not a separately-maintained Stepper component. Each action can independently be Disabled at Min/Max. **The 2px inset in Small needs focus-ring clearance and target-usability review**; it does not by itself certify touch ergonomics.

Stepper accepts an intended numeric Step; its exact runtime API is not specified here. Buttons can alter a numeric value but must not silently turn an empty value into a prefilled one without an agreed starting-value rule. Min/Max enforcement, whether out-of-range typed values are clamped on commit, decimal precision, press-and-hold, mouse-wheel behavior and localized formatting are implementation acceptance points and require live validation. **Mouse-wheel changes should be off by default** to avoid accidental modifications during scrolling.

## Semantics and accessibility

- Give the numeric input a meaningful accessible name, normally from a visible Label. Include the unit in the Label or programmatically associated description when it materially affects interpretation. Visible Unit text alone is not sufficient accessible naming.
- Use native input semantics and an appropriate numeric/spinbutton pattern when stepping is available. Preserve keyboard editing; define Arrow Up/Down behavior for increment/decrement and verify it against ordinary text selection.
- The visible Unit is not separately focusable, announces no duplicate independent control, and forwards pointer focus to the editable input. Focus on click over Unit is a runtime acceptance requirement, not a Figma-proven interaction.
- Reused Icon Button actions retain their distinct accessible action names (increase/decrease) and Tooltip obligations; ensure the tab order and keyboard behavior are purposeful. Do not rely on plus/minus glyphs alone.
- Preserve shared error message and focus ring semantics. An error on the numeric value does not transform Unit into an error-colored string. Avoid color-only error communication.
- Unit and numeral direction must not reorder meaning in mixed Persian/Latin content. Test RTL with px, kg, %, decimals, grouped amounts, and long text at constrained widths.

## Boundaries and open QA

**Accepted design choices:** always-visible configured Unit (including Empty/Focus), independent raw numeric Value, whole-field click-to-focus, click-on-unit caret at numeric end, Secondary Icon Button steppers, border-based Field shell, shared states, optional Prefix.

**Not yet verified in Storybook/Runtime:** actual input caret and selection behavior, formatter/parse API, digit normalization, arbitrary precision, locale/bi-directional behavior, true accessibility tree, reader announcements, min/max/step and small-size hit-target comfort.

Do not claim shipped runtime, code parity, production accessibility certification or migration completion from Figma inspection or the earlier in-chat prototype.

## Live references

- [Figma Number Input source](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24570-743)
- [Figma Number Input presentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24605-40344)
- [Icon Button contract](icon-button.md) and [Text Input contract](text-input.md)
- [Accessibility forms](../../accessibility/forms.md)
- Karbon Storybook: https://karbon.jvoffice.ir/ — **Number Input runtime behavior not verified**
