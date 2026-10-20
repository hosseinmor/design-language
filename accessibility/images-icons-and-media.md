---
id: design-system.accessibility.images-icons-and-media
collection: design-system
type: accessibility
title: Images, Icons, and Media
summary: Defines text alternatives, decorative imagery, icon semantics, complex images, captions, audio description, and media-control accessibility.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.screen-reader-semantics
- design-system.accessibility.content
last_reviewed: '2026-09-02'
---

# Images, Icons, and Media

This document owns cross-cutting accessibility for images, icons, audio, video, and complex visual media.

## Informative images — WCAG 1.1.1 A

Informative non-text content **MUST** have a text alternative that serves the equivalent purpose, subject to the criterion's specialized cases/exceptions.

The alternative should communicate the information/function, not describe every visual detail.

## Decorative images

Purely decorative imagery, visual formatting, or content already fully duplicated by adjacent text **SHOULD** be ignored by assistive technology using the appropriate native mechanism (for example empty `alt` for a decorative `<img>`).

Do not create repetitive announcements such as “check icon, success” when visible text already conveys “Success”.

## Functional images and icons

When an image/icon is the only visible content of a control, the **control** **MUST** have a meaningful accessible name describing the action/result.

Tooltip does not replace that name.

The image itself may be hidden from assistive technology when the control's accessible name already conveys the meaning.

## Complex images

Charts, diagrams, maps, and infographics **MUST** provide an equivalent accessible presentation of essential information appropriate to the task.

A short `alt` may identify the graphic; detailed values/relationships may need adjacent text, a data table, structured summary, or another equivalent representation.

Do not place the entire dataset into an excessively long `alt` string.

Data visualization specifics belong to `tables-and-data-visualization.md`.

## Images of text — WCAG 1.4.5 AA

**MUST** use text rather than images of text when the visual presentation can be achieved with available technologies, except where the criterion permits an exception (for example essential/logotype cases).

## Audio/video alternatives

For prerecorded synchronized media, provide applicable WCAG A/AA alternatives:
- captions for prerecorded audio content in synchronized media (1.2.2 A);
- audio description or media alternative for prerecorded video where 1.2.3 applies (A);
- audio description for prerecorded video where 1.2.5 applies (AA).

For live synchronized media, provide captions where WCAG 1.2.4 AA applies.

For prerecorded audio-only/video-only content, provide the applicable alternatives under 1.2.1 A.

Do not mislabel AAA media criteria as AA requirements.

## Captions

Captions **MUST** convey meaningful spoken content and relevant non-speech audio needed to understand the media.

Automatically generated captions may be used as a starting point but **MUST** be accurate enough for the published content in scope.

## Media controls

Media controls **MUST** be keyboard operable, have meaningful accessible names/states, maintain visible focus, and meet applicable pointer target requirements.

Do not create icon-only player controls that depend on Tooltip for their accessible name.

Autoplay/timing/moving-content behavior belongs to `motion.md`.

## Color/visual encoding

Meaning in images/charts **MUST NOT** depend on color alone. Contrast for essential graphical objects belongs to `color-and-contrast.md`.

## Product-generated/user-uploaded images

When users upload content, the Product/Pattern should determine whether alternative text is required, optional, derived, or not applicable based on the user-facing purpose. Do not invent a universal requirement for every uploaded image without the product context.

## Testing

Inspect images/icons for informative vs decorative purpose, functional control names, duplicate announcements, complex-image equivalent information, captions/audio description where applicable, keyboard/focus behavior of media controls, and color/contrast dependencies.

## AI contract

AI **MUST** decide purpose before writing `alt`, keep functional naming on the control, avoid duplicate decorative announcements, apply correct media criterion levels, and route chart/data-equivalence questions to the data-visualization owner.

## References

- WCAG 2.2 — 1.1.1 Non-text Content
- WCAG 2.2 — 1.2.1–1.2.5 applicable A/AA media criteria
- WCAG 2.2 — 1.4.1 Use of Color
- WCAG 2.2 — 1.4.5 Images of Text
