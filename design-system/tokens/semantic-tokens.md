---
id: design-system.token.semantic-tokens
collection: design-system
type: token
title: Semantic Tokens
summary: Stable shared Color roles and their usage boundaries across compatible Theme and Appearance contexts.
knowledge_state: canonical
document_maturity: reviewed
related: []
last_reviewed: '2026-09-14'
---

# Semantic Tokens

Semantic tokens are the default Color interface consumed by product UI and most components. Their role meaning remains stable across compatible Themes and Appearances.

## Resolution

Semantic tokens are the stable shared Color interface. Their names and role meaning remain constant across compatible Themes and Appearances.

```text
Theme-local Primitive
→ Semantic role
→ Product UI / Component
```

The installed Theme provides concrete values for every required Semantic role in both Light and Dark Appearance.

Brand is represented by Semantic roles such as `surface/brand` and `fg/on-brand`; a separate Brand alias layer is not required by the target runtime architecture.

Product UI does not consume Theme-local Primitives directly.

Current Figma authoring keeps the public `03 Semantic` contract in a single `Value` mode. Product and Appearance are resolved behind it through two independent collections:

```text
02 Product          → JobVision | Cando
03 Semantic Values  → Light | Dark
                      ├── jobvision/*
                      └── cando/*
```

The public Semantic variables alias through the Product router to the selected Product branch, while `03 Semantic Values` supplies the selected Light/Dark value. Product and Appearance therefore do not enter public Semantic token names.

## Surface

Structural surfaces:

```text
surface/default
surface/muted
surface/inset
surface/raised
surface/inverse
```

Interactive neutral surfaces:

```text
surface/neutral-muted
surface/neutral-muted-hover
surface/neutral-muted-active

surface/neutral-emphasis
surface/neutral-emphasis-hover
surface/neutral-emphasis-active
```

Transparent interaction states:

```text
surface/transparent-hover
surface/transparent-active
surface/transparent-inverse-hover
surface/transparent-inverse-active
```

Persistent neutral selected containers:

```text
surface/selected
surface/selected-hover
```

Brand:

```text
surface/brand
surface/brand-hover
surface/brand-active
```

Accent:

```text
surface/accent-muted
surface/accent-muted-hover
surface/accent-muted-active

surface/accent-emphasis
surface/accent-emphasis-hover
surface/accent-emphasis-active
```

Magic:

```text
surface/magic-muted
surface/magic-emphasis
surface/magic-emphasis-hover
surface/magic-emphasis-active
```

Danger:

```text
surface/danger-muted
surface/danger-emphasis
surface/danger-emphasis-hover
surface/danger-emphasis-active
```

Support:

```text
surface/info-muted
surface/success-muted
surface/warning-muted
surface/error-muted
```

Disabled:

```text
surface/disabled
```

`canvas`, `surface/floating`, the v3 `surface/control*` and `surface/emphasis*` names, `surface/brand-muted`, and the expanded v3 Selected matrix are not part of v4.

### Surface meanings

- `surface/default`: ordinary base content surface and default root page/workspace surface.
- `surface/muted`: passive lower-emphasis structure; it has no interaction states.
- `surface/inset`: recessed/background structural region behind the local default surface.
- `surface/raised`: surface elevated relative to its parent. Elevation/shadow remains separate.
- `surface/neutral-muted`: visible neutral interactive treatment; not interchangeable with structural `surface/muted`.
- `surface/neutral-emphasis`: strong neutral interaction used by operational Primary actions.
- `surface/selected`: neutral persistent selected-container background, not a general Selected Color family.
- `surface/selected-hover`: only for selected containers that remain interactive while selected.
- `surface/brand`: Product identity or an approved key Product/conversion moment.
- Accent surfaces communicate chromatic interaction or affordance.
- Magic surfaces communicate AI-assisted/generated capability.
- Danger surfaces communicate destructive intent, not system failure.

Transparent interaction surfaces store their resolved RGBA values directly in Semantic Color variables. A published alpha-palette layer is not part of the current contract.

## Foreground

Use `fg/*` for text and icons.

```text
fg/primary
fg/secondary
fg/tertiary
fg/placeholder
fg/disabled

fg/on-inverse
fg/on-brand
fg/on-color

fg/accent
fg/magic
fg/danger

fg/info
fg/success
fg/warning
fg/error

fg/info-inverse
fg/success-inverse
fg/warning-inverse
fg/error-inverse
```

Role boundaries:

- `fg/primary`: essential/default readable content.
- `fg/secondary`: supporting readable content that contributes to understanding.
- `fg/tertiary`: auxiliary low-priority metadata; not a generic “make it lighter” option.
- `fg/placeholder`: placeholder content in input-like controls.
- `fg/disabled`: unavailable control/content styling; read-only is not Disabled.
- inverse Support foregrounds are intentionally narrow: colored Support content on `surface/inverse`.

