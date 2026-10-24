---
id: design-system.accessibility.focus-management
collection: design-system
type: accessibility
title: Focus Management
summary: Defines practical rules for visible focus, logical focus order, programmatic focus, overlays, dynamic changes, validation, removal, and focus restoration.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.keyboard-navigation
- design-system.accessibility.dynamic-content-and-feedback
- design-system.accessibility.forms
last_reviewed: '2026-09-19'
---

# Focus Management

This document defines **where keyboard focus goes, when it moves, where it may travel, and how it remains visible**.

It does not redefine component-specific keyboard models. Components such as Modal, Menu, Tabs, Combobox, and Text Input should encode their exact focus contract in their own component guidelines.

The practical goal is:

```text
Do not move focus unless moving it improves or preserves the user's context.
When focus must move, move it to the most logical usable target.
Never leave the user with focus lost, hidden, or trapped unintentionally.
```

---

# 1. Shared Focus Visibility Contract

This section is the canonical owner for the **shared visible-focus treatment** used by reusable JobVision/Cando UI.

Component and Pattern guidelines MUST NOT redefine the default Focus ring geometry, token selection, or web trigger. They only document:
- whether and where the component can receive focus;
- which perceived control/sub-control owns the visible indicator when placement is not obvious;
- focus movement, containment, restoration, and composite-widget behavior;
- state composition that is specific to that component;
- a justified, reviewed exception to this shared contract.

If no exception is documented, this contract applies.

## Terminology

Treat these concepts as related but distinct:

```text
DOM focus / :focus
→ the element currently owns focus
→ may result from pointer, touch, keyboard, or programmatic focus

Visible focus / :focus-visible
→ the user agent determines that an explicit focus indicator is appropriate
→ show the shared JV Focus ring

Focus-within / :focus-within
→ the element itself or one of its descendants owns focus
→ useful for container state, but not a substitute for the visible indicator
```

A component being focused does **not** automatically mean that the shared Focus ring must be drawn.

## Visibility trigger

**MUST — web implementations**

Use `:focus-visible` as the default trigger for the shared Focus ring.

Do not use `:focus` alone to force the ring on every focused control.

```css
:focus-visible {
  outline: 2px solid var(--focus-default);
  outline-offset: 1px;
}
```

JV accepts the browser/user-agent `:focus-visible` heuristic. Do not add global JavaScript, CSS classes, or `data-input-modality` logic solely to distinguish keyboard from pointer input.

`:focus-visible` is not defined as “keyboard-only”. A text-editing control may still match it after pointer interaction. Do not suppress that standards-based behavior merely to force a pointer-specific visual result.

This policy aligns with WCAG 2.4.7, which allows a mode of operation where the keyboard focus indicator is visible and explicitly recognizes user-agent behavior that may optimize when the indicator is shown.

## Visual geometry

**MUST**

The shared authored Focus treatment is:

```text
component edge
→ 1px visual gap
→ 2px Focus ring
```

The ring is external to the perceived interactive boundary.

It must not:
- replace the component border;
- recolor the component border as a Focus substitute;
- thicken the component border;
- resize the component;
- create layout shift.

The 2px + 1px geometry is a **JV Design System contract** even though WCAG 2.4.13 Focus Appearance is Level AAA. WCAG conformance level and the internal visual standard are separate decisions.

## Focus tokens

Use only the shared semantic Focus roles:

```text
focus/default
→ normal/local supported surfaces

focus/inverse
→ approved inverse-surface contexts
```

Do not consume Accent, Brand, Line, Error, or raw Primitive colors as substitutes for Focus.

Do not infer `focus/inverse` from global Dark mode. Inverse is a **local semantic surface context**.

Exact Light/Dark/Product mappings are owned by the Color token contract under `design-system/tokens/color/`; this document owns **when the Focus roles are used**, not their Primitive values.

## Focus target

**MUST**

Draw the visible indicator around the perceived interactive control or sub-control that currently owns visible focus.

Examples:

```text
Button
→ Button boundary

Text field
→ field/control shell perceived as the editable control

Menu item
→ focused menu-item row

Slider
→ focused thumb, when the thumb is the keyboard focus target

Composite widget with roving focus
→ active focused sub-control, not automatically the entire composite
```

Do not place the Focus ring around labels, helper text, decorative wrappers, or an entire composite merely because they contain the focused element.

