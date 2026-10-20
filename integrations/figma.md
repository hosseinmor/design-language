---
id: design-system.reference.figma
collection: design-system
type: reference
title: Figma Reference
summary: Operational reference for the current JV Design System Figma file, its variable architecture, stable component identities, and live-source boundaries.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: '2026-10-19'
related:
  - design-system.reference.source-of-truth
  - design-system.reference.component-mapping
---

# Figma Reference

Figma is the live source for **current editable visual construction**: component anatomy, variants/properties, Variables, Styles, spacing/layout construction, and the current design asset itself.

It does not own semantic usage rules, Product business behavior, runtime API names, or generated package syntax.

## Current library source

Primary Design System file:

- File: `-DS--Job-Vision-NEXT`
- File key: `rROD8ctH9UfPGAMrRrOzHe`
- URL: https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT

Use the live file for exact visual facts instead of copying changing values into Markdown.

## Current variable architecture

Verified from the live file on 2026-09-16:

| Collection | Modes | Role |
|---|---|---|
| `01 Primitives` | `Value` | raw Color authoring palette; not Product-facing API |
| `02 Product` | `JobVision / Cando` | Figma Product selector; routes Product-aware typography and Semantic Color |
| `03 Semantic` | `Value` | stable public Semantic Color contract |
| `03 Semantic Values` | `Light / Dark` | Product-nested implementation values for the public Semantic contract |
| `04 Component Tokens` | `Light / Dark` | private component-owned values; currently categorical Tag |
| `Spacing` | `Mode 1` | shared spacing values |
| `Radius` | `Mode 1` | shared radius roles/values |
| `Typography breakpoint` | `LG / SM` | design-time Fluid Heading resolution |
| `Responsive layout` | `Value` | breakpoint/container/padding foundation values |

The Color routing model is:

```text
01 Primitives
      ↓
03 Semantic Values
  Light | Dark
  ├── jobvision/*
  └── cando/*
      ↑
02 Product
 JobVision | Cando
      ↓
03 Semantic
 stable public contract
```

`02 Product` and `03 Semantic Values` are authoring implementation layers. Runtime Theme packages do not need to reproduce this routing graph.

Only the stable Semantic contract should be treated as the normal Product-facing Color API. Collection visibility in Figma does not redefine that API boundary.

## Theme and Product representation

The current Figma model preserves independent selectors:

- **Product** → `02 Product: JobVision | Cando`
- **Appearance** → `03 Semantic Values: Light | Dark`

Switching Product changes the Product branch used by the public Semantic contract and the Product-aware font family. Switching Appearance resolves Light/Dark values independently.

`04 Component Tokens` is Product-independent in the current contract and varies only by Appearance.

## Component page authoring standard

Every canonical component page in the Design System Figma file should use the same documentation structure. The goal is to make the editable source understandable without requiring designers to inspect hidden layers or infer variant axes from the properties sidebar.

### Required canonical structure

Use this top-level order inside the canonical documentation frame:

```text
Header
01 · Component set
02 · Playground
```

Recommended deterministic node names:

```text
<Component> / Documentation
Header
01 · Component set
Variant matrix
Axes & properties
02 · Playground
Playground / <Component>
Archive — legacy & scratch
```

The default canonical documentation frame is **2528 px wide** with a white `surface/default` background. Use shared Spacing/Typography/Color foundations for documentation construction. A component may exceed this width only when a readable variant matrix genuinely cannot fit after re-layout.

### Header

Header contains:

- component name;
- one short sentence describing what the page contains and what is canonical.

Do not duplicate the full Knowledge guideline in Figma. Figma documents the editable construction and provides direct authoring context.

### Component set section

The canonical Component Set must be visually prominent and readable as a matrix.

Rules:

- Re-layout variants so the matrix communicates the axes rather than preserving creation order.
- Use **columns for one or two compact axes** and **rows for the remaining major axes**.
- Add human-readable column and row labels around the Component Set.
- Use larger spacing between major row groups when it improves scanning.
- Do not rely on variant names inside the properties sidebar as the only explanation of the matrix.
- Keep the actual editable Component Set in this section, not a detached screenshot or duplicate.
- Prefer a `surface/muted` documentation canvas around the set; this is documentation treatment, not a component visual token.

For example, the Accordion Item page uses:

