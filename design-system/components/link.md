---
id: design-system.component.link
collection: design-system
type: component
title: Link
summary: Links navigate users to another destination through a standalone component with three sizes and an inline native-text recipe.
knowledge_state: verified
document_maturity: draft
related: []
design_status: ready-for-dev
design_maturity: handoff-ready
last_reviewed: '2026-09-19'
---

# Link

## Purpose

Links navigate users to another destination.

Use native anchor semantics when activation changes the current destination. Use Button when the control changes state, submits data, confirms a decision, or otherwise performs work in the current context.

## Authoring Model

v4 separates two authoring cases.

### Standalone Link

Use the canonical Figma component when the Link is a standalone or contextual control.

Component set: `Link / Default`

Standalone Link exposes Style and Size authoring choices. Interaction states are documented in the Figma set, but runtime hover, active, and focus behavior should normally be implemented through CSS/platform states rather than application props.

### Inline Link

When a Link appears inside running text, do **not** insert the atomic Link component into the sentence.

Use a native Text layer and style only the Link range with:

- the appropriate `link/*` semantic color;
- a persistent underline;
- the typography inherited from the surrounding text.

This keeps inline Links naturally multiline and avoids forcing the standalone Size model onto running copy.

## Canonical Figma API

Canonical file: `[DS] Job Vision NEXT`

- Figma file key: `rROD8ctH9UfPGAMrRrOzHe`
- Component set: `Link / Default`
- Figma node ID: `22920:125581`
- Figma component key: `f31eac5461a0d8a608089f696b3b1402590be8a9`
- Variant count: `27`
- Matrix: `3 Style × 3 Size × 3 Figma State`
- Default variant: `Style=Default, Size=Medium, State=Enabled`

### Variant properties

| Property | Values |
|---|---|
| `Style` | `Default`, `Subtle`, `Inverse` |
| `Size` | `Small`, `Medium`, `Large` |
| `State` | `Enabled`, `Hover`, `Focus` |

`Active` is intentionally not a separate Figma variant because its approved visual treatment is identical to Hover. Runtime Active must use the same foreground token and underline treatment as Hover.

### Content properties

| Property | Behavior |
|---|---|
| `Link text` | Visible destination label |
| `End icon` | Optional boolean |
| `Swap end icon` | Instance swap |

The canonical component intentionally has **no** Underline, Start icon, Visited, Disabled, Bold, or legacy Inline axis/property.

The pre-v4 component is retained in Figma as `Link / Legacy` only for migration compatibility and must not be used for new designs.

## Sizes, Typography, and Anatomy

| Size | Typography |
|---|---|
| Small | Body / Compact / XS — 12/16, Regular 400 |
| Medium | Body / Compact / SM — 14/20, Regular 400 |
| Large | Body / Compact / MD — 16/24, Regular 400 |

Medium is the default standalone size.

Why Size remains in the Figma component:

- standalone Links are used in more than one text scale across product surfaces;
- an atomic Figma component cannot cleanly inherit arbitrary surrounding typography from its consumer;
- the three approved sizes preserve consistent text styles without detaching the component;
- inline Links still inherit surrounding typography and therefore do not use this Size axis.

Shared anatomy:

- component background is transparent in every Style, Size, and State;
- the internal label wrapper also has no fill or stroke;
- width hugs content by default;
- text weight is Regular `400`;
- one optional End icon is supported;
- icon size is fixed at `18px` at every Link size;
- icon-label gap is `8px`;
- no Start icon is exposed;
- do not add background, border, or container styling to create another Link treatment.

## Style Selection

### Default

Default is the recognizable chromatic Link treatment.

```text
Enabled / Focus → link/default
Hover / Active → link/hover
```

Use it when the destination should remain clearly recognizable as a Link.

### Subtle

Subtle is the lower-prominence neutral Link treatment.

```text
Enabled / Focus → link/subtle
Hover / Active → link/subtle-hover
```

Use when surrounding context already communicates navigation, for example:

- dense ATS/product UI;
- navigation;
- card metadata;
- breadcrumb-like destinations;
- contextual “View all” or “Learn more” links.

Do not use Subtle as an unadorned inline body-copy Link.

### Inverse

