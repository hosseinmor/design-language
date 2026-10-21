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
3. Use the **inclusive source line range** below to read only the corresponding part of `component-mapping.md` (e.g. `start_line=55`, `end_line=76` in a ranged file reader). The exact heading is a fallback for clients without ranged reads. Do not load the entire register by default.
4. Inspect the record's explicitly stated source status. For a runtime question, query the [Code](code.md) or [Storybook](storybook.md) owner; unknown runtime mapping remains **unverified**.
5. For semantic component usage, prefer the owning document under `design-system/components/` or `design-system/patterns/`; mapping evidence is not a competing usage guideline.

The heading list is a retrieval index; it does not independently review or promote the maturity of any component.

## Available evidence sections

These inclusive line numbers are generated from the current `component-mapping.md` contents. Use the exact heading as a fallback when line-range reads are unavailable. The number of rows and boundaries are checked automatically in CI.

<!-- BEGIN GENERATED COMPONENT MAPPING SECTIONS -->
| Component / evidence section | Source lines (inclusive) | Exact heading |
|---|---:|---|
| Progress Circle and Loading pattern — HOS-46 final design contract | 55–76 | ### Progress Circle and Loading pattern — HOS-46 final design contract |
| Skeleton — HOS-47 design handoff (Figma verified; runtime unregistered) | 78–97 | ### Skeleton — HOS-47 design handoff (Figma verified; runtime unregistered) |
| Dialog — HOS-42 design handoff (Figma verified; runtime unregistered) | 99–122 | ### Dialog — HOS-42 design handoff (Figma verified; runtime unregistered) |
| Confirmation Dialog — standalone Figma component (review draft) | 124–134 | ### Confirmation Dialog — standalone Figma component (review draft) |
| Alert Dialog — standalone Figma component (review draft) | 136–146 | ### Alert Dialog — standalone Figma component (review draft) |
| File Uploader — final Carbon design source (runtime unverified) | 148–172 | ### File Uploader — final Carbon design source (runtime unverified) |
| Button | 174–198 | ### Button |
| Icon Button | 201–225 | ### Icon Button |
| Menu | 229–269 | ### Menu |
| Menu Button | 271–296 | ### Menu Button |
| Combo Button | 299–326 | ### Combo Button |
| Tooltip | 329–351 | ### Tooltip |
| Accordion | 354–372 | ### Accordion |
| Accordion Item | 374–398 | ### Accordion Item |
| Link | 400–429 | ### Link |
| Breadcrumb | 432–462 | ### Breadcrumb |
| Inline Notification | 465–486 | ### Inline Notification |
| Toast | 488–511 | ### Toast |
| Checkbox | 514–549 | ### Checkbox |
| Radio | 552–584 | ### Radio |
| Toggle | 587–613 | ### Toggle |
| Content Switcher | 616–652 | ### Content Switcher |
| Tabs | 655–695 | ### Tabs |
| Chip | 697–749 | ### Chip |
| Progress Bar (HOS-37) | 752–782 | ### Progress Bar (HOS-37) |
| Progress Indicator (HOS-31) | 784–816 | ### Progress Indicator (HOS-31) |
| Choice Group | 819–848 | ### Choice Group |
| Timeline | 850–879 | ### Timeline |
| Data Table (HOS-35) | 881–910 | ### Data Table (HOS-35) |
<!-- END GENERATED COMPONENT MAPPING SECTIONS -->

## Maintenance

Run `python tooling/generate_component_mapping_index.py generate` when the mapping registry changes. CI runs the matching `check` command, and rejects stale ranges, renamed/missing headings or duplicate section identities. Preserve the originating Design Language document ID, Figma keys and known verification gaps. Do not fabricate a Code/Storybook mapping to fill an empty field.