A wrapper may visually carry the ring when it is the correct perceived control boundary and its state is driven by a descendant's `:focus-visible`; document non-obvious placement in the component contract.

## State composition

Focus is independent from:
- Hover;
- Active/Pressed;
- Selected/Current;
- Checked;
- Expanded;
- Error/Danger;
- loading or other component-specific states.

**MUST**

When Focus composes with another meaningful state, preserve both meanings.

```text
Error + Focus
→ keep Error border/state
→ add external Focus ring

Selected + Focus
→ keep Selected treatment
→ add external Focus ring
```

Do not use Selected, Error, Active, or Accent styling as the only Focus indicator.

## Implementation mechanism

**MUST**

Prefer CSS `outline` + `outline-offset` for the standard web treatment because it:
- does not participate in layout;
- directly expresses the required external offset;
- keeps Focus separate from the component border.

A `box-shadow`-based ring MAY be used only when a documented component/platform constraint prevents `outline` from producing the required result. The fallback must preserve:
- the same 2px visible ring;
- the same 1px gap;
- the correct semantic Focus token;
- no layout shift.

`:focus-within` MAY style a composite/container when the container needs a focused internal state, but it MUST NOT remove or replace the visible indicator required for the actual focus target.

## Figma authoring contract

Figma represents the shared web Focus treatment with:

```text
Focus/Default
Focus/Inverse
```

These shared Effect Styles model the external 1px gap + 2px ring. Their shadow construction is a **design representation**, not the required runtime mechanism.

For Figma component variants:

- a visual `State=Focus` represents the **visible-focus treatment** corresponding to the shared `:focus-visible` contract; it does not mean “every possible DOM `:focus` event”;
- use the shared Focus Effect Style; do not recreate Focus with manual strokes, ad hoc shadows, or component-specific colors;
- apply the effect to the layer that matches the perceived interactive boundary;
- keep the Focus effect outside the component's own border/state styling;
- ensure the effect and its owning wrapper are not clipped by `Clip content` / overflow;
- use `Focus/Inverse` only for an approved inverse-surface context.

A component that needs a visually distinct pointer-focused/editing state MAY model that separately, but it must not redefine the shared visible-focus ring.

## Contrast

**MUST**

Keyboard focus remains visibly identifiable and the author-created Focus indicator satisfies the applicable non-text contrast requirements in every supported context.

See `color-and-contrast.md` for contrast ownership and validation.

**SHOULD**

Aim for the WCAG 2.4.13 Focus Appearance model for indicator area and focused-vs-unfocused change. This remains a Level AAA external criterion; the shared JV geometry above is still the Design System's required authored treatment.

## Exceptions

An exception to the shared Focus Visibility contract requires:
- a concrete component/platform constraint;
- the same or stronger focus identifiability;
- preserved keyboard accessibility;
- explicit documentation in the owning Component/Pattern guideline;
- owner review.

Do not create an exception only to make one component look visually different.

---

# 2. Focus must not be obscured

## WCAG 2.2 AA

**MUST**

When a UI component receives keyboard focus, it must not be **entirely hidden by author-created content**.

Common risks:
- sticky header;
- sticky footer;
- fixed action bar;
- persistent chat/support widget;
- non-modal drawer;
- cookie/banner layer;
- sticky Modal footer;
- overlapping notification.

This is WCAG 2.4.11 Focus Not Obscured (Minimum), Level AA.

## JV quality target

**SHOULD**

Keep the focused component **fully visible** whenever practical.

Full visibility corresponds to the stronger WCAG 2.4.12 Enhanced criterion, which is Level AAA.

Do not make “fully visible at all times” a hard global JV requirement when dense/responsive layouts make partial overlap unavoidable but the AA requirement is still satisfied.

## Implementation guidance

Useful mechanisms include:
- appropriate `scroll-padding`;
- `scroll-margin`;
- layout space reserved for sticky regions;
- scrolling a newly focused target into a safe visible area.

When programmatically moving focus:

**MUST**
ensure the target is visible enough to identify and operate.

Do not use `preventScroll` unless visibility is handled deliberately.

---

# 3. Logical focus order

## WCAG baseline

**MUST**

Sequential focus order preserves meaning and operability.

Focus order does not have to match visual order pixel-for-pixel, but it must not create confusing jumps or contradict the task structure.

## DOM order

**SHOULD**

Prefer DOM order that naturally matches the meaningful visual/reading sequence.

This makes:
- keyboard order;
- screen-reader reading order;
- responsive layout;
- implementation