Use Inverse only on `surface/inverse` or another reviewed inverse surface.

```text
Enabled / Focus → link/inverse
Hover / Active → link/inverse-hover
```

Focus composes with the shared inverse Focus treatment.

## State Behavior

Standalone Link behavior:

| Runtime state | Foreground | Underline | Focus treatment | Figma representation |
|---|---|---|---|---|
| Enabled | style rest token | No | No | `Enabled` |
| Hover | style hover token | Yes | No | `Hover` |
| Active | style hover token | Yes | No | same visual as `Hover`; no separate variant |
| Focus | style rest token | Yes | shared focus recipe | `Focus` |

Default and Subtle use the shared default Focus recipe. Inverse uses the shared inverse Focus recipe.

There is no Link-specific Active color token; Active deliberately reuses the relevant Hover semantic token.

### Figma underline implementation

Figma normalizes native Text decoration across component variants, so the canonical component uses a **Figma-only responsive 1px underline helper** inside the label wrapper:

- opacity `0` in Enabled;
- opacity `1` in Hover and Focus;
- width follows the current Link text automatically;
- the helper does not change the component's approved line-height.

Active is not represented separately; its runtime visual equals Hover.

This helper is a design-authoring implementation detail.

### Runtime underline implementation

Runtime code should use real text decoration:

```text
Enabled → no text-decoration
Hover / Active / Focus → underline
```

Do not reproduce the Figma helper rectangle in application code.

Inline Links remain persistently underlined in all states.

## Icons

The standalone component supports only an optional End icon.

Use an End icon when it adds destination or navigation meaning.

Examples:

- external destination → `launch`;
- a reviewed destination/directional cue where an icon materially improves comprehension.

Rules:

- no Start icon;
- no icon for ordinary inline sentence Links;
- the icon is normally decorative when the visible label already communicates the destination;
- the icon uses the same semantic foreground color as the Link text;
- icon size is `18px`;
- icon-label gap is `8px`;
- the component itself and label wrapper stay transparent when an icon is present.

The external-link icon does not define whether the browser opens a new tab.

## Inline and Multiline Links

Inline Links are authored as native Text ranges in Figma.

Recipe:

1. use the surrounding Text style;
2. select the Link range;
3. apply the appropriate `link/*` semantic color;
4. apply persistent underline;
5. preserve normal wrapping.

Runtime anchors may wrap naturally in constrained layouts. Do not force `white-space: nowrap` globally on Links.

For a long standalone Link that must wrap in a design mockup, use the same native-Text recipe rather than detaching the atomic component or introducing a Width variant.

## Link vs Button

Use Link when activation navigates to another page, route, document, anchor, email, phone target, or external resource.

Use Button when activation changes state, mutates data, confirms/cancels an operation, or otherwise performs work in the current context.

A navigation element may use a reviewed Button visual treatment while remaining an anchor semantically. Do not create a parallel `link-button/*` token family.

## Deliberate Exclusions

### Underline property

There is no author-facing Underline toggle.

- standalone underline behavior is state-driven;
- inline underline is persistent by definition.

### Start icon

Not part of the current Link contract. Destination cues belong in the optional End slot.

### Active Figma variant

Active remains part of the runtime interaction contract but does not need a duplicate Figma variant because it is visually identical to Hover.

### Disabled

Disabled is not part of the Link API. If a destination is unavailable, reconsider whether it should be rendered as an interactive Link at all.

### Visited

Visited is not part of shared v4 because no reviewed product pattern currently requires persistent visited styling.

### Bold

Bold is not a Link hierarchy axis. Use surrounding typography hierarchy and semantic Link roles instead.

## RTL

Do not create separate RTL variants.

The single optional icon represents the logical destination/end cue. Runtime layout should place it at the logical End according to direction.

In the current RTL product authoring context, the End icon appears to the left of the Persian label.

Directional glyphs must follow the icon-system RTL behavior rather than being manually duplicated inside Link.

## Accessibility and Interaction Contract

