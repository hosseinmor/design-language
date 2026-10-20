---
id: design-system.integration.figma-component-presentation
collection: design-system
type: integration
title: Figma Component Presentation
summary: Defines a consistent, AI-readable presentation layout for JobVision Design System component pages without duplicating canonical component or runtime contracts.
knowledge_state: draft
document_maturity: draft
owner: Design System team
related:
  - design-system.structure
  - design-system.governance.documentation-maintenance
  - design-system.reference.source-of-truth
  - design-system.reference.figma
---

# Figma Component Presentation

> **Status: draft for Design System owner review.** This is the single detailed documentation-page presentation proposal. The older 2528px / three-section draft preserved in earlier `figma.md` revisions must not be treated as a parallel rule. This is a rule for **presenting** existing components in Figma, not a redesign of any component API or a release/production approval.

## Purpose and authority

The Figma component page should let a designer locate and inspect the canonical sources, understand the main authoring choices, and test typical/edge compositions without searching an unstructured canvas.

- **Figma** owns editable sources, variant organization, presentation, and real instances.
- **Component documentation** owns intended usage, semantic distinctions, important non-obvious behavior, and component-specific gaps.
- **Code/Storybook** owns implementation behavior, runtime coverage, and executed tests.
- **Accessibility corpus** owns cross-component accessibility standards.

Do not replicate full API/state tables, token inventories, keyboard specifications, or runtime tests in this presentation. Link to their owning sources when needed. Refer to `overview/design-language.md` and the relevant component contract before proposing substantive changes.

## Standard page structure

Use **one visually dominant documentation frame** per component. **The original canonical Main Component / Component Set must live inside the presentation frame**. Older documentation frames may remain temporarily as archives, but must no longer contain the active master sources. Reparent existing masters; preserve node IDs, component keys, published identities, variant children, slots, variables, and connected instances.

| Order | Section name | Required | Content |
| --- | --- | --- | --- |
| 00 | **Header** | Yes | Component name, one-line purpose, optional category/task/source link |
| 01 | **Component set** | Yes | **Original public Main Component / Component Set (not an instance)**, all canonical variants, and concise authoring/property summary |
| 02 | **Playground** | Yes | Real component instances in representative usages and meaningful edge cases |
| 03 | **Anatomy & composition** | For composite components | **Actual internal Component Sets and standalone Main Components**, slots, relationships, and composition rules |
| 04 | **Usage & handoff** | Only when needed | Essential do/don't, known boundary, source links, and implementation caveats |

**Keep section numbers fixed even when optional sections are absent** (for example: Radio has 00, 01, 02, 04). Do not fill the canvas with an empty optional section.

### Source vs presentation distinction

**Section 01 must contain the original canonical public Master / Component Set itself, not an instance-based visual index.** The Component Set retains its real children/variant properties; no separate matrix is needed to imitate it.

**Section 03 must contain the original nested Component Sets and standalone Main Components** when the public component has reusable internal source families. Large masters are placed at their natural dimensions in full-width source rows or an explicit wide exception. Do not present only instances or text-only references as substitutes for these sources.

**Section 02 is the instance-only zone:** its examples must remain connected to those original sources. Never duplicate, detach, recreate, or swap the canonical master simply to achieve a symmetric layout. Preserve its source identity during reparenting.

The canonical public component must be searchable in Figma and remain attached to its expected file/library identity.

## Layout rules (v1)

| Rule | Default |
| --- | --- |
| Documentation frame | **1600 px** wide, vertical Auto Layout, white `surface/default` |
| Outer page padding | **64 px** on all sides (content width **1472 px**) |
| Space between main sections | **48 px** |
| Section heading | `Heading/2XL` with brief `Body/SM` summary |
| Page title | `Heading/3XL` |
| Card heading | `Heading/MD` or `Heading/LG` according to hierarchy |
| Body and captions | Shared `Body/SM`, `Body/Compact/XS`, and `Label/XS` styles |
| Surface | Neutral / `surface/muted`; `surface/neutral-muted` for the spec panel |
| Color | Semantic `fg/primary`, `fg/secondary`, and small `fg/accent` accents |
| Container shape | Use system `Large` radius for independent documentation cards (12 px) |
| Borders | Avoid repeated section borders; use only when needed for separation |
| Layout behavior | Auto Layout, fixed intentional widths, Hug content height, no clipping of content |

