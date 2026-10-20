---
id: design-system.product-variation.theme-context
collection: design-system
type: product-variation
title: Theme Package Architecture
summary: Defines Theme as an installable visual-token implementation selected by an application, with stable shared Design System contracts and runtime Appearance resolution.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.token.product-overrides
  - design-system.token.architecture
  - design-system.reference.code
  - design-system.reference.theme-initialization
last_reviewed: '2026-09-14'
---

# Theme Package Architecture

Theme is an **installable implementation of Design System visual token values**. It is not Product identity itself and it does not own token meaning.

The architecture separates three concerns:

```text
Product / application
→ selects an installed Theme package

Theme package
→ provides token values for supported Foundations

Appearance
→ selects the runtime appearance variant inside that Theme
```

## Product is not Theme

Product and Theme are related but not identical.

```text
JobVision application → JobVision Theme package
Cando application     → Cando Theme package
```

This is the current mapping, not a permanent one-to-one architectural rule. A future Product may reuse an existing Theme, and a deployment may intentionally select another compatible Theme.

Product remains application/business identity. Theme is visual-system implementation.

## Shared contract versus Theme implementation

The shared Design System owns stable token names, meanings, component contracts, accessibility rules, and consumption policy.

Each Theme package owns the concrete values needed to implement those contracts.

```text
Shared DS contract
  surface/default
  surface/brand
  fg/primary
  line/default
  ...
        │
        ├── JobVision Theme → values
        └── Cando Theme     → values
```

Product code consumes the stable Design System contract. It must not depend on which Primitive value a Theme uses to implement that contract.

## Theme package scope

Theme packages are Foundation-agnostic by architecture but intentionally narrow by implementation.

### v1

Theme packages provide **Color only**:

```text
Theme package
├── theme-local Color Primitives
└── Semantic Color values
    ├── Light
    └── Dark
```

Both Light and Dark belong to the same Theme package. Do not create separate packages such as `jobvision-light` and `jobvision-dark`.

### Future-ready

A Theme may later provide values for other Foundations when a validated cross-theme difference exists:

```text
Theme
├── color        v1
├── spacing      future if needed
├── radius       future if needed
├── typography   future if needed
├── elevation    future if needed
└── motion       future if needed
```

Do not move a Foundation into Theme merely because the architecture permits it. Shared Foundations remain shared until a real Theme-level variation requires otherwise.

## Appearance

Appearance remains a runtime choice inside the installed Theme.

Resolved Appearance is only:

```text
light | dark
```

If the application supports:

```text
light | dark | system
```

`system` is a preference/source, not a third resolved Appearance.

Appearance may change at runtime without installing or switching Theme packages.

## Primitive ownership

Primitive values are **Theme-local implementation details** in the target runtime architecture.

The Design System may define required semantic behavior and palette quality constraints, but Product code must not depend on a global cross-Theme Primitive identity.

For example, two Themes may both contain a Blue ramp but they are not required to share identical Primitive values merely because their Semantic contracts use the same token names.

## Brand

Brand is semantic meaning, not a required runtime token layer.

In the target architecture, a Theme may resolve Brand semantics directly from its local Primitives:

```text
JobVision Theme
  surface/brand → local blue

Cando Theme
  surface/brand → local yellow
```

A separate global `Brand` alias layer is therefore not required by the runtime contract.

Figma no longer uses a live Brand Color layer. The former `02 Brand` collection is now `02 Product`; Product-aware typography remains there, while former Brand Color aliases are hidden legacy variables only. Semantic and Tag contracts no longer depend on those legacy aliases.

## Components

Default component behavior:

```text
Component
→ Semantic tokens
→ values supplied by installed Theme
```

Private Component tokens may alias Semantic tokens when they add useful component-owned meaning, but they do not become Theme responsibilities merely because they exist.

Categorical Tag is the approved Component Color-token exception. Tag owns the `tag/{color}/*` contract and those values are shared across Products; only Light/Dark Appearance affects them.

Tag Component Tokens are component-implementation API, not Product-facing API, and they are not supplied by Theme packages.

## Runtime ownership

```text
Application / deployment
→ selects and installs Theme package
→ owns Product identity

Application shell / Theme service
→ owns Appearance preference and runtime Light/Dark resolution

Theme package
→ provides Foundation values for the selected visual system

Design System components
→ consume shared Semantic / approved private component contracts
→ do not branch on Product identity for normal styling
```

## Current Figma model

The Figma authoring model separates Product and Appearance into independent selectors while preserving the existing public Semantic variable IDs and bindings:

```text
01 Primitives            → Value

02 Product               → JobVision | Cando
  ├── typography/font-family
  └── semantic/* router values

03 Semantic              → Value
  └── public surface/*, fg/*, line/*, link/*, focus/* contracts

03 Semantic Values       → Light | Dark
  ├── jobvision/*
  └── cando/*

04 Component Tokens      → Light | Dark
```

Rules:

- `01 Primitives` remains the raw authoring palette.
- `02 Product` is the Product selector in Figma. Switching its mode changes both Product-aware typography and the Product branch used by Semantic Color.
- `03 Semantic` remains the public stable token contract; it has no Product or Appearance names in its public token paths.
- `03 Semantic Values` is the Figma implementation matrix: Product is nested by variable group and Appearance is selected by `Light | Dark` modes.
- `04 Component Tokens` remains Product-independent and uses only `Light | Dark`.
- old Brand Color aliases remain hidden legacy only.

This routing is a Figma authoring mechanism; runtime Theme packages do not need to reproduce the router layers.

## Deferred implementation contracts

This document does not define:

- exact package names or import syntax;
- whether Theme artifacts are CSS, JSON, TypeScript, or generated combinations;
- exact CSS selector/attribute mechanism;
- exact Theme build/publish pipeline;
- SSR preference persistence and no-flash mechanism.

Those belong to the frontend token-package, Tailwind, component-token, and Theme-initialization contracts.
