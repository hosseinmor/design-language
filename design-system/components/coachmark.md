---
id: design-system.component.coachmark
collection: design-system
type: component
title: Coachmark
summary: Coachmark proactively introduces a feature, workflow, or contextual concept at a specific product moment.
knowledge_state: verified
document_maturity: draft
related:
  - design-system.component.popover
  - design-system.pattern.tour
  - design-system.experience-rule.contextual-guidance
---

# Coachmark

## Purpose

Coachmark is a proactive contextual-guidance component used when the product needs to draw attention to a feature, workflow, or first-use concept.

Unlike Tooltip and Toggletip, Coachmark does not require the user to ask for help first.

Coachmark may be used independently or as the visual step component inside a Tour.

## When to Use

Use Coachmark when:

- a new or changed feature needs contextual introduction;
- a first-use moment benefits from brief guided explanation;
- the product needs to point to a specific nearby target;
- a single proactive guidance step is sufficient;
- one step of a multi-step Tour needs an anchored guidance surface.

## When Not to Use

Do not use Coachmark when:

- the user only needs a brief passive label; use Tooltip;
- the user explicitly requests contextual explanation; use Toggletip;
- the user is performing a small contextual task; use Popover;
- the information is critical, blocking, legally required, or must remain visible until acted upon;
- the guidance can be communicated more clearly through persistent inline UI;
- repeated interruptions would train users to dismiss guidance automatically.

Coachmark is not a substitute for product clarity.

## Canonical Figma API

Component set: `Coachmark / Default`

Figma file key: `rROD8ctH9UfPGAMrRrOzHe`

Component set node: `22796:647`

Component key: `da0cc1d606dfad2870fa6f93cbaac7b616aee278`

### Properties

| Property | Values / behavior |
|---|---|
| `Side` | `Top`, `Bottom`, `Left`, `Right` |
| `Align` | `Start`, `Center`, `End` |
| `Actions` | `One`, `Two` |
| `Dismiss` | Boolean; default `True` |
| `Progress` | Boolean; default `False` |
| `Arrow` | Boolean; default `True` |
| `Title text` | Text |
| `Description` | Text |
| `Progress text` | Text |

Default variant: `Top / Start / One`.

There is intentionally no `Open`, `Visible`, lifecycle trigger, spotlight, target, or persistence property in the Figma API.

Those belong to the Tour/product runtime layer.

## Anatomy

Coachmark contains:

1. raised Surface;
2. absolute Dismiss Icon Button when enabled;
3. Header with Title;
4. Description;
5. Footer;
6. optional Progress;
7. one or two actions;
8. optional caret.

Media/illustration is intentionally not part of Coachmark v1.

Do not add a generic media slot until a real recurring product need establishes its contract.

## Visual Contract

- Surface background: `surface/raised`
- Title foreground: `fg/primary`
- Description/progress foreground: `fg/secondary`
- Radius: 12px
- Surface padding: 16px
- Section gap: 16px
- Explicit border: none
- Floating separation: `Shadow/Floating` (1px outline-like layer + two elevation layers)
- Surface width: 320px
- Content width at current padding: 288px
- Title typography: `Heading/Compact/SM`
- Description/progress typography: `Body/Compact/SM`

Coachmark deliberately avoids a full Brand-colored surface.

Brand or AI/Magic emphasis may appear in small contextual elements when a separate product rule requires it, but the default Coachmark surface remains raised neutral.

## Dismiss Control

Coachmark does not define a separate Close Button component.

Dismiss uses the canonical Icon Button:

- Style: `Ghost`
- Size: `Medium` — 40×40px
- Icon: `close` at the shared 18px Icon Button visual size

In the canonical RTL layout, the Dismiss hit area is absolutely positioned flush to the top-left edge of the Coachmark Surface:

```text
top = 0
left = 0
size = 40 × 40
```

The Header reserves 32px of left-side internal space. Because Surface content begins 16px from the left, this places the Title at x=48 while the Dismiss hit area ends at x=40, preserving an 8px gap.

Equivalent logical runtime intent:

```css
dismiss {
  inset-block-start: 0;
  inset-inline-end: 0;
}

header {
  padding-inline-end: 32px;
}
```

For RTL, `inline-end` is the physical left side.

The absolute Dismiss control must not determine Header height or displace the Title in normal flow.

## Actions

`Actions=One` is the default.

Use one action for acknowledgement or simple progression.

Examples:

```text
متوجه شدم
بعدی
شروع
```

Use two actions primarily for multi-step navigation or a meaningful alternative.

The canonical two-action arrangement uses real Button instances:

- Primary action on the right;
- lower-emphasis / previous action to its left.

Current canonical action Buttons use Small / 32px controls.

Do not create a three-action Coachmark variant.

If a guidance step needs complex decision-making, reconsider the pattern.

## Progress

Progress is optional.

Use Progress primarily when Coachmark participates in a Tour.

Example:

```text
۲ از ۴
```

A standalone Coachmark normally uses `Progress=False`.

Production Progress copy must reflect actual Tour state and must not be manually hard-coded inconsistently across steps.

Static Figma examples and isolated Storybook demonstration stories may hard-code representative progress text to demonstrate the visual state. Those examples are not evidence of a production Tour state model.

## Placement and RTL

Coachmark supports four sides and three alignments.

RTL is canonical.

For `Top` and `Bottom`:

- `Start` = right;
- `Center` = center;
- `End` = left.

