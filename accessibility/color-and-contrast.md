---
id: design-system.accessibility.color-and-contrast
collection: design-system
type: accessibility
title: Color and Contrast
summary: Practical contrast, color-use, focus, disabled-state, mode, compositing, and palette-acceptance requirements.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
last_reviewed: '2026-09-02'
---

# Color and Contrast

> This document is the primary accessibility input for Primitive / Brand / Semantic Color palette work.

## 1. Validate semantic pairings, not isolated swatches

**MUST**

Accessibility is evaluated on the actual foreground/background/state relationship in which a color is used.

Do not label a Primitive step “accessible” or “inaccessible” in isolation.

A Primitive family is acceptable when it provides the values needed for the Semantic roles and real component pairings that consume it.

Examples:

```text
blue/700
✕ accessible

fg/accent → blue/700
on surface/default in Light
→ measured as readable text
→ pass/fail
```

A token may pass one use and fail another.

---

## 2. Text contrast

### WCAG AA baseline

**MUST**

For readable text and images of text, use the applicable WCAG 2.2 AA contrast requirement:

```text
Normal text → ≥ 4.5:1
Large text  → ≥ 3:1
```

WCAG large-scale text is at least:
- 18 pt regular; or
- 14 pt bold (700+).

In CSS units this is approximately:
- 24 CSS px regular; or
- 18.67 CSS px bold.

Applicable WCAG exceptions such as inactive UI content, incidental text, and logotypes remain exceptions. Do not extend those exceptions to ordinary product UI.

A Brand surface, Button, banner, or marketing CTA is **not** exempt merely because it uses Brand color.

### JV palette policy

**SHOULD**

Design ordinary readable UI text roles to reach at least **4.5:1** in their intended contexts instead of relying on the large-text exception as the normal palette strategy.

This includes readable uses of roles such as:
- `fg/primary`;
- `fg/secondary`;
- `fg/tertiary`;
- `fg/placeholder`;
- `link/*`;
- `fg/info`;
- `fg/success`;
- `fg/warning`;
- `fg/error`;
- `fg/danger`;
- `fg/accent`;
- `fg/magic`.

Placeholder is still text and is not exempt merely because it is lower emphasis.

If one Semantic token is intended for both readable text and non-text graphics, validate it against the stricter intended text requirement where that text use is real.

---

## 3. Text on strong surfaces

**MUST**

Readable content on strong surfaces meets the applicable text-contrast requirement.

Validate independently:

```text
fg/on-brand
→ surface/brand*
→ separately for JobVision and Cando

fg/on-color
→ Neutral / Danger / Accent / Magic strong surfaces where used

fg/on-inverse
→ surface/inverse

severity inverse foregrounds
→ surface/inverse when used as readable text
```

`fg/on-brand`, `fg/on-color`, and `fg/on-inverse` are separate contracts because the surface luminance and intended contexts differ.

Do not assume one foreground can serve all strong surfaces.

---

## 4. Non-text contrast

**MUST**

Visual information required to identify a UI component, its state, or a meaningful graphical object reaches **≥3:1 against the relevant adjacent color(s)** where WCAG 1.4.11 applies.

Examples include:
- a Text Input boundary when that boundary is needed to identify the input;
- a checkbox/radio mark or essential selected state;
- a selected/current Tab indicator when it is needed to identify state;
- a meaningful standalone icon;
- essential chart marks;
- an author-styled focus indicator needed to identify keyboard focus.

A visible component border is **not automatically required** to reach 3:1 when the component is already identifiable without that border.

Decorative separators such as `line/muted` are not automatically subject to 3:1 if they carry no essential identification/state meaning.

When testing thin lines/icons, passing the mathematical threshold is the minimum; very thin anti-aliased shapes may still be visually weak.

---

## 5. Color cannot be the only visual cue

**MUST**

Essential information, action, or state must not depend on hue alone.

Programmatic semantics are also required where applicable, but programmatic semantics do **not** replace the visual non-color cue required for sighted users who cannot distinguish color differences.

Examples:

```text
Error
→ error message / icon / other visible cue
+ programmatic invalid state where applicable
not only a red border

Selected
→ indicator / shape / position / text treatment
+ selected/current semantics where applicable
not only blue hue

Checked
→ checkmark / shape
+ checked semantics
not only colored fill

Chart series
→ labels / shapes / patterns / direct values / accessible data alternative as applicable
not only different hues
```

