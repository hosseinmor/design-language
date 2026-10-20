---
id: design-system.accessibility.conformance-and-policy
collection: design-system
type: accessibility
title: Accessibility Conformance and Policy
summary: Defines the WCAG baseline, internal requirement levels, evidence language, exceptions, ownership, support expectations, and accessibility-debt policy.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.router
- design-system.accessibility.testing
last_reviewed: '2026-09-02'
---

# Accessibility Conformance and Policy

This document defines how JobVision and Cando interpret and operationalize accessibility requirements for web Design System work, Product Design, frontend implementation, testing, and accessibility reporting.

It intentionally separates:

```text
WCAG conformance
from
JV accessibility-ready status
from
JV internal recommendations
```

These are not interchangeable.

---

# 1. Scope

This policy applies to:

- JobVision web products;
- Cando web products;
- shared web Design System components and patterns;
- Product Design and frontend implementation;
- accessibility review and QA.

Native iOS/Android implementations require platform-specific accessibility guidance in addition to the shared principles here.

ARIA implementation rules are web-specific and must not be copied directly into native-app accessibility APIs.

---

# 2. Baseline

## WCAG baseline

**MUST**

Web products target **WCAG 2.2 Level AA**.

For content and functionality in scope, this means satisfying every applicable:

```text
Level A Success Criterion
+
Level AA Success Criterion
```

A Level AAA criterion is not automatically a JV requirement.

WCAG itself does not recommend requiring Level AAA conformance as a general policy for entire sites.

## Supporting standards

**MUST**

- prefer valid native HTML semantics;
- follow ARIA-in-HTML constraints when ARIA is used;
- treat WAI-ARIA 1.2 as the stable production baseline unless a later stable version is explicitly adopted.

**SHOULD**

Use established WAI-ARIA APG patterns as the default behavioral reference for custom widgets when native HTML does not provide the required interaction.

APG is not itself a normative W3C standard and does not define an independent conformance model.

This `SHOULD` applies to adopting APG as the default pattern/reference. It does not downgrade normative requirements that a pattern relies on:
- applicable WCAG A/AA requirements remain `MUST`;
- WAI-ARIA role/state/property requirements remain `MUST` when that ARIA pattern is used;
- ARIA-in-HTML constraints remain `MUST`.

A component guideline may make a chosen interaction contract mandatory for that component after the design-system decision is made.

**MUST NOT**

Use draft-only ARIA behavior as a production assumption without explicit review and interoperability evidence.

---

# 3. Three sources of accessibility rules

Every accessibility rule should be understandable as one of these:

## A. WCAG requirement

An applicable WCAG 2.2 Level A or AA requirement.

```text
Example:
Keyboard-operable functionality
→ WCAG requirement
→ MUST
```

A team preference cannot downgrade it.

## B. JV internal policy

A rule intentionally adopted by JV beyond or more specifically than WCAG.

Example:

```text
Ordinary UI text palette
→ design around ≥4.5:1 where practical
→ SHOULD
```

or, if explicitly adopted later:

```text
A stronger requirement
→ JV MUST
```

The document must not imply that an internal JV rule is itself WCAG AA.

## C. Best-practice enhancement

Useful accessibility or usability guidance that is not a baseline requirement.

```text
→ SHOULD or CONSIDER
```

AI and documentation MUST preserve this distinction.

---

# 4. Requirement levels

Accessibility documentation uses:

## MUST

Required for the defined scope.

A MUST may come from:
- applicable WCAG A/AA;
- an explicitly adopted JV requirement;
- a component/pattern contract required to preserve accessible behavior.

A MUST failure cannot be relabeled SHOULD merely because it is difficult or late.

## SHOULD

Default recommendation.

Deviation is acceptable when a real product, platform, density, or implementation trade-off justifies it and no underlying MUST requirement is violated.

One-off SHOULD deviations do not require process-heavy documentation.

A reusable Design System deviation SHOULD be documented.

## CONSIDER

Optional improvement.

No exception process is required.

---