For `Left` and `Right`:

- `Start` = top;
- `Center` = center;
- `End` = bottom.

Title and Description are right-aligned.

Coachmark keeps `Arrow=True` by default because pointing to the introduced target is part of its core guidance model.

The caret uses the shared raised two-layer floating-caret geometry: an outer Floating boundary layer and an inner `surface/raised` layer. This continues the floating outline around the arrow without adding a separate stroke to the triangle.

Runtime target collision/flip must preserve logical Start/End semantics.

Coachmark uses a 2px anchor offset:
- with the default `Arrow=True`, measure from the caret tip to the target edge;
- when `Arrow=False`, measure from the Surface edge to the target edge.

## Behavior

Coachmark is normally initiated by product lifecycle or context rather than ordinary hover/click help behavior.

Possible triggers include:

- first relevant visit;
- first use of a feature;
- introduction of a meaningful product change;
- manual restart of an onboarding/help flow.

The exact trigger is product-owned and must not be encoded into the reusable Coachmark component.

### Dismissal

When Dismiss is enabled, the user must be able to close the Coachmark.

`Escape` should also dismiss the current Coachmark/Tour layer where appropriate.

For Tour behavior, dismissal semantics such as “close current step” vs “exit entire Tour” belong to the Tour pattern and runtime.

## Content Guidelines

Coachmark copy should explain:

1. what the user is seeing;
2. why it matters;
3. what to do next, when an action is necessary.

Keep Title short.

Keep Description focused on one concept.

Do not place long documentation, policy text, or multiple unrelated concepts inside a Coachmark.

Prefer product language over implementation language.

## Accessibility

### MUST

- Dismiss control has a meaningful accessible name such as “بستن”.
- Dismiss must be keyboard operable.
- Action Buttons follow the canonical Button accessibility contract.
- Keyboard users must be able to reach all interactive controls.
- `Escape` must provide a reliable dismissal path where the Coachmark is dismissible.
- Focus must not be lost when the Coachmark/Tour ends.
- Target relationship must not be communicated only through visual caret placement.

### Target relationship — runtime gap

The caret alone is not a sufficient programmatic relationship between a Coachmark and its target.

The production runtime must provide an assistive-technology relationship or announcement strategy appropriate to the target and interaction context. There is intentionally **no universal ARIA mapping locked yet**; do not blindly apply `aria-describedby`, `aria-controls`, or dialog semantics to every Coachmark without validating the resulting experience.

Until the runtime relationship is verified, Storybook examples may demonstrate visual targeting but must not be described as accessibility-complete for target association.

### Focus

Exact initial focus behavior depends on how intrusive the guidance is and remains a runtime/pattern decision.

Do not automatically trap focus merely because a Coachmark is floating.

A Coachmark with actions must remain fully keyboard operable.

## Touch / Mobile

Coachmark may be shown on touch interfaces when the anchored relationship remains clear and the surface fits the viewport.

When a narrow viewport makes the target relationship or controls unusable, the Tour/product may switch to a larger guidance presentation rather than forcing the desktop geometry.

## Development Contract

Runtime source is currently unregistered.

Conceptual component inputs:

```text
Coachmark
- title
- description
- actions: one | two
- dismiss
- progress
- progressText?
- arrow
- side
- align
```

Runtime / pattern layer owns:

- target element;
- open/closed state;
- lifecycle eligibility;
- persistence / seen state;
- step order;
- next/back navigation;
- spotlight or backdrop;
- collision/flip;
- focus strategy;
- portal/layering;
- analytics.

Do not encode Tour orchestration as Coachmark visual variants.

## QA Checklist

Verify:

- all 24 Side × Align × Actions combinations;
- default variant is `Top / Start / One`;
- caret direction for four sides;
- Start/End semantics in RTL;
- anchored examples preserve the 2px target offset from caret tip, or Surface edge when `Arrow=False`;
- Dismiss true/false;
- Progress true/false;
- Arrow true/false;
- one- and two-action layouts;
- Actions rows hug their content and never overflow Footer;
- Primary remains on the right in RTL;
- Dismiss is Ghost Medium 40 with the close icon;
- Dismiss hit area is absolute at top-left, flush to the Surface edge;
- Title maintains an 8px safe gap from the Dismiss hit area;
- Description can use the full 288px content width;
- Surface uses `surface/raised`, radius 12, and the canonical three-layer `Shadow/Floating`;
- no additional explicit component border is present;
- caret boundary visually continues the Floating boundary without a seam;
- keyboard access and dismissal work in runtime;
- the production implementation defines and tests a non-visual target-association / announcement strategy; a visual caret alone does not pass accessibility QA.

## Live References

- Figma file: `rROD8ctH9UfPGAMrRrOzHe`
- Component set: `Coachmark / Default`
- Node: `22796:647`
- Component key: `da0cc1d606dfad2870fa6f93cbaac7b616aee278`
- Matrix: 4 Sides × 3 Alignments × 2 Action counts = 24 variants
- Dismiss dependency: `Icon Button / Default`, Ghost / Medium
- Action dependency: canonical Button, Small
- Runtime / Storybook / Code Connect: unregistered / unverified

## Related

- `tooltip.md`
- `toggletip.md`
- `popover.md`
- `button.md`
- `icon-button.md`
- `../patterns/tour.md`
- `../../foundations/interaction/contextual-guidance.md`
- `../../accessibility/focus-management.md`
