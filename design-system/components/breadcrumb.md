---
id: design-system.component.breadcrumb
collection: design-system
type: component
title: Breadcrumb
summary: Breadcrumbs show the current page in a hierarchy and provide navigation to ancestor destinations.
knowledge_state: verified
document_maturity: draft
design_status: ready-for-dev
design_maturity: handoff-ready
last_reviewed: '2026-09-19'
related:
  - design-system.component.link
  - design-system.reference.component-mapping
---

# Breadcrumb

## Purpose

Breadcrumb shows the current page in its hierarchical context and lets users navigate to ancestor destinations.

Use it when the page belongs to a meaningful multi-level hierarchy. Do not use it as a replacement for primary navigation, tabs, step/progress navigation, or browser history.

## Canonical Figma Model

Canonical file: `[DS] Job Vision NEXT`

### Breadcrumb

- Component: `Breadcrumb`
- Figma node ID: `22973:282463`
- Figma component key: `b0fb38288d8b84e0ff6e1d5ded6eeb31574581fa`
- Content property: native `Items` SLOT
- Default authoring content: 3 visible items
- Slot preferred content: `Breadcrumb Item / Default`
- Slot minimum: 2 items
- Default content remains visible when a new Breadcrumb instance is inserted.

### Breadcrumb Item

- Component set: `Breadcrumb Item / Default`
- Figma node ID: `22986:407`
- Figma component key: `e0fcea8c52b6deb183c6d2c4624243875ae21425`
- Variant property: `Type = Link / Current / Overflow`
- Content property: `Current label`

The set is intentionally small. Link and Overflow interaction states are owned by their nested canonical components rather than duplicated as Breadcrumb variants.

## Anatomy and Composition

A Breadcrumb contains:

1. one current-page item;
2. zero or more ancestor Link items;
3. an optional Overflow item when middle hierarchy levels are collapsed.

### Link item

`Type=Link` composes the canonical `Link / Default` component at:

- Style: `Subtle`
- Size: `Medium`

Link text and interaction states remain owned by Link.

Do not add Breadcrumb-specific Hover, Active, Focus, Disabled, or Visited states.

### Current item

The current page:

- is always present;
- is the last semantic hierarchy item;
- is non-interactive;
- uses the primary foreground treatment;
- must be identifiable as the current page to assistive technology.

Do not render the current page as another ancestor Link.

### Overflow item

`Type=Overflow` composes the canonical `Icon Button / Ghost / Extra Small`.

It represents hidden middle hierarchy levels. The overflow surface/menu implementation is a runtime dependency and is not duplicated as a Breadcrumb variant.

### Separator

The visual separator is `/` using the secondary foreground treatment.

Separators are presentation only and must not become meaningful screen-reader content.

Current has no trailing separator.

## Spacing and Sizing

The reviewed Figma composition uses:

- Breadcrumb Items Slot gap: `8px`;
- Link item separator-to-Link gap: `8px`;
- Overflow separator-to-trigger gap: `4px`;
- minimum stable Breadcrumb height: `28px`, driven by the Extra Small overflow Icon Button.

Breadcrumb remains single-line.

Do not introduce a wrapping Breadcrumb layout as a second shared variant.

## Hierarchy and Overflow

For short paths, show the complete useful hierarchy.

For deep or constrained paths, preserve the most useful context with the reviewed pattern:

```text
Root / … / Parent / Current
```

Rules:

- Current is always visible.
- The nearest Parent is preserved.
- Root remains a normal text Link by default; do not replace it with a home-icon-only convention.
- Overflow represents hidden middle levels.
- There is no fixed maximum item-count contract.
- The exact runtime measurement threshold and collapse algorithm remain unverified until the owning runtime source is registered.

Primer and Carbon both support an overflow model for constrained/deep Breadcrumbs; the JV contract keeps a visible Root, nearest Parent, and Current in the reviewed collapsed state.

## Long Labels and Responsive Behavior

Breadcrumb stays on one line.

Long labels truncate rather than wrap.

Current uses a reviewed Figma authoring cap of approximately `240px` with end truncation.

Ancestor items directly compose the canonical Link component. Canonical Link is currently hug-content and does not expose a truncation/max-width property, so the Breadcrumb Figma component does **not** fake ancestor ellipsis by detaching or duplicating Link.