`fg/brand`, `fg/selected`, `fg/on-disabled`, and `fg/on-color-disabled` are not part of the canonical v4 API. The old disabled-foreground variable remains hidden only for migration safety and is not part of the canonical API.

## Line

```text
line/muted
line/default
line/emphasis
line/disabled
line/inverse

line/accent
line/magic
line/danger

line/info
line/success
line/warning
line/error
```

- `line/muted`: subtle structural separation.
- `line/default`: normal control/container boundary; also the neutral unfilled path of operation-progress indicators.
- `line/emphasis`: stronger neutral interactive boundary.
- `line/disabled`: disabled control boundary.
- `line/inverse`: neutral boundary on an inverse surface.

Use `line/accent` for chromatic indicators such as a selected line Tab and the active arc/segment of Progress Circle and Progress Bar, including measured 100%. Use `line/success` / `line/error` for their complete static terminal outcome rings/segments. These are graphic line roles, independent of whether Figma/runtime renders them using Stroke or Fill. `line/brand` and `line/selected` are not part of v4.

Keep `line` rather than `border` as the source-token family; implementation utilities may use different naming.

## Selection

Selection is a component state rather than a parallel global Color family.

```text
selected line Tab → fg/primary + line/accent
checked checkbox  → surface/accent-emphasis + fg/on-color
saved bookmark    → fg/accent
selected row      → surface/selected + fg/primary
applied filter    → surface/accent-muted* + appropriate foreground/line
```

Only persistent neutral selected-container backgrounds receive shared selected tokens: `surface/selected` and, when the selected container remains interactive, `surface/selected-hover`.

## Brand and Accent

```text
Brand  → Product identity + approved key conversion moments
Accent → general chromatic interaction / affordance
```

The JobVision Theme may map Brand and Accent to Blue while the Cando Theme maps Brand to Yellow and Accent to Blue. Shared hue does not merge semantic meaning.

An actionable Accent banner or applied filter may use Accent Muted. A passive informational/system message uses Support Info.

## Magic

Magic is reserved for AI-assisted, AI-generated, or explicitly magical Product capability.

```text
surface/magic-muted     → subtle AI container/chip/section
surface/magic-emphasis* → strong interactive AI action or entry point
fg/magic                → AI icon, label, inline emphasis
line/magic              → AI-specific outline or indicator
```

Do not use Magic merely as decorative Purple.

## Danger and Error

```text
Danger → destructive intent/action
Error  → validation failure or system/problem state
```

Danger is not a fifth standard Notification severity. Standard system feedback remains Info / Success / Warning / Error.

## Support

Only muted Support surfaces are approved globally. A baseline inline-feedback recipe may use:

```text
surface/{severity}-muted
fg/{severity}
line/{severity}        # only when anatomy uses a semantic boundary
fg/primary
fg/secondary
```

Inverse feedback may use:

```text
surface/inverse
fg/on-inverse
fg/{severity}-inverse
```

The inverse foreground roles do not imply inverse Support surfaces or lines.

## Focus

Canonical roles:

```text
focus/default
focus/inverse
```

Figma uses the same canonical names: `focus/default` and `focus/inverse`. Focus remains a dedicated Semantic role. `focus/default` currently shares the approved Accent primitives (`palette/blue/600` in Light and `palette/blue/500` in Dark), but components consume the Focus role rather than Accent directly. Sharing a Primitive does not merge the semantic meanings.

## Link

```text
link/default
link/hover
link/subtle
link/subtle-hover
link/inverse
link/inverse-hover
```

Default is chromatic and recognizable; Subtle is intentionally neutral where clickability is already clear; Inverse adapts Link for `surface/inverse`. Link remains independent from Accent even when both resolve to Blue.

`link/visited`, `link/emphasis`, and `link/emphasis-hover` are not part of v4.

## Utility

Current shared utility Color roles cover overlay and skeleton treatments. Focus is its own Semantic family. In Figma the utility roles are:

```text
utility/overlay
utility/skeleton-background
utility/skeleton-base
utility/skeleton-element
utility/skeleton-shimmer
```

Overlay stores its resolved RGBA value directly. Skeleton roles use Neutral Primitive aliases. Exact mappings are documented in `color-token-aliases.md`.

## Component-owned exception

Categorical Tag Color is component-owned rather than Semantic. Its finalized contract is:

```text
tag/{color}/surface
tag/{color}/surface-hover
tag/{color}/fg
tag/{color}/line
```

for:

```text
neutral | blue | teal | green | yellow | orange | red | magenta | purple
```

Categorical hues communicate grouping, not Support meaning. Cyan and Warm Gray are hidden legacy variants, not canonical API.

## Source of truth

- Semantic meaning and usage → this document.
- Exact current visual aliases/values → Figma, with `color-token-aliases.md` as the documented mapping contract.
- Component recipes → the corresponding component guideline.
- Layering and collection responsibilities → `architecture.md`.
