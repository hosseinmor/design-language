---
id: design-system.accessibility.testing
collection: design-system
type: accessibility
title: Accessibility Testing
summary: Defines practical accessibility test scope, evidence, manual and automated checks, complete-process evaluation, and specialized validation coverage.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.conformance-and-policy
- design-system.accessibility.router
last_reviewed: '2026-09-02'
---

# Accessibility Testing

This document owns **how and what to test**. `conformance-and-policy.md` owns the meaning of WCAG conformance, formal claims, standards exceptions, partial-conformance terminology, accessibility support policy, and risk acceptance.

Testing evidence does not silently redefine product behavior or component contracts.

## 1. Evidence rule

**MUST NOT** claim a component, feature, page, or process is accessible solely because an automated scanner passes.

Automated tools are valuable for detectable classes such as invalid/missing semantics, some contrast problems, duplicate IDs, and common ARIA misuse. They do not establish keyboard/focus quality, meaningful accessible names, interaction correctness, full screen-reader behavior, reflow, or complete-process conformance.

## 2. Test the applicable scope

Select tests based on the Router triggers and the actual feature/component behavior.

Do not run every specialized test on every static page merely for completeness.

For interactive work, consider the applicable subset:
- keyboard operation;
- focus visibility/order/management;
- name/role/state/value/relationships;
- screen-reader behavior;
- contrast/color meaning;
- pointer/touch/target/gesture behavior;
- zoom/reflow/text spacing/RTL;
- form labels/errors/authentication;
- dynamic status/async feedback;
- motion/timing/flashing;
- image/media alternatives;
- table/grid/data-visualization behavior.

## 3. Component vs product/process evidence

A reusable component test proves only its defined component scope.

A Product feature **MUST** also validate accessibility created by composition: page order, actual labels/content, cross-component focus, validation, navigation, responsive layout, status feedback, permissions/states, and workflow sequence.

Using a tested Design System does not prove a Product flow is conformant.

## 4. Full-page and complete-process evaluation

For evidence intended to support WCAG conformance, evaluate full pages and required complete processes according to `conformance-and-policy.md`.

Examples include authentication, job application/resume submission, job creation, package purchase, and required approval/submission flows.

A passing first step does not prove a multi-step process passes.

For formal product/site evaluation, **SHOULD** use WCAG-EM 2.0 or an equivalently rigorous documented evaluation method.

## 5. Keyboard test

For applicable interactive features:
- complete the required task using keyboard only;
- verify Tab/Shift+Tab order;
- test Enter/Space/Escape/Arrow/Home/End only where the component contract defines them;
- verify all functionality, not merely focusability;
- verify no keyboard trap;
- verify hidden/inert content is not tabbable;
- verify text-entry keys/shortcuts remain usable.

## 6. Focus test

Verify:
- focus is visibly identifiable;
- sticky/fixed author content does not completely obscure it;
- programmatic focus changes are logical;
- Modal focus enters/contains/restores according to contract;
- non-modal UI does not create modal trapping;
- removing the focused element relocates focus deliberately;
- loading/async transitions do not strand focus;
- Focus remains distinguishable from Selected/Error/Expanded state.

## 7. Semantics and screen reader

Inspect the accessibility tree and test representative supported AT/browser combinations for complex/shared widgets.

Verify:
- name/role/state/value;
- visible label in accessible name;
- descriptions and relationships;
- state synchronization;
- hidden/decorative exposure;
- repeated control names distinguishable in context;
- custom widget interaction remains operable.

Do not require identical spoken strings across screen readers; test the semantic outcome.

## 8. Forms

Test applicable:
- persistent/accessible labels;
- required/readonly/disabled/invalid semantics;
- helper/error association;
- one error and multiple simultaneous errors;
- failed-submit recovery/focus strategy;
- data preservation;
- correct autocomplete/input purpose;
- password manager and paste;
- Accessible Authentication;
- Redundant Entry across multi-step process;
- Error Prevention only where WCAG 3.3.4 scope actually applies.

### On Focus / On Input

Explicitly test WCAG 3.2.1 and 3.2.2 when focus/value changes can navigate, open a new window, move focus, submit, or otherwise create a change of context.

Record whether the behavior is a true change of context or only a local UI update. If a value change causes a context change, verify prior advice as required by 3.2.2.

## 9. Consistent Help

When qualifying Help/Support/Contact/Chat/self-help mechanisms exist across a set of pages:
1. identify the repeated mechanism(s);
2. sample representative pages in the set;
3. compare their relative order to other page content;
4. account for user-initiated personalization/change.

Do **not** report a WCAG 3.2.6 failure merely because a page has no Help mechanism.

## 10. Pointer, touch, gestures, and Motion Actuation

Test applicable:
- 24×24 CSS px Target Size (Minimum) or valid criterion exception;
- pointer cancellation for custom/high-impact interaction;
- single-pointer alternative to multipoint/path gestures;
- single-pointer non-drag alternative for dragging;
- keyboard access separately where required;
- hover-only functionality availability by keyboard/touch.

### WCAG 2.5.4 Motion Actuation

