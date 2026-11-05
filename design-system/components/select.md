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
  - design-system.pattern.hierarchical-selection
---

# Select — Sandbox Implementation Handoff

**Design decision status:** READY FOR SANDBOX, 2026-10-17. This is a **design/behavior specification**, not evidence that an Angular implementation has passed QA. Refer to shared QA handoff. Runtime component selectors, exact @Input/@Output names and DOM structure are illustrative until code-reviewed.

> **Hierarchical options** (added 2026-11-05) were owner-reviewed and are built in the canonical Figma sources. They are part of the Ready for Sandbox design scope; as with the rest of this document, runtime behavior is not yet verified.

## Purpose, boundaries

Select commits option IDs from a **known option set**. `Select / Single` commits one ID (or null), `Select / Multiple` commits an ordered unique list of IDs.

- For unbounded typed text → Text Input.
- For typed query with suggestions and value-policy → Autocomplete.
- For a product search submission → Search.
- For commands instead of value selection → Menu.
- Filtering options *inside* a Selection Panel does **not** make the Select trigger an editable Autocomplete.
- For a tree-shaped option set whose parents are themselves selectable → [Hierarchical options](#hierarchical-options), following the [Hierarchical Selection pattern](../patterns/hierarchical-selection.md). Parents that are only labels stay Option Group Headers.

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

### Hierarchical options

**Status:** owner-reviewed 2026-11-05 after prototype and Figma review; canonical in Figma. The cross-component decisions (when to use, exact vs inclusive scope, composition edge cases) are owned by the [Hierarchical Selection pattern](../patterns/hierarchical-selection.md). This section owns only what Select itself renders and does.

**Scope:** `Select / Single` and `Select / Multiple`. In Multiple, hierarchical options always use **cascade** selection (rule 7). Independent per-node multiple selection over a hierarchy is not supported in v1; when parent and child must be chosen independently, the consumer is treating the data as flat and should use a flat Multiple.

1. **Model.** Each option may carry `parentId`, from which the runtime derives `level` (0 = root); a consumer may supply `level` directly. Options render in **depth-first tree order**. Identity stays the option ID; labels may repeat under different parents. More than one root is valid.
2. **Rows.** Every node, including a parent, is a normal selectable Option with the existing states. Parents are **not** styled as Option Group Headers and get no extra weight. The list is always expanded: no disclosure chevron and no expand/collapse state, so each row has a single select target. Hierarchical options and Option Group Headers are **not combined** in one list. Leading icons are all-or-none within a hierarchical list.
3. **Indent, indicator and guides.** Row order from the logical start (right in RTL) is `[Option Indent] [Selection indicator slot] [Content]`, in Single **and** Multiple: the indicator moves with the indent, because it belongs to the node.
   - **Alignment rule:** a child's indicator aligns exactly with the start of its parent's content (the leading icon when shown, otherwise the label). The indent step is therefore derived, not chosen: step = indicator slot (16px) + indicator-to-content gap (8px) = **24px** (`spacing` 24px). Visual cap at level 3 (proposed); deeper levels keep the level-3 indent. If the indicator size or the Option gap ever changes, the step changes with it.
   - **Indent guides are always shown** for level ≥ 1: one 1px vertical line per ancestor level, `line/default`, centred under that ancestor's indicator (8px from the step's logical start). They are part of Option Indent, never cross the indicator, and have no consumer toggle. A flat list has level 0 everywhere, so it shows no guides.
   - Selected state follows the existing Option contract: Single shows the check in the indicator slot with **no selected background**; Multiple shows the checkbox (rule 7). Hover keeps the existing hover surface.
4. **Search keeps the structure (default).** With `filterable=true` and a non-empty query, the list shows the **matching options plus their ancestor chain**, with the same indent and guides as the unfiltered list.
   - Ancestors that do not match are **context rows**: label in `fg/secondary`, still enabled and selectable (they are real values), never styled as Disabled. Exceptions: a context row that is the committed (Single) or drafted (Multiple) selection keeps `fg/primary`; a disabled row keeps the Disabled treatment.
   - **No substring highlighting** of the query, consistent with current Select and Autocomplete. It would also risk breaking Persian letter joining when weight changes mid-word. The context/match colour difference is the only cue; it is supplementary, since all content stays readable. Descendants of a match are not shown unless they match too.
   - Keyboard highlight starts on the **first matching row**, not on a context row.
   - Clearing the query restores the full list. A `flat-path` presentation is a documented alternative for constrained width or very deep trees: flat results, each non-root result with its ancestor path as secondary text in the [Breadcrumb](breadcrumb.md) format (`/`, `Root / … / Parent` beyond two ancestors). Its clearest layout is still open; choose it per product context, not per query.
