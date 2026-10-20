---
id: design-system.pattern.responsive-layout
document_type: design-system
collection: design-system
type: pattern
title: Responsive Layout Patterns
summary: Adaptive behavior guidance for navigation, tables, forms, overlays, master-detail layouts, filters, and toolbars.
knowledge_state: unverified
document_maturity: draft
related:
  - design-system.foundation.responsive-layout
  - design-system.foundation.responsive-layout-spec
---

# Responsive Layout Patterns

> Status: Draft — pattern behavior must be validated against existing product implementations.

This document describes common adaptations. It does not prescribe one responsive transformation for every use case. Product context, information priority, task continuity, and implementation constraints must be considered.

## Navigation

### Compact layouts

- Use a collapsed, drawer, sheet, or bottom-level navigation pattern where the product architecture supports it.
- Keep essential destinations and current location visible or easily recoverable.
- Do not hide critical actions behind hover.

### Expanded layouts

- Persistent side navigation may begin at `lg` when the remaining content width is sufficient.
- A compact rail may be used before a full sidebar when navigation density requires it.
- Do not show a persistent sidebar solely because the viewport crossed `lg`; validate the remaining workspace width.

## Tables and dense data

Responsive tables must be adapted according to task priority. Do not convert every table to cards by default.

Preferred strategies, from least to most structural change:

1. Preserve the table and reduce non-essential spacing.
2. Hide or move secondary columns behind disclosure.
3. Freeze important columns and allow controlled horizontal scrolling.
4. Split summary and detail information.
5. Convert rows to cards only when row comparison is not the primary task.

Requirements:

- Keep primary identifiers and primary actions available.
- Preserve sorting and filtering meaning when columns are hidden.
- Do not truncate critical values without a recovery mechanism.
- Horizontal scrolling must be visually discoverable and keyboard accessible.

## Forms

- Use one column by default in compact layouts.
- Introduce multiple columns only for fields with a clear relationship and adequate width.
- Keep dependent fields close together.
- Do not reorganize fields in a way that changes the task sequence without documenting the behavioral reason.
- Constrain long forms to approximately `720–800px` rather than stretching them across the page.
- Stacked actions are acceptable in compact layouts; expanded layouts may align actions horizontally when priority remains clear.

## Dialogs, sheets, and full-screen overlays

Choose the overlay form based on task complexity and available content width, not device labels.

- Short confirmation and simple input tasks may remain dialogs across ranges.
- Complex tasks may use full-screen presentation in compact layouts and a dialog or side sheet in expanded layouts.
- A side sheet is appropriate when the parent context must remain visible and the remaining workspace is sufficient.
- Do not transform a complex workflow into a narrow dialog solely at a breakpoint.

Suggested behavioral variants:

- `Dialog`
- `Side sheet`
- `Bottom sheet`
- `Full-screen`

Avoid variant names such as `Mobile modal` or `Desktop modal`.

## Master-detail and split view

- Use a single-pane flow in compact layouts unless simultaneous comparison is essential.
- At `lg`, introduce split view only when both panes remain usable.
- Preserve selection and scroll position when moving between single- and multi-pane presentations.
- Deep links must open the correct detail content regardless of layout mode.
- Back behavior must remain predictable when detail content replaces the list in compact layouts.

## Filters

### Compact layouts

- Prioritize active filters and result count.
- Move complex controls into a sheet or full-screen filter view when inline space is insufficient.
- Keep a clear reset mechanism and show applied-filter state outside the overlay.

### Expanded layouts

- Filters may appear inline, in a sidebar, or in a persistent toolbar.
- Avoid showing all filters persistently when this reduces the primary workspace excessively.

Reusable filter groups should adapt through container queries when used in multiple page regions.

## Toolbars and action groups

- Preserve the primary action before secondary actions.
- Allow wrapping only when the resulting reading and action order remain clear.
- Move low-priority actions into an overflow menu before hiding primary actions.
- Icon-only transformations require recognizable icons, accessible labels, and adequate target size.
- A toolbar embedded in a narrow panel should respond to its container, not the overall viewport.

## Cards and result items

- Use vertical composition as the compact default.
- Switch to horizontal composition only when the container provides enough width for the content and actions.
- Keep title, primary metadata, status, and primary action visible.
- Secondary metadata may move into disclosure or a detail view.
- Avoid creating separate device-named card components.

## Kanban and boards

- Prefer horizontal board scrolling when column comparison remains central.
- Provide a clear alternative view when dense boards become impractical in compact layouts.
- Do not compress cards or columns below their readable minimum width.
- Preserve column status, item count, and drag-and-drop alternatives for keyboard and touch users.

## Charts and data visualization

- Use container queries for charts placed in flexible dashboards.
- Reduce annotation density before reducing essential meaning.
- Move legends or details below the chart when horizontal space is limited.
- Provide a text or table equivalent for critical data.
- Do not rely on tooltip hover as the only way to access values.

## Content priority rule

When space becomes limited, adapt in this order:

1. Remove decorative or redundant information.
2. Reduce non-essential spacing within approved density limits.
3. Reflow content.
4. Move secondary information behind disclosure.
5. Change the interaction pattern.
6. Remove information only when its product priority is explicitly lower.

## Documentation requirement

A product-specific responsive decision should document:

- affected pattern or component;
- trigger mechanism: viewport, container, or content condition;
- behavior before and after the threshold;
- information that is hidden, moved, or disclosed;
- focus, keyboard, and back-navigation behavior;
- unresolved implementation or product decisions.
