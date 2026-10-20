---
id: design-system.accessibility.component-authoring-contract
collection: design-system
type: accessibility
title: Component Accessibility Authoring Contract
summary: Minimum accessibility information a reusable Design System component must define before its accessibility behavior is considered complete.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
related:
- design-system.accessibility.core
- design-system.accessibility.router
last_reviewed: '2026-09-02'
---

# Component Accessibility Authoring Contract

Use this contract when **designing, redesigning, implementing, or materially changing a reusable Design System component**.

It is not required context for ordinary Product Design when the component already has an approved accessibility contract.

The goal is practical: define accessibility once at the reusable-component layer so downstream designers and developers do not need to re-solve the same behavior.

This Authoring Contract owns **what a reusable component guideline must decide and document**.

It is not the primary technical source for general ARIA, keyboard, focus, form, pointer, or responsive rules. Those mechanics remain owned by the corresponding specialized accessibility documents. The component guideline records the resolved component-specific contract.

## Core principle

A reusable component is not accessibility-complete merely because its visual states are complete.

Before a component's accessibility behavior is considered ready, its guideline must define every **applicable** item below.

Do not create empty boilerplate.

Use:

```text
Not applicable
```

when a concern genuinely does not apply.

Use:

```text
Open accessibility decision
```

when the concern applies but the behavior is unresolved.

AI MUST NOT convert an unresolved accessibility decision into an invented convention.

---

# 1. Classify documentation depth first

Before writing the Accessibility section, classify the component.

## Level 1 — Simple / native control

Examples:
- Button
- Link
- native Checkbox

Expected documentation:
- concise;
- relies heavily on native behavior and the Accessibility Core;
- usually one compact grouped `## Accessibility` section.

Do **not** mechanically create every subsection in this contract.

## Level 2 — Stateful native-based component

Examples:
- Text Input
- Accordion
- Switch
- segmented control

Expected documentation:
- semantics and labeling;
- relevant state model;
- focus/keyboard behavior where applicable;
- descriptions/errors;
- visual accessibility;
- a focused component-specific test list.

## Level 3 — Composite / overlay / custom widget

Examples:
- Modal
- Tabs
- Menu
- Listbox
- Combobox
- Tree
- interactive Grid

Expected documentation:
- full interaction contract;
- explicit interaction scope;
- native/platform primitive evaluation;
- focus and keyboard behavior;
- semantic state/relationship model;
- stronger manual testing.

The purpose of levels is to prevent simple components from accumulating complex-widget documentation.

---

# 2. Required component Accessibility section

Every reusable interactive component guideline MUST include an `## Accessibility` section.

A non-interactive component needs only the relevant subset.

Recommended structure for Level 2–3 components:

```md
## Accessibility

### Semantics and accessible name
...

### Keyboard and focus
...

### States
...

### Pointer / touch
...

### Visual accessibility
...

### Responsive / RTL
...

### Screen reader / announcements
...

### Testing
...

### Open accessibility decisions
...
```

Level 1 components MAY use a shorter grouped section.

The component guideline documents the **component contract**, not general accessibility theory.

---

# 3. Native/platform primitive evaluation

Before defining custom semantics or interaction for a reusable component:

**SHOULD**
Evaluate whether the current web platform already provides a suitable native primitive.

Record, when relevant:

```text
Native/platform primitive evaluated?
Can it satisfy the required behavior?
Why is a custom implementation necessary?
```

Examples:
- Button → native `<button>`
- Text Input → native `<input>`
- Modal → evaluate native `<dialog>` + `showModal()`

A custom implementation is allowed when native behavior is unsuitable, but complex accessibility mechanics should not be recreated without a reason.

---

# 4. Semantics

## MUST define

When applicable:
- preferred native HTML element(s);
- ARIA role only when native semantics are insufficient;
- meaningful semantic relationships;
- whether the component is interactive, presentational, structural, or composite.

Examples:

```text
Button
→ native <button>

Link
→ native <a href>

Text Input
→ native <input> with an associated label

Modal
→ modal-dialog semantics and actual modal behavior
```

## MUST NOT

- add ARIA only to match visual styling;
- use a semantic role without implementing the behavior that role implies;
- recreate a native control without an implementation need.

---

# 5. Accessible name and description

## MUST define, when applicable

- accessible-name source;
- whether a visible label is required;
- naming behavior for icon-only variants;
- description source for helper text, instructions, metadata, or errors;
- whether visible text must be associated programmatically.

Visible text SHOULD be the accessible-name source when practical.

Example:

```text
Icon Button
→ accessible name required from action meaning
→ icon alone is insufficient
→ Tooltip does not replace the accessible name
```

Define the semantic outcome first. Exact ARIA syntax belongs in implementation guidance only when needed.

---

# 6. Native behavior shortcut

For a component based on a native HTML control:

**MAY**
State:

