---
id: design-system.foundation.spacing
collection: design-system
type: foundation
title: Spacing
summary: Defines the canonical shared spacing scale and how Product code consumes it without making Tailwind the source of truth.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: 2026-09-12
related:
  - design-system.reference.tailwind
---

# Spacing

## Purpose

Spacing provides one shared scale for recurring Product layout and component spacing. The Design System owns the values; implementation frameworks consume generated outputs from that source.

Product teams should use the shared scale for ordinary padding, margin, and gap decisions rather than inventing nearby raw values.

## Canonical scale

| Value | Shared key | Tailwind key |
|---:|---|---|
| 0px | `spacing-0` | `0` |
| 2px | `spacing-0.5` | `0.5` |
| 4px | `spacing-1` | `1` |
| 6px | `spacing-1.5` | `1.5` |
| 8px | `spacing-2` | `2` |
| 12px | `spacing-3` | `3` |
| 16px | `spacing-4` | `4` |
| 20px | `spacing-5` | `5` |
| 24px | `spacing-6` | `6` |
| 32px | `spacing-8` | `8` |
| 40px | `spacing-10` | `10` |
| 48px | `spacing-12` | `12` |
| 56px | `spacing-14` | `14` |
| 64px | `spacing-16` | `16` |
| 80px | `spacing-20` | `20` |
| 96px | `spacing-24` | `24` |
| 160px | `spacing-40` | `40` |

Figma variables are value-first for quick scanning (`0px`, `2px`, `4px`, …) and expose the shared key as WEB code syntax.

## Usage rules

- Use native Tailwind spacing utilities such as `p-*`, `m-*`, and `gap-*` when Product code uses Tailwind.
- Tailwind must consume a generated map from the canonical Design System spacing source; Tailwind defaults are not the source of truth.
- Do not create a second DS-specific spacing utility vocabulary when the native Tailwind namespace already expresses the property.
- Use the shared scale for recurring visual spacing decisions.
- Contextual layout measurements that are not useful shared tokens may remain local, including page-specific widths/heights, grid tracks, and `calc()` expressions.
- Do not promote component-internal geometry into the global scale merely because it appears in one component. Values such as 3px, 7px, 10px, 11px, 14px, or 15px can remain local when they describe component construction rather than shared spacing.
- A raw or arbitrary spacing value should not bypass an established shared spacing decision. Prefer the nearest approved scale value when the difference is not functionally meaningful.

## Source boundary

The semantic scale and usage rules are owned here. Figma owns the editable design variables. The generated runtime artifact and Tailwind preset/config are Code-owned implementation outputs.

The exact generated file/module format remains a Frontend decision; it must not require manually re-authoring the scale in Product configuration.
