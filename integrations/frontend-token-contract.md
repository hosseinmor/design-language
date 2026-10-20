---
id: design-system.token.frontend-contract
collection: design-system
type: token
title: Frontend Token and Theme Package Contract
summary: Design-side contract for installable Theme packages, stable token APIs, consumption audiences, serialization boundaries, and future Foundation extension.
knowledge_state: unverified
document_maturity: draft
related:
  - design-system.token.architecture
  - design-system.product-variation.theme-context
last_reviewed: '2026-09-14'
---

# Frontend Token and Theme Package Contract

## Status

This document reflects the revised architecture agreed with Frontend on 2026-09-14. The logical Theme-package, Semantic API, and Component Token boundaries are defined. Exact package names, build tooling, serialization, lint implementation, and release compatibility remain implementation-owned/open.

## Purpose

Define how a Product consumes a stable Design System token API while concrete visual values are supplied by an installable Theme package.

## Core architecture

```text
Shared Design System contract
→ stable token names + meaning

Product/application
→ selects and imports a compatible Theme package

Theme package
→ provides concrete values
→ includes Light/Dark Appearance mappings

Product UI / DS Components
→ consume the stable shared contract
```

Product identity and Theme identity are related but not the same architectural concept.

Current intended mapping:

```text
JobVision application → JobVision Theme package
Cando application     → Cando Theme package
```

A future Product may reuse an existing compatible Theme or intentionally select another Theme without changing the shared Semantic vocabulary.

### Figma authoring selectors

Figma uses two independent authoring selectors without changing the runtime contract:

```text
02 Product          → JobVision | Cando
03 Semantic Values  → Light | Dark
                      ├── jobvision/*
                      └── cando/*
03 Semantic         → stable public Value contract
```

`02 Product` routes the public Semantic contract to the selected Product branch and also switches Product-aware typography. `03 Semantic Values` independently resolves Light/Dark Appearance.

These router/value collections are Figma authoring implementation. Runtime Theme packages may flatten this graph into their own Primitive + Semantic Light/Dark artifacts.

## Theme package contract

Each Theme is an independently installable package.

### v1 required scope

Theme packages provide Color:

```text
Theme package
├── Theme-local Color Primitives
└── shared Semantic Color API values
    ├── Light
    └── Dark
```

Both Light and Dark live in the same Theme package. Do not model Appearance as separate packages such as `theme-jobvision-light` and `theme-jobvision-dark`.

### Future Foundation extension

The package model must be capable of providing additional Foundation values later when a real Theme-level difference exists:

```text
Theme
├── color        required in v1
├── spacing      future if needed
├── radius       future if needed
├── typography   future if needed
├── elevation    future if needed
└── motion       future if needed
```

Do not duplicate an invariant Foundation into every Theme package merely because the architecture supports it. Shared Foundations remain outside Theme until Theme-level variation is justified.

## Shared contract versus Theme-owned values

The Design System owns:

- token names;
- token meaning and usage;
- Product-facing API boundaries;
- component contracts;
- accessibility and compatibility requirements.

The Theme owns:

- Primitive Color inventory and values;
- Light/Dark Semantic Color values;
- future Theme-specific Foundation values;
- approved internal Theme implementation values required by the final contract.

Therefore:

```text
surface/brand
fg/primary
line/default
...
```

remain stable across Themes even when their concrete values differ.

## Primitive policy

Primitive Color is Theme-local internal implementation detail.

Product code and ordinary component code must not depend on Theme-local Primitive names or values.

Conceptually:

```text
JobVision Theme local blue → surface/brand
Cando Theme local yellow   → surface/brand
```

A shared global `Brand` alias layer is not required.

## Appearance

Appearance is runtime state inside the installed Theme:

```text
light | dark
```

If a preference supports `system`, it resolves to Light or Dark before final token resolution.

Appearance names do not enter public Semantic token names.

## Consumption audiences

Generated/runtime presence and Product-facing API visibility are separate concerns.

### Product-facing Design System API

Product code consumes contracts explicitly exposed by their owning Foundation.

For Color, this is the shared Semantic API such as `surface/*`, `fg/*`, `line/*`, `link/*`, and approved utility roles.

