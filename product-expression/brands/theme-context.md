---
id: design-system.product-variation.theme-context
collection: design-system
type: product-variation
title: Theme Package Architecture
summary: Canonical Product-to-Theme relationship, package selection responsibility, supported variation scope, and boundaries with Semantic tokens and Appearance.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.token.architecture
  - design-system.token.semantic-tokens
  - design-system.product-variation.brand-variants
  - design-system.product-variation.product-overrides
  - design-system.reference.figma
  - design-system.reference.code
  - design-system.reference.theme-initialization
  - design-system.token.frontend-contract
last_reviewed: '2026-09-14'
---

# Theme Package Architecture

## Purpose and ownership

A **Theme** is an independently installable implementation of Design System visual-token values. A **Product** is an application/business identity; its identity is **not** itself a Theme, a global runtime token-resolution axis, or a new Semantic token namespace.

This document owns the **Product ↔ Theme relationship and intended variation policy**, not the full Color token architecture, Figma variable inventory, generated package format, or first-paint runtime mechanics.

| Decision | Canonical owner |
|---|---|
| Which compatible Theme an application selects | Product/application deployment, within this Design Language selection contract |
| Stable token names, consumption rules, Brand/Accent meaning, Primitive versus Semantic API | [Color Token Architecture](../../design-system/tokens/color/architecture.md), [Color Semantics](../../design-system/tokens/color/semantics.md), and [Color Usage](../../design-system/tokens/color/usage.md) |
| Values and aliases of current editable design | [Figma Reference](../../integrations/figma.md) and live Figma; [Color Aliases](../../design-system/tokens/color/aliases.md) is the documented design mapping |
| Concrete Theme package values and implemented imports/exports | Registered Karbon Code/Theme package source; [Frontend Token Contract](../../integrations/frontend-token-contract.md) is the **design-side** interface proposal |
| Effective Appearance and first paint | [Theme Initialization](../../integrations/theme-initialization.md) (design-side contract); implementation mechanics are Frontend-owned |
| Brand usage and exceptions | [Brand Variants](brand-variants.md), [Product Overrides](product-overrides.md), and owning Product Knowledge for feature-specific eligibility |

## Product is not Theme

Current intended application-to-package selection:

```text
JobVision application → JobVision Theme package
Cando application     → Cando Theme package
```

This is **not** a permanent one-to-one rule. Another Product may reuse a compatible Theme, and an application/deployment may intentionally select another compatible Theme without changing the shared Semantic vocabulary or the Product's business identity.

The application/deployment **chooses the installed Theme**. A shared component or ordinary Product UI must not branch on Product identity simply to choose Semantic Color values. Theme changes are not an acceptable substitute for a product-specific business rule.

## Theme participation

**V1 design contract:** Theme packages provide **Color** values, including their own internal Primitives and mappings for both `light` and `dark` Appearance. One Theme contains both Appearances; separate per-Appearance packages are not part of the intended contract.

The model can later support **Spacing, Radius, Typography, Elevation, or Motion** values when a validated cross-Theme difference requires them. Merely being able to vary a Foundation is **not** approval to move it into every Theme. Shared Foundations stay shared unless the Design System owner explicitly approves a variation.

The Semantic role API and accessibility/compatibility obligations remain shared across compatible Themes. Component-local/private contracts do not automatically become Theme-level inputs: the currently approved categorical **Tag** Color family stays component-owned, Product-independent, and Light/Dark-aware.

## Appearance and Figma authoring

Resolved runtime Appearance is `light | dark`; if supported, `system` is a preference **source**, not a third resolved Appearance. The application shell/Theme service owns preference resolution and runtime changes. [Theme Initialization](../../integrations/theme-initialization.md) owns its detailed no-flash and hydration requirements.

Figma currently exposes independent authoring choices for **Product** (JobVision/Cando) and **Appearance** (Light/Dark), using the public Semantic Color API. That authoring graph is **not** a prescribed runtime package graph. The current Figma collections, legacy aliases and editable bindings are registered in [Figma Reference](../../integrations/figma.md); do not maintain their full parallel inventory here.

## Brand versus Theme

Brand is **semantic design meaning** used for Product identity and approved key conversion moments; it is **not** a required independent runtime Brand alias layer. For example, JobVision and Cando Themes can resolve `surface/brand` and `fg/on-brand` from their own internal palettes while preserving one shared Semantic meaning.

The choice to **use** a Brand Button follows [Brand Variants](brand-variants.md) and [Button](../../design-system/components/button.md); it is not an automatic consequence of installing a Product Theme. Actual palette values and accessible foreground mappings belong to Color/Figma, not this file.

## Product-level exceptions

A different Theme **value** for the same Semantic role is normal Theme variation, not a Product Override. A different Product rule or a one-off UI composition is also **not** automatically a new shared override.

When a Product deliberately needs to depart from a reusable Design Language guideline, use the [Product Overrides](product-overrides.md) review route, with explicit affected scope, owner, evidence and accessibility implications. Product permissions, eligibility, lifecycle and feature flow remain with **Product Knowledge / Product Walkthrough**.

## Runtime status and unresolved implementation

The architectural decisions above are **reviewed design contracts**, not a claim that a particular Theme package, serializer, Storybook build or first-paint implementation is already shipped.

Exact package names/import paths, CSS/JSON/TypeScript output, runtime selector/attribute mechanism, build/publish pipeline, SSR persistence and no-flash implementation belong to the frontend integration documents and owning runtime repository. Until those sources are registered and verified, AI must not infer implemented package details from this document.