5. **Trigger.**
   - Single shows the committed label. When labels are non-unique, or the field is read-only after a lifecycle lock, it prefixes the **nearest parent** only, as `Parent / Label` with the Breadcrumb `/` separator in secondary foreground. The full path goes to the accessible description. Showing more ancestors in the trigger pushes out or truncates the label itself, which is the part the user needs.
   - Multiple keeps the existing display policies. With `labels`, a fully selected subtree is shown once as `{label} {qualifier}` instead of listing every descendant; `+N` overflow counts these groups. With `count`, the count is the number of committed IDs.
6. **Inclusive scope (Single).** A consumer sets `hierarchyScope: 'exact' | 'inclusive'` (default `exact`). Select still commits one option ID; the consumer interprets descendants. With `inclusive`, the trigger appends the scope qualifier after commit and the field helper states the rule once. Rows do **not** show descendant counts or per-row qualifiers. Wording is owned by Content.
7. **Cascade (Multiple).**
   - A node's checkbox reflects its whole subtree: all selected → checked; some → indeterminate; none → unchecked.
   - Toggling a checked node removes the node and its subtree; toggling an unchecked or indeterminate node adds the node and its subtree.
   - Unchecking a child leaves the parent itself selected and shows it indeterminate, because the parent is a real value.
   - The committed value is every selected ID in tree order. Compression for display (rule 5) never changes the committed value.
   - Draft, Confirm, Cancel, Clear All and dismissal follow the existing Multiple rules. **Select All** applies to matching rows only, never to context rows.
   - Known risk: in search, toggling a matching parent also selects descendants that are not visible. The trigger and the Confirm footer must show the true resulting count before commit.
8. **Accessibility.** The popup stays a **listbox** (`aria-multiselectable="true"` for Multiple). Do not use `role="tree"` to express indentation. `aria-level` is not valid on `option`; associate each option with its full ancestor path via `aria-describedby` (visually hidden), in both the full list and search. `aria-checked="mixed"` is not available on `option`, so an indeterminate parent adds "partially selected" (localized) to its description. Context rows in search are announced as ordinary options. For `inclusive`, the trigger's accessible value includes the qualifier.

**Figma (canonical, Select page):**
- **`_Option / Indent`** component set, `Level = 0/1/2/3`, in `03 · Anatomy & composition › Canonical Masters / Option · Header · Select All`. Each level adds one 24px step bound to the Spacing `24px` variable, with a 1px `line/default` guide centred under the ancestor's indicator. Level 0 is effectively zero width, so existing instances are visually unchanged. Levels above 3 use `Level=3`.
- **Option** (`20613:21`, now 20 variants): `Selection indicator slot` holds `[Indicator 16×16 fixed][Indent]`. The fixed Indicator frame keeps the 16px reserve when the check is hidden. Indent is a nested, exposed instance, so `Level` is set on the Option instance. No new axis for level.
- **`Selected=Indeterminate`** exists for `Selection=Multiple` only (4 variants, sparse matrix), for cascade parents.
- **Context rows** are authored by overriding the Option Label fill to `fg/secondary` on the instance. No variant or property: a new axis would double the Option matrix and collide with State, and a boolean cannot change colour.
- **Playground:** `02 · Playground › Playground / Hierarchical options`: four complete Select instances (`State=Default`, `Open=true`, filterable Selection Panel): Single full list, structure-preserving search with a `Parent / Label` trigger, Multiple cascade with `labels` + `+N` summary and Confirm footer, level cap.
- **Option spacing:** the Selection Panel `Options` slot now stacks Option rows with **0 gap** (previously 2px) in every Results variant, so indent guides run continuously. This applies to all Selects, hierarchical or not. See *Focus in the open panel* for the related fill and clipping changes.
- **Playground selects** use `State=Default` + `Open=true`; the search example shows the keyboard-active first match in `State=Focus`.