more likely to stay aligned.

## Positive tabindex

**SHOULD NOT**

Use positive `tabindex` values (`tabindex="1"`, `2`, etc.) to repair layout/order.

Prefer fixing DOM structure.

Positive tabindex is not automatically a WCAG failure, but it is fragile and easily produces an illogical focus sequence.

## Static content

**SHOULD NOT**

Put ordinary static text into the normal Tab sequence merely to make it “accessible”.

Use `tabindex="-1"` when a static element needs to receive **programmatic** focus for orientation but should not become another routine Tab stop.

Examples:
- heading after a client-side route change;
- beginning of a long Modal;
- error summary.

---

# 4. Programmatic focus: move only for a reason

Programmatic focus is useful when the user's interaction context changes.

It is harmful when it steals the user's current point of interaction.

## MUST

Move focus programmatically when failing to do so would:
- leave focus on a removed/nonexistent element;
- strand focus outside an active modal interaction context;
- violate a component's established focus contract;
- leave keyboard users unable to continue logically.

## SHOULD

Move focus when a user-triggered context change creates a clearly new interaction context and focus movement materially improves orientation.

Examples:
- opening a Modal;
- entering a composite widget according to its pattern;
- advancing to a newly rendered required workflow step;
- moving to an error summary after failed submission when errors would otherwise be difficult to discover.

## SHOULD NOT

Move focus for:
- routine async updates;
- passive Toast/Notification;
- auto-save confirmation;
- search-result count changes;
- background refresh;
- decorative reveal;
- every validation message as the user types.

Use programmatic announcements where appropriate instead of stealing focus.

See `dynamic-content-and-feedback.md`.

---

# 5. Focus after client-side navigation / view replacement

Traditional full-page navigation already provides browser-level navigation behavior.

Client-side applications can replace substantial page content without a full page load, which can leave keyboard/screen-reader users without a clear new point of context.

## MUST

After a client-side route/view change:
- do not leave focus on an element that was removed;
- do not leave focus in a hidden/inert previous view;
- preserve a logical keyboard entry point into the new state.

## SHOULD

For a substantial user-initiated page/view replacement, move focus to a meaningful beginning point when this improves orientation, commonly:
- the new page/view heading;
- the main content container;
- another explicit task target.

A static heading may use `tabindex="-1"` for programmatic focus.

Do **not** create a universal rule that every route change must focus `h1`.

Examples where another target may be more logical:
- successful item creation → newly created item;
- opening an edit route → first meaningful form field when appropriate;
- returning from detail → previously active list item/row;
- workflow continuation → next task control.

Route-change focus is a **strategy point**: the shared navigation/pattern layer provides the mechanism; the Product flow chooses the logical target.

---

# 6. Modal focus

Modal is a special interaction scope.

A true Modal:
- moves focus inside when opened;
- keeps sequential Tab focus inside while active;
- makes outside content unavailable for interaction;
- restores or deliberately relocates focus when closed.

See `components/modal.md`.

## Initial focus

**MUST**

Focus enters the Modal.

**MUST NOT**

Use one universal rule such as:

```text
always focus first input
```

or:

```text
always focus Primary Button
```

Initial focus depends on the content/task.

Common strategies:
- first logical control;
- suitable static heading/content near the start of a long structured Modal;
- acknowledgement/continue action for a simple message;
- least-destructive action for a difficult-to-reverse decision.

## Restore focus

**MUST**

When the Modal closes, preserve a logical point of work.

Default:

```text
return focus to invoker
```

Exceptions:
- invoker was removed;
- the completed action created a more logical next target;
- workflow intentionally advanced.

Then move to the most logical new target.

---

# 7. Non-modal temporary UI

Not every overlay is a Modal.

Examples:
- Dropdown Menu;
- Popover;
- Combobox popup;
- Tooltip;
- non-modal Drawer.

## MUST

Do not trap focus in a non-modal component unless its established component pattern explicitly requires an internal composite focus model.

Background/page interaction remains available for genuinely non-modal UI.

## On close

If keyboard focus moved **inside** temporary UI and that UI closes:

**SHOULD**
return focus to:
- its trigger;
- or another logical successor if the trigger disappeared or the action advanced the task.

If focus never left the trigger, leave it there.

Component-specific patterns override this generic fallback.

## Tooltip

Tooltip content does not become a new keyboard-focus destination merely because it appears.

