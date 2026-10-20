---
id: design-system.token.color-token-aliases
collection: design-system
type: token
title: Color Token Alias Mappings
summary: Validated current Figma Color mappings for the Theme package architecture.
knowledge_state: canonical
document_maturity: reviewed
related: []
last_reviewed: '2026-09-19'
---

# Color Token Alias Mappings

## Purpose

This document records the current validated Figma Color mappings after the Theme architecture migration. Figma owns the editable aliases and values; this file is the documented review snapshot.

If this document and Figma diverge, treat the mismatch as a maintenance gap and inspect Figma rather than guessing.

Figma variable names now match the canonical token contract directly. Semantic names use forms such as `surface/default`, `fg/primary`, `line/default`, `link/default`, and `focus/default`; Primitive names use the `palette/*` prefix.

## Current Figma resolution

The active Figma Color resolution is now:

```text
01 Primitives
→ 03 Semantic Values (jobvision/* + cando/*, Light | Dark)
→ 02 Product semantic/* router (JobVision | Cando)
→ 03 Semantic public contract
→ Product UI / Components

01 Primitives
→ 04 Component Tokens
→ owning DS component
```

`02 Product` is an active **Figma authoring router** for Product selection. This does not make Product a public Color-token dimension or require runtime packages to reproduce the Figma routing layers.

The runtime architecture remains:

```text
Theme-local Primitive → shared Semantic role → Product UI / Component
```

Component Tokens such as Tag are owned by the Design System/component implementation and are not Theme-provided when their values are shared across Products.

Current Figma collections:

```text
01 Primitives            → Value
02 Product               → JobVision | Cando
03 Semantic              → Value
03 Semantic Values       → Light | Dark
  ├── jobvision/*
  └── cando/*
04 Component Tokens      → Light | Dark
```

Product and Appearance are independent Figma mode axes. `02 Product` selects the Product branch; `03 Semantic Values` selects Light/Dark. `03 Semantic` remains the stable public Color API and keeps its existing variable IDs/bindings.

`01 Primitives` is the raw authoring palette. `04 Component Tokens` remains Product-independent and currently contains Tag Color tokens.

Most non-Brand Semantic values currently resolve identically in JobVision and Cando, so their tables show Light/Dark once and apply to both Themes. Tag Component Tokens are explicitly Product-independent. Transparent Semantic interaction colors and overlay intentionally store resolved RGBA directly.

## 02 Product

Active Product-aware authoring:

| Role | JobVision | Cando |
|---|---|---|
| `typography/font-family` | `Vazirmatn` | `IRANYekanX` |
| `semantic/{role}` | aliases `jobvision/{role}` | aliases `cando/{role}` |

The `semantic/*` variables are Figma-only router values with no property scopes. Product UI continues to bind to the public `03 Semantic` variables, not to these router variables.

Former Brand Color variables are retained under `_legacy/brand/*` only for migration continuity.

## 03 Semantic Values

`03 Semantic Values` contains two nested Product groups:

```text
jobvision/{semantic-role}
cando/{semantic-role}
```

and two modes:

```text
Light | Dark
```

These variables are implementation values used by the Product router.

## 03 Semantic

### Structural Surface

| Canonical role | Light | Dark |
|---|---|---|
| `surface/default` | `palette/bw/white` | `palette/neutral/900` |
| `surface/muted` | `palette/neutral/50` | `palette/neutral/800` |
| `surface/inset` | `palette/neutral/100` | `palette/neutral/950` |
| `surface/raised` | `palette/bw/white` | `palette/neutral/800` |
| `surface/inverse` | `palette/neutral/950` | `palette/bw/white` |

Dark uses a dimmed-dark hierarchy rather than numerical inversion.

### Neutral interactive Surface

| Role | Light | Dark |
|---|---|---|
| `surface/neutral-muted` | `neutral/200` | `neutral/700` |
| `surface/neutral-muted-hover` | `neutral/300` | `neutral/600` |
| `surface/neutral-muted-active` | `neutral/400` | `neutral/500` |
| `surface/neutral-emphasis` | `neutral/900` | `neutral/200` |
| `surface/neutral-emphasis-hover` | `neutral/800` | `neutral/300` |
| `surface/neutral-emphasis-active` | `neutral/700` | `neutral/400` |

All unqualified hue paths in tables refer to `palette/{hue}/{step}`.

### Transparent Surface

