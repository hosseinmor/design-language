---
id: design-system.accessibility.router
collection: design-system
type: accessibility
title: Accessibility Task Router
summary: Routes design and frontend tasks to the smallest sufficient accessibility context.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.component-authoring-contract
last_reviewed: '2026-09-02'
---

# Accessibility Task Router

This router determines the **smallest sufficient accessibility context** for a design, implementation, or review task.

It does not replace the Accessibility Core, specialized accessibility documents, component guidelines, or pattern guidelines.

## Routing principle

**Always apply every accessibility requirement relevant to the task.
Do not load every accessibility document for every task.**

The routing sequence is:

```text
Task
→ classify work type
→ load Accessibility Core
→ load relevant component/pattern guidelines
→ detect accessibility domain triggers
→ load only unresolved/relevant specialized docs
→ escalate depth for high-risk/custom behavior
→ perform applicable tests
```

## 1. Always-loaded context

For every web design or frontend implementation task:

```text
accessibility/core.md
```

The Core is intentionally compact and contains the baseline rules that should not require specialized retrieval.

## 2. Classify the work type

Choose the primary work type based on the requested outcome, not the user's job title.

### A. Product Design

Examples:
- design a page, flow, modal, form, dashboard, or feature;
- revise UX using existing design-system components;
- define states, information architecture, or interaction flow.

Default retrieval:

```text
Core
+ relevant Component guidelines
+ relevant Pattern guidelines
```

Load specialized accessibility docs only when:
- the component/pattern guideline does not already resolve the accessibility question;
- accessibility emerges from composition or flow;
- the design introduces custom behavior;
- a domain trigger below applies materially.

Product Design should not load low-level ARIA implementation guidance by default.

### B. Product Implementation

Examples:
- implement a product screen or flow;
- integrate existing DS components;
- implement validation, routing, async feedback, or responsive behavior.

Default retrieval:

```text
Core
+ relevant Component guidelines
+ relevant Pattern guidelines
```

Then add specialized docs for feature-level behavior not already encapsulated by components, especially:
- page structure;
- focus across view changes;
- forms/validation;
- dynamic feedback;
- responsive/reflow;
- custom interaction.

If existing DS components already define their internal accessibility contract, do not re-derive their internal ARIA/keyboard mechanics.

### C. Design-System Component Design

Examples:
- design a new shared component;
- redesign component states or interaction;
- define a component's accessibility behavior.

Default retrieval:

```text
Core
+ component-accessibility-authoring-contract.md
+ existing/new Component guideline
+ all specialized docs materially relevant to that component
```

This route is intentionally deeper because accessibility behavior is being encoded for downstream reuse.

### D. Design-System Component Implementation

Examples:
- implement a shared Button, Modal, Combobox, Tabs, Input, Menu, or other DS component;
- revise shared DOM/ARIA/keyboard behavior.

Default retrieval:

```text
Core
+ component-accessibility-authoring-contract.md
+ Component guideline
+ relevant specialized docs
+ testing.md
```

For custom widgets, use native semantics or the established APG pattern as the behavioral reference.

### E. Accessibility Review / QA

Examples:
- audit a component or flow;
- investigate an accessibility regression;
- verify accessibility before release.

Default retrieval:

```text
Core
+ testing.md
+ relevant Component/Pattern guidelines
+ specialized docs implicated by the behavior under review
```

Do not load unrelated accessibility domains merely because the task is an audit.

## 3. Component and pattern guidelines come before specialized mechanics

When a component or pattern already has an approved accessibility contract, use that contract as the primary task-level source.

Example:

```text
Product task uses Button
→ read components/button.md
→ do not also load keyboard + semantics + pointer docs
   unless the task changes Button behavior or exposes an unresolved question
```

This is how the Design System encapsulates accessibility.

Specialized docs remain the source for:
- cross-cutting rules;
- rationale;
- unresolved behavior;
- designing/implementing the reusable component itself.

### Encapsulation precondition

A Component/Pattern guideline may replace lower-level specialized retrieval only when its accessibility contract is sufficiently mature for the task.

Use the repository's existing maturity metadata rather than inventing a separate accessibility-maturity schema:

```text
knowledge_state: canonical
+
document_maturity: reviewed | stable
```

The metadata is a necessary signal, not sufficient evidence by itself. The behavior relevant to the current task must also be defined in the guideline and must not be listed as an open/known gap.

Treat the contract as **not sufficient for retrieval stopping** when any of the following is true:
- `document_maturity` is `scaffold`, `draft`, missing, or otherwise not reviewed/stable;
- `knowledge_state` is not `canonical`;
- the relevant accessibility behavior is undefined or listed as an open/known gap;
- the task changes or challenges the component's documented accessibility behavior;
- implementation evidence shows a known gap;
- the contract does not cover the triggered domain.

In those cases:

```text
Component/Pattern guideline
+ directly relevant Specialized doc(s)
```

must be loaded until the unresolved behavior is specified.

Do not infer maturity from the existence of a component filename alone.

## 4. Domain triggers

Add the corresponding specialized document when the task materially involves the trigger and the requirement is not already resolved by an approved component/pattern contract.

### Color / contrast

Triggers:
- palette or token design;
- foreground/background changes;
- status colors;
- focus color;
- disabled colors;
- chart colors;
- Light/Dark/Inverse color decisions.

Load:

```text
color-and-contrast.md
```

### Forms / validation / authentication

Triggers:
- input;
- form;
- required fields;
- error handling;
- validation;
- autocomplete;
- login/password/OTP;
- multi-step data entry.

Load:

```text
forms.md
```

Also load `content.md` when labels, instructions, errors, or form copy are being designed.

### Keyboard / custom interaction

Triggers:
- custom interactive widget;
- custom keyboard behavior;
- menu;
- combobox;
- listbox;
- tabs;
- tree;
- grid;
- roving focus;
- shortcuts.

Load:

```text
keyboard-navigation.md
```

Add `focus-management.md` when focus movement/order is part of the behavior.

### Focus / overlays / context change

Triggers:
- dialog/modal;
- popover/menu;
- drawer;
- route/view replacement;
- opening/closing temporary UI;
- removing the focused item;
- sticky/fixed UI;
- validation focus strategy.

Load:

```text
focus-management.md
```

### Screen-reader semantics / ARIA

Triggers:
- custom widget;
- custom ARIA;
- icon-only control;
- ambiguous accessible naming;
- programmatic state;
- relationships not provided by native HTML;
- component implementation where semantic behavior is unresolved.

Load:

```text
screen-reader-semantics.md
```

Do not load this document merely because a normal product screen contains buttons, links, or inputs whose component semantics are already defined.

### Dynamic feedback

Triggers:
- toast;
- alert;
- status;
- async save;
- loading;
- search-result updates;
- item added/removed;
- background processing;
- notification that does not receive focus.

Load:

```text
dynamic-content-and-feedback.md
```

### Responsive / zoom / RTL

Triggers:
- responsive redesign;
- dense layout;
- sticky/fixed regions;
- horizontal overflow;
- truncation;
- layout reordering;
- mobile adaptation;
- RTL/bidirectional complexity.

Load:

```text
responsive-and-zoom.md
```

Core rules remain applicable even when this specialized document is not loaded.

### Pointer / touch / gestures

Triggers:
- small or dense targets;
- icon-only action;
- drag/drop;
- swipe;
- multipoint/path gesture;
- touch-primary interface;
- hover-dependent interaction;
- device-motion input;
- user-motion / sensor gesture input;
- shake / tilt / camera-detected gesture used to operate functionality;

Load:

```text
pointer-touch-and-gestures.md
```

### Motion / time / auto-update

Triggers:
- animation;
- transition that moves/zooms content substantially;
- carousel;
- autoplay;
- timeout/session expiry;
- blinking/flashing;
- auto-refresh;
- repeated moving content.

Load:

```text
motion.md
```

Do not load for ordinary short state transitions already defined by the component unless motion behavior is being changed.

### Content / language

Triggers:
- UX copy;
- labels;
- instructions;
- ambiguous links;
- heading wording;
- bilingual content;
- Persian/English mixed strings;
- accessible-name wording.

Load:

```text
content.md
```

### Page structure / navigation

Triggers:
- page shell;
- navigation architecture;
- headings/landmarks;
- breadcrumbs;
- skip behavior;
- route/view titles;
- reading-order changes;
- focus-triggered context change;
- input/value change that may cause navigation, new window, or other change of context;
- repeated Help / Support / Contact / Chat / self-help mechanisms across pages (WCAG 3.2.6 Consistent Help);

Load:

```text
structure-and-navigation.md
```

### Images / icons / media

Triggers:
- informative/decorative image;
- icon semantics;
- icon-only control;
- video/audio;
- complex infographic.

Load:

```text
images-icons-and-media.md
```

For icon-only interactive controls, the Component guideline remains primary; load this document when the image/icon content decision itself is unresolved.

### Tables / grids / data visualization

Triggers:
- data table;
- sortable/filterable table;
- interactive grid;
- chart;
- graph;
- dashboard visualization;
- color-coded data.

Load:

```text
tables-and-data-visualization.md
```

Add `color-and-contrast.md` when visual encoding or contrast is being decided.

## 5. High-risk escalation

Increase accessibility retrieval/testing depth when the task introduces one or more of these:

```text
custom interactive widget
modal or focus-trapped context
drag-only interaction
authentication
legal/financial/irreversible submission
complex validation
data grid
data visualization carrying essential information
time limit / session expiry
auto-updating or auto-advancing content
custom keyboard shortcuts
new ARIA behavior
device/user motion used as an input mechanism when the behavior is custom/shared or relies on sensors
```