Interactive content belongs in another component/pattern such as Popover, not Tooltip.

---

# 8. Dynamic insertion and removal

Dynamic products frequently add/remove:
- table rows;
- candidate cards;
- chips;
- form sections;
- list items;
- menu items.

## Removing the focused item

**MUST**

If the currently focused element is removed, intentionally place focus on a logical remaining target.

Preferred candidates:
1. next equivalent item;
2. previous equivalent item if there is no next item;
3. parent/container control;
4. action that logically follows the completed workflow.

Do not allow focus to silently fall to `<body>` when that loses the user's position.

Example:

```text
Delete candidate row
→ focus next candidate row action

Last candidate removed
→ focus list heading / empty-state action as defined by pattern
```

## Adding content

**SHOULD NOT**

Automatically focus newly inserted content merely because it exists.

Move focus when:
- the user explicitly requested creation/editing and immediate interaction is expected;
- the new content is the logical next workflow step.

Otherwise preserve current focus and announce/update context as needed.

---

# 9. Hiding, disabling, or making content inert

## Hidden/inert content

**MUST**

Content that is visually/interactionally unavailable must not leave reachable interactive descendants in the sequential keyboard order.

Examples:
- closed Drawer;
- hidden menu;
- inactive Modal background;
- collapsed content that is not meant to remain operable.

Do not hide focusable content only visually while leaving it keyboard reachable.

## Disabling the focused control

**MUST**

Do not disable, hide, or remove the currently focused element in a way that causes unexplained focus loss.

If state transition requires it:
- preserve focus when possible;
- or move focus intentionally to the next logical target.

This is especially important during:
- async submit/loading;
- destructive actions;
- step transitions.

Exact behavior belongs in the component/pattern contract.

---

# 10. Forms and validation focus

Focus behavior is shared between `forms.md` and this document.

## Field-level validation

**SHOULD NOT**

Move focus to an error message on every blur/keystroke.

Keep the user at the field they are editing and expose the error programmatically/visually.

## Failed submission

**MUST**

After failed submission, the user must have a logical way to discover and reach the errors.

The exact focus strategy depends on form complexity.

### Small/simple form

**SHOULD**

Focus the first invalid field when that is the clearest recovery path.

### Large/multi-error form

**SHOULD**

Use an error summary near the beginning of the relevant form/step and focus that summary, especially when:
- several fields are invalid;
- errors span beyond the viewport;
- errors occur across sections.

The summary can use `tabindex="-1"` for programmatic focus without becoming a permanent Tab stop.

Do not make “always focus the first invalid field” a universal DS rule.

## Successful submission

Do not automatically return focus to the Submit Button if the workflow has clearly moved elsewhere.

Focus should follow the resulting workflow:
- new page/view heading;
- created object;
- confirmation context;
- next required step.

---

# 11. Loading and async states

## MUST

Loading behavior must not strand keyboard focus.

If a focused trigger starts loading:
- prefer preserving the user's focus point when the control remains conceptually present;
- prevent repeated activation through the component's defined loading contract;
- if the control is replaced/removed, move focus deliberately.

## SHOULD NOT

Move focus to a spinner/progress indicator unless the progress UI itself becomes the user's required interaction context.

Use status semantics/announcements for routine progress instead.

---

# 12. Selection is not focus

Keyboard Focus, Selected, Current, Checked, and Active are different concepts.

**MUST**

Do not use a Selected visual state as the only Focus indicator.

Examples:

```text
Tab
→ one item may be selected/current
→ another tab may temporarily hold keyboard focus depending on activation model

Listbox
→ selected option and focused option may differ during navigation

Checkbox
→ checked state persists after focus leaves
```

Component-specific keyboard patterns define when Focus movement also changes Selection.

---

# 13. Hover/focus-triggered content

When keyboard Focus reveals additional content that later disappears, WCAG 1.4.13 may apply.

For qualifying Hover/Focus content:

**MUST**
ensure the content is:
- dismissible where required;
- hoverable when pointer hover triggers it;
- persistent until the relevant dismissal conditions occur.

Focus management must not make the content impossible to inspect or dismiss.

Typical examples:
- Tooltip;
- custom hover/focus help;
- some Popovers.

Use the dedicated component contract rather than implementing ad hoc focus behavior.

---

# 14. Sticky/fixed product UI

JobVision/Cando contain dense operational interfaces where sticky/fixed controls may be useful.

Sticky UI is allowed.