```text
Preserve native behavior
```

when the native platform fully defines that interaction domain.

Do not duplicate large platform keyboard/interaction specifications without value.

Examples:
- Text Input should preserve normal native text editing, selection, and browser shortcuts.
- Native Button should preserve native Button activation behavior.

If the component overrides native behavior, the deviation MUST be documented.

---

# 7. Keyboard model

When native behavior does not fully determine the component interaction, define the applicable keyboard contract.

Possible keys:
- `Tab` / `Shift+Tab`
- `Enter`
- `Space`
- Arrow keys
- `Escape`
- `Home` / `End`
- Page keys
- Typeahead
- Custom shortcuts

## MUST

- avoid keyboard traps;
- preserve native keyboard behavior when using native controls;
- satisfy all applicable WCAG/WAI-ARIA requirements for the chosen widget semantics and interaction.

## SHOULD

- use the established APG pattern/keyboard behavior as the default reference for custom composite widgets unless a justified alternative is documented and tested;
- reference the relevant APG pattern rather than copying a generic keyboard table into every component guideline.

If a component guideline adopts a specific interaction model, implementation MUST follow that component contract until the contract is intentionally revised.

---

# 8. Focus behavior

Define focus behavior only when the component can receive, move, contain, restore, or lose focus.

## MUST define, when applicable

- whether the component is focusable;
- visible focus treatment;
- focus order within composite components;
- initial focus on open;
- focus containment;
- focus destination on close;
- behavior after focused content is removed;
- interaction between Focus and Error / Selected / Expanded states.

Simple controls can use a concise contract.

Level 3 components require a deeper focus contract.

---

# 9. Interaction scope — Level 3

For overlays and composite/custom widgets, explicitly define the active interaction scope.

Answer:

```text
What becomes active?
What becomes inactive or inert?
Where can focus travel?
What ends the interaction context?
What happens to focus after it ends?
```

Examples:
- Modal → background becomes inert; focus remains inside until close.
- Menu → menu receives a defined internal keyboard interaction scope but does not make the whole page inert.

This is separate from visual layering.

---

# 10. Context-dependent strategy points

Do not create a false universal rule when correct accessibility behavior depends on the task/content.

Instead define:

```text
Supported mechanism
+ default/fallback
+ context-controlled policy point
```

Examples:
- Modal initial focus;
- Modal focus restoration target;
- dismissal policy;
- Tab automatic vs manual activation when a Tabs component supports a configurable activation model.

The reusable component guarantees the mechanism. The consuming Pattern/Product chooses the contextual policy when needed.

---

# 11. Programmatic state and value

For each meaningful component state, determine whether it requires programmatic exposure.

Possible states include:

```text
disabled
readonly
checked
indeterminate
selected
current
pressed
expanded
invalid
required
busy/loading
value
```

## MUST

- define only states that materially affect meaning or operation;
- keep visual and programmatic state consistent;
- distinguish different concepts such as `disabled` and `readonly`.

## MUST NOT

Mechanically add every accessibility state to every component.

Example:

```text
Button
→ disabled: applicable
→ expanded: only for a control that actually expands content
→ selected: not a generic Button state
```

---

# 12. Mechanism vs consuming policy

For every reusable component, explicitly separate:

```text
What accessibility mechanism does the component provide?
vs.
What policy/value does the consuming Product or Pattern supply?
```

Examples:

### Text Input

Component provides:
- label mechanism;
- helper/error association;
- `required`, `invalid`, `readonly`, `disabled` support;
- autocomplete/input-purpose pass-through.

Product decides:
- whether this field is required;
- the validation rule;
- exact error copy;
- the appropriate autocomplete value.

### Modal

Component provides:
- focus containment;
- initial-focus mechanism;
- focus-restoration mechanism;
- supported dismissal mechanisms.

Pattern/Product decides:
- which initial focus target is correct;
- whether backdrop dismissal is appropriate;
- where focus should move if the workflow advances.

This separation prevents product policy from becoming hard-coded component behavior.

---

# 13. Pointer, touch, and gesture behavior

Interactive components MUST define relevant target/gesture constraints.

## MUST define, when applicable

- supported hit-target minimum;
- difference between visual size and hit target;
- hover-only dependencies;
- drag behavior and non-drag alternative;
- complex gesture alternative;
- pointer-cancellation considerations for high-impact actions.

Use the shared Accessibility Core for baseline target requirements instead of repeating standards text.

A component MAY define a stronger minimum when it is practical and consistently enforceable.

---

# 14. Visual accessibility

Each component guideline MUST define the accessibility implications of its supported visual states.

Use Semantic tokens rather than hard-coded values where possible.

Define, when applicable:
- text/background contrast pairing;
- essential boundary/state-indicator contrast;
- non-color state cue;
- Light / Dark / Inverse behavior;
- visible focus;
- disabled treatment;
- error treatment;
- forced/high-contrast resilience where custom styling may remove essential cues.

