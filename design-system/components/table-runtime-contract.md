---
id: design-system.component.table-runtime-contract
collection: design-system
type: component
title: Data Table — Runtime and Accessibility Contract
summary: Proposed implementation contract and acceptance tests for the HOS-35 RTL Data Table pilot.
knowledge_state: unverified
document_maturity: draft
design_status: in-progress
design_maturity: pilot
related:
  - design-system.component.table
  - design-system.pattern.data-views
  - design-system.accessibility.tables-and-data-visualization
last_reviewed: '2026-10-14'
---

# Data Table — Runtime and Accessibility Contract

> **Status: development-handoff proposal, NOT a verified runtime implementation.** Figma geometry, instance composition and visual states have been tested. Angular/browser functionality, assistive-technology behavior, live scrolling/zoom, and automated tests have **not** been implemented or run. Preserve the canonical [cross-cutting table accessibility document](../../accessibility/tables-and-data-visualization.md) as authority; this document specifies HOS-35 component-specific behavior only.

Figma: [Data Table / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23522-13721).

## 1. Native semantic model

- Default to a native HTML `<table>` inside a descriptive scroll wrapper, with `<caption>` or one appropriate externally labelled heading. Use `<thead>`, `<tbody>`, `<tr>`, column `<th scope="col">`, and `<td>`.
- **Do not** apply `role="grid"`, `role="row"`, or generic clickable `div` rows to implement normal checkbox selection. Each Button/Checkbox/Link in a native table is an ordinary Tab stop. Do not simulate spreadsheet Arrow-key navigation.
- In RTL, use `dir="rtl"`, stable logical column order, CSS logical properties, and meaningful relationships between each visible header and its data cells. The visual right-to-left position must match the actual DOM column order.
- Visible column count includes selection, disclosure and action columns. When rendering a full-width detail or state cell, set `colSpan` to the **actual** number of visible columns; do not hardcode `4`, `6`, etc.
- Provide at least one accessible table name without duplicating the same label excessively (native `caption` when appropriate; otherwise `aria-labelledby` to an existing heading).

## 2. Component state ownership

**Proposed public-facing state model, to review during Angular sandbox implementation:**

| Item | State owner | Minimum contract |
| --- | --- | --- |
| Table Size | Parent Table | `small / medium / large` maps to 32 / 40 / 48 px minimum visual row heights |
| Columns | Parent Table | Ordered IDs, header labels, widths, sortability, alignments; a single schema across Header and every Row |
| Sort | Parent Table / consumer | At most one active column + direction; one controlled update callback |
| Selection | Parent Table / consumer | Stable row IDs, selectable/disabled criteria, explicit Select All scope |
| Expansion | Parent Table / consumer | Expanded row IDs; independent from selection |
| Row actions | Row composition | One to three direct named actions; others in canonical overflow Menu |
| Cell content | Per column/row | One-line default, max-two-line Wrap or text+description; Tag/custom through composition |
| Loading/error/empty/pagination | Data View pattern | Separate view states/patterns; not Table Size or Row State variants |

Use stable, semantic row IDs; **never** use page array indexes for selection/expansion keys. Do not infer the selected state from CSS or a Checkbox's transient internal state.

## 3. Layout and overflow

| Size | Minimum single-line Row | Vertical Cell padding | Expected 40px content Row |
| --- | ---: | ---: | ---: |
| Small | 32px | 4px each side | 48px |
| Medium | 40px | 8px each side | 56px |
| Large | 48px | 12px each side | 64px |

- Table/Row height is driven by the **tallest Cell**, not by a multiline Boolean or a fixed CSS `height` on `tr`. A text + description recipe is 20px primary + 4px gap + 16px description = 40px content.
- Apply the minimum size to a reliably measurable Cell inner wrapper or equivalent table layout, as native table-row `min-height` is not sufficiently dependable across browsers. Ensure controls remain vertically centered.
- Render bottom separators without adding an extra pixel to Size (CSS `inset` shadow/border-box strategy, verified against the Figma 1px absolute `line/muted` divider).
- Content Wrap is deliberately opt-in and limited to **two lines** with ellipsis for additional text. Truncate is one line with ellipsis. Never cut off interactive elements, numeric values, dates, or status text without an explicit, accessible alternative.
- Keep logical column widths consistent under resize; never let the Header label position move away from its data. Implement column minimum widths and horizontal scrolling in a container. Do not silently transform a data table into cards.
- If the scroll wrapper needs keyboard focus for scrolling in a target browser, give it an accessible name and `tabindex="0"` (and role/landmark only when actually warranted). Avoid introducing redundant tab stops.
- Virtualization is **not** part of the HOS-35 baseline. If later introduced, define row indices/count, recycled DOM focus stability and AT tests explicitly.

## 4. Sorting

