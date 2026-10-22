---
id: design-system.component.tag
collection: design-system
type: component
title: Tag
summary: TBD Tag component anatomy and behavior; approved categorical Tag Color tokens exist separately from this unverified component scaffold.
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.token.component-tokens
  - design-system.component.chip
  - design-system.component.badge
---

# Tag

> **Design contract proposed for HOS-33 owner review.** The Figma construction below was inspected live on 2026-10-22, including a targeted component-property repair and an independent color-contrast check. This document remains `unverified / scaffold` until the Design System owner approves the proposed contract, required validations are complete, and the generated knowledge registry is updated. A component existing in Figma does not establish library publication or runtime availability.

## Purpose

Tag is a **passive, short, descriptive/categorical label** attached to content. It conveys a category, attribute, or compact metadata value without inviting action. Its nine hues identify categories, not feedback severity. The categorical color vocabulary is owned by [Component Color Tokens](../tokens/color/component-tokens.md).

## When to Use

- Describe an attribute of an entity, such as `دورکاری`, `تهران`, or `ارشد`, without changing that value.
- Group or categorize content with a concise label where that categorization is meaningful.
- Present multiple independent category labels in a wrapping collection.

## When Not to Use

- To select, filter, add, remove, open or edit a value: use the appropriate [Chip](chip.md) interaction family.
- To signal an operation's Success/Warning/Error state: use the owning feedback/status contract; a green, yellow or red Tag hue must **not** stand in for system status.
- To display counts or unrelated compact indicators under an assumed Badge API: [Badge](badge.md) remains a separate, unverified decision.
- For standalone navigation, action or icon-only content.

## Anatomy

Proposed visual anatomy:

1. A borderless, fully rounded categorical surface.
2. A **required, visible, single-line Label**.
3. An **optional decorative leading Icon**, controlled by an independent Boolean and instance-swap property.

The icon is optional, not a separate `Type` or `State` axis. It does not turn Tag into an action, dismissal control or status indicator. In RTL, logical leading is visually to the right; the equivalent LTR placement is visually to the left.

## Variants and Figma Property Model

The inspected Figma component set contains **27 variants = 3 Size × 9 Color**.

| Figma property | Current design model |
|---|---|
| `Size` | `Extra Small / Small / Medium` |
| `Color` | `Neutral / Blue / Teal / Green / Yellow / Orange / Red / Magenta / Purple` |
| `Label` | Required text property |
| `Show icon` | Optional Boolean, default `false` |
| `Icon` | Instance swap, default `Icon/work`; used only if `Show icon=true` |

**No interaction states:** Hover, Active, Focus, Selected, Disabled, Skeleton and removable/actionable behavior do not exist for Tag. Do not infer runtime prop names from Figma property names.

## Sizes and Visual Tokens

| Size | Height | Block padding | Inline padding | Leading icon size |
|---|---:|---:|---:|---:|
| Extra Small | 20 px | 2 px | 6 px | 12 px |
| Small | 24 px | 4 px | 8 px | 16 px |
| Medium | 28 px | 6 px | 12 px | 16 px |

The current construction uses token-bound Spacing and `Radius/Full`, a 4 px text/icon gap, and `Label/XS` typography (Vazirmatn Medium, 12 px size, 16 px line-height) at **all three sizes**. Tag itself hugs its content and has no width variant. A default **180 px max-inline-size**, a 32 px minimum width and text truncation are present in the live masters. A consuming context may set a more appropriate width limit; it must preserve the single-line label and accessible full meaning.

**Line treatment:** Tag is borderless in the currently reviewed Figma design. The approved `tag/{color}/line` token remains in the token contract but is not consumed by the present Tag visual. Do not invent a visible border to use a token.

## Categorical Color

Supported colors are exactly the nine values above. Tag consumes its private `tag/{color}/surface` and `tag/{color}/fg` token roles. The existing Color architecture additionally defines `line` and `surface-hover` roles; neither grants Tag a border or interactive hover behavior. The hover role may remain for historical/token compatibility, but passive Tag must not consume it.

- Shared category meanings do not map to Product Brand/Themes, Success, Warning or Error.
- Categorical roles resolve independently for Light and Dark appearance.
- The component-token family is internal to Tag implementation; do not expose its tokens as generic Product Semantic utilities.

