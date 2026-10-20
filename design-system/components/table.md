---
id: design-system.component.table
collection: design-system
type: component
title: Data Table
summary: Composable RTL table for comparing and managing structured data in Job Vision products; HOS-35 working Figma pilot.
knowledge_state: unverified
document_maturity: draft
design_status: in-progress
design_maturity: pilot
related:
  - design-system.accessibility.tables-and-data-visualization
  - design-system.pattern.data-views
last_reviewed: '2026-10-20'
---

# Data Table

> **HOS-35 · Ready for Angular/Storybook sandbox, not production approved.** The Figma page follows the JV Documentation layout (Header, actual canonical Component Set, instance Playground, internal Master Anatomy, Usage & handoff). Legacy Carbon sources and V1 experiments have been moved to the separate *Archive / Data Table Legacy* Figma page without breaking source references. Runtime, cross-browser and AT tests have not been executed. This remains draft guidance, not a verified production component.

## Purpose and boundary

Use **Data Table** when users need to compare multiple entities across labeled columns, sort columns, select several rows, or perform row-level actions. Use a simple content List/Structured List when column-to-column comparison is not essential. Interactive Grid is a separate, considerably more demanding keyboard/navigation pattern.

**Accessibility authority:** [tables-and-data-visualization.md](../../accessibility/tables-and-data-visualization.md). **Runtime implementation and test contract:** [table-runtime-contract.md](./table-runtime-contract.md). The runtime specification and acceptance matrix are a draft proposal and do not imply a browser implementation exists. Normal Data Tables retain native `<table>`, `<th>`, `<tr>`, and `<td>` semantics; selection and buttons inside cells do **not** imply `role="grid"`.

## Canonical Figma sources (pilot)

File: [JV NEXT DS — Data Table / Documentation · canonical sources](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23835-127556). The original public and internal Master nodes were reparented into Sections 01 and 03; their IDs and variant contracts remain unchanged. The superseded documentation frame is archived on the same page.

| Source | Figma API | Responsibilities |
| --- | --- | --- |
| `Data Table / Default` | `Size: Small / Medium / Large`; `Selection: None / Multiple`; `Rows` SLOT | Shared table width, Header Row, body composition |
| `Data Table Header Row / Default` | `Size`; booleans for selection/Select all/expansion/actions columns; `Columns` SLOT | Header background, column positions, header select-all |
| `Data Table Header Cell / Default` | `Sort: None / Unsorted / Ascending / Descending`; `Label` | Column label and sort control; `None` means non-sortable |
| `Data Table Row / Default` | `Size` × `State: Default / Hover / Selected / Selected Hover`; booleans `Show selection`, `Show expansion`, `Show actions`; `Cells` + `Actions` SLOTs | Row surface, separator, Checkbox, disclosure, data cells, inline actions |
| `Data Table Row Item / Default` | `Size` × `Expanded: false / true` | Binds a Row and its Expanded Content in one movable unit; synchronizes chevron/detail visibility |
| `Data Table Cell / Default` | `Size`; `Content` SLOT; legacy convenience `Label` TEXT | Minimum 32/40/48px; padding-block 4/8/12px; width Fill and height Hug |
| `Data Table Text Content / Default` | `Overflow: Truncate / Wrap`; `Text` | Standard 14/20 text: 1-line ellipsis or max 2-line wrapping with ellipsis |
| `Data Table Cell Content / Text + Description` | `Primary text` and `Description` | 14/20 primary + 4px gap + 12/16 description = 40px content; not a Cell presentation variant |
| `Data Table Expanded Content / Default` | `Content` SLOT | Optional detail region after owning Row; RTL right-aligned |

**Default:** Medium, Selection None. The Table has **6 variants**, not a Style axis; Row has **12 variants**. Checkbox is the sole selection control (no Radio). Outer border is not part of the Table shell; use a surrounding Card when a framed surface is required.

### Size and dynamic height

| Size | Single-line target / minimum | Notes |
| --- | ---: | --- |
| Small | 32 px | Compact dense management screens |
| Medium | 40 px | Default |
| Large | 48 px | More room for text/content |

Size defines a **minimum**, never a maximum or a fixed height. A single-line 20px Cell Content has vertical padding **4px / 8px / 12px** in Small / Medium / Large, respectively. Cell Content is horizontally `FILL` and vertically `HUG`. Cell and Row use content-based vertical sizing with a minimum height. Multi-line content may make one row taller. Row and Header Row use an absolutely positioned 1px bottom Divider bound to `line/muted`, anchored to the bottom and stretched with width; it is excluded from the auto-layout height calculation. Figma QA confirms exact Small=32, Medium=40 and Large=48px for ordinary single-line rows, and that the divider follows dynamically taller rows. Verify the equivalent `box-sizing: border-box` CSS implementation in runtime before development handoff.

