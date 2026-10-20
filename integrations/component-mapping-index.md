---
id: design-system.reference.component-mapping-index
collection: design-system
type: reference
title: Component Mapping Lookup Index
summary: Compact AI retrieval index for locating the exact Figma/design evidence section without loading the full mapping registry; does not certify runtime parity.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.reference.component-mapping
  - design-system.reference.figma
  - design-system.reference.code
  - design-system.reference.storybook
---

# Component Mapping Lookup Index

Use this document to select the relevant portion of [Design-to-Code Component Mapping](component-mapping.md) instead of fetching its entire large evidence register.

**Important:** A record's Figma master key, variant count, or design handoff is **not** evidence of a shipped implementation. The referenced registry currently contains extensive design-side evidence; do not label runtime APIs, package exports, Storybook stories or tests as verified without source-specific registration and supporting revision/build evidence.

## Retrieval method for AI

1. Determine the smallest component or pattern requested.
2. Match its **exact source heading** below.
3. Search that heading in `component-mapping.md` and read only that section up to the next `###` heading (or next top-level section). Do not load the entire register by default.
4. Inspect the record's explicitly stated source status. For a runtime question, query the [Code](code.md) or [Storybook](storybook.md) owner; unknown runtime mapping remains **unverified**.
5. For semantic component usage, prefer the owning document under `design-system/components/` or `design-system/patterns/`; mapping evidence is not a competing usage guideline.

The heading list is a retrieval index; it does not independently review or promote the maturity of any component.

## Available evidence sections

| Topic | Exact heading to find in mapping registry |
|---|---|
| Progress Circle and Loading pattern — HOS-46 final design contract | `### Progress Circle and Loading pattern — HOS-46 final design contract` |
| Skeleton — HOS-47 design handoff (Figma verified; runtime unregistered) | `### Skeleton — HOS-47 design handoff (Figma verified; runtime unregistered)` |
| Dialog — HOS-42 design handoff (Figma verified; runtime unregistered) | `### Dialog — HOS-42 design handoff (Figma verified; runtime unregistered)` |
| Confirmation Dialog — standalone Figma component (review draft) | `### Confirmation Dialog — standalone Figma component (review draft)` |
| Alert Dialog — standalone Figma component (review draft) | `### Alert Dialog — standalone Figma component (review draft)` |
| File Uploader — final Carbon design source (runtime unverified) | `### File Uploader — final Carbon design source (runtime unverified)` |
| Button | `### Button` |
| Icon Button | `### Icon Button` |
| Menu | `### Menu` |
| Menu Button | `### Menu Button` |
| Combo Button | `### Combo Button` |
| Tooltip | `### Tooltip` |
| Accordion | `### Accordion` |
| Accordion Item | `### Accordion Item` |
| Link | `### Link` |
| Breadcrumb | `### Breadcrumb` |
| Inline Notification | `### Inline Notification` |
| Toast | `### Toast` |
| Checkbox | `### Checkbox` |
| Radio | `### Radio` |
| Toggle | `### Toggle` |
| Content Switcher | `### Content Switcher` |
| Tabs | `### Tabs` |
| Chip | `### Chip` |
| Progress Bar (HOS-37) | `### Progress Bar (HOS-37)` |
| Progress Indicator (HOS-31) | `### Progress Indicator (HOS-31)` |
| Choice Group | `### Choice Group` |
| Timeline | `### Timeline` |
| Data Table (HOS-35) | `### Data Table (HOS-35)` |

## Maintenance

When a mapping section is renamed, added, moved or retired, update this index in the same PR. Preserve the originating Design Language document ID, Figma keys and known verification gaps. Do not fabricate a Code/Storybook mapping to fill an empty field.
