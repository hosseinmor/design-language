---
id: design-system.component.autocomplete
collection: design-system
type: component
title: Autocomplete
summary: Editable single-value query input with suggestions; explicit free-form and selection-required value policies.
knowledge_state: verified
document_maturity: implementation-ready
design_status: ready-for-sandbox
related:
  - design-system.component.select
  - design-system.component.search
  - design-system.component.text-input
  - design-system.accessibility.forms
---

# Autocomplete — Sandbox Implementation Handoff

**Design status:** READY FOR SANDBOX, 2026-10-17. This is an approved UX/state contract for implementing and testing a v1 Sandbox—not proof of an existing production Angular API. Shared handoff and QA.

## Purpose and boundaries

Autocomplete is an **editable text field** with suggestions. It handles typed query, highlighted suggestion and committed value **separately**. It does not replace Search (search submission), Text Input (unassisted free text), Select (non-editable trigger), or Menu (actions).

**Value policies are approved for v1**, as previously resolved for Job Vision search fields:

1. **`free-form`** — arbitrary user text is valid, suggestions are optional. **Example: job title search query**.
2. **`selection-required`** — valid committed value must come from an option ID in the candidate list. **Examples: City and Job Group**.
3. `creatable` is not in v1. Do not silently treat arbitrary text as a new selectable ID.

`valuePolicy` is a conceptual implementation prop, not a new Figma variant axis.

## Canonical Figma and anatomy

- [Autocomplete / Single](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23861-24) — node `23861:24`.
- [Selection Panel](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=20619-306) — node `20619:306`; its real Option Slot is reused.
- 24 variants = Size Small/Medium/Large × State Default/Hover/Focus/Error/Error focus/Disabled/Read only/Read only focus.
- `Filled` is a Figma Boolean controlling sample visual placeholder/value, **not** a runtime Boolean state.
- Figma authoring: Placeholder, Value, Show label/helper/leading icon/clear, Open, Show chevron. Underlying label/helper/error use shared Field primitives.
- Medium 40px default, Small 32px, Large 48px; border-only radius 6px; shared focus effect, 2px error border + visible error text; 12px floating panel radius with 2px trigger offset.
- Leading icon on logical start (right in RTL); clear/chevron at logical end (left in RTL). Chevron is **optional** and not a required default for an editable Autocomplete.

## Figma token-compliance check — 2026-10-20

The canonical source audit verified the original **24 Autocomplete / Single** variants and shared Selection Panel inheritance. **No Autocomplete source edits were required.**

- **96/96** effective layout Spacing properties use Foundation Spacing variables.
- **48/48** owned text layers are linked to approved Text Styles.
- **48/48** owned positive Radius properties use `6px · Medium`.
- **120/120** owned visible solid fills/strokes consume public `03 Semantic` color variables.
- All **24/24** nested Selection Panel instances inherit `12px · Large` from the upstream Selection Panel source, without local raw Radius overrides.
- Focus, Error focus and Read only focus have the existing shared `Focus/Default` effect; Error focus keeps its 2px `line/error` Border and visible Error helper. Controls remain 32/40/48px by Size.

The page's three existing open linked Playground samples (job title, city, job group) are source-linked and display correctly in RTL. `Open` is intentionally false for the default 24 master variants; it is true in the consumer examples. Treat it as a Figma authoring property, not a default always-visible Popup.

**Remaining acceptance:** published override integrity following the upstream Selection Panel migration, live keyboard focus ring visibility (the screenshot renderer may not show the existing shadow), Product × Appearance editor/runtime visual testing and editable-combobox interaction/AT tests. This mechanical source audit does not upgrade the component's **Ready for Sandbox** status to production-ready. Image Uploader remains out of scope.

## State and event model — normative

Distinguish:
- `query`: transient text typed into the input.
- `activeOptionId`: keyboard-highlighted, **not selected**.
- `committedValue`: either a string (`free-form`) or a selected option ID (`selection-required`), plus display label.
- `displayText`: visible text after last commit; may equal the query while editing.
- `open`: panel visibility independent of query/focus/value.
- `loading`/`empty`/`error`: result-request states independent of field validation Error.

**Transitions:**

| Event | free-form | selection-required |
|---|---|---|
| Input typing | Updates query, results; does not force option commit | Updates query, results; does not force selection commit |
| Click/Enter highlighted suggestion | Commits candidate display text/semantic value, closes | Commits chosen **option ID** and label, closes |
| Enter without highlighted suggestion | Commits trimmed query text, closes | Does **not** commit arbitrary query; remains pending while focused |
| Blur/Tab with uncommitted query | Commits trimmed free-form text (or empty string/null per owning Form) | Reverts display to last committed option, or placeholder when none |
| Escape while open | Closes and restores last committed display if query uncommitted | Closes and restores last committed option label |
| Clear | Clears query, committed value, active suggestion and result error; invokes normal validation policy | Same, including selected option ID |
| Selecting another suggestion | Replaces the committed text/value | Replaces the committed option ID and display label |

