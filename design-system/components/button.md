---
id: button
collection: design-system
type: component
title: Button
summary: Buttons trigger actions through a constrained hierarchy of Brand, operational, low-emphasis, and destructive styles.
knowledge_state: verified
document_maturity: draft
related:
  - design-system.experience-rule.action-hierarchy
  - design-system.token.semantic-tokens
  - design-system.product-variation.brand-variants
design_status: ready-for-dev
design_maturity: handoff-ready
---

# Button

## Purpose

Buttons trigger actions. Designers choose from the approved Button styles rather than creating ad-hoc visual treatments.

Use Button when an action changes state, submits data, confirms a decision, opens an operation, or otherwise performs work in the current context.

Use Link when the primary behavior is navigation. Use dedicated controls for selection and specialized interactions such as Tab, Segmented Control, Toggle, Filter Chip, or Icon Button.

## Canonical Figma API

Component set: `Button / Default`

### Properties

| Property | Values / behavior |
|---|---|
| `Style` | `Brand`, `Primary`, `Secondary`, `Tertiary`, `Ghost`, `Danger Primary`, `Danger Tertiary`, `Danger Ghost` |
| `Size` | `Extra Small`, `Small`, `Medium`, `Large` |
| `State` | `Enabled`, `Hover`, `Active`, `Focus`, `Disabled` |
| `Loading` | `False`, `True`; independent from interaction `State` |
| `Button text` | Required visible action label |
| `Start Icon` | Optional boolean |
| `End Icon` | Optional boolean |
| `Swap Start Icon` | Instance swap |
| `Swap End Icon` | Instance swap |

Button always has a visible text label when not loading. Icon-only actions use Icon Button.

## Sizes and Anatomy

| Size | Height | Horizontal padding | Label typography |
|---|---:|---:|---|
| Extra Small | 28 px | 8 px | 12/16, weight 500 |
| Small | 32 px | 12 px | 14/20, weight 500 |
| Medium | 40 px | 16 px | 14/20, weight 500 |
| Large | 48 px | 20 px | 14/20, weight 500 |

Shared anatomy rules:

- Border radius: `6px`.
- Width: hug contents by default.
- Label must remain on one line; implementation must use `white-space: nowrap` / `whitespace-nowrap` or the framework equivalent.
- Start and End icons are optional.
- Button icon size is `18px` across all Button sizes.
- Gap between icon and label is `8px`.
- Button text weight is `500`.
- Button height is fixed by `Size`; content is vertically centered.
- Do not change width, padding, or label layout between interaction states.

## Style Selection

| Need | Style |
|---|---|
| Approved product conversion or product-defining entry point | Brand |
| Main operational action | Primary |
| Supporting medium-emphasis action | Secondary |
| General utility, filter, dropdown, toolbar, or control-like action | Tertiary |
| Back, Cancel, Later, or another intentionally low-emphasis action | Ghost |
| Final destructive confirmation | Danger Primary |
| Visible independent destructive action | Danger Tertiary |
| Low-emphasis or inline destructive action | Danger Ghost |

### Brand

Brand is reserved for approved conversion/product moments such as resume submission, sign-up, purchase/upgrade, request-demo, or a major entry into the product's core value.

Being the most important action on a page does not automatically make an action Brand. Everyday operational actions such as Save changes are normally Primary.

Use at most one Brand action in the same action group. Brand and Primary should not compete as equal CTAs in one group.

### Primary

Use for the most important operational action in the current decision region, such as Save, Continue, Confirm, Submit, or Send for approval.

A decision region normally has one strongest operational action.

### Secondary

Use for a supporting action that should remain visible with medium emphasis. Secondary does not mean “the second button.”

Use Tertiary for control-like actions and Ghost for exits such as Back or Cancel.

### Tertiary

Use for filters, sorting, dropdown triggers, export, settings, editing, toolbar actions, and similar independent utilities.

Tertiary is the normal outline treatment for dense operational interfaces such as ATS.

### Ghost

Use for Back, Cancel, Not now, third-or-later actions, and other intentionally low-emphasis operations.

If Ghost still feels too prominent, reconsider placement, copy, or whether the control should be a Link rather than creating another weaker Button style.

### Danger

Use Danger only for destructive intent, not merely negative wording.

- Final destructive confirmation → Danger Primary
- Visible independent destructive action → Danger Tertiary
- Low-emphasis destructive entry point or inline action → Danger Ghost

A reversible rejection or negative choice is not automatically destructive.

## Behavior and States

### Loading

Loading is independent from interaction `State` in the Figma API and should map to a boolean such as `loading` in code.

When `Loading=True`:

