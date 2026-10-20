---
id: design-system.token.jobvision-color-tokens-v4-surface-model
collection: design-system
type: token
title: JobVision Color Tokens v4 — Surface Model
summary: Draft canonical v4 Color-token catalog; unresolved alias values are tracked separately.
knowledge_state: unverified
document_maturity: draft
related: []
---

# JobVision Color Tokens v4 — Surface Model

> Status: draft
> Product scope: JobVision + Cando
> Appearance scope: Light + Dark
> Alias value status: partial — unresolved mappings remain `TBD`
> Figma implementation mapping: open decision

This document is the canonical v4 **Color-token catalog**. It records the approved semantic structure and the current audited role boundaries. Exact opaque Primitive scale values and final Light/Dark alias steps remain intentionally open until the palette pass.

The architecture below is specific to Color. Typography, Spacing, Radius, Elevation, and Motion may use different token graphs and must document their own resolution model.

---

## Architecture

```text
Core path
01 Primitives
      ↓
03 Semantic
      ↓
04 Component

Optional product-identity branch
01 Primitives
      ↓
02 Brand
      ↓
03 Semantic
```

Brand is not a mandatory hop between Primitive and Semantic. Semantic roles alias Brand only when their value intentionally depends on Product identity; otherwise they may alias Primitive values directly.

Collections and logical Theme dimensions:

```text
01 Primitives
- Value

02 Brand
- Product: JobVision | Cando

03 Semantic
- Appearance: Light | Dark

04 Component
- Appearance: Light | Dark
```

This describes the logical Product × Appearance model, not the final Figma collection/mode implementation. That implementation remains a separate open decision.

`Experience` is removed in v4. The former Productive/Expressive distinction was only resolving the root canvas and did not justify a dedicated Color alias layer.

Components consume Semantic Color tokens by default. Component Color tokens remain exceptional and are created only when a stable component-owned contract cannot be expressed by the shared Semantic vocabulary.

Figma Color variable names use slash grouping. Code may flatten `/` to `-` only when implementation mapping is approved. Until then, flattened identifiers in component docs are illustrative/proposed rather than production code-token contracts.

Existing Figma component names that still contain `Productive` are legacy naming references unless that component explicitly documents a separate active design dimension.

---

## Primitive color model

Primitive color scales are context-free and are named by hue rather than product ownership.

```text
color/neutral/*
color/blue/*
color/yellow/*
color/red/*
color/purple/*
color/green/*
color/emerald/*
color/orange/*
color/black-alpha/*
color/white-alpha/*
```

Remove product-owned Primitive families such as:

```text
color/brand/jobvision/*
color/brand/cando/*
```

Current brand color anchors:

```text
JobVision blue  → #0053FF
Cando yellow    → #FFC400
```

The exact 50–950 scale values and the final `green` versus `emerald` inventory remain open.

A Primitive palette may feed multiple independent semantic meanings. Sharing a Primitive value does not merge semantic roles.

```text
blue/*
├─ JobVision Brand
├─ Accent
├─ Link
├─ Info
└─ categorical blue

yellow/*
├─ Cando Brand
├─ Warning
└─ categorical yellow when needed
```

Do not create a second blue or yellow palette only to preserve semantic separation. Create a new Primitive family only when tonal or contrast requirements prove that one scale cannot serve the required roles.

---

## Brand collection

Brand is the optional product-identity alias branch. It resolves Product identity only and is consumed by Semantic roles when Product identity intentionally controls their value.

Current Product values:

```text
JobVision
Cando
```

Variables:

```text
brand/50
brand/100
brand/200
brand/300
brand/400
brand/500
brand/600
brand/700
brand/800
brand/900
brand/950

content/on-brand
```

Mappings:

```text
JobVision brand/* → color/blue/*
Cando brand/*     → color/yellow/*
```

`content/on-brand` is independently resolved because JobVision blue and Cando yellow may require different foreground polarity for contrast.

The v3 Brand names `accent/*` and `content/on-accent` are deprecated in favor of `brand/*` and `content/on-brand`. Accent is now a separate Semantic concept.

Do not put general interaction, selection, feedback, focus, or page-surface roles in Brand. Semantic roles that do not vary by Product identity should resolve directly from Primitive values.