# 5. WCAG conformance is not a component-level claim

WCAG 2.2 conformance is defined for **full web pages**, and complete multi-page processes must conform as a whole.

Therefore:

**MUST NOT**

Describe an isolated Design System component as:

```text
"WCAG 2.2 AA compliant"
```

or:

```text
"WCAG AA conformant"
```

A reusable component can instead be described as:

```text
accessibility-ready for its defined scope
tested against the applicable accessibility contract
tested against the relevant WCAG requirements
```

Similarly, a screen fragment or isolated feature test is not by itself a formal WCAG conformance claim.

This distinction prevents stronger claims than the evidence supports.

---

# 6. Full-page and complete-process rule

For formal WCAG conformance:

**MUST**

Evaluate the full page, including automatically presented responsive variations.

A page cannot be declared conformant while excluding a non-conforming region of that page.

**MUST**

When a page belongs to a required sequence for completing a user activity, evaluate the **complete process**.

Examples in JV products include:

- sign-up/login and authentication;
- job application and resume submission;
- job-post creation;
- package purchase/payment;
- employer onboarding;
- required approval/submission flows.

Example:

```text
Apply step 1 passes
Apply step 2 passes
Submit confirmation fails keyboard access

→ the complete application process does not conform
```

Do not use an accessible first step as evidence that the whole process is accessible.

---

# 7. Accessibility-supported technologies

WCAG conformance may rely only on **accessibility-supported ways of using technologies**.

In practical terms, when a feature depends on:
- custom ARIA;
- a new browser API;
- unusual CSS/DOM behavior;
- a complex third-party widget;
- a new native web primitive with uncertain interoperability;

there must be reasonable evidence that the relied-upon use works with the user agents and assistive technologies relevant to the product environment.

## Product support matrix

**SHOULD**

Each web product maintains a practical browser / assistive-technology test matrix.

The matrix should identify:
- supported browsers/platforms;
- representative screen-reader/browser combinations;
- important mobile accessibility combinations where relevant;
- known interoperability limitations.

W3C does **not** prescribe one universal number or set of assistive technologies that proves “accessibility support.”

JV should therefore choose a defensible product test matrix based on:
- supported browsers;
- user environment;
- technical risk;
- component complexity;
- language/RTL needs.

## Practical rule

Ordinary Design/Product work does not wait for a perfect universal AT matrix.

But a new complex/shared interaction MUST NOT be treated as proven merely because its ARIA markup appears theoretically correct.

---

# 8. Non-interference

Content or technology that is not relied upon for conformance must still not prevent access to the rest of the page.

WCAG applies specific non-interference protections even to content that is otherwise outside the relied-upon accessibility path.

In practice:

**MUST NOT**

Allow optional, third-party, experimental, or non-accessibility-supported content to:
- create a keyboard trap;
- introduce prohibited flashing;
- create moving/blinking content that blocks use in ways covered by WCAG;
- otherwise prevent use of the conforming content.

An “accessible alternative” is not sufficient if the inaccessible version itself interferes with the page.

---

# 9. Exceptions and deviations

This policy distinguishes **standards exceptions** from **product risk acceptance**.

They are not the same thing.

## A. Explicit WCAG exception

Some Success Criteria contain explicit exceptions.

Example:

```text
Target Size Minimum
→ 24×24 CSS px
→ or an applicable criterion-defined exception
```

If the exception truly applies, this is not a failure.

## B. Criterion-defined essential exception

Some criteria include an `essential` exception.

Use it only when the specific WCAG criterion permits it and the functionality genuinely cannot maintain the same purpose without that behavior.

Do not use “essential” as a generic justification for inconvenience.

## C. JV SHOULD deviation

A SHOULD may be deviated from when a reasonable trade-off exists and no MUST is violated.

This is not a WCAG exception because none is needed.

## D. Known MUST failure / risk acceptance

A product team may decide to release with a known accessibility defect for operational reasons.

If an applicable MUST still fails:

```text
→ record it as known non-conformance / accessibility debt
→ do not describe it as an exception to WCAG
→ do not make a conformance claim that ignores it
```

Approval to ship is a product/release decision.

It does not convert a failure into conformance.

---

# 10. Third-party content and dependencies

Third-party ownership does not automatically remove accessibility responsibility from the user experience.

**MUST**

Evaluate third-party content/components when users depend on them to complete an important task.

If the dependency fails accessibility requirements:

1. remediate or configure it where possible;
2. prefer a more accessible dependency when practical;
3. provide an equivalent accessible path where possible;
4. document the remaining risk and ownership.

## Partial conformance terminology

**MUST NOT**

Use “partial conformance” as a casual synonym for:

```text
mostly accessible
known accessibility bugs
third-party library issue
temporary technical debt
```

WCAG defines specific Statements of Partial Conformance, including cases involving content from uncontrolled third-party sources and language accessibility support.

When those formal conditions do not apply, say:

```text
does not currently conform
```

or describe the tested scope and known failures directly.

---

# 11. Design System vs Product ownership

Accessibility is shared, but ownership should be explicit.

| Design System owns | Product/Feature owns |
|---|---|
| Component semantics and mechanisms | Correct component choice |
| Supported keyboard behavior | Flow-specific sequencing |
| Component focus behavior | Focus between pages/steps when not component-owned |
| Component states | Which state applies in business context |
| Component target-size contract | Placement and surrounding spacing |
| Semantic token accessibility contract | Valid component/surface pairing |
| Component responsive anatomy | Page/layout composition |
| Component accessible-name mechanism | Actual label/copy |
| Component validation/error mechanism | Validation rules and error wording |
| Component tests | Whole-flow/process testing |

A conforming component can be composed into an inaccessible feature.

A Product Designer/Developer therefore cannot treat “uses Design System” as proof of feature accessibility.

---

# 12. Internal accessibility status language

Use status language proportional to evidence.

## For Design System components

Preferred:

```text
Scaffold
→ accessibility behavior not yet defined

Accessibility contract defined
→ behavior specified; implementation/test may still be pending

Accessibility-ready for current scope
→ applicable behavior defined + implementation matches + component tests pass

Known accessibility gap
→ one or more applicable behaviors remain unresolved/failing
```

## For product features / flows

Preferred:

```text
Designed against WCAG 2.2 AA baseline
Tested against the listed accessibility checks
No known failures in the tested scope
Known accessibility issues remain: ...
```

Do not jump from “axe passed” or “component passed” to:

```text
WCAG 2.2 AA conformant
```

---

# 13. Formal conformance claims

WCAG conformance claims are optional.

If a formal WCAG 2.2 claim is made, WCAG requires the claim to include:
- date;
- WCAG title/version/URI;
- conformance level;
- concise description of the pages in scope;
- web technologies relied upon.

**MUST NOT**

AI, automated tools, a Figma review, or one component test make a formal WCAG conformance claim from partial evidence.

## Evaluation method

**SHOULD**

Use the current **WCAG Evaluation Methodology (WCAG-EM 2.0)** or an equivalently rigorous documented evaluation process when producing product/site-level evidence intended to support a formal conformance statement.

WCAG-EM 2.0:
- defines evaluation scope;
- explores the product;
- selects representative samples where appropriate;
- evaluates the sample;
- reports findings.

WCAG-EM does not add new WCAG requirements.

It is an evaluation methodology, not a replacement for WCAG.

---

# 14. Automated and manual evidence

Automated accessibility checks are valuable but cannot establish full conformance.

**MUST**

Do not mark a reusable interactive component or feature accessibility-ready solely because automated checks pass.

Manual evaluation is required where applicable for behavior such as:
- keyboard interaction;
- focus order/management;
- accessible name quality;
- screen-reader behavior;
- semantic relationships;
- zoom/reflow;
- state communication;
- contextual error handling.

Automated checks SHOULD be used aggressively for what they can reliably detect.

Do not use their limitations as a reason to skip automation.

---

# 15. Accessibility debt