- Directly use `Progress Circle / Mode=Indeterminate / Size=Small / State=Active` (`16×16`). Track uses `line/default`, arc uses `line/accent`; see the [Loading pattern](../patterns/loading-and-progress.md). No separate Loading component is required.
- Preserve the Button's exact width and height.
- Preserve the label and icon layout space while visually hiding their content, so entering Loading never causes layout shift.
- Center Progress Circle relative to the current Button width. It must remain centered when the label changes or Start/End icons are toggled.
- Prevent repeated activation/submission while the operation is in progress.
- Preserve focus when possible; Loading must not unexpectedly move keyboard focus.
- Expose the busy state to assistive technology, e.g. `aria-busy="true"` where appropriate.
- Use the shared neutral `surface/disabled` background and suppress the original Style border/tone while busy. The blue active ring distinguishes ongoing work from an unavailable Disabled action. Keep focus treatment and busy semantics; Loading does not mean the operation was never available. The busy visual takes precedence in authored Loading + Disabled combinations.
- Do not animate Button width or layout when entering or leaving Loading.
- In Focus + Loading variants, hide the redundant internal Background rectangle: the Button root already owns the neutral busy surface. Preserve existing focus-ring effects; the internal backdrop must not cover the spinner.

Framework-specific implementation may use `disabled`, `aria-disabled`, event suppression, or a combination, but must satisfy the behavior above. Prefer an approach that does not unexpectedly remove keyboard focus from the triggering Button.

Flow-level rules decide whether competing actions are also disabled; that policy does not belong to Button alone.

### Disabled

Disabled suppresses the original tone. Do not preserve Brand or Danger chroma merely to show what the enabled action would have been.

All disabled Button styles use the shared `fg/disabled` foreground role. Filled disabled Buttons additionally use `surface/disabled`; outline disabled Buttons additionally use `line/disabled`.

```text
Filled disabled
→ surface/disabled + fg/disabled

Outline disabled
→ transparent + fg/disabled + line/disabled

Ghost / transparent disabled
→ transparent + fg/disabled
```

Disabled does not replace validation or error guidance. The reason an action is unavailable should be understandable from surrounding context when that reason matters to task completion.

### Hover / Active

- Hover and Active must use the corresponding semantic token state for the selected Style.
- Do not implement these states through opacity changes that reduce contrast unpredictably.
- State transitions must not affect dimensions or layout.

### Focus

- Focus treatment is independent from Button tone.
- Use the shared Focus contract; Brand or Danger color alone is not a sufficient focus indication.
- Keyboard focus must remain visibly distinguishable from Hover and Active.
- Do not remove the native focus behavior without replacing it with the approved focus treatment.

## Motion / Transition Contract

Use the shared motion/transition tokens when available. Button does not define a component-specific duration or easing.

Allowed transition targets are visual state properties such as background, foreground, border, and focus treatment. Do not transition width, height, padding, gap, or other layout-affecting properties.

Loading activity may animate through Progress Circle / Indeterminate, while the Button container remains dimensionally stable.

## Composition and Content

- Prefer one strongest action per action group.
- Do not use Brand merely to create visual emphasis.
- Avoid repeating high-emphasis Buttons across every row/card in dense interfaces.
- Use concise action labels that describe the result of activation.
- Keep labels on one line; do not allow wrapping inside Button.
- If an action navigates rather than performs an operation, use Link semantics even when its visual treatment resembles a Button.

Cross-component action hierarchy belongs in `../../foundations/interaction/action-hierarchy.md`.

## Semantic Mapping

The component consumes shared Semantic color roles; it does not introduce Button-specific color tokens.

| Style | Semantic treatment |
|---|---|
| Brand | `surface/brand` + `fg/on-brand` |
| Primary | `surface/neutral-emphasis` + on-color foreground |
| Secondary | `surface/neutral-muted` + normal foreground |
| Tertiary | transparent + normal border + normal foreground |
| Ghost | transparent + normal foreground |
| Danger Primary | danger emphasis surface + on-color foreground |
| Danger Tertiary | transparent + danger border + `fg/danger` |
| Danger Ghost | transparent + `fg/danger` |

Hover and Active states resolve through the corresponding Semantic family. Do not duplicate the complete token state matrix here when it can be resolved from the token system/live implementation.

`surface/muted` is a passive structural surface and must not be used as the Secondary Button background.

## Product Variation

Brand uses the active product Brand mapping. Brand meaning remains the same across products.

Everyday Cando operational actions remain Neutral even when Brand usage is rare. General chromatic interaction is Accent semantics, not another Button tone.

## Accessibility and Interaction Contract

- Prefer a native `<button>` element for Button behavior.
- Preserve native keyboard activation: `Enter` and `Space` must activate a focused Button according to platform semantics.
- Every Button requires an accessible name; for standard Button this is normally the visible label.
- Visible focus must follow the shared Focus contract.
- Disabled and Loading have distinct meanings. Loading can share the neutral Disabled background, but keeps the visible blue activity ring, operation name and busy semantics.
- Prevent duplicate activation while Loading.
- Loading should preserve focus when possible and expose busy state semantically.
- Start/End icons are decorative when the visible label already communicates the action; avoid duplicate accessible names from decorative icons.
- Button label must not wrap.
- Do not use color alone to communicate destructive state or focus.