| Role | Light | Dark |
|---|---|---|
| `surface/transparent-hover` | `rgba(0,0,0,.04)` | `rgba(255,255,255,.08)` |
| `surface/transparent-active` | `rgba(0,0,0,.08)` | `rgba(255,255,255,.12)` |
| `surface/transparent-inverse-hover` | `rgba(255,255,255,.08)` | `rgba(0,0,0,.04)` |
| `surface/transparent-inverse-active` | `rgba(255,255,255,.12)` | `rgba(0,0,0,.08)` |

These are direct Semantic COLOR values, not aliases to a published alpha Primitive family.

### Selected Surface

| Role | Light | Dark |
|---|---|---|
| `surface/selected` | `neutral/200` | `neutral/800` |
| `surface/selected-hover` | `neutral/300` | `neutral/700` |

### Brand — Theme-specific

| Role | JobVision Light | JobVision Dark | Cando Light | Cando Dark |
|---|---|---|---|---|
| `surface/brand` | `blue/700` | `blue/700` | `yellow/500` | `yellow/500` |
| `surface/brand-hover` | `blue/800` | `blue/800` | `yellow/600` | `yellow/600` |
| `surface/brand-active` | `blue/900` | `blue/900` | `yellow/700` | `yellow/700` |
| `fg/on-brand` | `bw/white` | `bw/white` | `neutral/900` | `neutral/900` |

These roles alias the Theme-appropriate Primitives directly; no active Brand Color layer sits between Primitive and Semantic.

### Accent

| Role | Light | Dark |
|---|---|---|
| `surface/accent-muted` | `blue/50` | `blue/950` |
| `surface/accent-muted-hover` | `blue/100` | `blue/900` |
| `surface/accent-muted-active` | `blue/200` | `blue/800` |
| `surface/accent-emphasis` | `blue/600` | `blue/500` |
| `surface/accent-emphasis-hover` | `blue/700` | `blue/400` |
| `surface/accent-emphasis-active` | `blue/800` | `blue/300` |
| `fg/accent` | `blue/700` | `blue/400` |
| `line/accent` | `blue/600` | `blue/500` |
| `fg/on-color` | `bw/white` | `neutral/950` |

### Magic

| Role | Light | Dark |
|---|---|---|
| `surface/magic-muted` | `purple/100` | `purple/950` |
| `surface/magic-emphasis` | `purple/600` | `purple/500` |
| `surface/magic-emphasis-hover` | `purple/700` | `purple/400` |
| `surface/magic-emphasis-active` | `purple/800` | `purple/300` |
| `fg/magic` | `purple/700` | `purple/400` |
| `line/magic` | `purple/600` | `purple/500` |

### Danger

| Role | Light | Dark |
|---|---|---|
| `surface/danger-muted` | `red/100` | `red/950` |
| `surface/danger-emphasis` | `red/600` | `red/500` |
| `surface/danger-emphasis-hover` | `red/700` | `red/400` |
| `surface/danger-emphasis-active` | `red/800` | `red/300` |
| `fg/danger` | `red/700` | `red/400` |
| `line/danger` | `red/600` | `red/500` |

### Support

| Severity | Muted Surface Light | Muted Surface Dark | FG Light | FG Dark | Inverse FG Light | Inverse FG Dark | Line Light | Line Dark |
|---|---|---|---|---|---|---|---|---|
| Info | `blue/100` | `blue/950` | `blue/700` | `blue/400` | `blue/500` | `blue/700` | `blue/500` | `blue/600` |
| Success | `green/100` | `green/950` | `green/700` | `green/500` | `green/600` | `green/700` | `green/600` | `green/600` |
| Warning | `yellow/100` | `yellow/950` | `yellow/800` | `yellow/600` | `yellow/700` | `yellow/800` | `yellow/700` | `yellow/700` |
| Error | `red/100` | `red/950` | `red/700` | `red/400` | `red/500` | `red/700` | `red/500` | `red/600` |

### Neutral Foreground

| Role | Light | Dark |
|---|---|---|
| `fg/primary` | `neutral/950` | `neutral/200` |
| `fg/secondary` | `neutral/700` | `neutral/400` |
| `fg/tertiary` | `neutral/600` | `neutral/500` |
| `fg/placeholder` | `neutral/600` | `neutral/500` |
| `fg/disabled` | `neutral/500` | `neutral/500` |
| `fg/on-inverse` | `bw/white` | `neutral/950` |

