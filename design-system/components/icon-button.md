---
id: design-system.component.icon-button
collection: design-system
type: component
title: Icon Button
summary: Icon Button triggers a compact action using one recognizable icon while preserving an explicit accessible name and visible Tooltip label.
knowledge_state: verified
document_maturity: draft
design_status: ready-for-dev
design_maturity: handoff-ready
related:
  - button
  - design-system.component.tooltip
  - design-system.accessibility.core
  - design-system.accessibility.component-authoring-contract
---

# Icon Button

## Purpose

Icon Button triggers an action using a single icon instead of a persistent text label.

Use it when the action is compact, repeated, or placed in a dense control region and the icon can remain recognizable without a visible label.

Icon Button is a separate component from Button. Do not recreate icon-only behavior by hiding the label of Button or by adding an `Icon only` type to Button.

## When to Use

Use Icon Button for actions such as:

- close;
- edit;
- delete entry point;
- add;
- refresh;
- overflow / more actions;
- compact toolbar utilities;
- other familiar actions where a persistent label would create unnecessary density.

The action must remain understandable from the icon, context, accessible name, and Tooltip label together.

## When Not to Use

Do not use Icon Button when:

- the action meaning is unfamiliar or cannot be represented clearly by one icon;
- the action is the final destructive confirmation; use a visible text Button instead;
- a persistent text label materially improves comprehension;
- the control represents persistent selected/on-off state; use the appropriate Toggle / Toggle Button / selection component;
- the primary behavior is navigation; use Link semantics or an appropriate icon-link pattern rather than Button semantics;
- the design needs rich explanatory or interactive content on hover/focus; use Popover or another appropriate disclosure pattern rather than Tooltip;
- an asynchronous action requires a Loading state in the current v1 contract; Loading is not supported by Icon Button v1.

## Canonical Figma API

Component set: `Icon Button / Default`

Figma file key: `rROD8ctH9UfPGAMrRrOzHe`

Component set node: `22685:1410`

Component key: `f9b7af4bd9afaf768ae955c51ccddd29833c5ca7`

### Properties

| Property | Values / behavior |
|---|---|
| `Style` | `Brand`, `Primary`, `Secondary`, `Tertiary`, `Ghost`, `Danger Tertiary`, `Danger Ghost` |
| `Size` | `Extra Small`, `Small`, `Medium`, `Large` |
| `State` | `Enabled`, `Hover`, `Active`, `Focus`, `Disabled` |
| `Icon` | Required instance swap; fixed visual size 18px |

Default Figma values are `Tertiary / Medium / Enabled`.

There is intentionally no `Danger Primary` Icon Button.

There is no Loading, Selected, Toggle, or Pressed variant in the current Icon Button contract.

## Anatomy

Icon Button contains:

1. one square interactive container;
2. one centered icon;
3. an accessible action name supplied by the consuming product;
4. a Tooltip label for visible discoverability on hover/focus.

The Tooltip is a behavioral/documentation dependency, not visual content inside the Icon Button container.

Do not add persistent text, badges, counters, secondary icons, or arbitrary slot content to the current Icon Button anatomy. When those needs are real, use a dedicated component or define an explicit extension instead of overloading Icon Button.

## Sizes

| Size | Visual container | Icon |
|---|---:|---:|
| Extra Small | 28 × 28 px | 18 × 18 px |
| Small | 32 × 32 px | 18 × 18 px |
| Medium | 40 × 40 px | 18 × 18 px |
| Large | 48 × 48 px | 18 × 18 px |

Shared geometry:

- container is square;
- radius: `6px`;
- icon remains centered;
- icon size remains `18px` across all four control sizes;
- interaction states must not change control dimensions or icon position.

### Size selection

- **Extra Small 28** — very dense desktop UI where compactness is necessary.
- **Small 32** — compact desktop controls and dense toolbars.
- **Medium 40** — default general-purpose Icon Button.
- **Large 48** — touch-oriented or high-comfort interaction.

All current sizes exceed the shared 24×24px minimum pointer-target baseline.

For frequently used controls in touch-oriented interfaces, prefer Medium or Large rather than relying on the minimum. Visual icon size and hit-target size are independent.

Do not use a 24px container; Extra Small is 28px.

## Style Selection

| Need | Style |
|---|---|
| Approved product-defining / conversion action that is genuinely clear as an icon | Brand |
| High-emphasis operational icon action | Primary |
| Supporting medium-emphasis action | Secondary |
| General independent utility or control | Tertiary |
| Intentionally low-emphasis / dense utility | Ghost |
| Visible destructive entry point | Danger Tertiary |
| Low-emphasis destructive entry point | Danger Ghost |

### Brand

Brand Icon Button is rare. Use it only when the action already qualifies for Brand semantics and the icon-only treatment remains unambiguous.

Do not use Brand merely to decorate a toolbar or make an ordinary utility more noticeable.

### Primary

Use Primary when one icon action needs strong operational emphasis without requiring a persistent text label.

If the action is important enough that comprehension or consequence needs explicit wording, use a labeled Button instead.

### Secondary