The full 50–950 Brand mirror is retained through the palette pass. After final Semantic aliases are chosen, actual Brand-step consumers should be reviewed before treating every step as a permanently required public API.

---

## Structural surfaces

`canvas` is removed. The root page or workspace uses the same Surface vocabulary as the rest of the interface.

```text
surface/default
surface/muted
surface/inset
surface/raised
surface/inverse
```

Definitions:

- `surface/default`: ordinary base content surface and default page/root surface.
- `surface/muted`: passive lower-emphasis supporting or grouping surface. It has no interaction states.
- `surface/inset`: surface behind `surface/default` in the local hierarchy; appropriate for recessed regions, workspace chrome, or structural backdrops.
- `surface/raised`: surface elevated above its immediate parent, including menus, popovers, dropdowns, floating panels, and dialogs when they behave as elevated panels.
- `surface/inverse`: high-contrast inverted neutral surface.

`surface/raised` is a Color role, not an elevation value. Pair it with the approved elevation or shadow token when depth must be visible.

There is no separate `surface/floating`; floating panels use `surface/raised`.

---

## Neutral interactive surfaces

The v3 `control` and generic `emphasis` names are replaced by an explicit neutral tone × prominence grammar.

```text
surface/neutral-muted
surface/neutral-muted-hover
surface/neutral-muted-active

surface/neutral-emphasis
surface/neutral-emphasis-hover
surface/neutral-emphasis-active
```

Use `neutral-muted` for visible neutral interactive treatments with medium emphasis, such as the Secondary Button.

Use `neutral-emphasis` for high-emphasis neutral operational actions, such as the Primary Button and strong neutral current/exclusive choices when the component anatomy makes selection unambiguous.

Do not confuse structural `surface/muted` with interactive `surface/neutral-muted`.

State suffix remains `active` in v4. A future `active → pressed` rename is not approved.

---

## Transparent interaction states

```text
surface/transparent-hover
surface/transparent-active
surface/transparent-inverse-hover
surface/transparent-inverse-active
```

Use the normal family for transparent-at-rest interactions on ordinary surfaces and the inverse family on `surface/inverse`.

---

## Selected container surfaces

Selection remains a component state, not a general color family.

Global Selected Color semantics are intentionally minimal:

```text
surface/selected
surface/selected-hover
```

`surface/selected` is the neutral persistent-selection background for selected rows, menu/list items, tree nodes, navigation items, and similar containers.

`surface/selected-hover` is only for a selected container that **remains interactive while selected**. It is not a universal selected state and does not imply that every selected component receives Hover. A current Tab that has no meaningful interaction on re-activation does not need a selected Hover state.

Do not add `fg/selected`, `line/selected`, selected emphasis, selected inverse, selected disabled, or selected active families without a repeated use case.

Chromatic selection cues use Accent semantics when appropriate:

```text
Selected line Tab
→ fg/primary + line/accent

Checked Checkbox
→ surface/accent-emphasis + fg/on-color

Saved bookmark
→ fg/accent

Selected row
→ surface/selected + fg/primary

Applied filter / selected tonal chip
→ surface/accent-muted* + appropriate fg/line
```

Strong current/exclusive choices such as Pill Tabs or Segmented Controls may use existing `surface/neutral-emphasis*` treatment when the component anatomy communicates selection clearly.

The component state may be named `selected`, `current`, `checked`, `on`, or `applied`; it does not need a same-named global Color token.

---

## Brand semantic

Brand is intentionally small and rare.

```text
surface/brand
surface/brand-hover
surface/brand-active

fg/on-brand
```

Brand means Product identity or a defined key product/conversion moment. It is not generic emphasis and it is not the default interaction color.

Removed from v3:

```text
surface/brand-muted
fg/brand
line/brand
```

A brand-colored foreground used only for expressive marketing composition should be handled by a reviewed component/pattern treatment if a repeated need emerges rather than by a general `fg/brand` semantic.

---

## Accent semantic

Accent is the general chromatic interaction/affordance color. It is independent from Brand, Danger, Magic, and Support. Selected/current/checked component states may use Accent as a visual cue when chromatic emphasis is appropriate.