Example:

```text
Text Input Error
→ line/error
→ textual error message
→ programmatic invalid state
```

not:

```text
Error
→ red border only
```

Primitive colors are not individually validated in the component guideline; semantic pairings are.

---

# 15. Responsive, zoom, text, and RTL behavior

Define when component anatomy can be affected by content or layout constraints.

Consider:
- label/value wrapping;
- long Persian strings;
- text enlargement;
- zoom/reflow;
- truncation;
- fixed heights;
- overflow;
- content reordering;
- RTL;
- mixed Persian/English values;
- directional icon mirroring.

## MUST

Essential component information or function must not disappear because the component assumes short text or a fixed desktop layout.

## SHOULD

Do not add a generic Responsive section to a simple component unless it has a real component-level risk.

---

# 16. Motion, timing, and updating content

Only required for components that animate, auto-update, auto-advance, expire, or display timed content.

Define, when relevant:
- what the motion communicates;
- reduced-motion behavior;
- auto-advance behavior;
- pause/stop controls;
- time-limit behavior;
- loading/progress semantics.

Static components should not include this as boilerplate.

---

# 17. Screen-reader output and announcements

Define the **semantic information** assistive technology must receive, not an exact phrase from a particular screen reader.

When applicable, define:

```text
Name
Role
State / value
Description
Relationship
Status announcement
```

## MUST

- avoid duplicate announcements;
- define status/live behavior when the component itself generates important asynchronous feedback;
- avoid assertive interruption for routine status.

Exact screen-reader wording should only be documented for a known implementation-specific test/debugging need.

---

# 18. Composition boundaries

A component guideline MUST distinguish:

```text
What the component guarantees
vs.
What the consuming Pattern/Flow must decide
```

Examples:

### Button owns
- Button semantics;
- focus state;
- disabled behavior;
- target behavior;
- accessible-name requirement.

Button does not own:
- form validation;
- whether Submit should be disabled;
- where focus moves after submission;
- success/error announcement for the workflow.

### Modal owns
- modal semantics;
- interaction scope;
- focus containment/restoration mechanism.

Modal does not own:
- destructive-confirmation wording;
- form-validation policy;
- post-submit workflow routing.

When accessibility depends on composition, reference the relevant Pattern guideline.

---

# 19. Testing contract

Every reusable interactive component MUST include a small component-specific accessibility test list.

Do not paste the full global accessibility testing checklist.

Choose only applicable tests:

```text
Keyboard
Focus
Name / role / state
Screen reader
Contrast
Zoom / text resize
RTL / long content
Pointer / target size
Reduced motion
Forced/high-contrast mode
Interaction scope
```

Example for Button:

```md
### Accessibility testing

- Keyboard: native activation works.
- Focus: visible in supported surface contexts.
- Semantics: exposes Button name and Disabled state.
- Pointer: every supported size meets the component target contract.
```

Complex Level 3 components require deeper tests.

`testing.md` remains the shared testing-methodology source.

---

# 20. Open accessibility decisions

If a relevant behavior is unresolved, record it explicitly.

Example:

```md
### Open accessibility decisions

- Decide automatic vs manual Tab activation.
- Validate focus behavior when the selected item is removed.
```

## MUST

An unresolved accessibility decision blocks claiming that specific behavior as canonical.

It does not automatically block unrelated, already-resolved component behavior.

---

# Definition of accessibility-ready

A reusable component may be considered **accessibility-ready for its current scope** when:

1. all applicable accessibility behavior is defined;
2. unresolved decisions are explicit;
3. component mechanisms are separated from Pattern/Product policy;
4. implementation matches the defined semantics and interaction;
5. applicable component-specific accessibility tests pass.

Accessibility-ready does **not** mean:
- every possible future variant is solved;
- every WCAG criterion is copied into the component guideline;
- every specialized accessibility document has been read;
- no future assistive-technology defect can occur.

---

# AI authoring procedure

When AI is asked to design or implement a reusable Design System component:

```text
1. Read Accessibility Core.
2. Read this Authoring Contract.
3. Classify the component as Level 1 / 2 / 3.
4. Read the existing Component guideline.
5. Evaluate relevant native/platform primitives.
6. Retrieve only specialized accessibility docs triggered by unresolved component behavior.

6a. Classify material requirements as WCAG/standards, JV policy, or best-practice guidance when that distinction affects MUST/SHOULD.
7. Define the applicable Accessibility contract.
8. Separate component mechanisms from consuming policy values.
9. Mark unresolved behavior explicitly.
10. Validate representative component usage.
11. Create a component-specific accessibility test list.
```

AI MUST NOT:
- generate every section mechanically;
- invent unresolved ARIA or focus behavior;
- load every accessibility document by default.