Use for a supporting icon action that should remain visible with medium emphasis.

### Tertiary

Tertiary is the default Icon Button style and is appropriate for most standalone utility controls and dense operational UI.

### Ghost

Use when the control should remain available with intentionally low visual emphasis, especially in dense groups or inline contexts.

### Danger

Danger Icon Button is limited to:

- `Danger Tertiary` — visible destructive entry point;
- `Danger Ghost` — low-emphasis destructive entry point.

`Danger Primary` is intentionally not available.

Final destructive confirmation must use a Button with a visible text label so the consequence is explicit.

Danger color alone must never carry the destructive meaning. The icon, accessible name, Tooltip label, and surrounding context must identify the action.

## States

### Enabled

The control is operable with pointer and keyboard and exposes its accessible name.

### Hover / Active

Use the corresponding semantic state for the selected Style.

Do not implement Hover or Active by changing dimensions, icon size, or container position.

### Focus

Focus treatment is independent from Style.

Keyboard focus must remain clearly visible for Brand, Neutral, Ghost, and Danger treatments.

Tooltip appearance on focus must not replace or obscure the focus indicator.

### Disabled

Disabled is a distinct state, not a low-emphasis Style.

Disabled suppresses Brand/Danger intent chroma according to the shared disabled semantic contract.

A disabled Icon Button must not activate.

Do not depend on Tooltip as the only way to explain why a disabled action is unavailable. Native disabled controls may not receive keyboard focus, so reasons that matter to task completion must be available in surrounding persistent UI or an appropriate feedback pattern.

Do not make a disabled control focusable solely so its Tooltip can appear.

## Tooltip Contract

Every operable Icon Button **MUST** provide a visible Tooltip label.

The Tooltip exists because Icon Button intentionally removes the persistent text label. It improves visible discoverability for mouse and keyboard users.

### Required behavior

Icon Button owns the requirement that every operable icon-only action provides a visible Tooltip label.

The Tooltip component contract owns the shared display and interaction behavior, including:

- hover and keyboard-origin focus triggering;
- canonical show/hide timing;
- hover persistence;
- `Escape` and activation dismissal;
- reopen suppression;
- placement/collision behavior;
- touch boundary;
- Tooltip focusability and accessibility relationship.

Do not redefine those values in Icon Button.

Icon Button-specific requirements remain:

- Tooltip must not be the only source of the accessible name;
- Tooltip must not be the only source of essential instructions or state;
- disabled Icon Buttons must not become focusable solely to expose Tooltip.

### Tooltip text

By default, Tooltip text should match the Icon Button's accessible action name.

Use an action label, not the icon's visual name.

Good:

```text
ویرایش
حذف
بستن
تازه‌سازی
افزودن
```

Avoid:

```text
مداد
سطل زباله
ضربدر
فلش دایره‌ای
علامت مثبت
```

Keep Tooltip text concise.

If the UI needs additional explanation beyond the action label, do not turn the ordinary Icon Button Tooltip into rich content. Use persistent help, a description mechanism supported by Tooltip, or another component/pattern as appropriate.

### Accessible name vs Tooltip

Accessible name is mandatory even when the Tooltip text is identical.

Implementation may use `aria-label`, visually hidden text, or another valid naming mechanism. Exact runtime API is not yet verified.

The icon itself should normally be decorative for assistive technology when the Button already owns the accessible name, avoiding duplicate announcements.

Do not include the word “button” in the accessible name; native Button semantics already expose the role.

## Keyboard and Focus

Prefer a native `<button>` element for action semantics.

Preserve native Button interaction:

- `Tab` / `Shift+Tab` move focus according to document order;
- `Enter` and `Space` activate the focused Icon Button;
- visible focus follows the shared Focus contract.

Tooltip appearance must not create an additional tab stop or move focus.

If Icon Button triggers a Menu, Popover, Dialog, or another popup, the consuming component/pattern must expose the relevant programmatic relationship/state such as expanded or popup semantics where applicable. Those states are not generic Icon Button variants.

## Navigation Boundary

Icon Button is an action control.

If activation navigates to a destination rather than performing an action, use semantic Link behavior even when the visual treatment is icon-only.

Do not use `role=button` or a click handler on a generic element to imitate navigation or Button semantics.

## Toggle / Selected Boundary

Persistent on/off, selected, favorited, bookmarked, pinned, or similar state is outside the current stateless Icon Button contract when that state needs to be represented programmatically.

Use or define the appropriate Toggle / Toggle Button pattern with the required programmatic pressed/selected state.

Do not represent persistent selection only by switching Icon Button Style or icon color.

## Loading Boundary

Icon Button v1 does not expose Loading.

Do not replace its icon with an ad-hoc spinner while leaving the same component contract; that removes the visible action cue and introduces additional busy-state behavior that is not currently specified.

For an async action that materially needs loading feedback:

- prefer a labeled Button when appropriate; or
- use flow-level progress/status feedback; or
- extend Icon Button only through an explicit future design-system decision.

Runtime implementations must not infer a `loading` prop from Button.

## Semantic Color Mapping

Icon Button consumes the same semantic action hierarchy as Button.