**Important:** If Enter with an unhighlighted query occurs in selection-required mode, it must **not** submit the parent form as though a valid ID were chosen. If there is a validation requirement, show it on form validation/submission; do not mark every keystroke invalid.

**Value-policy default:** No implicit switching based on content. Consumers must choose the policy explicitly. For product search: `free-form` for Title, `selection-required` for City and Job Group.

## Suggestions and async data

- Results come from a pluggable provider (local filter or remote). The component owns displaying queries/highlight/selection; the owning product/provider owns request data, ranking, deduplication, API/caching and business-specific ranking.
- **Default query threshold** for local providers can be 0; for remote providers use a configurable `minChars` (recommended 2, not hard-coded for every consumer) and configurable debounce (recommended ~250ms, not a universal product rule).
- Never let out-of-order request responses replace more recent query results. Abort obsolete requests or ignore responses by query/version key.
- Panel modes: Results, Empty/No results, fetch Error. Loading must have visible/announced pending feedback; **do not reuse field validation Error** for transport failures.
- Filter/selection occurs within the shared Selection Panel. Filterable search control inside the panel should not produce a second nested editable search when the Autocomplete input itself already filters; `Filterable=False` in this composition.
- When the list becomes empty, clear obsolete `activeOptionId`. Repeated opening preserves committed value but restarts the query presentation consistently.
- Optional Chevron can reveal the available suggestions only if the product genuinely requires a full-list affordance. Use plain Select for a non-editable predefined list.

## Disabled, readonly, errors and interaction

- Disabled: cannot type, clear or open. Accessible disabled semantics and disabled tokens, not just opacity.
- Readonly: legible committed text, no typing, clear or popup. If focusable, preserve focus ring; it is not a visually disabled field.
- Validation Error shows 2px error border and text, with a focus ring **also visible** in Error focus. Helper yields to Error, without the message becoming inaccessible while popup is open.
- Label and required indication from the shared Field primitives; placeholder alone is not a label.
- Selecting an option must not unexpectedly submit its enclosing form.
- For RTL: logical action order, correct Persian/Latin mixtures, and stable option ID, independent of label.

## Accessibility and keyboard

Editable input should implement the appropriate **editable combobox with listbox** accessibility contract where custom suggestions are rendered: text input retains focus as appropriate, `aria-expanded` follows open status, `aria-controls` references actual mounted popup, `aria-activedescendant` references the currently highlighted option only when it exists, and selection is separately announced. Use accessible error/helper associations and `aria-invalid` when validated invalid. Screen readers must hear loading/no-results/results and selection changes appropriately.

- ArrowDown/ArrowUp navigate options; Enter chooses highlighted option; Escape closes/restores; Tab moves on without trapping focus.
- Home/End and text editing keys must respect caret editing versus list navigation; do **not** hijack text cursor movement.
- Clicking an option with pointer/touch commits same semantics as keyboard.
- Close on outside click with predictable commit/revert per valuePolicy; restore focus sensibly.
- Popup anchoring must handle screen edges, scroll, zoom, short viewport and touch keyboard without helper/error being logically inaccessible.

## Conceptual Sandbox model (not current Angular signature)

```ts
type ValuePolicy = 'free-form' | 'selection-required';
type Suggestion = { id: string; label: string; disabled?: boolean; description?: string };
type AutocompleteConfig = {
  valuePolicy: ValuePolicy;
  value: string | null;   // free-form text OR selected option ID by policy
  displayText?: string;   // meaningful for selection-required
  size?: 'small' | 'medium' | 'large';
  disabled?: boolean; readonly?: boolean; required?: boolean;
  clearable?: boolean; showChevron?: boolean;
  minChars?: number; debounceMs?: number;
  helperText?: string; errorText?: string; invalid?: boolean;
  suggestions?: Suggestion[];
};
```

The actual implementation may use objects/IDs, Angular ControlValueAccessor, signal/observable bindings and separate display label/model props. Use the owning runtime architecture to decide, and **avoid an untyped `value` with ambiguous ID vs query meaning**.

## Sandbox acceptance

Use the shared executable QA matrix, including two real Job Vision examples: job title free-form and city/job group selection-required, asynchronous out-of-order results, long RTL + Latin values, and disabled/readonly/error-focus cases. **Ready for Sandbox, not signed off as production**.