The **1600 px frame is a documentation canvas convention**, not a product breakpoint. For components with genuinely wider masters, use a full-width source row or a clearly labeled wide exception; do not scale, crop, detach, or recreate the canonical source.

### Alignment and responsive presentation

- Use one left-aligned frame grid for documentation labels; product content inside samples keeps its own RTL behavior.
- Do not mirror the whole English documentation scaffold merely because sample content is Persian.
- For examples, use meaningful widths. A subcomponent that is 976 px wide must not be put into a 477 px anatomy card.
- Use full-width source containers for wide internal Masters. Text-only references are supplementary and cannot replace the actual source inside Section 03.
- Size/density axes are about the **product component**, not arbitrary documentation card sizes.

## Required section details

### 00 · Header

Show the component's official Figma name, a concise purpose and (when known) task ID. Optional: a category and a link to the owner document. Avoid dumping the full developer contract into the header.

### 01 · Component set

- Place the **existing public canonical Component Set** directly in this section; display its real variants and axes. Do not use an instance-generated matrix as the sole source display.
- Keep the full original variant set intact even when large; use full-width rows or a documented width exception rather than hiding canonical variants.
- Identify secondary component families separately (e.g., Radio Group under Radio).
- Put the *Axes & properties* panel beside the matrix when width permits; avoid a long standalone text section.
- Show true `Variant` axes separately from Text, Boolean, Instance Swap, and Slot authoring properties.
- Do not generate a variant explosion for layout direction, full content permutations, or purely authoring choices unless the canonical component actually has those axes.

### 02 · Playground

- All UI examples must be **live Figma instances** of existing components.
- Prefer three useful categories: **typical usage**, **alternate composition**, **meaningful edge case**. Change the count when the component needs fewer or more.
- Exercise RTL/Persian content, long labels and wrapping, focus/disabled/selected states where relevant, and component-specific constraints.
- Never duplicate the complete variant matrix in the Playground.
- Name scenarios by **behavior or use case**, not `Example 1`, `Example 2`.
- The examples explain intended use; they do not certify runtime behavior.

### 03 · Anatomy & composition (conditional)

Use for composite elements, such as Data Table, Select, Timeline, or complex overlays. The public parent Master stays in Section 01; put its **actual internal Master/Component Sets** in Section 03, with short descriptions of responsibilities and slots.

Use original node identities and preserve all variants. Display a wide Row or Header Row Master in a full-width source card at its original size. Small internal Masters may share a row when both fit without scaling or clipping.

### 04 · Usage & handoff (conditional)

Use concise cards or short notes for decisions designers and developers might otherwise miss. Link to canonical component and accessibility/runtime documents. Mark unverified implementation behavior explicitly. Avoid copying extensive interaction contracts.

## Reusable documentation utilities

The Figma file has a separate page, **`__DS Docs Utilities · internal`**, containing:

- `_Docs / Page Header` — Text properties for eyebrow, title and description.
- `_Docs / Section Heading` — Text properties for title and description.
- `_Docs / Spec Panel` — Title property and content Slot.
- `_Docs / Example Card` — Title/description properties and content Slot.
- `_Docs / Handoff Note` — Title and description properties.

These are **documentation-only utilities**, not product UI primitives. Keep the underscore naming convention, exclude them from product-library publication, and maintain them in the internal page. A Slot should accept source-linked content, rather than detached screenshot facsimiles.