### Disabled, readonly, validation

- Disabled: no focus/activation required, no popup, clear or selection actions. Use semantic disabled tokens (not raw global opacity).
- Readonly: selected value stays legible; no opening, clear, or commit. When readonly is focusable in the implementation, retain a visible focus ring (matching Read only focus in Figma).
- `required`: semantic validation; no standalone mandatory label asterisk without accessible required semantics.
- `invalid`: red 2px border + localized text error + aria association. Error and focus coexist. Warnings are optional product/form-level extension, not a v1 blocking requirement.
- Supporting priority: error > warning (if supported) > helper. Associate description/error using IDs; do not destroy the message when popup opens.

### Focus in the open panel (resolved 2026-11-05)

Follows the shared [Focus Management](../../accessibility/focus-management.md) contract; no exception is introduced.

- **Opening is not field focus.** Opening with pointer does not draw the field's Focus ring; the ring appears only under `:focus-visible`. While the panel is open, DOM focus is in the panel's Search (when filterable), so the field shows its normal state. Figma examples of an open Select therefore use `State=Default` + `Open=true`, never `State=Focus`.
- **Active option.** `Option / State=Focus` represents the visible focus of the keyboard-active option (`aria-activedescendant`), not hover and not selection; it composes with Selected. Pointer movement shows Hover; keyboard movement, typing in Search, or keyboard opening shows the Focus ring on the active option.
- **Ring not covered or clipped.** Option rows now touch (0 gap), so Option variants other than Hover and Focus have **no fill**; the panel surface shows through and a neighbor never paints over the focused row's external ring. Focus variants keep `surface/default`, which the `Focus/Default` effect needs to render. In Figma, `Results viewport` no longer clips; `Results region` still clips with 8px padding, which contains the 3px ring. At runtime, use `outline` + `outline-offset: 1px` on the active option and keep at least 3px inner padding in the scroll container so the outline is not clipped.

### Open issue: long labels

Option Label is `HUG` with truncation disabled, so long labels can overflow the row. This affects every Select, and hierarchical lists more (about 176px of text at level 3 in a 288px panel). Decide in the canonical Option, independently of hierarchy: proposed Label `FILL` with wrap to two lines, or end truncation with the full label available on focus/hover.

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
type Option = {
  id: string; label: string; disabled?: boolean; description?: string; groupId?: string;
  parentId?: string | null; // hierarchical options
  level?: number;           // derived from parentId when omitted
};
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
  hierarchyScope?: 'exact' | 'inclusive'; // hierarchical; single only; default 'exact'
  searchPresentation?: 'tree' | 'flat-path'; // hierarchical only; default 'tree'
  // hierarchical Multiple always cascades; no independent mode in v1
  helperText?: string; errorText?: string; invalid?: boolean;
};
```

Names above describe responsibilities only. The actual Angular API must align with the project's Storybook and form binding conventions; do not ship a second incompatible public API solely from this example.

## Acceptance

Follow shared executable QA matrix. Sandbox sign-off requires visual regression against Figma, keyboard/screen reader smoke tests, and functional checks for Single, Multiple, Search/Empty/Error/Confirm, RTL, disabled/readonly, Error focus and overflow. Component ready for **sandbox implementation** now; production readiness follows passing these tests.

**Hierarchical options — additional Sandbox checks:** depth-first order with multiple roots; indent cap; guides always present for level ≥ 1 and never crossing the indicator; indicator moving with indent in Single and Multiple; parent options selectable with ordinary states and no selected background in Single; tree-preserving search with context rows (secondary label, enabled, primary when selected, excluded from Select All, keyboard starting on the first match, no substring highlight); duplicate labels distinguishable in panel and trigger; `inclusive` qualifier in trigger and its accessible value; Multiple cascade states (checked, indeterminate, unchecked), parent remaining selected when a child is removed, compressed `labels` display and true count before Confirm; screen reader announces full path and partial selection; RTL with mixed Persian/Latin labels and paths.
