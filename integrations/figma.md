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
  - design-system.integration.figma-component-presentation
  - design-system.reference.figma-token-compliance
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

## Component page presentation source

The detailed component-page presentation and migration rules live **only** in [Figma Component Presentation](figma-component-presentation.md). Its current documented layout uses a 1600px presentation frame, required Header / public Component Set / Playground, and conditional Anatomy and Handoff sections; see that document for the actual structure and open owner-review decisions.

This reference **does not maintain a second layout specification**. The older 2528px / three-section scaffold previously documented here is superseded as a documentation proposal and must not be used by AI as a competing design rule.

**Maturity boundary:** The detailed Presentation document remains a `draft` with known open review items. The link is the current place to retrieve its proposed and evidence-backed decisions, **not** automatic approval or proof that every Figma page follows it. Exact current frame construction still requires inspecting the live Figma source at the final reconciliation phase.

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
- Storybook deployment details have not yet been verified or linked to an owning runtime source;
- Figma ↔ code prop mapping is not yet verified;
- per-component published-library status should be inspected live when needed rather than inferred from this document.