Accessibility debt should be managed proportionally.

## MUST record

A known applicable MUST failure when it:
- affects a critical or required process;
- exists in a shared Design System component;
- can block or substantially impair task completion;
- is intentionally shipped unresolved;
- affects a formal conformance scope.

Record at minimum:

```text
issue
affected scope
requirement / contract
user impact
owner
workaround if any
status
```

A due date or target release SHOULD be added for significant issues.

## SHOULD NOT require formal debt records for

- every missed CONSIDER;
- one-off SHOULD trade-offs;
- purely advisory improvements.

The goal is risk visibility, not documentation overhead.

---

# 16. Resolving accessibility vs product constraints

When accessibility conflicts with density, visual hierarchy, technical constraints, or delivery pressure:

## If a MUST is involved

1. identify the exact requirement;
2. check whether a real criterion exception applies;
3. search for an alternative compliant solution;
4. preserve product intent where possible;
5. if the failure is intentionally shipped, record it as known accessibility debt/non-conformance.

**MUST NOT**
quietly downgrade the requirement.

## If a SHOULD is involved

Choose the better overall product trade-off.

Example:

```text
44px touch target
→ SHOULD

32px dense desktop toolbar target
→ may be acceptable
provided the applicable WCAG minimum is satisfied
```

This is why JV separates hard baseline from recommendation.

---

# 17. AAA policy

Level AAA is **not** a blanket JV conformance requirement.

AAA criteria may be adopted selectively as:
- `SHOULD`;
- `CONSIDER`;
- or an explicit JV `MUST` after product/design-system approval.

When referencing an AAA criterion, documentation MUST label it accurately.

Example:

```text
WCAG 2.4.13 Focus Appearance
→ Level AAA
→ JV SHOULD quality target
```

Do not describe it as an AA requirement.

---

# 18. Legal and regulatory scope

WCAG is the technical accessibility baseline defined here.

This policy does not by itself establish compliance with:
- European Accessibility Act;
- EN 301 549;
- ADA;
- BITV;
- or another jurisdiction-specific law/regulation.

If a product needs a regulatory claim or procurement declaration, map the applicable legal/technical requirements separately.

Do not use “WCAG AA” and “legally compliant” as interchangeable phrases.

---

# 19. AI contract

AI working with JV accessibility knowledge:

**MUST**
- preserve `MUST / SHOULD / CONSIDER`;
- identify whether a rule comes from WCAG or JV policy when material;
- apply only criteria relevant to the task;
- distinguish component accessibility-readiness from page/process conformance;
- flag known failures and unresolved behavior;
- not invent WCAG exceptions;
- not call product risk acceptance “compliance”;
- not make a formal conformance claim from incomplete evidence;
- not use “partial conformance” loosely.

**SHOULD**
- find the smallest compliant product solution rather than automatically choosing the most conservative layout;
- prefer reusable Design System fixes when the same accessibility defect affects multiple products.

---

# 20. Practical decision table

| Situation | Status |
|---|---|
| Applicable WCAG A/AA passes | Baseline satisfied for that criterion |
| Explicit criterion exception truly applies | Requirement satisfied through exception |
| JV SHOULD not followed, WCAG still passes | Acceptable trade-off |
| Applicable WCAG/JV MUST fails | Known accessibility failure |
| Team approves shipping that failure | Product risk accepted; still a failure |
| Automated scanner passes | Useful evidence, not conformance proof |
| Shared component contract/tests pass | Component may be accessibility-ready for its scope |
| One component passes inside a flow | Does not prove flow conformance |
| Full scoped evaluation passes applicable WCAG conformance requirements | May support a formal conformance claim |
| Uncontrolled third-party content meets WCAG partial-conformance conditions | Formal Statement of Partial Conformance may be considered |

---

# References

- WCAG 2.2 — Conformance
- Understanding Conformance
- Understanding Accessibility-Supported Web Technology Uses
- WCAG Evaluation Methodology (WCAG-EM) 2.0
- ARIA in HTML
- WAI-ARIA 1.2