At runtime, available inline space should drive ancestor truncation and hierarchy collapse. The exact width constraint and measurement algorithm remain unverified until the owning runtime source is registered. Do not infer a fixed viewport breakpoint from the Figma examples.

This is an intentional Figma/runtime authoring boundary: preserving canonical Link composition takes precedence over simulating ancestor ellipsis inside the Figma component.

For increasingly narrow layouts, collapse hierarchy before allowing the Breadcrumb to become a multiline block.

## RTL and Direction

Do not create separate RTL variants.

The hierarchy remains semantic; visual layout follows the document direction.

In RTL product authoring:

- Current appears at the logical end of the path;
- ancestors extend toward the logical start;
- Link and Icon Button behavior follows their own RTL contracts.

The slash separator does not require a mirrored asset.

Runtime DOM/order must preserve understandable hierarchy for assistive technology rather than relying only on visual reversal.

## Accessibility Contract

Breadcrumb follows standard breadcrumb navigation semantics:

- expose the trail as a navigation landmark with an accessible label;
- represent hierarchy as an ordered list or equivalent semantic list structure;
- ancestor destinations are normal Links;
- identify the current page with `aria-current="page"` or the equivalent current-page semantic on the non-interactive current item;
- keep visual separators out of the accessibility tree;
- do not create custom keyboard navigation for the trail itself;
- ancestor Links use normal Link keyboard/focus behavior;
- the Overflow trigger uses normal Icon Button focus behavior and must have an accessible name;
- hidden hierarchy levels exposed through Overflow must remain keyboard-accessible through the owning popup/menu pattern;
- Breadcrumb wrappers must not clip Link or Icon Button focus outlines.

The WAI-ARIA APG Breadcrumb pattern uses a labeled navigation landmark and ordered-list structure. Carbon similarly treats the current page as non-link content and keeps a truncation/overflow trigger in the keyboard sequence.

## Figma Authoring Rules

- Insert `Breadcrumb` for the full path; do not assemble unrelated Link instances manually.
- Use `Breadcrumb Item / Default` inside the native Items Slot.
- Include exactly one `Type=Current`.
- Use `Type=Link` for ancestors.
- Use `Type=Overflow` only when levels are intentionally collapsed.
- Do not detach Link or Icon Button to create Breadcrumb-specific states.
- Do not use `Breadcrumb / Legacy` or `Breadcrumb Item / Legacy` for new work.

## Runtime Boundary

The owning JV Design System runtime repository/package is not registered in Design System Knowledge.

The verified Storybook source is also not registered.

Therefore the following remain explicitly unverified:

- exact runtime component/API name;
- exact props/inputs/outputs;
- DOM implementation details beyond the semantic contract above;
- exact collapse measurement/algorithm;
- popup/menu implementation used by Overflow;
- exact framework/Tailwind implementation;
- Storybook story/docs identifier;
- Figma-property to code-prop mapping;
- Code Connect mapping.

Do not infer these from Figma property names.

## QA Checklist

Verify:

- a newly inserted Breadcrumb shows visible default content;
- exactly one Current item exists;
- Current is non-interactive;
- ancestor items compose canonical Subtle / Medium Link;
- Overflow composes canonical Ghost / Extra Small Icon Button;
- short paths render without unnecessary Overflow;
- deep paths can represent Root / Overflow / Parent / Current;
- long labels stay single-line and truncate;
- RTL hierarchy is visually correct;
- Link and Overflow Focus treatments remain visible and unclipped;
- separators are decorative for assistive technology;
- runtime current-page semantics are present when implementation is registered.

## Legacy

Legacy Figma components remain separated from the canonical documentation area only for migration/reference:

- `Breadcrumb / Legacy`
- `Breadcrumb Item / Legacy`

Do not create new instances from legacy components.

## Live References

- Figma file key: `rROD8ctH9UfPGAMrRrOzHe`
- Breadcrumb node: `22973:282463`
- Breadcrumb key: `b0fb38288d8b84e0ff6e1d5ded6eeb31574581fa`
- Breadcrumb Item node: `22986:407`
- Breadcrumb Item key: `e0fcea8c52b6deb183c6d2c4624243875ae21425`
- Runtime code: unregistered
- Storybook: unregistered