Escalation means:
- load the directly relevant specialized docs;
- consult the component authoring contract if reusable behavior is being created;
- include manual keyboard/screen-reader testing requirements;
- explicitly record unresolved accessibility decisions.

It does **not** mean “load all accessibility docs.”

## 6. Typical routes

### Product designer uses existing Button in a simple page

```text
Core
+ Button guideline
```

No additional accessibility document required unless the page creates another trigger.

### Product designer creates a multi-step form

```text
Core
+ relevant Input / Select / Button guidelines
+ multi-step-flow pattern
+ forms.md
+ content.md
```

Add focus/dynamic feedback only if those behaviors need design decisions not already resolved by the pattern/components.

### Product designer creates a modal form

```text
Core
+ Modal guideline
+ relevant form components
+ confirmation/form pattern
+ forms.md
```

If Modal already defines open/close/focus behavior, do not reload `focus-management.md` unless the flow changes or challenges that behavior.

`Modal` is the Design System component name; its web accessibility semantic model is a modal dialog.

### Product developer implements an existing modal form

```text
Core
+ Modal guideline
+ form component guidelines
+ relevant Pattern guideline
+ forms.md
```

Add `dynamic-content-and-feedback.md` for async submit/status behavior.

### DS designer creates Combobox

```text
Core
+ component-accessibility-authoring-contract.md
+ Combobox guideline/draft
+ keyboard-navigation.md
+ focus-management.md
+ screen-reader-semantics.md
+ forms.md
+ pointer-touch-and-gestures.md
+ responsive-and-zoom.md
```

### DS developer implements Combobox

```text
Core
+ component-accessibility-authoring-contract.md
+ Combobox guideline
+ keyboard-navigation.md
+ focus-management.md
+ screen-reader-semantics.md
+ forms.md
+ pointer-touch-and-gestures.md
+ testing.md
```

### Color token / primitive palette work

```text
Core
+ color-and-contrast.md
```

Add relevant component consumers only when validating whether the palette supports real semantic use cases.

### Toast redesign

```text
Core
+ Notification/Toast component guideline
+ dynamic-content-and-feedback.md
+ color-and-contrast.md   # if visual severity/contrast changes
```

### Table-heavy ATS screen

Product design:

```text
Core
+ Table guideline
+ relevant controls
+ tables-and-data-visualization.md
```

Add responsive or pointer docs only if dense/overflow/target behavior is being changed.

## 7. Retrieval stop rule

Stop retrieving documents only when all accessibility behavior relevant to the task is sufficiently specified by:

```text
Core
+ selected approved/mature Component/Pattern contracts
+ selected specialized docs
```

A Component/Pattern guideline counts as an encapsulating contract only when the repository maturity signals show `knowledge_state: canonical` and `document_maturity: reviewed | stable`, **and** the behavior relevant to the current task is defined and not blocked by an open/known accessibility gap.

If contract maturity is unknown, `draft`, or `scaffold`, do not assume encapsulation; retrieve the directly relevant specialized document or mark an evidence gap.

Do not retrieve additional documents “just in case.”

A typical product-design task should usually need:
- Core;
- its relevant mature component/pattern guidelines;
- zero to three specialized accessibility docs.

Complex, custom, or immature component work may legitimately require more.

## 8. Missing guidance rule

If routing identifies an accessibility domain but:
- no relevant specialized doc exists;
- the component guideline is incomplete;
- two docs conflict;
- expected behavior is ambiguous;

then AI MUST mark an explicit accessibility gap and ask for/prepare a design-system decision when that gap materially affects the result.

Do not silently invent a new accessibility convention.

## 9. Metadata and maturity

Use the repository's existing Design System frontmatter as the retrieval signal. Do not introduce a parallel accessibility maturity field solely for this router.

For component/pattern encapsulation, interpret:

```yaml
knowledge_state: canonical
document_maturity: reviewed  # or stable
```

as the minimum metadata precondition for a mature contract. `scaffold`, `draft`, missing, or unknown maturity requires escalation to the relevant specialized accessibility docs.

Where `design_status` / `design_maturity` exist, they may provide additional product-design context, but they do not override an incomplete accessibility contract.

Metadata never overrides explicit `Known Gaps`, open decisions, or missing behavior in the document body.

## Relationship to the repository AI router

`ai/router.md` selects the primary product-knowledge/design workflow.

This Accessibility Router is subordinate to that route.

Example:

```text
User asks to design a new product flow
→ ai/router.md selects design-start
→ design-start retrieves relevant Design System knowledge
→ accessibility/router.md selects the smallest sufficient accessibility subset
```

Accessibility routing must not turn into a parallel mandatory workflow that loads the entire accessibility library.