### Inline links

**SHOULD**

Use a persistent non-color affordance such as underline for inline links inside body text.

If an inline link is distinguished from surrounding static text by color alone:

**MUST**
use a valid WCAG Use-of-Color solution.

JV's default practical fallback is:

```text
link text vs surrounding text → ≥3:1
+
a non-color cue appears on hover and keyboard focus
+
link text itself still meets text contrast against its background
```

Do not assume “blue looks clickable” is sufficient.

---

## 6. Focus color

Focus is a dedicated Semantic role and interaction state. Its current default value intentionally shares the approved Accent Primitive for each Appearance, but Accent styling does not substitute for Focus and components must consume `focus/default`. Focus remains distinct from Brand, Danger, and Selected state.

**MUST**

- keyboard focus remains visibly identifiable;
- an author-created focus indicator meets applicable non-text contrast against its adjacent background(s);
- `focus/default` works in every approved normal/local surface context;
- `focus/inverse` works in every approved inverse context;
- Error / Selected / Expanded styling must not erase Focus.

Do not infer `focus/inverse` merely from global Dark mode. Inverse is a local semantic context.

Unmodified browser focus appearance may use the user-agent exception, but it still has to remain visibly identifiable.

### Stronger JV target

**SHOULD**

Aim for the WCAG 2.4.13 Focus Appearance model:

```text
indicator area
→ at least equivalent to a 2 CSS px perimeter

focused vs unfocused change
→ ≥3:1
```

This is a JV quality target inspired by WCAG 2.4.13 Level AAA, not a WCAG AA requirement.

---

## 7. Hover and Active

Hover/Active treatments do **not** need to differ from Rest by 3:1 merely because they are different states.

**MUST**

During Hover/Active:
- readable text remains compliant;
- essential component boundaries and state indicators do not lose required contrast;
- Focus / Selected / Error information is not erased when states compose.

**SHOULD**

Hover and Active feedback remains perceptible enough to be useful without requiring excessive contrast or motion.

Do not distort the Primitive palette merely to manufacture a 3:1 Rest→Hover or Rest→Active delta.

---

## 8. Disabled and inactive

Inactive UI components are exempt from the ordinary WCAG text/non-text contrast minima that apply to enabled controls.

JV therefore does **not** invent a hard Disabled contrast ratio.

**MUST**

- Disabled remains visually distinguishable from the enabled state;
- explanatory text that users need in order to understand why something is unavailable must remain readable and must not inherit Disabled styling;
- Disabled styling suppresses misleading Brand/Danger affordance according to the approved component/color contract.

Current v4 semantic contract:

```text
fg/disabled
→ unavailable control/content styling, including disabled filled controls

surface/disabled + fg/disabled
→ disabled filled-control treatment
```

`fg/on-color-disabled` is not part of the current v4 semantic vocabulary. Disabled filled controls suppress their original tone instead of preserving a colored disabled surface.

---

## 9. Light, Dark, Inverse, and product Brand contexts

**MUST**

Validate contrast separately in every supported context.

Do not assume:
- Light values can be mathematically mirrored into Dark;
- the same on-color foreground works on JobVision Blue and Cando Yellow;
- Inverse can be inferred from Dark mode;
- a pairing that passes on `surface/default` also passes on `surface/muted`, `surface/raised`, or another supported surface.

`surface/inverse` is a local semantic context, not another name for Dark mode.

Brand contrast must be validated separately for every Brand mode that changes the actual resolved color.

---

## 10. Alpha, transparency, gradients, and variable backgrounds

The Design System contains alpha primitives and transparent interaction surfaces, so contrast must be tested after compositing.

**MUST**

For translucent foregrounds or surfaces:
- calculate/test the effective rendered color after it is composited onto the actual supported background;
- do not validate an RGBA value in isolation.

Example:

```text
black-alpha/40
on surface/default
→ evaluate composited result

black-alpha/40
on image
→ cannot inherit the same guaranteed result automatically
```

For text/icons over gradients, images, or otherwise variable backgrounds:

**MUST**
ensure the required contrast across the supported placement area, or provide a controlled backing treatment such as a scrim/surface that creates a testable pairing.