**2026-10-22 design-side contrast audit:** All 9 foreground/surface pairs were resolved from the live Figma variable aliases in both Light and Dark. Minimum observed WCAG text contrast: **5.30:1 in Light** (Yellow), **7.45:1 in Dark** (Orange), meeting the 4.5:1 text target in these modes. This is not an executed runtime accessibility test.

## Content and Overflow

- Keep category labels short and factual, not verbs, instructions or CTAs.
- A text label is mandatory even when the optional icon is visible; Tag does not support an icon-only variant.
- Render as a single line. Do not wrap inside one Tag; constrain the label area and use an **ellipsis at logical end** when the full label exceeds the available inline size.
- Do not rely on truncated visual text as the only place the full category can be understood; consuming experiences should make the unabridged value available through an appropriate accessible source/context.
- Several Tags may wrap at the **parent-group level**. The current Figma group example uses an 8 px spacing gap between independent Tags. Do not turn Tag into a Group variant.

## Behavior and RTL

Tag has no click, selection, dismissal, focus, keyboard action, popup or disabled state. It must not take part in the tab order merely because it is shaped like a compact control.

Its label and optional icon follow the surrounding writing direction and **logical** inline Start/End. Preserve Persian and mixed-direction text, natural reading order, and end-of-line truncation according to the resolved direction. Group wrapping belongs to the parent.

## Accessibility

Tag is a **non-interactive text-bearing descriptor**, not a button or input. The visible label is part of the consuming content's accessible information. A decorative icon repeats visual context and must not create a redundant spoken label. If category/color has important meaning, communicate it in text or programmatic context; color alone is insufficient.

The current design's 4.5:1 color target is supported by the Light/Dark variable audit. The consuming flow still needs manual screen-reader verification of meaningful full labels, RTL/mixed-script overflow, and contrast after composition or unusual overlays. No implementation DOM, ARIA strategy, runtime tests or keyboard behavior is asserted from Figma.

## Figma Reference

- **Live canonical component set:** [Tag](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23493-586) — node `23493:586`, key `d1acda5183dc106f7ee6da0169545a71489439af`.
- **Presentation / test examples:** [Tag / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23493-587) — node `23493:587`; Size, Color Light/Dark, RTL, truncation and parent wrapping.
- **Legacy reference only:** `.Legacy / Tag / Interactive and removable` — node `2845:38409`; `.Legacy / Tag / Close action` — node `3699:49526`. Do not use these as the new public Tag.
- **QA 2026-10-22:** Inspected all 27 variant color token bindings, shared Label/XS text style, spacing/radius variables, sizes, max width, single-line text, and Light/Dark contrast. Reconnected the previously nonfunctional `Icon` instance-swap property across all 27 variants; a temporary instance successfully swapped from `Icon/work` to `Icon/zoom_in`.
- **Publication status:** A library search returned the older legacy Tag asset, not the above canonical key; publication of the new set and downstream consumer smoke test remain **unverified**. A component key alone is not publication evidence.

## Code Reference

No owning runtime package, Code Connect mapping, Storybook story or implementation tests are registered for this component. Do not infer an exact DOM structure, public API, shipped CSS, or Figma-to-code parity. A separate runtime handoff is required if implementation is needed.

## Owner Review / Known Gaps

1. **Review sign-off:** use the existing Figma master as the design baseline; confirm the observed three-size model, optional leading icon, shared Label/XS typography, 180 px maximum and passive-only contract. No redesign or new Figma component is proposed.
2. **Library distribution is separate from this design contract:** the existing Tag master is the canonical source; no additional or replacement component is needed. Before teams consume it from the shared Library, confirm the current key is published and validate insertion in an independent consumer file. The available library search still resolves a legacy Tag key, so this publication check remains open but does **not** by itself block completion of design documentation.
3. Upon approval, update this document's summary/maturity and related component routing, regenerate the manifest/graph and the [Component Mapping Lookup Index](../../integrations/component-mapping-index.md) from canonical tooling, and record the reviewed identity in the mapping registry.
4. Perform manual accessibility/composition QA as appropriate. Keep runtime/Storybook APIs **unverified** until registered from actual owning sources.
