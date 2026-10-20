# Design Tokens

This section contains the detailed Color contracts. Start with `../../foundations/visual/color.md` for the operational model and use the smallest detailed document needed for the question.

The current architecture separates a **shared Design System token contract** from **installable Theme packages that provide values**.

Non-Color Foundations such as Typography, Spacing, Radius, Elevation, Motion, and Responsive Layout keep their own contracts. Theme packages are Foundation-agnostic in architecture, but v1 Theme packages provide Color only.

## Current Color documents

- `architecture.md` — shared-contract ↔ Theme-implementation model and current Figma representation
- `primitive-tokens.md` — current Primitive inventory and palette work; runtime ownership is Theme-local
- `semantic-tokens.md` — stable shared UI Color roles and usage boundaries
- `color-token-aliases.md` — current validated Figma Theme × Appearance mappings
- `component-tokens.md` — component-token criteria and the finalized categorical Tag Theme Extension
- Product ↔ Theme selection is owned by [`product-expression/brands/theme-context.md`](../../product-expression/brands/theme-context.md).
- `usage-rules.md` — Semantic Color consumption and migration rules
- Frontend packaging and serialization boundaries are documented in [`integrations/frontend-token-contract.md`](../../integrations/frontend-token-contract.md).

Superseded v3/v4 working catalogs are retained in Git history, not in the active knowledge corpus. The current contracts listed above are authoritative.

## Color model

```text
Shared DS contract
  Semantic names + meanings
          │
          ▼
Installed Theme package
  Theme-local Primitives
  Light/Dark Semantic values
  private Component Tokens
          │
          ▼
Product UI / DS Components
```

Product UI consumes Semantic Color by default. Theme-local Primitives are implementation detail.

Brand remains Semantic meaning, not a required runtime alias layer.

Categorical Tag is currently the only approved Component Color-token exception. Its `tag/*` contract is shared across Products, varies only by Light/Dark Appearance, and is not Product-facing API.

## Current Figma model

```text
01 Primitives            → Value
02 Product               → JobVision | Cando
03 Semantic              → Value
03 Semantic Values       → Light | Dark
  ├── jobvision/*
  └── cando/*
04 Component Tokens      → Light | Dark
```

- `02 Product` is the Figma Product selector and switches both Product-aware typography and Semantic routing.
- `03 Semantic` is the published stable Color contract.
- `03 Semantic Values` holds Product-nested Light/Dark implementation values.
- `04 Component Tokens` remains Product-independent and component-only.