**SHOULD**
Prefer deterministic Semantic pairings for reusable components rather than depending on unpredictable image colors.

---

## 11. Forced colors / high contrast

This requirement depends on the product's supported platform/test matrix.

**MUST**

When forced-colors/high-contrast behavior is included in the supported product matrix, custom controls must preserve essential:
- component identification;
- current state;
- focus;
- selected/checked state;
- operability.

**SHOULD**

Reusable custom controls should be designed resiliently even before the final browser/AT matrix is locked:
- prefer native semantics and native boundaries where practical;
- use `currentColor` where it improves resilience;
- do not rely only on authored background fills for Selected/Checked;
- do not disable platform color adjustment unless a tested alternative exists.

This is especially important for custom controls whose essential state could disappear when authored colors are replaced.

---

## 12. Respect Semantic Color contracts

Accessibility validation must not redefine Design System color semantics.

The canonical token/component documentation owns meanings such as:
- Support;
- Danger;
- Accent;
- Brand;
- Magic;
- Selected.

**MUST**

Do not swap to a different Semantic category merely because its current Primitive value produces an easier contrast ratio.

If the intended semantic pairing fails:
1. fix the palette value;
2. revise the approved token mapping if necessary;
3. or constrain the supported pairing.

Do not change the meaning of the token to solve contrast.

---

## 13. Primitive palette acceptance contract

A chromatic Primitive family does **not** need every step to be individually accessible or consumed.

The 11-step:

```text
50 100 200 300 400 500 600 700 800 900 950
```

is a palette-structure decision, not proof that every step needs a Semantic consumer.

Before accepting a chromatic family, verify that it can supply the **relevant** semantic roles for that family.

Typical capability checks:

| Intended capability | Validate |
|---|---|
| Muted surface | Intended text/icon content remains compliant on it |
| Essential line/state | ≥3:1 against adjacent color where 1.4.11 applies |
| Chromatic foreground on Light | ≥4.5:1 for ordinary readable UI text under JV policy |
| Strong/emphasis surface | Intended on-color text is compliant |
| Chromatic foreground on Dark | Intended readable use is compliant |
| Hover/Active source | State preserves required content/state contrast; no arbitrary 3:1 delta from Rest |

For Neutral, also verify candidate values for:
- `fg/primary`;
- `fg/secondary`;
- `fg/tertiary`;
- `fg/placeholder`;
- structural lines;
- neutral interactive surfaces;
- inverse surface/content;
- disabled pairings.

For Brand, validate both JobVision and Cando actual Brand mappings rather than assuming one Brand foreground contract works for both.

For alpha families, validate representative composited outputs rather than the alpha swatch alone.

---

## 14. Palette validation worksheet

For every semantic pairing under review, record:

```text
subject token
adjacent/background token(s)
resolved Primitive / actual value
product mode
Light / Dark / Inverse / local context
usage type:
  normal text
  large text
  non-text UI/state
  graphical object
WCAG criterion / JV policy
requirement level: MUST / SHOULD
target ratio
measured ratio
pass / fail / exception
consumer examples
notes
```

### Calculation rules

**MUST**
- test the actual resolved color pair, including compositing;
- use the least-contrasting relevant adjacent color when multiple adjacent colors matter;
- do not round a failing value up to the threshold (`2.999:1` does not become `3:1`);
- use authored/source colors for calculation rather than sampling anti-aliased edge pixels from a screenshot.

### Representative consumers

At minimum, Palette Pass should test the actual Semantic pairings required by:

- Text Input;
- Button presets, including JobVision/Cando Brand;
- Link;
- Checkbox / Radio / Selection;
- Focus Default and Focus Inverse;
- Support Info / Success / Warning / Error;
- Danger;
- Accent;
- Magic where used;
- inverse Toast/status treatment;
- Disabled pairings as visual-quality checks, not invented WCAG ratio checks;
- Tag categorical colors;
- charts/data visualization when a chromatic family is used there.

A Primitive family should not be accepted solely because its swatch ramp looks visually balanced.

---

## References

- WCAG 2.2 — Contrast (Minimum)
- WCAG 2.2 — Non-text Contrast
- WCAG 2.2 — Use of Color
- WCAG 2.2 — Focus Visible
- WCAG 2.2 — Focus Appearance
