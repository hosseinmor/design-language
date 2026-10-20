---
id: design-system.accessibility.tables-and-data-visualization
collection: design-system
type: accessibility
title: Tables and Data Visualization
summary: Defines Data Table versus Interactive Grid decisions, table semantics, sorting/filtering, custom Grid contracts, virtualization, charts, and accessible data alternatives.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.keyboard-navigation
- design-system.accessibility.focus-management
- design-system.accessibility.screen-reader-semantics
- design-system.accessibility.color-and-contrast
- design-system.accessibility.testing
last_reviewed: '2026-09-02'
---

# Tables and Data Visualization

This document owns the cross-cutting distinction between **Data Table**, **Interactive Grid**, and **Data Visualization**.

The first decision is semantic/interaction intent, not density.

## Data Table vs Interactive Grid

```text
Data Table
→ tabular data/relationships
→ native table semantics
→ ordinary interactive controls inside cells remain ordinary Tab stops

Interactive Grid
→ application-like cell/row navigation model
→ composite keyboard/focus behavior
→ custom Grid contract required
```

**MUST NOT** use `role="grid"` merely because:
- the table is dense;
- rows are selectable;
- cells contain Buttons/Links;
- the team wants fewer Tab stops.

If ordinary table semantics plus normal controls satisfy the task, keep a Data Table.

## Data Table semantics

For tabular data, **MUST** preserve programmatically determinable row/column header relationships where needed.

Prefer native `<table>`, `<th>`, `<caption>` and appropriate header scope/association mechanisms before ARIA.

A visual grid created only with generic `div`s is not sufficient when users need actual tabular relationships.

## Caption/title/context

**SHOULD** provide enough programmatic context for users to understand what the table represents. A native caption can be useful when the table needs its own concise title; surrounding heading/text may also provide context depending on structure.

Do not duplicate the same title unnecessarily across caption/heading/accessible name.

## Sorting and filtering

Sort/filter controls **MUST** be keyboard operable and expose their control purpose/state.

When a column sort state is meaningful, expose it programmatically using the appropriate table mechanism (for example `aria-sort` on the relevant header) and keep visual/programmatic state synchronized.

Filtering/result changes may require concise status feedback through `dynamic-content-and-feedback.md` when users would otherwise miss the update.

## Row selection and actions

Row selection, current row, checkbox selection, and keyboard focus are separate concepts.

Use native/selectable-control semantics for selection when practical; do not turn a table into Grid solely because rows can be selected.

Repeated row action Buttons/Links must have meaningful accessible names in context.

## Interactive Grid contract

A custom Grid is a Level 3 reusable component/custom widget.

Before use as a mature contract, **MUST** define and test:
- actual Grid semantics and row/cell relationships;
- entry/exit with Tab/Shift+Tab;
- internal Arrow/Home/End/Page navigation as applicable;
- focus strategy (roving tabindex or `aria-activedescendant` where valid);
- edit/interaction mode for controls inside cells;
- selection vs focus behavior;
- disabled/unavailable cell/item behavior;
- RTL behavior where directional navigation changes;
- virtualization and active-item stability;
- accessible names/states for cell actions;
- representative browser/assistive-technology interoperability.

**SHOULD** use the established WAI-ARIA APG Grid pattern as the default behavioral reference unless a justified alternative is documented and tested.

APG remains guidance; applicable WCAG/WAI-ARIA/ARIA-in-HTML requirements are mandatory.

A specialized Tables document does **not** make an absent/scaffold Grid component contract mature.

## Virtualization

Virtualized tables/grids **MUST** preserve coherent semantic relationships and focus/active-item behavior as DOM content is recycled.

If row/column counts/indices are exposed programmatically, they must reflect the actual accessible model rather than arbitrary rendered-chunk positions.

Do not silently drop the focused/active item during recycling.

## Responsive overflow

Data tables may qualify for the WCAG Reflow exception when two-dimensional layout is necessary for usage/meaning.

That exception does not remove requirements for keyboard operability, focus visibility, semantic relationships, or readable content.

Prefer predictable horizontal scrolling, preserved headers/context, and controls that remain reachable. Do not convert data into an inaccessible card layout merely to avoid horizontal overflow.

## Charts and graphs

Essential chart information **MUST** have an accessible equivalent appropriate to the task: direct values, structured summary, data table, or another programmatically understandable representation.

Color **MUST NOT** be the only visual differentiator for essential series/status meaning. Apply applicable non-text contrast to essential graphical objects.

Hover-only values/interactions need keyboard/touch alternatives where required.

## Dashboard visualizations

Do not make every chart/card a landmark. Use meaningful page structure and provide concise titles/labels so users can navigate the dashboard without excessive semantic noise.

If data refreshes asynchronously, use status feedback only when the update is important and otherwise not discoverable.

## Ownership

| Specialized owner | Component/Pattern/Product owner |
|---|---|
| Table vs Grid decision rules | Exact component selection/use |
| Cross-cutting table semantics | Table component anatomy/API |
| Grid minimum contract categories | Actual Grid keyboard/focus/API contract |
| Chart accessibility principles | Product-specific metric interpretation |
| Data-equivalent requirement | Actual summary/table/copy |

## Testing

### Data Table
Verify native/table semantics, headers, caption/context, sort state, keyboard access to cell controls, repeated action names, responsive overflow, zoom/reflow, and screen-reader table navigation.

### Interactive Grid
Run the component contract plus `keyboard-navigation.md`, `focus-management.md`, `screen-reader-semantics.md`, and `testing.md`; include representative AT/browser interoperability and virtualization states.

### Visualization
Verify equivalent data/summary, non-color cues, essential graphical contrast, keyboard/touch access to interactive values, and async updates.

## AI contract

AI **MUST** decide Data Table vs true Interactive Grid before choosing semantics, must not add Grid to reduce Tab stops, must not treat this specialized doc as a substitute for a reusable Grid component contract, and must escalate an absent/draft/scaffold Grid to specialized keyboard/focus/semantics/testing guidance.

## References

- WCAG 2.2 — 1.3.1 Info and Relationships
- WCAG 2.2 — 1.4.1 Use of Color
- WCAG 2.2 — 1.4.10 Reflow
- WCAG 2.2 — 1.4.11 Non-text Contrast
- WAI-ARIA APG — Grid Pattern