The old disabled-foreground variable remains hidden for migration safety and is not canonical.

### Neutral Line

| Role | Light | Dark |
|---|---|---|
| `line/muted` | `neutral/200` | `neutral/800` |
| `line/default` | `neutral/300` | `neutral/700` |
| `line/emphasis` | `neutral/400` | `neutral/600` |
| `line/disabled` | `neutral/200` | `neutral/800` |
| `line/inverse` | `neutral/600` | `neutral/500` |

### Disabled Surface

| Role | Light | Dark |
|---|---|---|
| `surface/disabled` | `neutral/100` | `neutral/800` |

### Link

| Role | Light | Dark |
|---|---|---|
| `link/default` | `blue/700` | `blue/400` |
| `link/hover` | `blue/800` | `blue/300` |
| `link/subtle` | `neutral/700` | `neutral/400` |
| `link/subtle-hover` | `neutral/900` | `neutral/200` |
| `link/inverse` | `blue/400` | `blue/700` |
| `link/inverse-hover` | `blue/300` | `blue/800` |

### Utility

Canonical semantic meaning and current Figma variable names are:

| Meaning | Figma variable | Light | Dark |
|---|---|---|---|
| Focus default | `focus/default` | `blue/600` | `blue/500` |
| Focus inverse | `focus/inverse` | `bw/white` | `neutral/950` |
| Overlay | `utility/overlay` | `rgba(0,0,0,.50)` | `rgba(0,0,0,.50)` |
| Skeleton background | `utility/skeleton-background` | `neutral/100` | `neutral/800` |
| Skeleton base | `utility/skeleton-base` | `neutral/300` | `neutral/700` |
| Skeleton element | `utility/skeleton-element` | `neutral/300` | `neutral/700` |
| Skeleton shimmer | `utility/skeleton-shimmer` | `neutral/100` | `neutral/600` |

## 04 Component Tokens — Tag

Canonical contract:

```text
tag/{color}/surface
tag/{color}/surface-hover
tag/{color}/fg
tag/{color}/line
```

Current canonical colors:

```text
neutral | blue | teal | green | yellow | orange | red | magenta | purple
```

Cyan and Warm Gray are hidden legacy variants only.

### Tag mappings

| Color | Surface Light | Surface Dark | Hover Light | Hover Dark | FG Light | FG Dark | Line Light | Line Dark |
|---|---|---|---|---|---|---|---|---|
| Neutral | `neutral/200` | `neutral/900` | `neutral/300` | `neutral/800` | `neutral/700` | `neutral/200` | `neutral/400` | `neutral/600` |
| Blue | `blue/100` | `blue/950` | `blue/200` | `blue/900` | `blue/800` | `blue/300` | `blue/500` | `blue/600` |
| Teal | `teal/100` | `teal/950` | `teal/200` | `teal/900` | `teal/700` | `teal/400` | `teal/500` | `teal/600` |
| Green | `green/100` | `green/950` | `green/200` | `green/900` | `green/800` | `green/400` | `green/600` | `green/600` |
| Yellow | `yellow/100` | `yellow/950` | `yellow/200` | `yellow/900` | `yellow/800` | `yellow/400` | `yellow/700` | `yellow/600` |
| Orange | `orange/100` | `orange/950` | `orange/200` | `orange/900` | `orange/700` | `orange/400` | `orange/500` | `orange/600` |
| Red | `red/100` | `red/950` | `red/200` | `red/900` | `red/800` | `red/300` | `red/500` | `red/600` |
| Magenta | `magenta/100` | `magenta/950` | `magenta/200` | `magenta/900` | `magenta/700` | `magenta/400` | `magenta/500` | `magenta/600` |
| Purple | `purple/100` | `purple/950` | `purple/200` | `purple/900` | `purple/700` | `purple/300` | `purple/500` | `purple/500` |

Categorical Tag mappings are chosen hue-by-hue for appearance and contrast; equivalent roles do not need matching numeric steps.

## Remaining implementation decisions

The Figma Color architecture and current alias values are synchronized.

Remaining concerns are downstream implementation or future evolution:

- runtime Theme package serialization and build pipeline;
- CSS representation of Theme-local Primitives;
- removal of hidden legacy variables only after migration consumers are known;
- future categorical hues only when real Tag use cases require them;
- promotion to a shared categorical contract only if repeated cross-component categorization needs emerge.