Representative enabled mappings currently verified in Figma:

| Style | Semantic treatment |
|---|---|
| Brand | `surface/brand` + on-brand foreground |
| Primary | `surface/neutral-emphasis` + on-color foreground |
| Secondary | `surface/neutral-muted` + normal foreground |
| Tertiary | transparent + `line/default` + normal foreground |
| Ghost | transparent + normal foreground |
| Danger Tertiary | transparent + `line/danger` + danger foreground |
| Danger Ghost | transparent + danger foreground |

Hover, Active, Focus, and Disabled resolve through the shared semantic state families. Do not create Icon-Button-specific color tokens merely to duplicate those roles.

## Icon Rules

- Exactly one icon is used.
- Icon visual size is fixed at 18px.
- Prefer icons from the approved Design System icon set.
- The icon must visually correspond to the action represented by the accessible name.
- Do not rely on color alone to distinguish two Icon Buttons with different meaning.
- Decorative internal SVG/icon content should be hidden from assistive technology when the Button has its own accessible name.
- Directional icons may mirror in RTL when their meaning is directional; non-directional icons must not be mirrored merely because the page is RTL.
- Swapping the icon must not alter the control dimensions.

If an action cannot be represented by a sufficiently recognizable icon, use a visible-label Button instead.

## RTL and Responsive Behavior

The square container does not change layout direction in RTL.

Directional icon behavior follows the icon-system RTL contract.

Tooltip placement should adapt to available space and direction without changing the Button's position.

At zoom/reflow or on narrow screens, the control must remain operable and its hit target must not be clipped by overflow containers.

## Motion / Transition Contract

Use shared motion/transition tokens when available.

Allowed transitions are visual state properties such as background, foreground, border, and focus treatment.

Do not animate control width/height, icon position, or target geometry between interaction states.

Tooltip motion belongs to Tooltip.

## Accessibility

Icon Button is a simple native-based control with additional accessible-name and Tooltip requirements.

### MUST

- Use native Button semantics for actions when possible.
- Provide a meaningful accessible name describing the action.
- Keep the icon and accessible action meaning aligned.
- Preserve keyboard activation.
- Preserve visible focus.
- Meet the shared minimum pointer target.
- Keep visual and programmatic disabled state consistent.
- Avoid conveying destructive or other essential meaning by color alone.
- Provide the Icon Button Tooltip contract for operable controls.

### SHOULD

- Prefer Medium or Large in touch-oriented contexts.
- Use familiar, visually recognizable icons.
- Keep accessible name and Tooltip text the same unless there is a deliberate reason to separate label and description.

Tooltip does not replace the accessible name.

## Development Contract

Runtime source is currently unregistered, so exact component/prop names must not be inferred from Figma.

The implementation should expose semantic inputs equivalent to:

```text
Icon Button
- style
- size
- icon
- accessible name
- disabled
```

It should not expose application-level props for `hover`, `active`, or `focus`; those are interaction states.

The current design contract does not include:

```text
loading
selected
pressed
toggle
badge
persistent text label
Danger Primary
```

Tooltip may be composed internally by the future runtime Icon Button or externally through the shared Tooltip component. That authoring choice remains a runtime decision, but the resulting product behavior must satisfy the Tooltip Contract above.

## QA Checklist

For every supported Style and Size, verify:

- container is square and matches 28 / 32 / 40 / 48px;
- icon remains centered at 18px;
- Enabled, Hover, Active, Focus, and Disabled use intended semantic roles;
- focus is clearly visible;
- native keyboard activation works;
- the control has a meaningful accessible name;
- internal icon does not create a duplicate screen-reader announcement;
- Tooltip appears on hover and keyboard focus for operable Icon Buttons;
- Tooltip does not receive focus;
- Tooltip can be dismissed with `Escape`;
- Tooltip text identifies the action rather than naming the glyph;
- Disabled does not activate and does not rely on Tooltip for essential explanation;
- destructive meaning is not conveyed by color alone;
- Directional icons behave correctly in RTL;
- no interaction state changes dimensions or icon position;
- no unsupported Loading or Selected behavior is introduced.

Representative manual tests should include Extra Small in dense desktop UI and Medium/Large in touch-oriented UI.

## Product Variation

Brand maps through the active product Brand tokens. Icon Button meaning and hierarchy remain the same across products.

Do not introduce product-specific Icon Button variants solely to change color.

## Live References

- Figma file: `rROD8ctH9UfPGAMrRrOzHe`
- Component set: `Icon Button / Default`
- Node: `22685:1410`
- Component key: `f9b7af4bd9afaf768ae955c51ccddd29833c5ca7`
- Current matrix: 7 Styles × 4 Sizes × 5 States = 140 variants
- Icon property: instance swap, 18px
- Runtime / Storybook / Code Connect: unregistered / unverified

## Related

- `button.md`
- `tooltip.md`
- `../../accessibility/core.md`
- `../../accessibility/component-accessibility-authoring-contract.md`
- `../../accessibility/screen-reader-semantics.md`
- `../../accessibility/focus-management.md`
- `../../integrations/component-mapping.md`
