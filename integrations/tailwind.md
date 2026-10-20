---
id: design-system.reference.tailwind
collection: design-system
type: reference
title: Tailwind Integration Contract
summary: Defines the Design System boundary for Tailwind consumption across Color, Spacing, Radius, Typography, Elevation, responsive breakpoints, component tokens, and arbitrary values.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: 2026-09-21
related:
  - design-system.token.architecture
  - design-system.token.semantic-tokens
  - design-system.token.component-tokens
  - design-system.foundation.spacing
  - design-system.foundation.radius
  - design-system.foundation.typography
  - design-system.foundation.elevation
  - design-system.foundation.responsive-layout
  - design-system.foundation.responsive-layout-spec
---

# Tailwind Integration Contract

## Purpose

Tailwind is a Product implementation interface over Design System decisions. It is not the source of truth for semantic Color, Foundation scales, responsive thresholds, or reusable component behavior.

This document records owner-approved Design-side invariants. Frontend review may choose the implementation shape, but it should preserve these boundaries and semantics.

The Design System package must remain framework-agnostic and must not depend on Tailwind.

Where Product code uses Tailwind, its configuration should consume generated Design System artifacts rather than re-authoring Foundation values manually.

## Color mapping

Canonical Design System Color vocabulary remains semantic and implementation-agnostic:

```text
surface/*
fg/*
line/*
focus/*
```

Tailwind maps those families to property-oriented utility namespaces:

| Design System role | Tailwind namespace |
|---|---|
| `surface/{role}` | `bg-{role}` |
| `fg/{role}` | `text-{role}` |
| `line/{role}` | `border-{role}` |
| `focus/{role}` | `outline-{role}` |

Do not repeat a family name when the utility namespace already communicates the CSS property.

```text
surface/default → bg-default
fg/primary      → text-primary
line/accent     → border-accent
focus/default   → outline-default
```

Special semantic families keep enough identity to avoid ambiguity. For example Link roles may map to `text-link*` instead of colliding with general foreground roles.

The canonical Focus implementation uses `outline` with a `1px` `outline-offset`; do not map the standard Focus contract to Tailwind `ring-*` utilities, which are box-shadow based. Primitive and Brand colors must not become normal Product-facing Tailwind utilities.

Normal Product theming should not require Tailwind `dark:` variants for Design System Color; Semantic variables resolve Appearance underneath the utility contract.

For Tailwind 3, prefer property-specific mappings such as `backgroundColor`, `textColor`, `borderColor`, and `ringColor` over one unrestricted shared `theme.colors` pool. Exact preset/config mechanics remain Frontend-owned.

## Component-token boundary

Approved Component tokens are implementation contracts for their owning Design System component. They do not generate general Product-facing Tailwind utilities by default.

Example:

```text
tag/blue/surface
tag/blue/fg
tag/blue/line
```

remain Tag-owned implementation roles; they should not automatically create Product utilities such as `bg-tag-blue-surface` or `text-tag-blue-fg`.

Product code should consume the existing Design System component rather than reconstruct it from utility recipes.

If a Component token repeatedly represents a cross-component Product need, evaluate promotion into the shared Semantic/Foundation contract instead of exposing the Component token directly.

## Spacing

Product code uses native Tailwind spacing utilities backed by the generated Design System spacing scale.

Examples:

```text
p-4
gap-6
mt-8
```

The Design System does not create a second custom spacing utility namespace.

See the Spacing Foundation for the canonical values and shared keys.

## Radius

Product Tailwind may expose the canonical Radius scale directly:

```text
rounded-none
rounded-small
rounded-medium
rounded-large
rounded-full
```

The Design System values are `0 / 3 / 6 / 12 / Full`; Tailwind's default radius scale is not canonical for Design System-governed components.

Legacy `rounded-control` and `rounded-surface` mappings are deprecated migration aliases. The former 20px large-surface value is not canonical; any temporary legacy adapter must use a distinct legacy name rather than `rounded-large`.

## Typography

Recurring Product typography uses Design System composite recipes.

Native Tailwind typography utilities remain available for local/exceptional composition and for landing/marketing/lead/display typography that intentionally sits outside the core Product recipe set.

Do not combine a DS typography recipe with Tailwind utilities that override the same owned properties:

```text
font-size
line-height
font-weight
```

