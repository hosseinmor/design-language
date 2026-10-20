---
id: design-system.accessibility.structure-and-navigation
collection: design-system
type: accessibility
title: Structure and Navigation
summary: Defines page structure, headings, landmarks, bypass/navigation, page titles, predictable context changes, and Consistent Help ownership.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.focus-management
- design-system.accessibility.content
- design-system.accessibility.forms
last_reviewed: '2026-09-02'
---

# Structure and Navigation

This document owns page/view structure and predictable navigation/context behavior. It is the canonical specialized owner for WCAG **3.2.1 On Focus**, **3.2.2 On Input**, and **3.2.6 Consistent Help**.

## Page and view titles — WCAG 2.4.2 A

Web pages **MUST** have titles that describe topic or purpose.

For substantial client-side view changes, keep document/view title behavior meaningful to the user. Focus relocation after route/view replacement is coordinated with `focus-management.md`.

## Headings and relationships

Information, structure, and relationships conveyed visually **MUST** also be programmatically determinable where WCAG 1.3.1 applies.

**SHOULD** use native heading levels that represent actual hierarchy rather than choosing heading tags for visual size.

Do not require one `h1` policy mechanically for every embedded application context; preserve a coherent semantic hierarchy in the resulting page/view.

## Landmarks

**SHOULD** use native landmarks/regions where they materially improve navigation: header/banner, nav, main, complementary, footer/contentinfo, search, and named regions as appropriate.

Avoid turning every Card/section into a named region. Landmark density should help rather than create noise.

## Bypass blocks — WCAG 2.4.1 A

Provide a mechanism to bypass blocks of content that are repeated on multiple pages where required. A skip link to main content is a common solution, but not the only valid mechanism.

Skip targets **MUST** be usable and receive/establish the expected reading/focus context.

## Multiple ways — WCAG 2.4.5 AA

For pages within a set, provide more than one way to locate a page unless it is the result of or a step in a process, according to the criterion. The exact mechanism may be search, sitemap, navigation, related links, etc.

## Consistent Navigation — WCAG 3.2.3 AA

Repeated navigation mechanisms occurring on multiple pages within a set **MUST** occur in the same relative order unless the user initiates a change.

## Consistent Identification — WCAG 3.2.4 AA

Components with the same functionality within a set of pages **MUST** be identified consistently.

This does not require identical wording when the function/context actually differs.

## On Focus — WCAG 3.2.1 A

**MUST** ensure that receiving focus does not itself initiate a change of context.

Examples of prohibited/unexpected focus-triggered context changes include automatically navigating, opening a new window, submitting, or moving to a new major context merely because a control received focus.

Normal focus styling, helper text, or local disclosure that does not meet the WCAG definition of change of context is not automatically prohibited.

If a component intentionally opens contextual content on focus, ensure the behavior remains predictable, dismissible/persistent as applicable, and does not become an unannounced major context change.

## On Input — WCAG 3.2.2 A

Changing the setting/value of a UI component **MUST NOT** automatically cause a change of context unless the user has been advised of that behavior before using the component.

Potential changes of context include:
- navigation to another page/view;
- opening a new window;
- significant focus movement;
- another major change that can disorient users.

Ordinary local result filtering, inline validation, conditional field reveal, or component state update is not automatically a change of context. Evaluate the actual effect.

Where a selection must immediately navigate, provide prior instruction or use an explicit activation/submit action when that is more predictable.

Forms owns form-specific validation/recovery; this document owns the cross-cutting predictability rule.

## Consistent Help — WCAG 3.2.6 A

If one or more qualifying help mechanisms are repeated on multiple pages within a set, those mechanisms **MUST** occur in the same relative order to other page content, unless the user initiates a change.

Qualifying examples include:
- human contact details;
- human contact mechanisms;
- self-help option;
- fully automated contact mechanism.

**Important:** WCAG 3.2.6 does **not** require the product to provide Help/Support/Chat/FAQ on every page. It governs consistency **when those help mechanisms are provided repeatedly**.

Typical JV triggers:
- repeated Support/Contact link;
- chat/contact mechanism;
- help center/self-help entry;
- repeated automated assistant/contact affordance.

Content wording belongs to `content.md`; component accessibility belongs to the relevant Link/Button/Popover/etc. contract.

## Focus after navigation

After substantial client-side navigation/view replacement, do not leave focus in removed/hidden content. `focus-management.md` owns target selection/relocation strategy.

This document owns whether navigation itself is predictable and whether structure/title/landmarks remain coherent.

## Visual vs DOM order

**MUST** preserve meaningful reading/navigation order when responsive layout visually reorders content. Use DOM order that remains coherent across breakpoints where practical.

## Breadcrumbs and current location

When breadcrumbs/navigation indicate current location, expose the relationship/current state programmatically where appropriate and keep link/current-item behavior distinct.

## Ownership

| Structure/Navigation owns | Other owner |
|---|---|
| Headings/landmarks/bypass | Content owns wording |
| Navigation predictability | Focus owns relocation mechanics |
| On Focus / On Input cross-cutting rule | Forms owns validation/input mechanism |
| Consistent Help relative-order rule | Content owns Help copy; component owns mechanism |
| Consistent navigation/identification | Component owns its internal semantics |

## Testing

Test keyboard navigation through page structure, skip/bypass behavior, headings/landmarks, page/view titles, responsive reading/focus order, route changes, focus-triggered behavior, value/input-triggered behavior, and repeated Help mechanisms across representative page sets.

For 3.2.6, record:
1. whether qualifying help mechanisms exist;
2. whether they repeat across pages in the set;
3. their relative position/order;
4. any user-initiated personalization/change.

Do not report “missing Help” as a 3.2.6 failure when no qualifying repeated help mechanism is required/provided.

## AI contract

AI **MUST** route On Focus, On Input, and Consistent Help questions here; must distinguish local UI updates from changes of context; and must not invent a global requirement to add Help.

## References

- WCAG 2.2 — 1.3.1 Info and Relationships
- WCAG 2.2 — 2.4.1 Bypass Blocks
- WCAG 2.2 — 2.4.2 Page Titled
- WCAG 2.2 — 2.4.5 Multiple Ways
- WCAG 2.2 — 3.2.1 On Focus
- WCAG 2.2 — 3.2.2 On Input
- WCAG 2.2 — 3.2.3 Consistent Navigation
- WCAG 2.2 — 3.2.4 Consistent Identification
- WCAG 2.2 — 3.2.6 Consistent Help