Header labels: `Label/SM` (Vazirmatn 14/20, weight 500), neutral secondary foreground. Header Row background: semantic `surface/muted`; Header has a subtle bottom divider. Individual body cells do not have vertical borders. RTL column titles and associated data share the same start position.

### Content overflow and two-line policy

**Default:** one line, ending truncation. Do not automatically wrap every column. Use `Wrap` **only for a meaningful textual field** when showing a second line materially improves understanding. Dates, numeric values, status and concise identifiers normally remain one line. Explanations longer than two lines belong in an expanded detail or dedicated view.

- To wrap text in Figma, select the Cell's **Content Slot**, replace its default Text node with `Data Table Text Content / Default`, and choose `Overflow=Wrap`. The reusable component exposes its own `Text` property. `Truncate` supports one line; `Wrap` supports **at most two lines**, both ending with an ellipsis if longer. **Editing the Cell's old `Label` property alone deliberately remains single-line**: it is preserved for existing instance compatibility.
- For intentional metadata hierarchy, insert `Data Table Cell Content / Text + Description`: primary 14/20 and secondary 12/16 with 4px gap, total content height 40px. It is not the same as automatic word wrapping.
- The parent Cell is width-Fill and height-Hug, so the Row grows to its tallest Cell. A 40px two-line content region plus Size-dependent 4/8/12px padding on each side yields actual **48px Small, 56px Medium and 64px Large**, *without changing the selected Size*. These are verified Figma pilot measurements, not Carbon/Spectrum token claims.
- Default Size minimums remain Small=32, Medium=40, Large=48. Adding a separate `Multiline` axis to the Table or Row is unnecessary. Keep selection, disclosure and action controls vertically centered when rows grow.
- For narrow columns, make sure the underlying Content instance uses horizontal Fill and vertical Hug, and the text child has an appropriate line limit. Preserve complete information through contextual details/accessibility where truncation would hide important meaning.

### Composition rules

- `Rows` SLOT accepts ordinary `Data Table Row` or grouped `Data Table Row Item`; prefer **Row Item whenever detail expansion exists**, so the detail cannot become detached from its row. The pilot does not retroactively re-wrap all existing rows.
- `Columns` SLOT uses `Data Table Header Cell`, and `Cells` SLOT defaults to four nested `Data Table Cell` instances. Table column counts and widths must be kept consistent across Header and all Rows. The last column is configured to fill remaining width. **Figma does not automatically propagate a shared column schema to arbitrary new slot children.**
- `Cell Content` SLOT allows the default one-line text, reusable `Text Content` (Truncate / Wrap), `Text + Description`, canonical passive `Tag`, or appropriately accessible custom content. Do not add `Cell Type` variants for these. The legacy `Label` property edits only the default plain-text fallback; once Slot content is replaced, edit the nested content component's own text property. This compatibility decision prevents loss of existing instance overrides.
- `Actions` SLOT initially contains three canonical `Ghost / Extra Small` Icon Buttons. **Up to three direct actions** are supported in the 96px reserved action column. Reduce to one/two through Slot editing; put further actions into a canonical overflow Menu rather than adding a fourth clipped button. Action icons require meaningful accessible names and Tooltips. If the action-column width is deliberately changed, keep Header and Body spacers identical.
- `Show selection`, `Show expansion`, and `Show actions` are Row booleans, not freeform Slots. Selection uses the canonical Checkbox. Expansion uses the canonical Icon Button/chevron.
- When the Table Selection variant is Multiple, show corresponding selection controls in Header and **every row**; the nested Row controls are not automatically synchronized when new slot items are introduced. New instances must be configured deliberately.
- For partial selection, Header Checkbox must be **Indeterminate**; none → Unchecked; all → Checked. Figma pilot examples have been updated, but runtime must derive this value from actual selected rows.
- Row selection, Hover, keyboard focus, and expansion are separate concepts. A selected Row has `surface/selected` and a checked checkbox; its expansion state does not imply selection.

### Sorting

`Sort=None` means **not sortable**; `Unsorted` is a sortable column without an active direction. Ascending/Descending display canonical JV sort icons through a nested Ghost Icon Button, which supports visual Hover/Focus states. The visible arrow does not itself implement sorting: in code provide operable button interaction, correct accessible name, `aria-sort` on the relevant `th`, focus treatment, and synchronized visual/programmatic sort state. Default sort and sort precedence remain product-specific.