```text
surface/accent-muted
surface/accent-muted-hover
surface/accent-muted-active

surface/accent-emphasis
surface/accent-emphasis-hover
surface/accent-emphasis-active

fg/accent
line/accent
```

In the current two-product system, Accent resolves from `color/blue/*` in both JobVision and Cando. It does not need to route through Brand because its value does not currently vary by Product.

### Accent Muted

`surface/accent-muted*` is retained for tonal interactive/actionable emphasis, including:

- Applied Filter Chips
- Selected tonal chips or controls
- Actionable/promotional banners where the user is invited to act

A passive informational/system message uses Support Info instead. Accent Muted and Info may both resolve from Blue primitives, but their semantic purpose is different.

### Accent Emphasis

`surface/accent-emphasis*` is the strong chromatic interaction treatment used by components whose anatomy needs a strong Accent cue, such as checked selection controls.

Do not add `fg/on-accent`; strong Accent surfaces use `fg/on-color`.

Do not add Accent-specific disabled, focus, or inverse families without a real use case.

---

## Magic

Magic is reserved for AI-assisted, AI-generated, or explicitly magical product capability.

```text
surface/magic-muted
surface/magic-emphasis
surface/magic-emphasis-hover
surface/magic-emphasis-active

fg/magic
line/magic
```

The family is shared Semantic because the AI meaning recurs across multiple component anatomies:

```text
surface/magic-muted
→ subtle AI card, AI section, AI chip, or AI container

surface/magic-emphasis*
→ strong interactive AI action or AI entry point

fg/magic
→ AI icon, label, sparkle, or inline AI emphasis

line/magic
→ AI-specific outline or indicator when anatomy needs a line
```

Magic must not replace Brand, Accent, Selected, or Support meaning and must not be used merely as a decorative purple treatment.

---

## Danger

Danger remains separate from Error.

```text
surface/danger-muted
surface/danger-emphasis
surface/danger-emphasis-hover
surface/danger-emphasis-active

fg/danger
line/danger
```

```text
Danger → destructive intent/action
Error  → validation failure or system/problem state
```

`surface/danger-muted` is retained for destructive-intent callouts, destructive confirmation warning regions, or pre-action explanation of irreversible consequences.

Examples:

```text
“This action permanently deletes the job.”
→ Danger

“Saving failed. Try again.”
→ Error
```

Danger is not a fifth standard Notification severity.

---

## Support

Support meanings remain invariant across Product and Appearance values.

```text
surface/info-muted
surface/success-muted
surface/warning-muted
surface/error-muted

fg/info
fg/success
fg/warning
fg/error

line/info
line/success
line/warning
line/error
```

Only muted Support surfaces are approved globally. Do not pre-build strong Support surface matrices without a repeated use case.

Standard system-feedback severities are:

```text
Info
Success
Warning
Error
```

A baseline inline-notification recipe may use:

```text
surface/{severity}-muted
fg/{severity}          # status icon/content
line/{severity}        # only if the anatomy uses a semantic border
fg/primary             # title/main readable content
fg/secondary           # supporting description
```

Colored Support foregrounds on inverse surfaces are retained for inverse Toast patterns:

```text
fg/info-inverse
fg/success-inverse
fg/warning-inverse
fg/error-inverse
```

These roles are intentionally narrow: colored Support content on `surface/inverse`, not a general Support-inverse family.

Canonical inverse Toast composition:

```text
Container   → surface/inverse
Text        → fg/on-inverse
Status icon → fg/{severity}-inverse
Action Link → link/inverse
```

---

## Foreground

General and contextual foreground inventory:

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

Neutral hierarchy:

- `fg/primary`: essential/default readable content, such as titles, main body text, input values, and primary component labels.
- `fg/secondary`: supporting readable content that contributes to understanding, such as supporting descriptions, field labels, company/location context, and ordinary helper text.
- `fg/tertiary`: auxiliary low-priority metadata that may recede during scanning, such as timestamps, passive counts, character counters, and similar metadata. It is not a generic “make it lighter” token.
- `fg/placeholder`: placeholder-like input content.
- `fg/disabled`: unavailable control/content styling. Read-only content is not automatically Disabled.

Removed in v4:

```text
fg/brand
fg/selected
fg/on-color-disabled
```

