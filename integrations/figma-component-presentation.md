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

> **Status: mixed evidence / document draft.** The 2528px three-section baseline below was recorded in a previously **reviewed** Figma reference. The separate 1600px/five-section model is a **proposed migration**, pending Design System owner approval. Neither document status nor sample pilots prove that the proposal has superseded the reviewed baseline or that all live Figma pages follow it. This guide concerns **presentation** only, not component API design or release approval.

## Purpose and authority

The Figma component page should let a designer locate and inspect the canonical sources, understand the main authoring choices, and test typical/edge compositions without searching an unstructured canvas.

- **Figma** owns editable sources, variant organization, presentation, and real instances.
- **Component documentation** owns intended usage, semantic distinctions, important non-obvious behavior, and component-specific gaps.
- **Code/Storybook** owns implementation behavior, runtime coverage, and executed tests.
- **Accessibility corpus** owns cross-component accessibility standards.

Do not replicate full API/state tables, token inventories, keyboard specifications, or runtime tests in this presentation. Link to their owning sources when needed. Refer to `overview/design-language.md` and the relevant component contract before proposing substantive changes.

## Observed live presentations — 2026-10-21, not a policy decision

A targeted read of the actual Figma document gives the following **current examples**, not a representative compliance score or approval of the proposed default:

| Live Figma documentation source | Frame width | Observed structure |
|---|---:|---|
| Button, node `22880:132625` | 2528px | Header, original Component Set, Playground (reviewed baseline layout) |
| Dialog, node `24058:9` | 1600px | 00 Header through 04 Usage & handoff |
| Chip, node `23900:128061` | 1600px | 00 Header through 04 Usage & handoff |
| File Uploader, node `24020:785` | 1600px | 00 Header through 04 Usage & handoff |
| Select, node `23864:904` | 3572px | 00 Header through 04 Usage & handoff; explicit wide-master layout |

These observations confirm that live component pages currently mix the reviewed 2528px baseline, 1600px proposed presentation and wide exceptions. **They do not authorize a global migration, promote this document out of Draft, or replace a previously approved authoring standard.** The Design System owner still needs to decide the default and the rules for wide exceptions.

The published Figma component inventory also includes helper sets such as `__Chip Remove Action` and `__Chip Chevron / Neutral`; a name prefix alone does **not** hide a source from library consumers. Confirm intended publication/exclusion status with the library owner before changing these helper identities. Do **not** unpublish or detach existing source components solely on the basis of this inventory.

## Reviewed baseline versus proposed presentation (decision pending)

The earlier `integrations/figma.md` had `document_maturity: reviewed` and explicitly recorded these **reviewed design-side authoring rules**:

- One canonical editable public Component Set, not a recreated instance matrix or screenshot.
- A **2528px-wide** default documentation frame, with a white `surface/default` background and the required `Header → 01 · Component set → 02 · Playground` sequence.
- A human-readable labelled variant matrix and an `Axes & properties` panel **directly beside** the Component Set.
- Editable source-linked Playground instances, with legacy material outside the canonical work area, while preserving source identities and existing consumers.

**Current proposal, not yet approved as a replacement:** a **1600px-wide** standard frame with the same mandatory core and optional `03 · Anatomy & composition` and `04 · Usage & handoff` sections. The proposal adds documentation utilities and specific layout defaults below; those newer decisions remain draft until owner review.

**Retrieval and authoring rule:** when a task requires an *approved* page-authoring standard, use the reviewed baseline above. When exploring or applying the proposed redesign, state clearly that 1600px and its related layout choices are draft, and request owner approval before treating them as globally normative. Preserve live source identities in either path. Do not present the old 2528px baseline as a rejected draft or infer the current construction of a Figma page without inspecting the file.

**Open decision:** accept the new proposal (including its default width and conditional sections), revise it, or retain the prior baseline; only the Design System owner can close this. Current-value/live-source reconciliation remains deferred.

## Proposed page structure (draft)

The structure below is the 1600px migration proposal until reviewed. Preserve the reviewed core safeguards above regardless of documentation layout. Use **one visually dominant documentation frame** per component. **The original canonical Main Component / Component Set must live inside the presentation frame**. Older documentation frames may remain temporarily as archives, but must no longer contain the active master sources. Reparent existing masters; preserve node IDs, component keys, published identities, variant children, slots, variables, and connected instances.

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

## Proposed layout rules (draft v1)

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

## Proposed section details and retained authoring safeguards