### Responsive / accessibility

- Prefer horizontal overflow with reachable controls and meaningful column context; do not silently transform tables into unrelated cards or crop content.
- Avoid cell text clipping from fixed-size nested Slots: content width follows available Cell width and height follows content. Plain long text defaults to a single-line ending truncation; meaningful hidden details require accessible full text or an appropriate reveal pattern.
- Row action buttons remain ordinary Tab stops unless the product has a separately specified, tested Interactive Grid contract.
- Header/Body widths and column starts must stay aligned when the containing Table width changes.
- Provide accessible contextual action names (for example “View Ali Rezaei's application”), not just “View” repeated in every row.
- Expanded content must remain programmatically associated with the owning row; wire `aria-expanded`/`aria-controls` appropriately in runtime.

## Design-token compliance follow-up — 2026-10-20

A read-only, source-scoped audit confirmed all **10 canonical Data Table masters** meet the current Karbon token binding contract. This check excludes Figma component-set presentation geometry, borrowed Instance wrappers, and one-child icon gaps that cannot affect layout.

- **94/94 effective nonzero Spacing properties in owned source layers** are bound to Spacing variables.
- **13/13 owned Text layers** use Text Styles. **50/50 owned visible SOLID paints** use public Semantic Color tokens.
- Table/Row/Cell containers retain their intentionally square geometry; they do not need a nonzero Radius token. The Row / Header dividers keep `line/muted` semantics.
- Semantic Color matches current anatomy: Header `surface/muted`, Row `surface/default`, Hover `surface/transparent-hover`, Selected `surface/selected`, Selected Hover `surface/selected-hover`, readable text `fg/primary` and secondary content `fg/secondary`.

**The previously open 110 nested-instance spacing observations are now resolved as false positives.** Each was a raw `itemSpacing=8px` on an inherited **Icon Button → Start Icon** frame with only one direct child, so the gap is inactive. They are repeated instance-descendant observations rather than 110 independent Table defects. The upstream Button audit records the same intentional inactive-gap exception. No Table or Icon Button Figma layers were changed in this follow-up. If a source icon wrapper gains multiple children, its gap must be re-audited.

Normal, Multiple Selection, Selected Row, and Expanded Row Figma screenshots were reviewed. This **Figma token-authoring QA does not upgrade the draft/pilot Table to production-ready**. Browser/Storybook RTL layout, dynamic two-line cell heights, keyboard/accessibility behavior, Product × Appearance visual contrasts and published Slot overrides remain separate acceptance tests.

See Data Table Token Compliance and Nested Instance Provenance for source IDs, exact counts and rationale.

## QA evidence (Figma pilot)

- Resizing a live Table from 976px to 840px resized Header, Body and the flexible column together without detaching.
- Inserting two-line content into a Small cell caused its Cell, Row, body and Table heights to grow automatically; its Divider stayed anchored to the bottom. Verified Small/Medium/Large Cell examples: truncate heights 32/40/48 and Wrap-to-two-lines heights 48/56/64, respectively. Verified a real Small Table Row growing 32→48px when `Text Content / Wrap` replaced single-line content, and a real Medium Table Row growing 40→56px with `Text + Description`. All six source Table variants have exact single-line 32/40/48px Header and Row heights after the divider became an absolute, token-bound element.
- Selected + unselected rows show Indeterminate in the corresponding Header checkbox.
- An expanded selected ATS example uses a grouped Row Item without losing the example's text and checkbox selection.
- Existing examples and master sources preserve editable Slots and canonical instances.

## Pending for production release (sandbox handoff may proceed)

The Angular/Storybook sandbox can begin with the [runtime contract and acceptance matrix](./table-runtime-contract.md); this does **not** mean the tests have passed.

## Open before handoff

1. Resolve dynamic column configuration as a single schema in runtime; Figma remains compositional and cannot auto-sync arbitrary newly inserted row slots.
2. Confirm browser border-box implementation of the exact Figma 32/40/48px sizing, minimum column widths, ellipsis, wrapping, numerical alignment and RTL horizontal overflow.
3. Complete Empty/Loading/Error states, pagination, batch actions, selection across pages, sticky headers and keyboard/screen-reader testing.
4. Review Tooltip and focus behavior for Header sort buttons, row actions and disclosure.
5. Confirm consumer implementation contract with Angular/Tailwind and align with Design QA.
6. Legacy Carbon Data Table components in the same Figma file must be explicitly deprecated or archived only after checking downstream consumers; do not delete or republish them blindly.
