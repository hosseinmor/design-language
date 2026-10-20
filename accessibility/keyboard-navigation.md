---
id: design-system.accessibility.keyboard-navigation
collection: design-system
type: accessibility
title: Keyboard Navigation
summary: Defines practical keyboard access, native behavior, composite-widget navigation, shortcuts, disabled-item behavior, and testing requirements.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.focus-management
- design-system.accessibility.screen-reader-semantics
- design-system.accessibility.pointer-touch-and-gestures
last_reviewed: '2026-09-02'
---

# Keyboard Navigation

This document defines how functionality remains operable by keyboard and how custom/composite components should expose predictable keyboard interaction.

It does **not** require every interactive element to implement the same keys.

The practical model is:

```text
Native control
→ preserve native keyboard behavior

Custom/composite widget
→ use its established component/APG keyboard pattern

Product flow
→ do not invent extra keyboard behavior unless it adds real value
```

---

# 1. Keyboard-operable functionality

## WCAG baseline

**MUST**

All functionality must be operable through a keyboard interface when the function is not inherently dependent on the path of pointer movement.

This is WCAG 2.1.1 Keyboard, Level A.

Examples that must have keyboard access:
- buttons and links;
- form controls;
- menus;
- tabs;
- expandable controls;
- sortable/filterable data controls;
- actions revealed on hover;
- item actions in cards/tables;
- reordering when the operation can be represented through discrete actions.

A feature is not keyboard accessible merely because the user can Tab to something.

The user must be able to **perform the actual operation**.

## Path-dependent exception

Some functions inherently depend on movement path, such as freehand drawing.

Do not broaden this exception to ordinary drag/reorder interactions.

Example:

```text
Reorder rows by drag
→ keyboard-accessible alternative can be Move up / Move down
```

Pointer-specific alternatives are also covered in `pointer-touch-and-gestures.md`.

---

# 2. Native controls first

**MUST**

Use native interactive HTML when it correctly represents the control.

Examples:

```text
action
→ <button>

navigation
→ <a href>

boolean choice
→ native checkbox where appropriate

text entry
→ native input / textarea
```

Native controls already provide browser/platform keyboard behavior.

**MUST NOT**

Rebuild a native control with a `div` plus `tabindex` and key handlers without a real product/implementation reason.

Example:

```text
<div tabindex="0" onclick="save()">
  Save
</div>

✕
```

Prefer:

```text
<button>
  Save
</button>
```

## Preserve native activation

**MUST**

Do not override native keyboard behavior in a way that breaks expected operation.

For example:
- native Button already supports keyboard activation;
- native Link already has navigation keyboard behavior;
- Text Input already has rich editing/navigation shortcuts.

Do not add redundant key handlers to native controls that cause:
- double activation;
- blocked browser behavior;
- blocked assistive-technology shortcuts.

---

# 3. Tab is for moving between interaction stops

For ordinary page-level navigation:

```text
Tab
→ next focusable interaction stop

Shift + Tab
→ previous focusable interaction stop
```

## MUST

The sequential keyboard path must:
- reach all required interactive functionality;
- preserve meaningful order;
- not enter hidden/inert UI;
- not contain unexplained traps.

See `focus-management.md` for focus order.

## SHOULD NOT

Make static content routinely tabbable.

Examples that generally should **not** become Tab stops:
- headings;
- paragraphs;
- decorative icons;
- table cells with no interaction;
- containers added only for layout.

Static content can receive `tabindex="-1"` when programmatic focus is needed for orientation without adding a normal Tab stop.

---

# 4. Composite widgets should usually be one Tab stop

Complex widgets often contain multiple internal options/items.

Examples:
- Tabs;
- Menu;
- Menubar;
- Listbox;
- Radio group;
- Toolbar;
- Tree;
- Grid;
- Combobox popup.

For these components, making every internal item a normal Tab stop can create excessive and unexpected keyboard navigation.

## SHOULD

Follow the established component/APG model:

```text
Tab / Shift+Tab
→ enters or leaves the composite

Arrow keys / component-specific keys
→ move within the composite
```

The exact model belongs in the component guideline.

Examples:

```text
Tabs
→ Tab reaches the tablist/current tab stop
→ Arrow keys move among tabs

Menu
→ Tab enters/leaves according to Menu pattern
→ Arrow keys move among menu items

Radio group
→ one group-level stop in normal sequential navigation
→ Arrow keys change/move among radio options according to native/pattern behavior
```

Do not generalize this model to every group of controls.