When shake, tilt, device sensors, camera-detected body/head motion, or other user/device motion operates functionality:
- verify the same function has a UI-component alternative;
- verify users can disable responding to motion;
- record any criterion-defined exception relied upon.

Run this separately from reduced-motion/animation testing.

## 11. Motion, timing, flashing

Test applicable:
- flashing threshold;
- pause/stop/hide for qualifying moving/blinking/auto-updating content;
- product-set time limits;
- autoplay audio/media controls;
- reduced-motion preference as JV guidance;
- retention of meaning/function when non-essential motion is reduced.

Do not classify WCAG AAA Animation from Interactions as an AA failure.

## 12. Contrast and color

Test actual resolved Semantic pairings in supported product/mode/surface contexts.

Verify:
- text contrast;
- essential non-text UI/graphical contrast;
- non-color cues for state/meaning;
- focus indicator contrast;
- composited alpha/transparent values;
- JobVision/Cando Brand differences;
- Light/Dark/Inverse contexts.

Disabled controls do not receive an invented hard WCAG contrast ratio; test their distinguishability/clarity under the component contract.

## 13. Responsive / zoom / RTL

Test applicable:
- 200% text resize;
- zoom/reflow reference widths;
- WCAG text-spacing override;
- narrow/mobile layout;
- horizontal overflow only where legitimate;
- long Persian content;
- mixed Persian/English strings;
- RTL reading/focus order;
- focused content around sticky/fixed UI.

## 14. Tables / Grid / visualization

### Data Table
Test table/header relationships, keyboard access to embedded controls, sort/filter state, repeated action naming, responsive overflow, and screen-reader table navigation.

### Interactive Grid
A custom Grid **MUST** be tested against its component contract plus keyboard/focus/semantics. Include entry/exit, internal navigation, selection vs focus, edit mode, virtualization, RTL where relevant, and representative AT/browser interoperability.

Do not approve Grid semantics merely because `role="grid"` exists.

### Charts
Verify equivalent data/summary, non-color cues, graphical contrast, keyboard/touch interaction where interactive, and dynamic updates.

## 15. Images/media

Test informative vs decorative alternatives, functional icon control names, complex-image equivalent information, applicable captions/audio description/media alternatives, and accessible media controls.

## 16. Accessibility-supported implementation evidence

For complex/custom/new platform behavior relied upon by a shared component, use representative combinations from the product's browser/assistive-technology support matrix.

Theoretical markup correctness is not sufficient proof of interoperability.

## 17. Result format

For material review findings, record:

```text
scope
requirement / component contract
input method / environment
steps
affected behavior
expected
actual
user impact
pass / fail / not applicable / blocked
owner or owning document
```

For a known MUST failure intentionally shipped, link the risk/debt record. Do not call risk acceptance a standards exception.

## 18. Validation gate for accessibility knowledge changes

When changing this accessibility corpus, run these repository/content gates before owner review:

### Gate 1 — missing A/AA ownership
- Motion Actuation 2.5.4 → Pointer/Touch owner + Router trigger + test.
- On Focus 3.2.1 → Structure owner + Router trigger + test.
- On Input 3.2.2 → Structure owner + Router trigger + test.
- Consistent Help 3.2.6 → Structure owner + Router trigger + test.
- No false claim that 3.2.6 requires adding Help.
- Motion Actuation kept distinct from reduced motion.

### Gate 2 — standards level consistency
- APG is system-level `SHOULD` guidance, not presented as a normative W3C conformance requirement.
- Applicable WCAG/WAI-ARIA/ARIA-in-HTML requirements remain `MUST`.
- Risk acceptance remains distinct from WCAG criterion exceptions.
- AAA criteria remain labeled AAA unless explicitly adopted as stronger JV policy.

### Gate 3 — retrieval integrity
- internal IDs and related references resolve;
- `Modal` is the component name; modal dialog is its semantic model;
- Router uses actual repository maturity metadata;
- Router does not stop on draft/scaffold/unknown component contracts;
- no obsolete `principles` document remains as a parallel canonical baseline.

### Gate 4 — ownership boundaries
- Conformance owns claim/exception/risk language; Testing owns test method/evidence.
- Forms owns validation model; Focus owns movement/recovery; Dynamic owns status/live mechanism.
- Screen Reader Semantics owns cross-cutting technical semantics; Component Authoring Contract owns what reusable components must document.
- Apply/Screening product policy is not invented inside specialized accessibility docs.

### Gate 5 — repository stress tests
Run Button, Text Input, Modal, Data Table/Interactive Grid, and JobVision Apply + Screening Questions through the actual Router. Record retrieval path, component/pattern maturity, specialized escalation, ambiguity/conflict, and final verdict.

## 19. AI contract

AI **MUST** choose tests based on actual behavior, separate evidence from conformance claims, preserve complete-process scope where applicable, run Motion Actuation separately from reduced-motion tests, explicitly test On Focus/On Input/Consistent Help when triggered, and never turn scanner output or a passing component into a formal WCAG claim.

## References

- WCAG 2.2
- WCAG-EM 2.0
- WAI-ARIA 1.2 / APG
- `conformance-and-policy.md`