A change to one of these utilities may affect every presentation instance; inspect at least a simple and a composite component after changing it.

## Canonical reference pilots

- [Radio Button / Documentation (canonical sources)](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23835-186): six Radio states, two Radio Group directions, a simple Playground.
- [Data Table / Documentation (canonical sources)](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23835-127556): composable public table presets, wide playground, conditional Anatomy.
- [Internal utilities](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23840-10): shared presentation-only components.

These are **presentation pilots**, not component maturity or runtime approval signals. Both pilots now contain the **original canonical sources moved in place with unchanged node IDs and variant counts**; master APIs were not redesigned.

## Migration / cleanup protocol

1. Identify published masters, nested source components, existing component-set IDs, slots, and connected instances.
2. Identify the *single* current canonical source per public component family.
3. Compose the presentation frame **without creating duplicate masters**.
4. **Reparent the original public Main Component / Component Set into Section 01**. Verify its node ID, published key, variants, nested dependencies and instance links are unchanged.
5. **Reparent the original internal Component Sets and standalone Masters into Section 03** for composite components; preserve natural sizes and stable identities.
6. Use existing source-linked instances in Section 02 Playground. Reuse `_Docs` utilities for headings and notes; a reusable documentation card is never itself a product master.
7. Mark superseded documentation frames as archive and position them out of the main presentation. Check any externally documented Figma frame links and update references after moving sources.
8. Perform visual and structural QA (below) before accepting the new presentation.
9. Update component documentation when live source links move, but do not change component behavior/runtime contracts for a presentation-only migration.

### QA checklist

- [ ] One recognizable 1600 px documentation frame; no unexplained loose content around it
- [ ] Header + Section 01 + Section 02 present; optional sections conditional, numbering stable
- [ ] Titles and section descriptions readable at practical Figma zoom
- [ ] Auto Layout governs all documentation groups; text uses shared styles and hugs height
- [ ] No overlap, clipped text, or narrow-card overflow
- [ ] Semantic token bindings used for documentation surfaces/foreground where available
- [ ] **Original canonical public Main Component / Component Set is physically inside Section 01**, not merely linked or imitated by instances
- [ ] **All reusable internal Main Components and Component Sets are inside Section 03**, when applicable
- [ ] Master node IDs, component keys, variant counts, slots, token bindings, and connected consumers remain unchanged after reparenting
- [ ] Playground items are genuine source-linked instances and do not duplicate public masters
- [ ] Primary variant axes and non-variant properties are distinguished
- [ ] Playground covers representative product use, RTL and relevant edge behavior
- [ ] Documentation-only `_Docs` components are not published as product components
- [ ] Correct authoritative links; no unsupported runtime or accessibility claims
- [ ] Simple-component and composite-component sample screenshots pass after scaffold edits

## Guidance for AI authoring

When asked to standardize a Figma component page:

1. Read this rule **only when editing the Figma presentation**, then read the target component contract and inspect the actual current Figma nodes.
2. Treat existing canonical Masters, published IDs, variable bindings and nested component contracts as protected; ask for owner review before changing them.
3. Build the documentation layout using `_Docs` utilities; then **move the existing canonical Master nodes** into Sections 01 and 03. Never create substitute instances in their place.
4. Never infer undocumented axis/state options from a generic template. Display only the target's real options.
5. Add conditional Anatomy/Handoff sections only when necessary.
6. Return the changed presentation link, affected node IDs, exceptions, and a short audit result. A passing Figma screenshot is not evidence of working runtime interaction.

## Open review points

- Confirm whether all component pages adopt 1600 px, or whether an explicitly defined **wide exception** is needed for unusual editors/data views.
- Confirm publication-exclusion enforcement for internal `_Docs` sources in library settings (the naming convention alone must not be treated as technical enforcement).
- Plan cleanup of already published legacy documentation frames carefully. Keep master identities stable and mark superseded documentation as archive; never silently substitute published component sources.