- Prefer native `<a href="…">` semantics for navigation.
- Every Link requires an accessible name; normally this is its visible label.
- Preserve expected browser Link behavior.
- Keyboard focus must follow the shared Focus contract and remain visibly distinct.
- Inline body-copy Links use persistent underline.
- Standalone Links have no underline at rest and add underline on Hover, Active, and Focus.
- Link foreground must meet applicable text contrast against its background.
- Do not expose Disabled as a Link state.
- End icons are decorative when the visible label already communicates the destination.
- Standalone targets must follow the shared target-size/spacing contract; the inline-text exception applies only to genuine running-text Links.

## Development Contract

Expected conceptual API:

```text
Link
- style: default | subtle | inverse
- size: sm | md | lg
- endIcon?: icon
- href / destination
- children / label
```

Implementation requirements:

- native anchor semantics for navigation;
- Small = 12/16, Medium = 14/20, Large = 16/24;
- weight 400 at every standalone size;
- icon size: 18px;
- icon-label gap: 8px;
- transparent background;
- optional End icon only;
- default style: Default;
- default size: Medium;
- Enabled has no underline;
- Hover and Active use the Style hover token and underline;
- Focus keeps the Style rest foreground, adds underline, and composes the shared Focus treatment;
- no public `underline`, `startIcon`, `visited`, `disabled`, or `bold` Link variants;
- runtime Links may wrap naturally;
- interaction pseudo-states should normally be CSS/platform behavior, not public application props;
- do not duplicate Link semantic tokens as component-local colors.

The exact framework/class architecture and exact runtime prop names remain unverified until the owning runtime Design System source is registered.

## QA Checklist

Verify:

- exactly 27 Figma variants: 3 Style × 3 Size × 3 Figma State;
- variant axes are `Style / Size / State`;
- default is `Default / Medium / Enabled`;
- Figma States are `Enabled / Hover / Focus`;
- Active runtime visual matches Hover and is not reintroduced as a duplicate Figma variant;
- content properties are only `Link text / End icon / Swap end icon`;
- Small / Medium / Large use 12/16, 14/20, and 16/24 Regular typography;
- component and Label wrapper have no background fill or stroke;
- End icon is 18px with an 8px gap at every size;
- Enabled underline helper opacity is 0;
- Hover and Focus underline helper opacity is 1;
- underline width follows Link text overrides;
- Focus uses the correct default/inverse treatment;
- all semantic Link color bindings resolve correctly;
- no Underline, Start icon, Visited, Disabled, Bold, or legacy Inline axes are reintroduced;
- inline body-copy Links use native Text with persistent underline;
- inline/multiline authoring preserves wrapping;
- runtime anchors can wrap naturally;
- keyboard focus is visible.

## Legacy Migration

Figma retains `Link / Legacy` only for migration.

```text
Inline=True
→ native Text + link token + persistent underline

Small / Medium / Large
→ map to the equivalent canonical Size

Active
→ runtime Hover visual treatment; no separate Figma variant

Bold=True
→ remove; use surrounding typography hierarchy

Visited
→ remove unless a future reviewed pattern explicitly requires it

Disabled
→ remove and revisit the availability/UX model

Icon
→ optional End icon
```

Do not create new instances of `Link / Legacy`.

## Open Items

Runtime implementation remains unverified until the owning Design System repository/package and Storybook source are registered.

Still requiring runtime verification:

- exact runtime component/API identifier;
- exact Angular/Tailwind authoring pattern;
- Storybook stable story/docs identifier;
- exact Figma-property → code-prop mapping;
- Code Connect or equivalent mapping mechanism.

## Live References

- Figma file: `[DS] Job Vision NEXT`
- Figma component set: `Link / Default`
- Figma node ID: `22920:125581`
- Figma component key: `f31eac5461a0d8a608089f696b3b1402590be8a9`
- Figma default: `Style=Default, Size=Medium, State=Enabled`
- Figma Playground: Default, Hover/underline, End icon, External, Subtle, Focus, Inverse, and native Text inline/multiline examples
- Storybook / Code: not yet connected as a canonical live reference

## Related Documents

- `button.md`
- `../../accessibility/focus-management.md`
- `../../accessibility/pointer-touch-and-gestures.md`
- `../../accessibility/color-and-contrast.md`
- `../../foundations/interaction/navigation.md`
- `../../integrations/component-mapping.md`
- `../tokens/semantic-tokens.md`
