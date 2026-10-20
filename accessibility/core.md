---
id: design-system.accessibility.core
collection: design-system
type: accessibility
title: Accessibility Core
summary: Compact accessibility baseline that must be considered for every design and frontend implementation task.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
related:
- design-system.accessibility.conformance-and-policy
- design-system.accessibility.router
last_reviewed: '2026-09-02'
---

# Accessibility Core

This file is the compact accessibility baseline that should be available to AI for every design and frontend implementation task. It intentionally contains only high-value cross-cutting rules. Detailed mechanics belong in specialized accessibility documents and component/pattern guidelines.

## Scope

Applies to:
- product design;
- design-system design;
- frontend implementation;
- design-system implementation;
- accessibility review and QA.

This is a web baseline. Native iOS/Android products require platform-specific accessibility guidance in addition to the shared principles here.

## Standards baseline

**MUST**
- Target WCAG 2.2 Level AA for web products, including all applicable Level A and AA Success Criteria.
- Prefer native HTML semantics.
- Use WAI-ARIA only when native semantics are insufficient and according to current ARIA-in-HTML constraints.

**SHOULD**
- Use established APG interaction patterns as the default behavioral reference for custom widgets when native HTML does not provide the required interaction, unless a component guideline documents a justified alternative.

APG is guidance rather than a normative W3C conformance standard. Any underlying WCAG, WAI-ARIA, or ARIA-in-HTML requirement remains mandatory when applicable.

Stable web semantics baseline:
- WAI-ARIA 1.2.
- ARIA 1.3 draft features are not default production guidance.

## Requirement levels

Every accessibility rule in the design system MUST use one of these levels:

### MUST
Required baseline.

A MUST can come from:
- an applicable WCAG A/AA or other adopted standards requirement;
- an explicit JV hard policy;
- a required component/pattern contract.

If a criterion-defined standards exception genuinely applies, the requirement may be satisfied through that exception.

Approval to ship a known MUST failure is product/release risk acceptance. It does **not** convert the failure into a WCAG exception or conformance.

### SHOULD
Default design-system recommendation. It may be deviated from when density, platform constraints, technical cost, or another usability concern creates a reasonable trade-off.

### CONSIDER
Optional enhancement to use when relevant and practical.

AI MUST NOT silently promote or downgrade requirement levels.

For SHOULD deviations, documentation is only required when the deviation becomes a reusable component or design-system decision.

## Core rules

### 1. Native semantics first

**MUST**
Use the native semantic element when it can correctly express the control or content.

Examples:
- action → `button`;
- navigation → `a`;
- text entry → `input` / `textarea`;
- ordinary choice controls → native checkbox, radio, select where appropriate.

**SHOULD**
Create a custom widget only when the native control does not satisfy the product requirement.

### 2. Accessible name, role, and state

**MUST**
Every interactive control exposes enough programmatic information for assistive technology:
- accessible name;
- correct role/element;
- relevant state or value.

Relevant states can include:
- disabled;
- expanded;
- selected/current;
- checked/pressed;
- invalid;
- required;
- busy/loading.

Visible label text SHOULD be the accessible-name source when practical.

### 3. Keyboard access

**MUST**
All functionality that is operable with a pointer must also be keyboard operable when the function is not inherently path-dependent.

**MUST**
No keyboard trap.

**SHOULD**
Use the established native/APG keyboard model for custom composite widgets rather than inventing a new interaction model.

### 4. Focus

**MUST**
Keyboard focus is visibly identifiable.

**MUST**
Author-created sticky/fixed content must not completely obscure the focused component.

**SHOULD**
Use a strong, consistent focus treatment that approaches the WCAG Focus Appearance model:
- visible area roughly equivalent to a 2 CSS px perimeter;
- approximately 3:1 focused/unfocused contrast change.

The exact Focus Appearance geometry is a recommended internal target, not currently a hard JV requirement.

### 5. Color and visual meaning

**MUST**
Do not use color as the only carrier of essential information or state.

**MUST**
Applicable WCAG AA text and non-text contrast requirements are met.

**SHOULD**
Design ordinary UI text tokens to reach at least 4.5:1 in their intended normal-text contexts instead of depending on the large-text exception as the default palette strategy.

Primitive color steps are not individually required to be accessible; semantic pairings are.

### 6. Pointer and touch

**MUST**
Pointer targets meet WCAG 2.5.8 Target Size (Minimum): at least 24×24 CSS px or a valid criterion exception.