Disabled filled controls suppress tone and use `surface/disabled + fg/disabled`; therefore a separate colored disabled foreground is not needed.

---

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

Neutral line roles:

```text
line/muted
→ subtle structural separation

line/default
→ normal control/container boundary

line/emphasis
→ stronger neutral interactive boundary

line/disabled
→ disabled control boundary

line/inverse
→ neutral boundary on an inverse surface
```

A Text Input is a canonical stress-test example:

```text
Rest border  → line/default
Hover border → line/emphasis
Focus        → line/emphasis + focus/default ring
Error border → line/error
Disabled     → line/disabled
```

Focus remains a separate layer; `line/emphasis` does not replace `focus/default`.

Selected indicators may use `line/accent`. Keep the source-token family named `line`, not `border`, to avoid collision with implementation utility naming.

Removed in v4:

```text
line/brand
line/selected
```

---

## Disabled

```text
surface/disabled
fg/disabled
line/disabled
```

Disabled suppresses tone by default. Do not create:

```text
brand-disabled
accent-disabled
neutral-disabled
danger-disabled
```

Filled Brand, Primary, Secondary, and Danger Buttons all resolve to the same general disabled treatment.

Disabled has no Hover or Active state.

Read-only remains a component/form-field behavior contract and must not be implemented merely by applying Disabled colors.

---

## Focus

```text
focus/default
focus/inverse
```

Focus remains a dedicated Semantic role rather than an Accent usage. The current `focus/default` value intentionally shares the approved Accent primitives (`blue/600` in Light and `blue/500` in Dark); components must consume `focus/default`, not Accent directly. `focus/inverse` remains a distinct inverse-context role.

Typical composition:

```text
normal surface component → focus/default
inverse surface component → focus/inverse
```

A dual-layer focus treatment for media remains an open pattern-level decision.

---

## Link

Link remains a dedicated navigation semantic family even when it shares the Blue Primitive palette with Accent.

```text
link/default
link/hover

link/subtle
link/subtle-hover

link/inverse
link/inverse-hover
```

Rules:

- `default` is the recognizable chromatic Link and uses the shared Blue interaction palette.
- `subtle` is a neutral lower-prominence Link for contexts where clickability is already clear, such as dense product UI, navigation, card metadata, or “View all” patterns.
- `subtle` should not replace the normal inline Link in body copy unless another persistent affordance such as underline preserves recognition.
- `inverse` adapts Link for `surface/inverse`; one inverse treatment is sufficient in v4.
- Link does not alias `fg/accent` directly. It may resolve to the same Primitive Blue while remaining an independent semantic contract.

Focus uses shared Focus roles:

```text
Default / Subtle Link → focus/default
Inverse Link          → focus/inverse
```

Removed in v4:

```text
link/visited
link/emphasis
link/emphasis-hover
```

Visited state can be introduced later only if a real product pattern such as visited search results requires it.

---

## Utility roles

```text
overlay/default
skeleton/base
skeleton/shimmer
```

`overlay/default` is the modal/sheet/dialog backdrop. It is not a Surface role.

The previous proposals:

```text
highlight/default
highlight/inverse
```

are removed. The original intended use was text highlighting, but no validated shared use case currently justifies a global Highlight Color family. A future text/search highlighting pattern must establish a concrete semantic contract before these roles return.

---

## Button mapping summary

`../components/button.md` is the canonical owner of Button presets, state behavior, and Semantic-token mappings. The table below is only an integration summary showing that the v4 Semantic API can resolve the current Button model without Button-owned Color tokens.

| Preset | Rest | Hover | Active | Foreground |
|---|---|---|---|---|
| Brand | `surface/brand` | `surface/brand-hover` | `surface/brand-active` | `fg/on-brand` |
| Primary | `surface/neutral-emphasis` | `surface/neutral-emphasis-hover` | `surface/neutral-emphasis-active` | `fg/on-color` |
| Secondary | `surface/neutral-muted` | `surface/neutral-muted-hover` | `surface/neutral-muted-active` | `fg/primary` |
| Danger Filled | `surface/danger-emphasis` | `surface/danger-emphasis-hover` | `surface/danger-emphasis-active` | `fg/on-color` |

Tertiary and Ghost remain transparent at rest and use `surface/transparent-hover/active`. Danger Outline and Danger Ghost use `fg/danger` and `line/danger` as appropriate.