It does **not** need to be removed merely to satisfy accessibility.

## MUST

Sticky/fixed author content must not completely hide the currently focused UI component.

## SHOULD

Reserve enough safe space that focused controls and focus rings remain fully visible when practical.

Test especially:
- desktop table/toolbars;
- sticky Modal footers;
- mobile bottom actions;
- support/chat FABs and panels;
- cookie/announcement banners;
- side navigation.

This is a layout/focus integration responsibility, not just a component token issue.

---

# 15. Focus and responsive / zoom states

At high zoom and narrow layouts:

**MUST**
- logical focus order remains understandable;
- focused controls remain operable;
- focus does not jump according to a desktop-only visual order;
- fixed/sticky regions do not fully obscure focused controls.

**SHOULD**
avoid programmatic focus movement that unexpectedly causes large horizontal/vertical jumps.

See `responsive-and-zoom.md`.

---

# 16. Practical ownership

| Design System / component owns | Product / pattern owns |
|---|---|
| Whether component is focusable | Whether/where component is used |
| Internal focus model | Cross-component workflow order |
| Modal containment mechanism | Correct initial-focus strategy for specific Modal |
| Restore-focus mechanism | Alternate restore target when workflow advances |
| Visible Focus treatment | Valid surface/context composition |
| Behavior if own internal item disappears | What should receive focus after product-level deletion |
| Trigger/popup focus contract | Why/when popup is opened |
| Component loading focus behavior | Resulting workflow after async success/failure |

If the decision depends on business/task meaning, it usually belongs to Product/Pattern rather than the atomic component.

---

# 17. Testing

For a feature/component where focus behavior is relevant, test the applicable subset.

## Keyboard walkthrough

Verify:
- initial entry point;
- Tab / Shift+Tab sequence;
- focus visibility;
- no unexpected traps;
- close/dismiss behavior;
- return/next focus after temporary contexts;
- focus after dynamic removal.

## Overlay

Verify:
- focus enters correctly;
- modal vs non-modal scope is correct;
- background interaction matches semantics;
- focus restoration is logical.

## Responsive / zoom

Verify:
- sticky/fixed content does not fully obscure focus;
- focused items scroll into view;
- reordered layouts preserve logical sequence.

## Forms

Verify:
- failed submission recovery;
- multi-error behavior;
- focus remains at the editing field during ordinary validation.

## Dynamic changes

Verify:
- removal of focused element;
- loading transitions;
- inserted content does not steal focus unnecessarily.

## Visual

Verify:
- Focus + Error;
- Focus + Selected;
- Focus on Light/Dark/Inverse supported contexts;
- focus indicator contrast according to `color-and-contrast.md`.

---

# 18. Anti-patterns

Avoid:

```text
outline: none
without an accessible replacement
```

```text
tabindex="1", "2", "3"...
to manually reconstruct page order
```

```text
Every route change
→ always focus h1
```

```text
Every async update
→ move focus to changed content
```

```text
Modal opens
→ always focus Primary Button
```

```text
Delete focused row
→ allow focus to fall to body
```

```text
Non-modal Popover
→ trap all page focus
```

```text
Closed Drawer
→ visually hidden but descendants remain tabbable
```

```text
Validation on blur
→ move focus away from the field
```

```text
Selected styling
→ treated as Focus styling
```

---

# 19. AI contract

When AI designs or implements focus behavior:

**MUST**
- identify whether the context is modal, non-modal, composite, navigation, form, or dynamic update;
- use the existing component focus contract first;
- preserve logical focus order;
- keep focused controls at least partially unobscured by author content;
- deliberately handle focus when the current focused element is removed;
- distinguish focus from selection;
- mark unresolved focus behavior instead of inventing it.

**SHOULD**
- move focus only when it improves/preserves user context;
- prefer native/default browser focus behavior when it already satisfies the interaction;
- avoid adding focus-management code to static/routine content unnecessarily.

---

# References

- WCAG 2.2 — 2.4.3 Focus Order
- WCAG 2.2 — 2.4.7 Focus Visible
- WCAG 2.2 — 2.4.11 Focus Not Obscured (Minimum)
- WCAG 2.2 — 2.4.12 Focus Not Obscured (Enhanced)
- WCAG 2.2 — 2.4.13 Focus Appearance
- WCAG 2.2 — 1.4.13 Content on Hover or Focus
- WAI-ARIA APG — Modal Dialog Pattern