Utilities for unrelated properties such as alignment are allowed.

The exact runtime consumption syntax for DS typography is not finalized. CSS classes, an Angular directive/component, or another generated adapter are valid implementation options for Frontend review. A `type-*` public class prefix is not a Design-side requirement.

## Elevation

The Design System exposes semantic shadow recipes rather than Tailwind's generic `shadow-sm/md/lg/xl` ladder.

Current Foundation roles are:

```text
Shadow/Floating
Shadow/Dragged
```

Product tooling may expose semantic utilities such as:

```text
shadow-floating
shadow-dragged
```

Exact generated names and adapter implementation remain Frontend-owned.

Component-owned directional or representational shadows, such as non-modal Drawer edge shadow or PDF page shadow, do not automatically become public Tailwind utilities.

## Responsive breakpoints

Responsive Layout exposes two related concepts:

- semantic viewport ranges for page structure: `narrow <768`, `regular >=768`, `wide >=1400`;
- a breakpoint ruler for fine-tuning.

The breakpoint ruler maps to Product Tailwind screens as follows:

| Design System token | Tailwind key | Value |
|---|---|---:|
| `xsmall` | `xs` | `320px` |
| `small` | `sm` | `544px` |
| `medium` | `md` | `768px` |
| `large` | `lg` | `1012px` |
| `xlarge` | `xl` | `1280px` |
| `xxlarge` | `2xl` | `1400px` |

Tailwind screen keys are an implementation adapter over the ruler. They do not imply six semantic page modes.

Breakpoint values have one canonical Design System source of truth. The same source must generate Design System responsive outputs, Product Tailwind `screens`, and any other runtime representation that needs the shared ruler.

Do not manually maintain a second set of breakpoint numbers in Product Tailwind configuration.

Page-level structure should prefer the `narrow / regular / wide` semantics. Exact Tailwind/custom-media variants for those ranges remain Frontend-owned.

Container-query implementation is also Frontend-owned. On Tailwind 3 this may use native CSS `@container`, an approved plugin/adapter, or component CSS; do not invent viewport breakpoints to substitute for a container-width dependency.

The Design System package must not depend on Tailwind. Exact machine-readable source format, generated module format, and build/import integration remain Frontend-owned.

Figma's `Typography breakpoint` modes are design-time Fluid Heading modes and are not the runtime breakpoint ruler.

## Arbitrary and raw values

Core rule:

> Arbitrary values may solve contextual Product layout needs; they must not bypass an established Design System decision.

### Blocked

Use of raw values that bypass a mature Design System contract.

Examples:
- raw Color when an approved Semantic role exists;
- reconstructing an existing Design System component from utilities instead of consuming the component;
- arbitrary Radius/Shadow when an approved role expresses the intended component anatomy.

### Discouraged or transitional

Use of raw/arbitrary values in a Foundation whose contract is still under validation.

These should be treated as migration exceptions and reduced as the Foundation becomes canonical.

### Allowed

Contextual layout constraints that are not useful shared tokens.

Examples:

```text
w-[376px]
grid-cols-[280px_1fr]
max-h-[calc(100vh-64px)]
```

Raw CSS is not a loophole around a governed Design System property.

Do not create a global token solely to eliminate an arbitrary value when the value is genuinely local to one layout.

## Structural utilities

Ordinary structural utilities remain normal Product tools:

```text
flex
grid
items-*
justify-*
order-*
overflow-*
positioning utilities
```

Use Flexbox or CSS Grid locally inside Layout regions when the composition requires it. Contextual track definitions such as `grid-cols-[280px_1fr]` remain allowed when they are genuinely page/component-specific.

Responsive Layout does not define a public global 4/8/12-column utility contract or global grid gutters. Product code must not infer such a contract from legacy Figma Grid styles.

The Design System should govern reusable semantic visual decisions, not replace every CSS/layout primitive with a token.

## Frontend-owned decisions

This document intentionally does not decide:
- exact Tailwind preset/package API;
- exact generated file/module names;
- exact import/build integration;
- how Tailwind's default palette/utilities are suppressed or linted;
- exact typography runtime adapter syntax;
- exact lint/CI implementation for arbitrary/raw-value enforcement.

Those are Frontend implementation decisions as long as they preserve the Design System invariants above.
