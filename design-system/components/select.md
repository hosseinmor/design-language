---
id: design-system.component.select
collection: design-system
type: component
title: Select
summary: Single- and multiple-value selection from predefined options, with a shared Selection Panel.
knowledge_state: verified
document_maturity: implementation-ready
design_status: ready-for-sandbox
related:
  - design-system.component.text-input
  - design-system.component.autocomplete
  - design-system.accessibility.forms
---

# Select — Sandbox Implementation Handoff

**Design decision status:** READY FOR SANDBOX, 2026-10-17. This is a **design/behavior specification**, not evidence that an Angular implementation has passed QA. Refer to shared QA handoff. Runtime component selectors, exact @Input/@Output names and DOM structure are illustrative until code-reviewed.

## Purpose, boundaries

Select commits option IDs from a **known option set**. `Select / Single` commits one ID (or null), `Select / Multiple` commits an ordered unique list of IDs.

- For unbounded typed text → Text Input.
- For typed query with suggestions and value-policy → Autocomplete.
- For a product search submission → Search.
- For commands instead of value selection → Menu.
- Filtering options *inside* a Selection Panel does **not** make the Select trigger an editable Autocomplete.

## Canonical Figma sources (verified)

- [Single](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=20552-3939) — `20552:3939`
- [Multiple](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23742-5660) — `23742:5660`
- [Selection Panel](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=20619-306) — `20619:306`
- Option `20613:21`; Option Group Header `20614:46`; Select All `20614:126920`
- [Field Family QA board](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23915-841)

**Figma axes (both sets):** Size = Small / Medium / Large; State = Default / Hover / Focus / Disabled / Error / **Error focus** / Warning / Read only / Read only focus; Filled = False / True. **54 variants each** (3 × 9 × 2). Error focus was added with a 2px red error border + retained text error + the shared visible-Focus treatment, without replacing earlier component IDs.

**Figma-only compatibility notes:** `Filled` remains a Variant axis describing placeholder versus populated visual. It is not a runtime state/API; derive from actual committed value(s). The historical `Mandatory` Figma Boolean corresponds to runtime **required**, not a separate property. The set's Figma default Size is **Large** to preserve existing instances; **Medium (40px) is the default size for NEW runtime usages** and should be set explicitly in Figma. Warning remains a legacy Figma visual and is *not* mandatory in the Sandbox v1 public API. Do not block a Sandbox implementation on deleting/reorganizing these authored variants.

## Common visual anatomy

```text
Label (optional presentation; accessible name always mandatory)
Control [Leading icon? Value / Placeholder  Clear? Chevron]
Floating Selection Panel (when open; shared Option rows)
Helper OR Error/Warning supporting region
```

| Size | Control height | Radius |
|---|---:|---:|
| Small | 32px | 6px |
| Medium (new default) | 40px | 6px |
| Large | 48px | 6px |

Field: neutral border 1px; error border 2px; visible Focus follows the shared [Focus Management](../../accessibility/focus-management.md) contract; no component-specific Focus tokens. Floating panel: radius 12px, 2px anchor offset, floating shadow, correct RTL alignment; it is **not** wrapped in an additional Popover shell. Label/helper/error use canonical semantic typography and field tokens. No layout jump between Focus/Error/Error focus. Error text must remain readable/associated even if a floating panel visually overlaps.


### Selection Panel and Option typography (Figma source QA, 2026-10-20)

The shared panel and row text use the Typography Foundation according to their semantic roles rather than a custom local scale:

| Element | Canonical Text Style | Purpose |
|---|---|---|
| Option label | Body/Compact/SM · 14/20 Regular | Main selectable value |
| Option metadata | Label/XS · 12/16 Medium | Short categorical/auxiliary metadata |
| Option secondary text | Body/Compact/XS · 12/16 Regular | Short supplementary explanation |
| Option group header | Label/XS · 12/16 Medium | Nonselectable group label |
| Selection Panel title | Heading/SM · 14/20 Bold | Panel title when presented |
| Empty/result message | Body/Compact/SM · 14/20 Regular | Short list feedback |

Previously unstyled Option metadata and secondary text used 12/18 Regular. Both were migrated in all 16 Option variants. The 12 unstyled Panel title layers previously used 14 SemiBold with Auto line height and now use Heading/SM. This intentionally standardizes type metrics and weight without changing component axes, option selection behavior, content, or authoring properties.

**Structural Figma QA:** All 16 Option, 12 Selection Panel, and two Option Group Header variants retained their source identity and dimensions, with zero unstyled owned text nodes remaining in the inspected sets. Option metadata and secondary text are hidden in all 16 source variants; visible examples with multiline and mixed-script content should be tested in Playground before full visual signoff. No new Typography variable or Text Style was created. The 32px Option row and panel source dimensions were unchanged.

## Required runtime behavior

### Single