- `Sort=None` means the column is **not sortable**: plain header, no Button. `Unsorted` means sortable but no active sort; active states are Ascending/Descending.
- Use a native `button type="button"` inside sortable `<th scope="col">`. The Button contains both the visible header label and the sort indicator as a **single activation target**, not a tiny icon-only button next to non-clickable text.
- Mouse/keyboard activation triggers one sorting action. Native Button keyboard contract: Tab/Shift+Tab focus; Enter or Space activates. No custom Arrow key interception.
- Render `aria-sort="ascending"` or `aria-sort="descending"` **only on the currently active `th`**. Remove it from the previous sorted Header. Do not put `aria-sort` on the Button.
- The accessible Button name must describe the column and operation/context (e.g., “مرتب‌سازی بر اساس نام کارجو”); the decorative sort icon must not add redundant words. Sort state is announced via `aria-sort`; concise result-count/sort feedback may be announced via a separate polite status region after asynchronous refresh.
- Baseline sort cycle when the same column is activated: Unsorted → Ascending → Descending → Ascending. Selecting a different sortable column starts at Ascending. Optional “clear sorting” belongs in explicit view controls if a product needs it, not an undocumented third toggle.
- Preserve sort state when updating the dataset; compare typed, stable values rather than localized display strings. Do not change rows visually without synchronizing `aria-sort`.

## 5. Checkbox selection

- Provide native `<input type="checkbox">` or the canonical JV Checkbox that renders semantically as one. Label each row checkbox with identifying context: “انتخاب درخواست [نام کارجو]”.
- Header Select All is labelled with the exact scope of selection. **Baseline scope for a paginated Table: currently rendered, eligible page rows.** All filtered/all-result selection needs an explicit product-owned policy and distinct UI.
- Compute `unchecked` for zero eligible rows selected, `checked` when all eligible rows are selected, and `mixed` otherwise. For a native checkbox, set the DOM `indeterminate` **property**, which is not a serialized HTML attribute. Disabled/unselectable rows are excluded from the denominator; Header checkbox is disabled when no eligible rows exist.
- Clicking a Checkbox **only** changes selection; it must not expand/open/navigate the row. A selected visual surface does not itself mean focus. Do not substitute `aria-selected` for the checkbox semantics on an otherwise ordinary Table.
- Persist selected IDs through sort and paginate only according to the chosen product scope. If user navigates to a new page, ensure the Header checkbox reflects only that scope; cross-page bulk selection must communicate both the count and target domain.
- Bulk actions belong in a separate Toolbar/Pattern, not the Header Cell and not a table variant. They must preserve focus and report their result.

## 6. Expandable details

- The disclosure is a native Button with a contextual accessible name (e.g., “نمایش جزئیات درخواست [نام]”), `aria-expanded` set from the row's expanded state, and optional `aria-controls` pointing at an element **that exists in the DOM**. Enter/Space toggles.
- The Figma `Row Item` is a **visual grouping**, not a literal single HTML `<tr>` containing another `<tr>`. In the HTML Table, render the data Row and its expanded detail as **two sibling `<tr>` elements** inside the same `<tbody>`, or an equivalent native semantic structure. Detail is a `<td [attr.colspan]="visibleColumnCount">` containing a labelled details wrapper.
- When collapsed, either keep detail markup hidden with correct native hiding semantics or remove it and omit an invalid `aria-controls` reference. Never leave controls in a visually hidden section tabbable.
- When collapsing details while focus is inside them, return focus to the owning disclosure Button before removing/hiding focused content. Expanding must not hijack focus.
- Expanded state is independent of Checkbox selection and Row Hover. Stable row IDs must keep state coherent through sorting and filtering.
- **Hierarchical tree rows are not the same feature**. They require a different treegrid/nested semantics decision; do not overload this detail-expansion pattern.

## 7. Actions, keyboard focus, and disabled states

- Every direct action is a native Button with `type="button"`, a distinct accessible name including row context, and a visually discoverable interaction state. Use canonical Icon Button and Tooltip/Popover where appropriate.
- Up to three direct action buttons share the 96px Figma column. Additional actions belong in a canonical Overflow Menu with its own keyboard contract. The Header actions spacer always matches this column.
- Keyboard focus ring follows JV focus tokens: visible for `:focus-visible`, not a blanket outline on every pointer click. Ensure ring is not clipped by Row/Cell/Scroll container. Maintain required contrast.
- Tab proceeds through selection, disclosure, cell actions, then subsequent table controls in DOM order. Repeated row actions need context to remain understandable out of context.
- Loading, updating, disabling or removing data must not strand keyboard focus on a disappearing element. On destructive actions choose a predictable successor or a concise status announcement.

## 8. Loading, empty, error, pagination and feedback

These are Data View compositions; **do not** add Size/State variants to the Table shell for them:

