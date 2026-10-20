---
id: design-system.reference.figma-token-compliance
collection: design-system
type: reference
title: Figma Component Token Compliance
summary: Required binding and semantic QA gate for canonical Figma design system components.
knowledge_state: verified
document_maturity: reviewed
owner: Design System team
last_reviewed: '2026-10-19'
---

# Figma Component Token Compliance

## Purpose and source-of-truth boundary

Token quality has two separate dimensions: **semantic role correctness** (why a token is chosen) and **binding correctness** (whether the node consumes the governed Figma variable/style). Correct visible color or numeric value is not sufficient evidence of either.

Figma owns actual values, IDs, authoring and bindings. The Design System Knowledge corpus owns token semantics and component recipes. Runtime and Storybook, when registered, own their implemented behavior. This guide does not introduce a new token layer.

## Canonical scope

Include actively maintained public Component Sets, their owned variant layers and internal masters. Exclude documentation frames, raw playground copies, archives, legacy drafts and screenshots from canonical compliance denominators. Audit borrowed nested instances at their **own source master**, not repeatedly as owned component layers. Include specific source node IDs and component-property / variant-count checks in every fix report.

## Color

- Normal components consume public 03 Semantic variables: surface/*, fg/*, line/*, link/*, focus/* and approved utility/*. Do not consume the internal 02 Product, 03 Semantic Values or 01 Primitives directly.
- The only approved categorical Component Token family is currently tag/{color}/* and belongs to Tag. Do not treat it as a generic UI palette.
- Choose Brand for product identity/approved conversion; Accent for interaction; Magic for AI capabilities; Danger for destructive intent; Error for validation/system failure; Support Info for passive feedback; focus/* for focus.
- Differentiate surface/default, muted, inset, raised, neutral-muted, selected and interactive/chromatic surface states by role, not hue.
- Raw colors require review. Legacy Paint Styles are a migration candidate, not automatically semantically correct.
- Fixed Primitive palette/bw/white is an explicitly documented exception for Toggle Thumb.
- Verify JobVision/Cando x Light/Dark, meaningful hover/active/selected/focus/error states, and contrast separately. A binding scan cannot prove semantic correctness or accessibility.

## Spacing

- Shared recurring padding and gap use canonical Spacing variables, even when their raw numeric value is already correct.
- Zero / structurally inactive gaps are not automatically defects.
- Component-local optical construction can stay raw with explanation, e.g. 3, 7, 10, 11, 14 or 15px. Do not create global tokens solely to remove these.
- Review context and component recipe before binding broad collections of raw values. Distinguish an owned master decision from a nested instance inherited from another master.

## Typography

- Product text uses Label, Body, Body Compact, Heading, Heading Compact or Heading Fluid styles by content role.
- An unstyled text layer matching the correct font size/weight/line-height still needs an appropriate Text Style unless an intentional construction exception is documented.
- Foreground color is a separate semantic decision.
- Live Product font router: 02 Product / typography/font-family, with JobVision Vazirmatn and Cando IRANYekanX; standard Text Styles use that fontFamily binding.
- Do not infer typography role from font size alone. Review mixed-language text and responsive content.

## Radius

- Default controls: 6px · Medium. Independent/floating surfaces: 12px · Large. Small component details: 3px · Small where justified. None and Full are boundary behaviors.
- Governed radii use canonical variables, not raw numbers or Deprecated role-based tokens.
- Deprecated radius variables are hidden from new use (not deleted), preserving existing component references until controlled migration.
- Approved explicit exceptions: Chip currently uses Full; Content Switcher Track has a component-local 8px while items use 6px Medium; circular/pill geometry uses Full.

## Severity and QA

| Severity | Condition | Gate |
|---|---|---|
| P0 | Verified inaccessible contrast/focus or broken critical component | Block handoff |
| P1 | Private Color routing in public master, semantically wrong Color, deprecated Radius in maintained source, wrong shared Radius/unstyled recurring text | Fix or document owned, compatibility-safe migration |
| P2 | Correct numeric but unbound Spacing, old Paint Style, uncertain styling or approved migration debt | Track owner and regression checks |
| Exception | Component-specific local geometry or documented Primitive use | Record rationale and validate appearances |

A component becomes **Design-token QA complete** only after P0/P1 resolution or explicit migration disposition, P2 tracking, semantic role review, and structural/visual Figma QA. This does **not** certify Angular/Storybook/runtime accessibility.

## Safe fix workflow

1. Record canonical source ID, variants/properties and current variable bindings.
2. Verify semantic role against Foundation and component guideline.
3. Rebind in place. Do not recreate published component/variant IDs, detach instances or lose overrides.
4. Confirm numeric/visual parity before and after; check inherited instances and all Product/Appearance modes.
5. Record affected node IDs and open migration debt in the audit register.
6. Keep runtime acceptance testing separate from Figma authoring.

## Audit implementation

Read-only code is located at [../tooling/figma/figma-token-compliance-audit.js](../tooling/figma/figma-token-compliance-audit.js). Run it on each **currently loaded** component page using the Figma JavaScript execution capability. On mixed-purpose pages, populate `CANONICAL_MASTER_IDS` with approved public/internal root IDs (for File Uploader: `5465:294860`, `3199:35182`, `3183:29103`, `4188:102462`) rather than claiming unrelated `image uploader` masters as File Uploader. The scanner skips component-set matrix spacing **and component-set shell Paint Styles**, borrowed-instance wrappers, and one-child non-wrapping itemSpacing values (an inert Gap cannot separate siblings), which are not effective owned-source UI decisions. For the Button audit, 640 such inert icon-wrapper gaps were correctly excluded rather than token-bound gratuitously. The script produces candidate findings only: it cannot judge semantic meaning, true exceptions, visual contrast or runtime behavior.

Current evidence and action register: Component Token Compliance Audit, 2026-10-19.