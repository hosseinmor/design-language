---
id: design-system.pattern.value-summary
collection: design-system
type: pattern
title: Value Summary
summary: Compose converted numeric values and shared multi-field numeric range summaries without adding new Number Input properties or duplicating field support.
knowledge_state: verified
document_maturity: draft
owner: Design System team
related:
  - design-system.component.number-input
  - design-system.component.text-input
  - design-system.accessibility.forms
  - design-system.accessibility.dynamic-content-and-feedback
topics:
  - numeric-range
  - summary
  - conversion
  - salary
  - helper
  - form-group
---

# Value Summary — converted values and numeric ranges

> **Approved composition boundary; runtime unverified.** This pattern describes how to display derived, non-editable values underneath numeric inputs. The product owns the source units, conversion factor, precision, salary eligibility, constraints and business copy. Do not infer a runtime Value Summary API or Storybook parity from these design examples.

## Purpose and ownership

Users may enter a compact value, for example `۲۰` **میلیون تومان**, but need to verify its exact equivalent: `۲۰٬۰۰۰٬۰۰۰ تومان`. Sometimes two related numeric fields require **one combined explanation**, such as a salary range.

**Two distinct presentation scopes:**

1. **One field → existing Field Helper:** show that field's derived equivalent in its ordinary supporting-content area. No new Number Input component property, variant, nested unit, or dedicated Value Summary component is necessary. Example: numeric value `20`, Unit `میلیون تومان` → Helper **`معادل ۲۰٬۰۰۰٬۰۰۰ تومان`**.
2. **Several related fields → Value Summary pattern:** show one non-interactive summary **under the entire Field Group**, not under either field individually. Compose existing Number Inputs and a shared text region. Example: **`از ۲۰٬۰۰۰٬۰۰۰ تومان تا ۲۴٬۰۰۰٬۰۰۰ تومان`**.

A summary is **derived presentation**, never an editable input value, placeholder, second unit slot, or separately saved source of truth. Runtime calculates it from the underlying numeric field values and product-defined conversion functions.

## Composition

```text
Single converted value
└── Number Input
    ├── Field label
    ├── Editable numeric control + persistent Unit
    └── Helper → formatted equivalent

Multiple related values
└── Field Group: salary range
    ├── Number Input: minimum
    ├── Number Input: maximum
    └── Value Summary region
        └── one combined, formatted sentence OR validation feedback
```

Place the shared region **below the pair or group**, after the input row, following the Field Family's supporting-content spacing and semantic text roles. Use an ordinary `Body/Compact/SM`-scale, `fg/secondary` presentation for a neutral summary; it must remain readable, wrap naturally at narrow widths and follow RTL reading order. No extra informational icon is required when the sentence is self-explanatory. Do not introduce a new component-token family.

In RTL, minimum is the **right-side** field and maximum is the **left-side** field; the summary reads naturally from **از** to **تا**. This arrangement can reflow to one column on narrow screens while preserving logical order.

## Empty, partial and complete values

The following is a **demonstration of optional bounds**, not a universal salary product policy. Products may instead require both bounds.

| Minimum | Maximum | Example group presentation |
|---|---|---|
| empty | empty | No summary visible |
| 20 million | empty | `از ۲۰٬۰۰۰٬۰۰۰ تومان` |
| empty | 24 million | `تا ۲۴٬۰۰۰٬۰۰۰ تومان` |
| 20 million | 24 million | `از ۲۰٬۰۰۰٬۰۰۰ تومان تا ۲۴٬۰۰۰٬۰۰۰ تومان` |
| 24 million | 20 million | Group-level validation error; normal summary is suppressed |

**Important:** an actual numeric **zero** is not empty; if zero is permitted by product policy, represent it as a real bound and include it in the derived sentence. Never insert `۰`, `—` or invented min/max values for empty inputs. A field may continue showing its own persistent Unit even when no group summary exists.

### Conversion and formatting

- The **source unit** and **display unit** are independently defined by Product/Pattern usage. In this example, `1 million تومان = 1,000,000 تومان`; this factor is not hardcoded as a Number Input requirement.
- Preserve numeric precision until formatting. Use locale-aware Persian digits and grouping in the readout without modifying raw values or corrupting caret behavior in either input.
- Format each bound with its **own explicit display unit**, even if both share تومان. Avoid ambiguous constructions or repeating a partly specified suffix.
- Update the displayed sentence when committed/valid values change; product policy owns any debounce and whether updates happen on each input, blur, or validation commit.
- Unknown, invalid, intermediate or partially typed numeric states must not produce a misleading computed amount. A previously valid summary must not be presented as current after a relevant value becomes invalid.

### Error priority and message placement

Group validation feedback takes priority over the neutral Value Summary. Do not render the contradictory range sentence under a range error. If the error is **presented once at Field Group level**, avoid duplicating the same copy inside a constituent Number Input's inline Error slot; visually mark the offending field(s) and programmatically associate the shared error with the affected inputs. **There must still be a textual error**, not just an error-colored border. Conversely, a localized field-specific error can use that field's existing Error region when group-level feedback is unnecessary.

Exact range constraints and copy are **Product-owned**; the demonstration message `حداقل حقوق نباید از حداکثر حقوق بیشتر باشد.` is an example, not a universal validation rule.

## Accessibility and content

- Give each Number Input its own discernible Label and retain the group's accessible name (e.g. **محدوده حقوق**). The summary is **read-only output** and not a tab stop.
- Associate a meaningful group-level explanation with the group or its input controls where appropriate, e.g. an `aria-describedby` relationship. Reuse the existing per-field Helper semantics for one-field conversion.
- Do not automatically trigger an assertive live-region announcement on **every keypress**. Prefer a non-live description or non-disruptive updates after commit/blur; when announcements are required, test timing and deduplication with assistive technology.
- Error messages must be programmatically associated with the invalid control(s). Semantic invalid state and focus handling remain part of the constituent Number Inputs and product form.
- Avoid making the derived output the only place that expresses essential units; keep the unit visible beside each numeric field, including the empty state, according to the Number Input contract.
- Ensure RTL punctuation, Persian grouping, mixed Latin units and long formatted amounts remain legible without horizontal overflow.

## Figma review examples

[Number Input documentation — Derived value and group range examples](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24805-1893) includes:

- one Number Input with a real instance of the existing Helper;
- two source-linked Number Inputs plus one neutral range summary;
- minimum-only, maximum-only and no-value examples;
- invalid-range example with shared error replacing the normal summary.

These are **composition examples**, not a new published Value Summary component. The canonical [Number Input source](../components/number-input.md) remains unchanged. Validation of dynamic behavior in Karbon/Storybook is pending.

## Open implementation questions

- Product-specific optional/required bound policies, exact salary unit conversions and rounding;
- whether to update derivations live or on commit/blur, including IME and partially entered decimals;
- accessible linking/announcement strategies in actual forms;
- responsive two-field layout and whether other product domains justify a published Figma/Storybook composition API.