**SHOULD**
Frequently used or important controls in touch-oriented UI use a larger target, roughly 40–44 CSS px or more where practical.

Dense desktop UI does not need to enlarge every control to 44 px when doing so harms useful information density and the minimum requirement is otherwise met.

Visual icon size and hit-target size are independent.

### 7. Dragging and gestures

**MUST**
Where required by WCAG, functionality that uses dragging also provides a single-pointer alternative unless dragging is essential.

**MUST**
Where required by WCAG, complex/path-based gestures have a simpler pointer alternative unless the gesture is essential.

**MUST**
When functionality can be operated by device motion or user motion, provide the required user-interface alternative and a way to disable motion response unless a WCAG 2.5.4 exception applies.

Device/user motion used as an input mechanism is different from visual animation or reduced-motion preferences.

### 8. Responsive layout and text adaptation

**MUST**
Essential content and functionality remain available with required text resize, zoom, and reflow.

**MUST**
Visual reordering must not create a contradictory reading or keyboard focus order.

**SHOULD**
Components and flows are tested with:
- long Persian content;
- RTL;
- mixed Persian/English strings.

### 9. Forms and errors

**MUST**
Form controls have an accessible name/label.

**MUST**
Placeholder text is not the only label.

**MUST**
Errors are not communicated by color alone and are programmatically associated with the relevant control where applicable.

**SHOULD**
Avoid validation that interrupts users while they are still entering a value unless immediate feedback materially helps completion.

**SHOULD**
Do not disable a submit/continue action when doing so makes the reason the user cannot proceed unclear.

### 10. Motion and time

**MUST**
Meet applicable WCAG A/AA requirements for flashing, moving or auto-updating content, time limits, and motion-actuated input.

**SHOULD**
Non-essential motion respects the user's reduced-motion preference and provides a lower-motion alternative without losing information.

### 11. Dynamic feedback

**MUST**
Important status changes that do not receive focus are exposed programmatically when required.

Examples:
- submission succeeded;
- save failed;
- results updated;
- item added or removed.

**SHOULD**
Routine updates should not use unnecessarily interruptive announcements.

### 12. Testing

**MUST**
Do not claim a feature is accessible based only on automated testing.

For interactive work, validate the applicable subset of:
- keyboard operation;
- focus behavior;
- accessible name/role/state;
- screen-reader output;
- contrast;
- zoom/reflow;
- reduced motion;
- pointer/touch behavior.

The accessibility router determines which specialized checks and documents apply to a task.

### 13. Unknown behavior

**MUST**
When accessibility behavior is unresolved:
- do not guess;
- do not invent ARIA;
- do not copy a visually similar component's behavior without validation.

Instead:
1. retrieve the relevant component/pattern/accessibility guideline;
2. use established native/APG behavior when applicable;
3. otherwise mark the behavior as an explicit accessibility gap.

## Layering rule

This Core does not contain component-specific implementation details.

Accessibility ownership is layered:

1. **Core**
   - small rules relevant to almost all design/development tasks.

2. **Specialized accessibility docs**
   - detailed cross-cutting rules such as color, focus, forms, keyboard, semantics, motion, and testing.

3. **Component guidelines**
   - exact accessibility contract for a component: semantics, keyboard behavior, states, focus behavior, accessible naming, and supported contexts.

4. **Pattern/flow guidelines**
   - accessibility created by composition, sequencing, dynamic feedback, and context.

5. **Component accessibility authoring contract**
   - used when designing or implementing a reusable design-system component; not required context for ordinary product-design tasks.

### Ownership order vs retrieval order

The layering list above describes **where accessibility rules are owned**.

It does not require AI to retrieve documents in that same order.

For task execution, the Accessibility Task Router may retrieve an approved Component/Pattern contract before specialized mechanics so that mature reusable behavior is not re-derived. Specialized docs remain the cross-cutting rule source and are loaded when the component/pattern contract is incomplete, challenged, or does not resolve the task.

## AI retrieval rule

AI must apply all accessibility requirements relevant to the task, but MUST NOT load every accessibility document for every task.

The task router should determine the smallest sufficient set of specialized accessibility and component/pattern documents.

## Primary references

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- WCAG 2.2 Quick Reference: https://www.w3.org/WAI/WCAG22/quickref/
- WAI-ARIA: https://www.w3.org/WAI/standards-guidelines/aria/
- ARIA in HTML: https://www.w3.org/TR/html-aria/
- WAI-ARIA APG: https://www.w3.org/WAI/ARIA/apg/
