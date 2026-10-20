---
id: design-system.reference.theme-initialization
collection: design-system
type: reference
title: Theme Initialization Contract
summary: Defines installed Theme package readiness, Appearance resolution, first-paint invariants, hydration continuity, and no-flash requirements.
knowledge_state: unverified
document_maturity: draft
owner: Design System team
last_reviewed: '2026-09-14'
related:
  - design-system.product-variation.theme-context
  - design-system.reference.source-of-truth
---

# Theme Initialization Contract

## Status

Design-side runtime contract for HOS-9 after adopting installable Theme packages. Exact framework, storage, DOM, selector, bootstrap-script, and server integration mechanics remain Frontend-owned.

## Purpose

The application must have a compatible Theme package available and the correct Appearance effective for the **first styled paint**.

The runtime concerns are now:

```text
Application/deployment
→ selects/imports Theme package

Theme package
→ provides token values

Appearance preference
→ resolves light | dark inside the installed Theme
```

Product identity itself is not a runtime token-resolution dimension.

## Theme package readiness

Theme selection/import is an application/deployment concern.

- A compatible Theme package must be available before DS-governed UI is styled.
- The Design System does not define a fallback Theme package.
- Missing/incompatible Theme integration is a configuration/build/integration error; do not silently fall back to another Product Theme.
- Current intended application mapping is JobVision → JobVision Theme and Cando → Cando Theme, but this is not a permanent Product=Theme identity rule.

How the package is imported, bundled, lazy/eager loaded, versioned, or injected is Frontend-owned as long as the first-paint invariant is met.

## Appearance preference model

If a user-facing Appearance preference is supported, its logical values are:

```text
light | dark | system
```

Resolved Appearance remains only:

```text
light | dark
```

`system` is a preference source, not a third resolved Appearance.

### Resolution precedence

Resolve Appearance in this order:

1. explicit user preference `light` or `dark`;
2. current system/user-agent color-scheme preference when effective preference is `system` or no explicit preference exists;
3. `light` when system preference cannot be determined.

Invalid/unknown stored values are treated as no explicit preference.

The Design System does not define preference storage or precedence between multiple storage locations. The application provides one effective preference to initialization.

## First-paint invariant

The first styled paint must already use:

- values from the selected compatible Theme package; and
- the effective Light/Dark Appearance.

A compliant implementation must not intentionally paint one Appearance and then correct it after hydration.

It must also not paint using a different Theme package and later swap to the intended Theme as the normal initialization strategy.

Valid strategies may include:

- server-readable effective preference;
- CSS-native `prefers-color-scheme` resolution;
- a minimal pre-paint client bootstrap;
- another mechanism that satisfies the same invariant.

If the server cannot know a `system` preference on the first request, implementation must still avoid painting a guessed Appearance and then visibly correcting it.

## Hydration continuity

Hydration must adopt/reconcile with the Theme values and Appearance already effective at first paint.

```text
installed Theme package
+ effective Appearance
→ first styled paint
→ hydration adopts same effective visual state
→ normal runtime Appearance updates
```

Individual components must not implement their own Theme detection, package selection, or flash prevention.

## Runtime Appearance changes

- Explicit `light` ignores later OS Light/Dark changes.
- Explicit `dark` ignores later OS Light/Dark changes.
- `system` follows current system/user-agent color-scheme changes.
- When no explicit preference exists, system behavior follows the same rule as `system`.
- Changing Appearance updates Semantic resolution within the already-selected Theme package.

Switching Theme packages at runtime is **not required by the v1 contract**. If a future application requires runtime Theme switching, treat that as a separate capability with its own compatibility and loading contract.

## User-agent UI

Browser-provided UI such as form controls, scrollbars, and document canvas should be informed of the effective supported color scheme early enough to avoid mismatch with application surfaces.

Exact use of HTML metadata, CSS `color-scheme`, or another platform mechanism is Frontend-owned.

## No-flash acceptance criteria

At minimum, validate:

| Scenario | Required first paint |
|---|---|
| Selected Theme + explicit Light | selected Theme / Light |
| Selected Theme + explicit Dark | selected Theme / Dark |
| Selected Theme + system Dark | selected Theme / Dark |
| Selected Theme + system Light | selected Theme / Light |
| Selected Theme + no explicit preference + system Dark | selected Theme / Dark |
| Selected Theme + no explicit preference + system Light | selected Theme / Light |
| System preference unavailable | selected Theme / Light fallback |
| Invalid stored Appearance preference | resolve as no explicit preference |
| Theme package missing/incompatible | configuration error; do not silently substitute another Theme |

Also verify:

- hydration does not visibly change Theme or Appearance;
- system preference changes update Appearance only while effective preference is `system` or absent;
- explicit Light/Dark remains stable when OS Theme changes;
- browser-controlled UI does not visibly contradict the application Appearance;
- components do not need individual initialization guards;
- correctness is not achieved by globally hiding normal page content until hydration as the default strategy.

## Frontend-owned decisions

This contract intentionally does not define:

- package import/bundle mechanism;
- Theme package naming;
- cookie/profile/local-storage preference persistence;
- precedence between multiple persistence locations;
- exact SSR framework integration;
- root attribute/class/selector names;
- inline script versus external bootstrap;
- caching strategy;
- runtime Theme switching beyond v1.