Disabled filled Buttons use:

```text
surface/disabled + fg/disabled
```

Internal Button tone:

```text
brand | neutral | danger
```

`brand × strong` is the currently approved Brand combination. Do not generate Brand Subtle, Brand Outline, or Brand Ghost merely to complete a matrix.

Brand Button is reserved for defined product conversions or product-defining entry points. Everyday operational actions remain Neutral Primary even when they are the most important action in the current context.

---

## Component tokens

Component Color tokens remain exceptional. The approved categorical Tag family continues to live in the Component collection and must not be reused by unrelated components as a generic categorical palette.

Current retained structure:

```text
tag/surface/{neutral|blue|purple|green|orange}
tag/surface/{variant}-hover
tag/fg/{variant}
tag/line/{variant}
```

The family remains approved for now, but its exact five variants and full Hover/Line matrix must be revalidated during the Tag component review rather than treated as permanently required by convention.

Applied Filter Chip should first use shared Semantic roles such as `surface/accent-muted*`. If a stable component-specific applied treatment cannot be expressed by those roles, introduce a reviewed `filter-chip/*` Component contract rather than consuming Tag tokens directly.

---

## Architecture stress-test evidence

The current Semantic-first model has been checked against high-information component patterns without requiring new Semantic Color roles.

### Text Input

```text
Value       → fg/primary
Label       → fg/secondary
Placeholder → fg/placeholder
Helper      → fg/secondary
Counter     → fg/tertiary
Rest line   → line/default
Hover line  → line/emphasis
Focus       → line/emphasis + focus/default
Error       → line/error + fg/error
Disabled    → surface/disabled + line/disabled + fg/disabled
```

Read-only remains a component behavior decision and does not currently justify `read-only/*` Color tokens.

### Selection

```text
Line Tab           → fg/primary + line/accent
Checked Checkbox   → surface/accent-emphasis + fg/on-color
Applied Filter     → surface/accent-muted*
Selected Row       → surface/selected + fg/primary
Strong Pill choice → surface/neutral-emphasis + fg/on-color
```

A selected Tab does not receive a selected Hover state when the selected item is not meaningfully interactive.

### Notifications

```text
Inline feedback
→ surface/{severity}-muted + fg/{severity} + optional line/{severity}

Inverse Toast
→ surface/inverse + fg/on-inverse + fg/{severity}-inverse

Destructive warning callout
→ surface/danger-muted + Danger roles
```

These stress tests validate the existing Semantic Color vocabulary; they do not replace component-specific behavior/anatomy documentation.

---

## v3 → v4 migration summary

```text
Remove Experience Color collection
Remove canvas

surface/control*           → surface/neutral-muted*
surface/emphasis*          → surface/neutral-emphasis*

surface/brand-emphasis*    → surface/brand*
remove surface/brand-muted
remove fg/brand
remove line/brand

add surface/accent-muted*
add surface/accent-emphasis*
add fg/accent
add line/accent

replace full selected family with:
surface/selected
surface/selected-hover

remove fg/selected
remove line/selected
remove fg/on-color-disabled

link/emphasis* → link/subtle*
remove link/visited

remove highlight/default
remove highlight/inverse

Button Accent preset/tone → Brand preset/tone

Brand collection accent/* → brand/*
Brand content/on-accent    → content/on-brand

product-specific Primitive brand palettes → generic hue palettes
```

---

## Open decisions

The following are intentionally not blockers for the v4 Semantic Color architecture:

1. Final opaque Primitive scale values, including Blue and Yellow ramps
2. Final `green` versus `emerald` Primitive inventory
3. Exact Light/Dark alias steps and contrast validation
4. Consumer review of the full Brand 50–950 mirror after final aliases are known
5. Final Tag variant/state matrix during Tag component review
6. Final Figma Product × Appearance mode implementation
7. CSS variable strategy
8. Tailwind implementation mapping
9. Dual-layer focus treatment for media
10. Non-color foundation architectures for Typography, Spacing, Radius, Elevation, and Motion

Do not infer or ship unresolved opaque values from this document. The alias graph in `color-token-aliases.md` records value-resolution status separately from this Semantic catalog.