A group of ordinary independent Buttons remains separate Tab stops unless it is intentionally implemented as a composite such as Toolbar.

---

# 5. Focus management inside composites

Two common implementation strategies are valid.

## Roving tabindex

Typical model:

```text
active item
→ tabindex="0"

other items
→ tabindex="-1"

Arrow navigation
→ moves DOM focus
→ updates which item has tabindex="0"
```

Useful when actual DOM focus should move among items.

## aria-activedescendant

Typical model:

```text
DOM focus remains on container/input
+
aria-activedescendant identifies active internal item
```

Useful in patterns where retaining DOM focus on the container/input is beneficial, such as some Listbox/Combobox implementations.

## MUST

For a reusable component:
- choose a coherent model;
- expose the correct active item visually and programmatically;
- preserve the component's expected focus position after updates;
- ensure the referenced active descendant is valid in the accessibility tree.

## MUST NOT

Mix focus strategies ad hoc within the same component in a way that creates two competing notions of keyboard focus.

The component guideline owns the chosen approach.

---

# 6. Arrow-key behavior is component-specific

Do not create a global rule such as:

```text
Arrow keys always navigate every grouped control
```

or:

```text
Left always means previous
Right always means next
```

Arrow behavior depends on:
- widget role;
- orientation;
- selection model;
- spatial meaning;
- value model;
- RTL/LTR behavior.

## MUST

Use the established keyboard model for the actual component.

Examples:
- Tabs use directional navigation among tabs;
- Menu uses directional navigation and submenu behavior;
- Slider arrows change value;
- Text Input arrows move the text caret;
- Data Grid may use arrows between cells only when implemented as an interactive Grid.

## RTL

**MUST NOT**

Blindly reverse all Left/Right keyboard behavior just because the page is RTL.

Some interactions follow:
- visual/spatial order;
- logical previous/next;
- numeric increase/decrease;
- platform/native behavior.

The component contract must define RTL behavior when direction materially changes expected navigation.

---

# 7. Enter and Space

Enter and Space do not have one universal meaning across all components.

**MUST**

Preserve native behavior for native controls.

For custom components, follow the established pattern.

Typical examples:

```text
native Button
→ Enter / Space activation

native Link
→ Enter activation/navigation

native Checkbox
→ Space toggles

Menu item
→ activation according to Menu pattern
```

**MUST NOT**

Add Space activation to every element that can be focused.

Doing so can:
- break page scrolling;
- conflict with text entry;
- create nonstandard behavior.

---

# 8. Escape and dismissal

Escape is a common dismissal/cancel key for temporary contexts, but it is not a universal “go back” key.

Typical contexts:
- Modal;
- Menu;
- Combobox popup;
- dismissible Popover;
- some editing/cancel modes.

## MUST

If a component's established keyboard pattern uses Escape, support it consistently.

## MUST NOT

Use Escape globally for:
- route navigation;
- arbitrary page back behavior;
- destructive action;
- behavior that conflicts with an active component context.

Examples:

```text
Modal
→ Escape closes when dismissible

Menu
→ Escape closes and returns to logical trigger context

Page
→ Escape does not mean browser Back
```

Exact behavior belongs in the component/pattern contract.

---

# 9. No keyboard trap

## WCAG baseline

**MUST**

If keyboard focus can enter a component, users must be able to move focus away using a keyboard interface.

This is WCAG 2.1.2 No Keyboard Trap, Level A.

If a nonstandard exit method is required, the user must be informed.

## Modal containment is not automatically a trap

A true Modal intentionally keeps Tab focus inside while it is active.

This is acceptable when the user has a keyboard-operable way to:
- close the Modal when dismissible;
- complete/cancel the task according to its contract;
- otherwise leave the interaction context.

A broken Modal that offers no keyboard route out or forward is a keyboard trap.

---

# 10. Hidden and collapsed content

**MUST**

Interactive descendants of content that is currently unavailable must not remain accidentally reachable by Tab.

Examples:
- closed Drawer;
- collapsed Menu;
- hidden Popover;
- inactive Modal background;
- collapsed disclosure region when its content is not meant to be active.

Visual hiding alone is insufficient if keyboard interaction remains possible.

Coordinate with focus-management and semantic hiding/inertness behavior.

---

# 11. Disabled items

Disabled keyboard behavior depends on component type.

## Native controls

For ordinary native controls:

**SHOULD**
preserve native disabled behavior unless the component contract has a reason not to.

Native disabled controls are commonly removed from sequential focus navigation.

## Composite widgets