For non-Color Foundations, current shared contracts such as Spacing, Radius, Typography, Elevation, and Responsive Layout remain Product-facing according to their own Foundation rules.

### Component implementation API

Ordinary component-owned tokens are private implementation contracts and should normally alias shared Semantic roles.

Example:

```text
button/primary/surface
→ surface/accent-emphasis
```

The Theme package should not need to know about Button anatomy to provide this value.

Component-owned tokens do not generate general Product utilities by default.

### Theme-internal dependencies

Theme-local Primitives are internal. They may exist in generated output for resolution but are not Product-facing API.

Any future Theme-internal slot must have an explicit DS contract and must not become a general Product escape hatch.

## Categorical Tag Component Tokens

Tag owns a private categorical Component Color-token contract whose values are shared across Products.

```text
Tag / Design System
→ owns tag/{color}/* names + meaning + Light/Dark values

Tag component implementation
→ consumes tag/*

Product code
→ must not consume tag/*
```

Tag Component Tokens are **not Theme package values**. Product/Theme identity does not affect them in the current contract; only Light/Dark Appearance does.

Product-facing tooling must not expose `tag/*` as general DS API:

- no public Tailwind utilities;
- no general Product token registry/autocomplete;
- lint/CI should reject direct use in ordinary Product code where practical;
- only the Tag implementation (and DS-owned tooling/build code that implements it) consumes the contract directly.

If Tag tokens are emitted as global CSS variables, their physical visibility does not make them public API.

Do not introduce a shared `categorical/*` contract until categorization becomes a demonstrated cross-component need.

## Runtime serialization and namespace

Canonical Design System token names do not include a product or library prefix.

Examples:

```text
surface/default
fg/primary
line/accent
focus/default
```

If runtime output uses CSS custom properties, the serializer may transform those names into a CSS-safe form such as:

```text
surface/default → --surface-default
fg/primary      → --fg-primary
line/accent     → --line-accent
```

No library namespace prefix is required in v1. Frontend may add one later if collision or isolation needs justify it, without changing the canonical token contract.

Theme, Product, and Appearance identity do not enter canonical Semantic token names.

Theme-local Primitive variables, if serialized, remain internal even though CSS cannot make custom properties physically private. Exact Primitive serialization is Frontend-owned as long as Product code is not expected to consume it.

## Alias and generation rules

The canonical source must preserve intentional dependency/alias meaning. Generated runtime output may flatten internal Theme-local aliases when behavior remains equivalent.

Runtime optimization is acceptable only when:

- Product-facing token identity stays stable;
- Light/Dark values resolve correctly;
- Product code does not depend on internal alias structure;
- generation remains deterministic;
- the canonical Theme source remains traceable.

## Enforcement

Do not rely on CSS visibility to enforce internal boundaries.

Tooling should be able to distinguish at least:

```text
Product-facing DS contract
Component implementation contract
Theme-internal dependency
```

From that classification, tooling may generate registries, framework adapters, lint allowlists, and documentation surfaces.

## Tailwind boundary

Tailwind consumes the stable Product-facing Design System contract, not Theme-local Primitives or private Component Tokens.

Changing from JobVision Theme to another compatible Theme must not require changing ordinary semantic Tailwind utility names.

Exact Tailwind configuration remains HOS-8.

## Confirmed with Frontend

- each Theme is imported as a package by the project that needs it;
- Primitive Color values are Theme-owned;
- Semantic Color token names remain fixed while their values are Theme-owned;
- one Theme package contains both Light and Dark mappings;
- the architecture is ready to include Foundations such as Spacing/Radius later;
- v1 Theme scope is expected to be Color;
- Tag Component Tokens are Product-independent and vary only by Light/Dark Appearance;
- Tag values are not part of Theme packages;
- Product code does not treat `tag/*` as a public token API.

## Still open / implementation-owned

- exact package names and repository layout;
- whether shared contract metadata/types live in a separate physical package;
- exact Theme source format and build pipeline;
- exact CSS selector/attribute mechanism for Light/Dark;
- exact Primitive serialization;
- exact lint/CI implementation;
- release/version compatibility policy between DS components and Theme packages.
