---
id: design-system.pattern.data-views
collection: design-system
type: pattern
title: Data Views
summary: Choosing between tables, lists, and interactive grids, and composing common data-view controls.
knowledge_state: unverified
document_maturity: draft
related:
  - design-system.component.table
  - design-system.accessibility.tables-and-data-visualization
last_reviewed: '2026-10-14'
---

# Data Views

> Draft pattern guidance supporting the HOS-35 Table pilot. Not yet verified across all Job Vision products.

## When to use

Select by **user task and information structure**, not density or fashion.

- **Data Table** — users must compare entities by shared columns, sort structured information, select multiple rows, or take actions on records.
- **Structured List** — users need to scan rich items with uneven metadata and comparison across columns is not important.
- **Simple List** — ordered/unordered sequences or basic repeated content.
- **Interactive Grid** — spreadsheet-like cell/row navigation, editing, or a compound keyboard interaction model. Requires a distinct accessible composite-widget contract.

See [Tables and Data Visualization accessibility](../../accessibility/tables-and-data-visualization.md): a selectable table with Buttons inside cells is **not** automatically an ARIA Grid.

## Recommended Data Table composition

```text
Data View Header (optional title, count and supporting actions)
Filters / Search (if applicable)
Table toolbar (optional)
Data Table
  Header Row: select-all, sortable header cells, expansion spacer, actions spacer
  Rows slot:
    Row (ordinary record)
      Checkbox?  Disclosure?  Cells[]  Actions[]
    Row Item (if expandable detail is present)
      Row
      Expanded Content
Pagination / result count (separate pattern)
```

Do not build distinct Table variants for Loading, Empty, Filters, Pagination, or number of rows. Represent these at the data-view/pattern level.

## Row actions

Keep 1–3 direct icon actions in the reserved column, using canonical Icon Button instances. Additional actions belong in the canonical Menu/Overflow pattern. Every action needs a contextual accessible name and Tooltip. The action column stays aligned with its Header spacer.

## Selection

None and Multiple (Checkbox) are the currently supported HOS-35 selection modes. Header Select All has Unchecked, Indeterminate and Checked states derived from the current selection domain. Explicitly define whether select-all spans the page, filtered results, or all results; HOS-35 Figma does not settle this product policy.

## Expansion

Use grouped Row Item for a row with additional details: Row and Expanded Content travel together in reorder, duplicate, or delete flows. Keep expansion independent of selection. Expansion is not the same as hierarchical parent/child tree rows.

## Responsive behavior

Preserve column correspondence and semantic relationships. Prioritize predictable horizontal scrolling with accessible controls. Only provide a mobile card/list alternative when product requirements and accessibility have been reviewed; it must not silently change the meaning of the data.

## Content guidelines

Prefer concise data labels, predictable number/date formatting and semantic Tag components rather than ad-hoc status colors. Two-line content is a controlled exception, not the default for every column. Default single-line content truncates. For meaningful long text use `Data Table Text Content` with `Overflow=Wrap` (maximum two lines, ellipsis beyond that); for intentional primary/secondary metadata use `Text + Description`. Both belong inside a Cell Content slot and grow only their owning Row through Hug height. The Table Size remains Small/Medium/Large, with minimum heights 32/40/48px and two-line examples 48/56/64px thanks to 4/8/12px Cell vertical padding. Dates, numbers and statuses should normally remain one line. Avoid excessive per-row actions and unnecessary multi-line columns in dense management tables.

## Known gaps

Cross-page selection, row virtualization, editable cells, persistent sort/filter state, loading/empty/error, bulk toolbar composition, pagination and accessibility interoperability need separate pattern/product validation.

Related: [Data Table component draft](../components/table.md).