Some established APG patterns keep disabled items discoverable during **arrow-key navigation** even though they cannot be activated.

This can be useful in:
- menus;
- toolbars;
- list-like composites.

## MUST

Define disabled-item focusability at the component level.

## MUST NOT

Apply one universal rule:

```text
all disabled items must be focusable
```

or:

```text
all disabled items must be skipped
```

The correct behavior depends on native semantics and the composite pattern.

---

# 12. Hover-only functionality

**MUST**

Functionality exposed through pointer hover must also be discoverable/operable through keyboard when it is interactive or required for completing the task.

Examples:
- card action shown on hover;
- table row action;
- reveal/edit control;
- help trigger.

Do not rely on:

```text
:hover
```

as the only route to an action.

The keyboard route does not always need to reproduce the identical visual hover state; it needs to expose equivalent functionality.

---

# 13. Keyboard shortcuts

Keyboard shortcuts are enhancements.

They do not replace ordinary keyboard navigation and activation.

**MUST**

Core functionality remains discoverable and usable without knowing a shortcut.

## Character-key shortcuts

WCAG 2.1.4 Character Key Shortcuts applies when a keyboard shortcut uses **only** one or more printable character keys such as letters, numbers, punctuation, or symbols.

If such a shortcut is active:

**MUST**
provide at least one applicable solution:
- ability to turn it off;
- ability to remap it to include one or more non-printable modifier keys;
- make it active only while the relevant UI component has focus.

This avoids accidental activation during speech input or ordinary typing.

## Modifier shortcuts

Shortcuts using `Ctrl`, `Command`, `Alt`, etc. are not covered by the same character-only condition, but they can still conflict with:
- browser shortcuts;
- operating-system shortcuts;
- assistive technology;
- text editing;
- international keyboard layouts.

**SHOULD**
avoid overriding established platform/browser shortcuts.

**SHOULD**
use platform-appropriate conventions if shortcuts are offered.

Examples:

```text
Windows/Linux
→ Ctrl + ...

macOS
→ Command + ...
```

when applicable.

## Global shortcuts

**SHOULD**
be rare in form-heavy products unless they provide substantial repeated-user value.

JobVision/Cando include dense data-entry and operational contexts; global single-letter shortcuts can easily conflict with typing.

---

# 14. Shortcut discovery

When a non-obvious shortcut materially improves a repeated workflow:

**SHOULD**
make it discoverable where practical.

Possible methods:
- Menu label;
- Tooltip/help;
- command/help panel;
- documentation;
- `aria-keyshortcuts` where semantically useful.

Do not assume exposing `aria-keyshortcuts` alone makes the shortcut visually discoverable.

Keyboard shortcuts should augment, not replace, standard navigation.

---

# 15. Text-entry contexts

**MUST**

Do not intercept ordinary typing/editing keys inside editable controls unless the component's established pattern requires it.

Preserve expected behavior for:
- character entry;
- Arrow navigation/caret movement;
- Home/End where native;
- selection shortcuts;
- copy/paste/cut;
- Undo/Redo;
- browser/assistive-technology text navigation.

This is especially important for:
- Text Input;
- Textarea;
- search fields;
- contenteditable editors.

Combobox is an exception only to the extent its component pattern intentionally shares keys between text editing and popup navigation.

The Combobox guideline must define those interactions precisely.

---

# 16. Selection and keyboard focus

Focus and selection are different states.

Do not assume keyboard focus automatically changes selection.

Component patterns define the relationship.

Examples:

```text
Tabs
→ may use automatic activation
or manual activation
→ component contract must choose

Listbox
→ focus movement and selection may be coupled or separate depending on selection model

Checkbox
→ Space changes checked state
→ Tab moving away does not clear checked state
```

If automatic selection causes expensive/slow content changes, a manual activation model may be more usable.

---

# 17. Repeated/dense controls

Dense operational products like Cando ATS can contain many actions.

Keyboard accessibility does **not** mean:

```text
make every visible cell/card fragment a Tab stop
```

## SHOULD

Reduce unnecessary Tab stops by:
- using semantic grouping;
- using established composite widgets when the UI truly behaves as one;
- moving rare actions into an accessible Menu;
- avoiding redundant clickable wrappers around already-interactive child controls.

Do not convert a dense table into ARIA Grid merely to reduce Tab stops.

Use Grid only when the interaction model genuinely requires cell-level keyboard navigation.

---

# 18. Cards and clickable containers

A visual card is not itself a keyboard pattern.

If the whole card navigates:

**SHOULD**
use a real Link strategy appropriate to the card structure.

If the whole card performs an action:

**SHOULD**
use Button semantics only when the entire card truly represents one action.

If a card contains several independent controls:

**MUST NOT**
make the wrapper a competing generic keyboard control that creates nested/ambiguous interactions.

Prefer normal child Link/Button controls and a clear focus order.

---

# 19. Virtualized and dynamic composites

Virtualized lists/grids can remove DOM items while keyboard navigation is active.

For components using virtualization:

**MUST**
preserve a coherent keyboard position and accessible active-item relationship.

If the active/focused item is removed or recycled:
- intentionally select/focus the next logical item;
- keep `aria-activedescendant` references valid where used;
- do not let focus fall silently to the document body.

This behavior belongs in the reusable component contract, not individual product screens.

---

# 20. Product vs component ownership

| Component / Design System owns | Product / Pattern owns |
|---|---|
| Native vs custom keyboard model | Correct component choice |
| Internal Arrow/Home/End behavior | Page-level task order |
| Escape behavior for component context | Why/when context opens |
| Composite focus strategy | Product sequence after completion |
| Disabled-item navigation behavior | Whether item should be disabled |
| Shortcut mechanism if component includes one | Whether a product shortcut is worthwhile |
| RTL keyboard behavior when component-specific | Product content/layout direction |
| Keyboard-specific tests | Whole-flow keyboard walkthrough |

Product designers should not re-invent the internal keyboard model of a mature DS component.

---

# 21. Testing

For any feature with interactive behavior:

## Basic keyboard walkthrough

Test using keyboard only:
- `Tab`;
- `Shift+Tab`;
- `Enter`;
- `Space`;
- `Escape` where applicable;
- Arrow keys where the component contract defines them.

Verify:
- all required functionality is reachable;
- activation works;
- order is logical;
- no hidden content receives focus;
- no trap exists;
- focus remains visible.

## Composite components

Also verify:
- Tab enters/leaves as designed;
- internal directional keys work;
- disabled items behave according to contract;
- Home/End/typeahead where supported;
- selection vs focus behavior;
- focus is preserved after dynamic updates.

## Text entry

Verify:
- ordinary editing/navigation keys are not blocked;
- product/global shortcuts do not fire while typing unless intentionally scoped.

## Shortcuts

Verify:
- standard functionality remains available without shortcut;
- conflicts with browser/OS/AT are considered;
- character-only shortcuts meet WCAG 2.1.4;
- shortcut is discoverable when required by product design.

## RTL

Test directional composite behavior in actual RTL UI instead of assuming mirrored behavior.

---

# 22. Anti-patterns

Avoid:

```text
Clickable div
+ tabindex=0
+ custom key handlers
when native Button/Link would work
```

```text
Every item in a Menu/Tabs/Radio group
→ independent Tab stop
```

```text
Every group of Buttons
→ Arrow-key composite
```

```text
All Left/Right behavior
→ blindly reversed in RTL
```

```text
Space
→ activate every focusable element
```

```text
Single-letter global shortcuts
→ active while user is typing
```

```text
Hidden Drawer
→ controls still tabbable
```

```text
Native Text Input
→ Arrow keys intercepted for page navigation
```

```text
Disabled behavior
→ same rule forced on every native/composite component
```

```text
ARIA Grid
→ added just to reduce number of Tab stops
```

---

# 23. AI contract

When AI designs or implements keyboard behavior:

**MUST**
- first identify whether the control is native, simple custom, or composite;
- preserve native behavior when available;
- use the existing component/APG keyboard contract for custom widgets;
- ensure actual functionality, not only focusability, is keyboard operable;
- distinguish Tab navigation from internal composite navigation;
- avoid keyboard traps;
- preserve text-entry behavior;
- mark unresolved keyboard behavior instead of inventing keys.

**SHOULD**
- minimize unnecessary Tab stops;
- avoid custom/global shortcuts unless they materially improve repeated workflows;
- reference the component pattern instead of duplicating large key tables into Product Design docs;
- test RTL behavior when horizontal directional keys are involved.

---

# References

- WCAG 2.2 — 2.1.1 Keyboard
- WCAG 2.2 — 2.1.2 No Keyboard Trap
- WCAG 2.2 — 2.1.4 Character Key Shortcuts
- WCAG 2.2 — 2.4.3 Focus Order
- WAI-ARIA APG — Developing a Keyboard Interface
- WAI-ARIA APG — Design Patterns and Widgets