## Development Contract

The code component should expose semantic inputs equivalent to the Figma API, but it does not need to model interaction pseudo-states as application props.

Expected conceptual API:

```text
Button
- style: brand | primary | secondary | tertiary | ghost | danger-primary | danger-tertiary | danger-ghost
- size: xs | sm | md | lg
- loading: boolean
- disabled: boolean
- startIcon?: icon
- endIcon?: icon
- children / label
```

`hover`, `active`, and `focus` are interaction states and should normally be implemented through platform/CSS state mechanisms rather than public component props.

Implementation requirements:

- label: `white-space: nowrap` / `whitespace-nowrap`;
- fixed height per size: 28 / 32 / 40 / 48 px;
- horizontal padding per size: 8 / 12 / 16 / 20 px for XS / S / M / L;
- label typography: XS = 12/16; S / M / L = 14/20; weight 500;
- radius: 6 px;
- icon size: 18 px;
- icon-label gap: 8 px;
- no layout-changing transitions;
- loading spinner: direct Progress Circle / Indeterminate / Small, 16 px, with contextual foreground and neutral track;
- no width jump during Loading;
- suppress repeated activation while Loading;
- preserve keyboard/focus behavior and visible focus treatment.

### Class architecture — Open with Frontend

The exact CSS/Tailwind class architecture is intentionally not locked by design. Candidate decomposition discussed so far is approximately:

```text
btn
btn-[size]
btn-[style]
```

Before implementation, align with frontend on whether this remains separate composable classes, becomes a variant utility/CVA-style API, or follows the existing Angular/Tailwind component convention. The semantic API and behavior contract above are fixed; the class-authoring strategy is not.

## Figma Spacing binding QA — 2026-10-20

The canonical Button / Default component set (node `1854:1776`) still has the existing 320 variants. A source-only Figma audit identified 808 correct but unbound effective layout properties. They were rebound **in place** to the existing Spacing variables, without changing values, variant dimensions, component identities or API.

- **244** new content `paddingLeft` bindings and **244** new content `paddingRight` bindings.
- **320** new content `itemSpacing` bindings, for the real 8px icon–label gap.
- **152** effective bindings were already present, giving **960/960** correct bound non-zero effective `Button content` spacing properties.
- All four sizes retain documented 28/32/40/48px heights and 8/12/16/20px horizontal padding.
- The 320 Variant source text styles and Radius bindings were unchanged; all were already governed.

Each variant additionally contains one `Start Icon` and one `End Icon` frame, each with only one direct child. Those **640** raw `itemSpacing=8px` values are **inactive** because no sibling spacing can be produced within a single-child frame. They are not a layout-token failure, were left unchanged, and are exempted by the scoped source audit. If the icon wrapper anatomy gains multiple children, review its gap.

**Remaining:** Legacy `Transparent/Transparent` Paint Style remains in some Button Focus visuals; it uses blending behavior and was not indiscriminately replaced. Product × Appearance visual regression, published instance overrides, keyboard focus and Angular/Storybook QA still require separate verification.

Detailed evidence: Button Spacing Migration Audit. No new tokens were added.
## QA Checklist

For each Style and Size, verify:

- Enabled, Hover, Active, Focus, Disabled render with the intended tokens.
- Height, horizontal padding, and label typography match the size contract.
- Label never wraps.
- Start and End icons remain 18 px and preserve the 8 px label gap.
- Keyboard focus is visible.
- Disabled does not trigger the action.
- Loading prevents repeated activation.
- Switching Loading on/off does not change width or height, including with custom labels and Start/End icon combinations.
- Progress Circle / Indeterminate / Small remains centered at every Button width.
- No interaction state causes layout shift.

## Open Items

Still open and requiring frontend coordination:

- exact class / variant authoring architecture in Angular + Tailwind;
- exact shared motion token to use for Button state transitions if one is not already established;
- Storybook / code canonical reference and eventual Code Connect mapping.

These are implementation-system decisions; the Button visual and behavioral contract is otherwise complete.

## Live References

- Figma component set: `Button / Default` in `[DS] Job Vision NEXT`.
- Figma properties: `Style`, `Size`, `State`, `Loading`, `Button text`, Start/End Icon, Start/End Icon swap.
- Loading dependency: direct `Progress Circle / Mode=Indeterminate / Size=Small / State=Active`, with `line/default` track and `line/accent` arc on a neutral `surface/disabled` busy background; see the [Loading pattern](../patterns/loading-and-progress.md) and [Progress Circle](progress-circle.md).
- Storybook / Code: not yet connected as a canonical live reference.

## Related

- `../../foundations/interaction/action-hierarchy.md`
- `../../foundations/interaction/navigation.md`
- `../../foundations/interaction/selection.md`
- `../patterns/multi-step-flow.md`
- `../patterns/confirmation.md`
- `../patterns/destructive-actions.md`
- [Brand Variants](../../product-expression/brands/brand-variants.md)
- `../tokens/color/semantics.md`