- **Loading:** keep enough table context to orient users; use `aria-busy` only while loading; announce meaningful completion concisely through a polite status region. Skeleton shapes must not become fake navigable rows.
- **Empty:** keep headings if useful; place concise empty-state content in a spanning cell or adjacent Data View content. Explain filter-specific emptiness and provide Clear Filters where appropriate.
- **Error:** show error + Retry Button with an accessible name; announce it without blocking keyboard use.
- **Pagination:** native buttons/links with current page and count semantics; maintain reasonable focus position on transitions, and communicate visible range. Pagination is not yet a mature standalone DS component, so confirm its own contract before claiming complete implementation.
- **Async sort/filter:** avoid duplicated live announcements on every data mutation. Convey one intelligible update when the result change would otherwise not be discoverable.

## 9. Minimal native markup (conceptual; not production Angular code)

```html
<div class="table-scroll" dir="rtl">
  <table>
    <caption>درخواست‌های فرصت شغلی</caption>
    <thead>
      <tr>
        <th scope="col"><input type="checkbox" aria-label="انتخاب همه درخواست‌های این صفحه"></th>
        <th scope="col" aria-sort="ascending">
          <button type="button">نام کارجو <span aria-hidden="true">↑</span></button>
        </th>
        <th scope="col">وضعیت</th>
        <th scope="col">اکشن‌ها</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><input type="checkbox" aria-label="انتخاب درخواست علی رضایی"></td>
        <td>علی رضایی</td><td>در انتظار بررسی</td>
        <td><button type="button" aria-label="مشاهده درخواست علی رضایی">...</button></td>
      </tr>
    </tbody>
  </table>
</div>
```

This example intentionally omits framework wiring and expansion. Treat it as a semantic shape, not a copy-paste finished implementation. Angular consumers should bind checkbox `indeterminate`, `aria-sort`, `colSpan`, aria labels and controlled state from real data, not from screenshot state.

## 10. Developer acceptance matrix

Each test is a pass/fail assertion; record browser, device, assistive technology and screenshot/recording evidence as appropriate.

| Test | Expected result |
| --- | --- |
| S01 — Table semantics | Screen reader identifies Table caption, columns and correct header relationships. No accidental `role=grid`. |
| S02 — RTL order | Programmatic column order matches visual RTL order; Header and data align under width changes. |
| L01 — Small/Medium/Large | Single-line rows render at 32/40/48px including divider, without clipped focus or content. |
| L02 — Two-line heights | Two-line text content yields 48/56/64px with Row controls vertically centered. |
| L03 — Long text | One-line truncate and max-two-line wrap truncate correctly; full meaningful detail remains available. |
| L04 — Narrow viewport | Horizontal scroll is reachable with keyboard, text still readable and headers associated. |
| L05 — Zoom 200%/400% | Table remains operable, no unrecoverable clipped controls; verify actual Reflow exception applicability. |
| K01 — Tab order | Native focus visits only operable controls, not inert cells or wrappers. |
| K02 — Sort | Both Enter and Space sort, active `th` updates `aria-sort`, only one active sorted column. |
| K03 — Focus ring | Visible on keyboard focus, not clipped, pointer styling does not replace keyboard focus. |
| C01 — Checkbox | Space toggles row selection; no accidental disclosure or navigation. |
| C02 — Select All | Zero / some / all → unchecked / indeterminate / checked, excluding disabled rows. |
| C03 — Page scope | Header name and selection count match the defined page/filter scope. |
| C04 — Sort with selection | Stable selected IDs remain attached to the correct rows after reorder. |
| E01 — Disclosure | Enter and Space toggle details; `aria-expanded` matches; detail is not tabbable while hidden. |
| E02 — Expanded markup | Detail is an adjacent native table row with computed `colspan`, not a nested row. |
| E03 — Focus on collapse | Collapsing focused detail returns focus to the correct disclosure. |
| A01 — Action names | Screen reader announces row-specific purpose, not indistinguishable repeated “Edit”. |
| A02 — Overflow Menu | >3 actions use canonical Menu with standard keyboard navigation; no fourth button clips. |
| D01 — Async states | Loading/error/empty are announced appropriately; focus persists on updates. |
| D02 — Pagination | Current page, range and selectable scope remain understandable. |
| T01 — High contrast | Sort, Checkbox, focus and selected status are distinguishable beyond hue. |
| T02 — AT interoperability | Run at least one desktop screen reader + supported browser and one representative mobile AT/browser combination. |

### Implementation gate

**Ready for sandbox implementation:** Yes — Figma and this draft contract are sufficient to start an Angular/Storybook sandbox.
**Verified in browser:** No.
**Ready for canonical production release:** No — requires all applicable acceptance tests, product-specific selection/pagination decisions, and Code/Design QA before merging documentation or closing HOS-35.

## References

- [W3C APG Table Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/table/)
- [W3C APG Sortable Table Example](https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/)
- [W3C APG Disclosure Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/)
- [W3C APG Grid and Table Properties](https://www.w3.org/WAI/ARIA/apg/practices/grid-and-table-properties/)
- [JV canonical Tables and Data Visualization accessibility](../../accessibility/tables-and-data-visualization.md)