1. Empty value shows placeholder; selected value displays option label. Actual model stores option ID (or typed value if consumer option type is an equivalent unique ID); never use label as unique identity.
2. Clicking/tapping trigger, or Enter/Space where appropriate, opens list. Arrow keys move **highlight** without committing; Enter/Space on an option commits and closes (provided it is enabled). Clicking option also commits and closes.
3. Escape closes without changing the last committed value; a second activation reopens. Tab exits without an implicit commit.
4. Optional Clear removes committed value only when `clearable=true` and not required/disabled/readonly according to the owning validation policy; if required, clearing may be allowed but leaves the field invalid on validation—avoid forcibly disabling Clear solely because required is true.
5. Options may be grouped; group headers are non-selectable. Disabled options cannot commit.

### Multiple

1. Store unique option IDs and retain a stable ordering (option-list order unless the consumer explicitly requires selection order).
2. Default UI supports selected count and placeholder. Two **display policies**: `count` (placeholder/label + selected count) and `labels` (comma-separated selected labels and `+N` overflow). Overflow is a display concern, not data loss. No inline removable chip required in the Select control.
3. When `confirmOnSelect=true` (footer Confirm), clicking options modifies a **draft**; Confirm commits the draft and closes, Escape/outside dismiss discards uncommitted draft, Clear All edits draft; Cancel discards.
4. When `confirmOnSelect=false` (no confirm footer), each selection commits immediately, panel remains open until dismissed. The default for **Multiple** Sandbox should be **confirmOnSelect=true** when a footer is shown in the design; otherwise false when no footer exists. Do not show a dead Confirm action.
5. Select All applies only to enabled options in current intended scope (entire loaded list vs filtered view must be documented for the consumer). Partial selection uses Indeterminate. For v1, use **visible/filtered enabled options** and preserve hidden selections.

### Filtering panel

`filterable=true` adds the shared Search field **inside** Selection Panel, never changes the Select trigger into a text input. Search filters options without committing. Empty results use the Panel Empty state; load failure uses the Panel Error state. A consumer may supply remote options, loading and retry strategy, but it must not overwrite committed values on transient fetch errors.

### Disabled, readonly, validation

- Disabled: no focus/activation required, no popup, clear or selection actions. Use semantic disabled tokens (not raw global opacity).
- Readonly: selected value stays legible; no opening, clear, or commit. When readonly is focusable in the implementation, retain a visible focus ring (matching Read only focus in Figma).
- `required`: semantic validation; no standalone mandatory label asterisk without accessible required semantics.
- `invalid`: red 2px border + localized text error + aria association. Error and focus coexist. Warnings are optional product/form-level extension, not a v1 blocking requirement.
- Supporting priority: error > warning (if supported) > helper. Associate description/error using IDs; do not destroy the message when popup opens.

## Accessibility and keyboard acceptance

Use native select elements when they satisfy the actual UX; if the design requires a custom listbox, implement equivalent combobox/listbox (or button + listbox) semantics. **The exact DOM strategy must be chosen in runtime**, not guessed from a Figma instance. For a custom solution:

- Proper accessible label independent of placeholder; `aria-expanded`, `aria-controls` (only for mounted target), `aria-required`/`required`, `aria-invalid` and described-by relationships as applicable.
- Options expose selected/disabled and highlighted state distinctly. Never equate focus highlight with commit.
- Focus remains deterministic across Enter, Space, Up/Down, Home/End, Escape, Tab, outside click, and when the panel flips above; no keyboard trap. Test RTL.
- Interactive sub-controls (Clear, multi Confirm, Select All) have accessible names and reachable focus.
- No unexpected form submit on Enter/Space; no inaccessible popup under zoom, scroll or narrow mobile viewport.
- Mixed Persian/Latin and digits preserve logical beginning/end alignment and option identity.

## Sandbox API model (conceptual, not shipping Angular names)

```ts
type Option = { id: string; label: string; disabled?: boolean; description?: string; groupId?: string };
type SelectModel =
  | { selection: 'single'; value: string | null }
  | { selection: 'multiple'; value: string[] };
type SelectConfig = {
  options: Option[];
  size?: 'small' | 'medium' | 'large'; // default medium
  required?: boolean; disabled?: boolean; readonly?: boolean;
  clearable?: boolean; filterable?: boolean;
  display?: 'count' | 'labels'; // multiple only
  confirmOnSelect?: boolean; // multiple only
  helperText?: string; errorText?: string; invalid?: boolean;
};
```

Names above describe responsibilities only. The actual Angular API must align with the project's Storybook and form binding conventions; do not ship a second incompatible public API solely from this example.

## Acceptance

Follow shared executable QA matrix. Sandbox sign-off requires visual regression against Figma, keyboard/screen reader smoke tests, and functional checks for Single, Multiple, Search/Empty/Error/Confirm, RTL, disabled/readonly, Error focus and overflow. Component ready for **sandbox implementation** now; production readiness follows passing these tests.
