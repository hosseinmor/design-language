---
id: design-system.token.component-tokens
collection: design-system
type: token
title: Component Tokens
summary: Defines when component-specific Color tokens are justified and documents the approved Tag exception.
knowledge_state: canonical
document_maturity: reviewed
related: []
last_reviewed: '2026-09-14'
---

# Component Tokens

## Purpose

Component Color tokens are exceptions. Create them only when a stable component-owned contract cannot be expressed clearly through shared Semantic Color roles.

Other foundations may define component-owned geometry or motion tokens under their own contracts; they are not required to follow the Color graph.

## Default rule

Most components consume Semantic Color directly:

```text
Theme-local Primitive → Semantic → Product UI / Component
```

A private Component token may alias a Semantic role when that indirection adds useful component-owned meaning, but Theme packages should not need to know about ordinary component anatomy.

Do not insert a Component-token layer merely to rename an existing Semantic token.

For example, Button presets map directly to Semantic roles. Button does not need its own Color-token family.

## When a Component Color token is justified

Create one only when:

- existing Semantic roles cannot express the value clearly;
- the meaning is stable and owned by that component;
- the role recurs across variants, states, or implementations;
- the extra layer reduces real implementation or theming complexity;
- the contract can be mapped consistently in Figma and code;
- the Design System owner approves it.

Do not create Component Color tokens for one-off values, experiments, every Figma property/state, or aliases that only rename Semantic Color.

## Approved Color exception: Tag

Tag owns a private categorical Color contract because its hues communicate grouping/categorization rather than shared system semantics such as Success, Warning, or Error.

Canonical component contract:

```text
tag/{color}/surface
tag/{color}/surface-hover
tag/{color}/fg
tag/{color}/line
```

Current canonical colors:

```text
neutral
blue
teal
green
yellow
orange
red
magenta
purple
```

This set is intentionally not a complete hue palette. Cyan and Warm Gray remain legacy-only.

### Product and Appearance model

Tag categorical values are **shared across Products**. They are not Brand/Theme values.

```text
04 Component Tokens
├── Light
└── Dark
```

The Tag contract does not include a `brand` color. Product identity is handled by shared Brand Semantic roles elsewhere in the Color system, not by categorical Tag variants.

Tag Component Tokens belong to the Design System/component implementation rather than Theme packages.

### Consumption boundary

Tag tokens are component-implementation API, not Product-facing Design System API.

Product tooling should therefore:

- omit `tag/*` from general Semantic token registries/autocomplete;
- not generate public Tailwind utilities for `tag/*`;
- reject direct `tag/*` use in ordinary Product code where lint/CI can enforce it;
- allow the Tag implementation to consume the contract.

If CSS custom properties for Tag are emitted globally, physical CSS visibility does not make them public API.

### Resolution rules

- `neutral` resolves from the shared neutral categorization treatment.
- categorical hue mappings are shared across Products.
- Light/Dark Appearance may resolve different Primitive steps for contrast and visual balance;
- do not map categorical Green to Success, Yellow to Warning, Red to Error, or Purple to Magic merely because the hues match;
- equivalent Tag roles across hues do not need identical numeric Primitive steps when contrast/appearance requires otherwise.

The current four Tag roles are retained for every canonical color. `surface-hover` is consumed only when the rendered Tag is interactive.

### Promotion rule

Do not create a shared `categorical/*` API while Tag is the only real consumer.

If the same categorization meaning later becomes a stable cross-component need—for example across Tag, Legend, Category Badge, and other reviewed components—evaluate promotion from `tag/*` into a shared categorical contract at that time.

Abstract after repeated cross-component need, not before it.

## Applied Filter rule

Do not use Tag tokens merely because an applied Filter Chip visually resembles a Tag.

Use this order:

1. Express the state with existing Semantic roles, such as `surface/accent-muted*` when appropriate.
2. If a stable component-owned treatment still cannot be expressed, introduce a reviewed component-specific contract.
3. Reuse Tag tokens only when the UI is actually rendering the Tag component.

## Naming

Canonical Tag naming follows:

```text
{component}/{variant}/{role-or-state}
```

Examples:

```text
tag/blue/surface
tag/blue/surface-hover
tag/blue/fg
tag/blue/line
```

Runtime/CSS flattening is a separate implementation decision.

## Review checklist

- Can an existing Semantic token express this value?
- Does the token add stable component meaning?
- Is it reused enough to justify another layer?
- Does it reduce real branching or duplication?
- Is the name independent from an accidental visual value, except where hue itself is the approved categorical contract?
- Is the mapping valid across supported Light/Dark Appearance contexts?
