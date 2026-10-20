---
id: design-system.accessibility.responsive-and-zoom
collection: design-system
type: accessibility
title: Responsive and Zoom
summary: Defines text resize, zoom, reflow, overflow, truncation, reading-order, RTL, and responsive accessibility requirements.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.focus-management
- design-system.accessibility.structure-and-navigation
last_reviewed: '2026-09-02'
---

# Responsive and Zoom

This document owns cross-cutting responsive, zoom, text-resize, reflow, overflow, truncation, and bidirectional-layout accessibility.

## Text resize — WCAG 1.4.4 AA

Except for captions and images of text, text **MUST** be resizable up to 200% without loss of content or functionality and without requiring assistive technology.

Avoid fixed-height containers that clip enlarged labels, helper text, errors, buttons, or table controls.

## Reflow — WCAG 1.4.10 AA

Content **MUST** reflow without loss of information/functionality and without two-dimensional scrolling at the WCAG reference dimensions, except content that genuinely requires two-dimensional layout for usage/meaning (for example some data tables, maps, diagrams, or editing surfaces).

An exception for a true data table does not justify horizontal scrolling for unrelated page content.

When horizontal overflow is necessary for a table/grid, keep controls, labels, row/column relationships, and focus behavior usable.

## Text spacing — WCAG 1.4.12 AA

Author styling **MUST NOT** cause loss of content/functionality when users apply the WCAG text-spacing values.

Do not depend on fixed line heights or clipped single-line containers for essential text.

## Orientation — WCAG 1.3.4 AA

Content **MUST NOT** restrict view/operation to one display orientation unless a specific orientation is essential.

## Reading and focus order

Responsive visual rearrangement **MUST NOT** create a contradictory programmatic reading or keyboard focus order.

**SHOULD** use DOM order that remains meaningful across breakpoints rather than using CSS `order` to create a different semantic sequence.

At high zoom/narrow widths, focused controls **MUST** remain operable and not be completely obscured by author-created sticky/fixed regions. See `focus-management.md`.

## Truncation

Truncation is allowed when it does not remove essential information required to understand or complete the task.

**MUST** provide a usable way to access essential truncated content where the visible abbreviation would otherwise be insufficient.

Do not use a hover-only Tooltip as the only path to essential information; keyboard/touch access must also work when such disclosure is used.

## Fixed/sticky regions

Sticky headers, action bars, filters, and mobile bottom actions are allowed.

**MUST** ensure they do not completely obscure keyboard focus. **SHOULD** reserve enough space so focus and important content remain fully visible when practical.

## Responsive component behavior

Components **MUST** preserve essential content and functionality when labels wrap, controls stack, or content grows.

**SHOULD** test:
- long Persian labels and errors;
- mixed Persian/English strings;
- narrow mobile width;
- high zoom;
- text enlargement;
- RTL.

Do not solve responsive pressure by removing labels, instructions, or essential actions.

## RTL and bidirectional content

RTL is a content/layout direction, not a signal to reverse every interaction rule.

**MUST** preserve meaningful reading order and correct direction for mixed Persian/English content.

Directional icons **SHOULD** mirror only when their meaning is spatial/directional. Brand/logotype or intrinsically directional graphics should not be mirrored automatically.

Keyboard Left/Right behavior belongs to the component interaction contract and may follow visual order, logical progression, numeric change, or native behavior.

## Data tables and grids

An ordinary data table may legitimately need horizontal scrolling. Keep table semantics intact and avoid transforming data into an inaccessible visual-only layout merely to eliminate scrolling.

A custom interactive Grid requires its own component contract plus keyboard/focus/semantics testing; responsive virtualization must not break the active/focused item relationship.

## Ownership

| Design System/component owns | Product/layout owns |
|---|---|
| Component wrapping/overflow contract | Page composition at breakpoints |
| Component RTL behavior | Product content direction |
| Component minimum geometry | Available container/layout space |
| Internal focus resilience | Sticky/fixed composition around it |

## Testing

Test the applicable feature at 200% text resize, browser zoom/reflow reference widths, increased text spacing, narrow viewport, long Persian/RTL content, keyboard focus through responsive/sticky states, and any necessary horizontal overflow.

Automated screenshot comparison alone is insufficient; verify actual content/functionality and focus/reading order.

## AI contract

AI **MUST** preserve essential information/functionality under resize/reflow, distinguish legitimate two-dimensional content from avoidable page overflow, preserve semantic/focus order, and test RTL rather than mechanically mirroring behavior.

## References

- WCAG 2.2 — 1.3.4 Orientation
- WCAG 2.2 — 1.4.4 Resize Text
- WCAG 2.2 — 1.4.10 Reflow
- WCAG 2.2 — 1.4.12 Text Spacing
- WCAG 2.2 — 2.4.11 Focus Not Obscured (Minimum)