### 00 · Header

Show the component's official Figma name, a concise purpose and (when known) task ID. Optional: a category and a link to the owner document. Avoid dumping the full developer contract into the header.

### 01 · Component set

- Place the **existing public canonical Component Set** directly in this section; display its real variants and axes. Do not use an instance-generated matrix as the sole source display.
- Keep the full original variant set intact even when large; use full-width rows or a documented width exception rather than hiding canonical variants.
- Identify secondary component families separately (e.g., Radio Group under Radio).
- **Retained reviewed baseline:** Keep the `Axes & properties` panel directly beside the canonical Component Set. If the proposed 1600px frame cannot accommodate it at natural size, document an explicit wide-layout exception rather than separating the panel from the set or squeezing/altering the masters. Show every Variant axis and permitted value; also document public Text, Boolean, Instance Swap, and Slot properties and any related wrapper/group component.
- Show true `Variant` axes separately from Text, Boolean, Instance Swap, and Slot authoring properties. **Retained design guideline:** arrange one or two compact axes in columns, remaining major axes in rows; add human-readable row/column labels and spacing between meaningful row groups. For example, Accordion Item was documented with columns `Indicator position × Expanded` and rows `Size × State`. This is a matrix-design example, **not** a claim that those are the current live variant options.
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

## Retained cleanup and exploration safeguards

The previous reviewed Figma reference also included these **non-duplicative safeguards**; they remain in force regardless of the proposed canvas width:

- Keep canonical documentation at the page origin and clearly separated from archival/scratch material.
- Keep an `Archive — legacy & scratch` area **only** for material with genuine migration or reference value. Delete obsolete copies when safely preserved elsewhere and no outstanding migration dependency exists.
- If both legacy assets and current `Scratch / exploration` need deliberate preservation, keep them in distinct named groups; do not place either among canonical variant sources or Playground instances.
- **Never delete user-owned exploration solely to declutter a component page.** Follow the intended preservation/review workflow and protect outstanding work.
- Treat archived assets as noncanonical. Do not change identifiers, detach source components, or recreate masters as a shortcut to a cleaner page.

## Migration / cleanup protocol

1. Identify published masters, nested source components, existing component-set IDs, slots, and connected instances.
2. Identify the *single* current canonical source per public component family.
3. Compose the presentation frame **without creating duplicate masters**.
4. **Reparent the original public Main Component / Component Set into Section 01**. Verify its node ID, published key, variants, nested dependencies and instance links are unchanged.
5. **Reparent the original internal Component Sets and standalone Masters into Section 03** for composite components; preserve natural sizes and stable identities.
6. Use existing source-linked instances in Section 02 Playground. Reuse `_Docs` utilities for headings and notes; a reusable documentation card is never itself a product master.
7. Move superseded documentation to a separate archive **only when it retains migration/reference value**; otherwise remove obsolete duplicates after verifying they are safely preserved. Keep user-owned current exploration intact, away from the canonical presentation. Check externally documented Figma links after moving sources.
8. Perform visual and structural QA (below) before accepting the new presentation.
9. Update component documentation when live source links move, but do not change component behavior/runtime contracts for a presentation-only migration.

### QA checklist

- [ ] Approved page-width rule respected; 1600px is **draft** unless the owner approves the migration. No unexplained loose content around the canonical presentation.
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

1. Read this guide for the approved baseline **and the explicitly draft proposal**, then read the target component contract and inspect actual live Figma nodes; do not silently enforce the new width without owner review.
2. Treat existing canonical Masters, published IDs, variable bindings and nested component contracts as protected; ask for owner review before changing them.
3. Build the documentation layout using `_Docs` utilities; then **move the existing canonical Master nodes** into Sections 01 and 03. Never create substitute instances in their place.
4. Never infer undocumented axis/state options from a generic template. Display only the target's real options.
5. Add conditional Anatomy/Handoff sections only when necessary.
6. Return the changed presentation link, affected node IDs, exceptions, and a short audit result. A passing Figma screenshot is not evidence of working runtime interaction.

## Open review points

- Resolve whether the 1600px proposal supersedes the reviewed 2528px baseline and which wide exceptions are necessary for unusual editors/data views.
- Confirm publication-exclusion enforcement for internal `_Docs` sources in library settings (the naming convention alone must not be treated as technical enforcement).
- Plan cleanup of already published legacy documentation frames carefully. Keep master identities stable and mark superseded documentation as archive; never silently substitute published component sources.
