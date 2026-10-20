---
id: design-system.accessibility.content
collection: design-system
type: accessibility
title: Accessible Content
summary: Defines accessible UX content, labels, instructions, link purpose, language, abbreviations, error copy, and accessible-name wording.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.forms
- design-system.accessibility.structure-and-navigation
last_reviewed: '2026-09-02'
---

# Accessible Content

This document owns content/copy accessibility. Semantic mechanism remains in the relevant component or specialized document.

## Plain and actionable language

**SHOULD** use concise, direct language that tells users what the interface means and what action/result to expect.

Avoid relying on internal product/technical terminology when users need a plain-language explanation.

## Labels and instructions

Labels **MUST** identify the control's purpose sufficiently. Instructions required to complete a task **MUST** be available before the user needs them.

Placeholder is not a substitute for a persistent label.

For visible control labels, the accessible name **MUST** contain the visible label text where WCAG 2.5.3 applies.

## Link purpose

Link text **MUST** provide sufficient purpose from the link text alone or together with the programmatically determinable context as required by WCAG 2.4.4.

Avoid repeated ambiguous links such as “اینجا کلیک کنید” or “بیشتر” where surrounding programmatic context does not distinguish destinations.

Repeated cards/tables may need contextual accessible names when visible action text is intentionally short, but do not create verbose names that contradict the visible label.

## Headings and page titles

Headings **SHOULD** describe the following section and support scanning. Page/view titles **MUST** identify the topic or purpose where WCAG 2.4.2 applies.

Heading level/landmark structure belongs to `structure-and-navigation.md`; this document owns the wording quality.

## Form copy

Error copy **SHOULD** state what is wrong and how to correct it when known. Avoid blame, backend jargon, or “invalid” with no correction guidance.

Required/optional language should be understandable without depending only on an asterisk or color.

Security/authentication instructions should tell users what is allowed (paste, password-manager, code format) rather than adding unnecessary memorization/transcription burden.

## Language and mixed Persian/English

**MUST** set the default human language of the page where WCAG 3.1.1 applies, and **MUST** programmatically identify changes in the human language of passages/phrases where WCAG 3.1.2 applies and an exception does not apply.

Persian/English product names, technical terms, and proper nouns should not receive unnecessary language switching when the criterion exceptions/usage make it inappropriate.

For mixed Persian/English content, **SHOULD** preserve readable punctuation, number, URL, and code ordering; use semantic direction/language attributes where needed instead of visually inserting manual directional characters as a fragile workaround.

## Abbreviations and jargon

For uncommon abbreviations or domain language needed to complete a task, **SHOULD** provide an understandable expansion/definition at first meaningful use or through contextual help.

Do not make every familiar product abbreviation a forced expansion when that would reduce clarity.

## Status and severity wording

Copy should match the semantic severity. A routine successful save should not use urgent language/alert semantics; destructive consequences should be stated before commitment when users need them.

Announcement mechanism belongs to `dynamic-content-and-feedback.md`.

## Icon-only controls

The action meaning must have a programmatic accessible name; Tooltip/help text may support visible discoverability but is not the only naming mechanism.

## Help content

This document owns **what Help/Support text says**. `structure-and-navigation.md` owns WCAG 3.2.6 Consistent Help when repeated help mechanisms occur across a set of pages.

WCAG 3.2.6 does not require JV to create a help mechanism on every page; it requires relative-order consistency when qualifying help mechanisms are repeated.

## Testing

Review visible labels against accessible names, ambiguous/repeated links, errors/instructions, page/heading wording, Persian/English language/direction behavior, and whether critical consequences/recovery guidance are understandable without relying on visual presentation alone.

## AI contract

AI **MUST** preserve visible-label/name consistency, not invent legal/security meaning, distinguish content ownership from semantic mechanism, and not misstate Consistent Help as a requirement to add help everywhere.

## References

- WCAG 2.2 — 2.4.2 Page Titled
- WCAG 2.2 — 2.4.4 Link Purpose (In Context)
- WCAG 2.2 — 2.5.3 Label in Name
- WCAG 2.2 — 3.1.1 Language of Page
- WCAG 2.2 — 3.1.2 Language of Parts
- WCAG 2.2 — 3.3.1–3.3.3