```text
Columns → Indicator position × Expanded
Rows    → Size × State
```

### Axes & properties panel

Every component page must have an **`Axes & properties`** panel directly beside the Component Set.

Record:

- every Variant axis and its allowed values;
- public Text/Boolean/Instance-swap/Slot properties;
- native Figma Slot roles;
- related wrapper/group component when it is part of the same component family.

This panel is an authoring aid. Runtime prop names must still come from the registered Code source and must not be inferred from Figma labels.

### Playground

Every canonical component page must include a **Playground built from real component instances**.

The Playground should cover the component's meaningful authoring surface rather than repeating every visual variant. Include representative cases such as:

- default instance;
- long or multiline content;
- RTL/directional behavior where applicable;
- editable Text/Boolean/Instance properties;
- native Slot composition with real arbitrary content;
- grouped/composed usage for component families;
- disabled or other behaviorally important states when useful;
- width/content stress cases where layout is a material part of the contract.

Playground content must remain editable. Do not use screenshots as substitutes for real instances.

### Legacy and scratch content

Do not leave legacy variants, migration references, or exploration frames mixed with the canonical source.

Move preserved material into a clearly separated top-level area named:

`Archive — legacy & scratch`

Use that archive only when preserved legacy material still has migration/reference value. If no legacy material needs to remain, delete it rather than carrying obsolete assets forward and keep only a top-level `Scratch / exploration` area when current exploration still exists.

Use separate `Legacy assets` and `Scratch / exploration` groups only when both kinds of material are intentionally retained.

Archive rules:

- preserve legacy material only when migration/reference value still exists;
- delete obsolete legacy material when an authoritative prior version is already preserved elsewhere and no migration dependency remains;
- do not treat archived assets as canonical;
- do not delete user-owned exploration material merely to make the page cleaner;
- canonical documentation must start at the page origin and remain visually separate from the Archive.

### Completion rule for component pilots

A Figma component pilot is not visually complete until:

- the Component Set is arranged as a readable labeled matrix;
- `Axes & properties` is present beside it;
- the Playground covers the meaningful authoring API with real instances;
- legacy/scratch content is separated from canonical work;
- structural and visual QA have been run on the final documentation frame.

This page-authoring standard applies to new component pilots and should be used when cleaning older component pages.

## Stable component identity example: Button

Verified design identity:

- Component set: `Button / Default`
- Node ID: `1854:1776`
- Component key: `be5d0d9cd5fdd02f9d7afa1e371c2f2a23acb329`

Use the live Figma component for current variants, properties, anatomy, and visual construction. Do not copy its full property matrix into this reference because that information changes during component pilots.

These are **design identifiers**. Do not infer runtime component names, props, or shipped support until the Code mapping is registered.

## Token authoring compliance

Read [Figma Component Token Compliance](figma-token-compliance.md) before authoring or handing off a canonical component. Check semantic Color role versus actual collection binding; owned Spacing and Radius bindings; Typography Text Styles; documented exceptions; and whether a component source or borrowed instance owns each property. The [read-only audit recipe](../tooling/figma/figma-token-compliance-audit.js) runs on one loaded component page at a time. The 2026-10-19 audit register tracks current Figma remediation and remaining migration debt.

Deprecated radius variables remain live for existing consumers but are hidden from new selection. Do not remove a legacy variable or regenerate published variant identities to pass audit checks.

## Figma → code mapping

Mapping status is tracked in `component-mapping.md`.

Current rule:

- Figma component key / node ID identifies the design asset.
- Code repository/package/component and prop mapping must come from the real implementation source.
- Storybook story IDs/URLs must come from the real Storybook source.
- Do not invent code names from Figma page/component/property names.
- Code Connect may become the mapping mechanism, but no Code Connect contract is currently registered.

## AI retrieval rule

```text
semantic meaning / usage
→ Design System Knowledge

current visual value / anatomy / property / binding
→ live Figma file

runtime prop / default / behavior
→ registered Code source

runnable state / interaction / accessibility evidence
→ registered Storybook/test source
```

If the required live source is unavailable, report the integration gap rather than substituting a Markdown guess.

## Known gaps

- runtime Design System repository/package is not yet registered;
- Storybook is not yet registered;
- Figma ↔ code prop mapping is not yet verified;
- per-component published-library status should be inspected live when needed rather than inferred from this document.
