---
id: design-system.foundation.directionality
collection: design-system
type: foundation
title: Directionality (Bidirectional RTL/LTR)
summary: Shared inheritable UI direction model, logical layout, directional icon decisions, bidi-content boundaries and RTL/LTR authoring expectations without duplicating component contracts.
knowledge_state: verified
document_maturity: draft
owner: Design System team
related:
  - content.localization
  - design-system.foundation.responsive-layout
  - design-system.foundation.layout
  - design-system.foundation.iconography
  - design-system.experience-rule.segmented-field-editing
  - design-system.accessibility.keyboard-navigation
  - design-system.accessibility.responsive-and-zoom
  - design-system.accessibility.structure-and-navigation
  - design-system.accessibility.focus-management
  - design-system.component.app-shell
  - design-system.component.drawer
  - design-system.component.menu
topics:
  - directionality
  - bidirectional
  - rtl
  - ltr
  - logical-properties
  - mirroring
  - localization
  - figma
---

# Directionality (Bidirectional RTL/LTR)

> **HOS-56 · design proposal for owner review.** This document defines the shared Directionality model derived from existing reviewed component and accessibility contracts and the 2026-10-24 live Figma audit. It is **not yet an approved runtime API**, Figma property specification, or proof of shipped RTL/LTR parity. Existing reviewed component contracts remain controlling where more specific. The decision on whether an English-language flow also changes its enclosing App Shell direction is deliberately **TBD**.

## Purpose and ownership

Directionality is the shared, **inheritable UI layout-direction context**. The system supports RTL and LTR as directions of the **same** components and tokens, not as duplicated libraries, token scales, or global variant axes.

The Foundation owns:
- how the effective UI direction is determined for a surface;
- semantic Start/End and inline/block layout placement;
- shared mirroring classification and directional-icon selection principles;
- distinction between component layout direction and content/input direction;
- common RTL/LTR composition, motion-direction and Figma authoring expectations.

It **does not** own translations, product preference persistence, choice of supported languages, locale-specific number/calendar/time-zone/currency formatting, exact code APIs, DOM implementation, or any component-specific keyboard model. Use [Persian Localization](../../foundations/content/localization.md), owning Product Knowledge, component contracts, Karbon runtime, and Accessibility respectively.

## Direction contexts and inheritance

Treat **locale/language, theme, UI direction, and content direction as separate concerns**:

| Concern | Meaning | Owner |
| --- | --- | --- |
| Theme / brand | Visual values such as Light/Dark and Product expression | Existing Theme/Product token contracts |
| Locale / language | Translation and language metadata; may suggest a UI direction | Product / Localization |
| Effective UI direction | Structural RTL/LTR direction of the current application/flow/component scope | Directionality |
| Content/input direction | Paragraph and caret direction of a specific value or editable region | Localization and field/component owner |
| Data formatting | Numerals, calendar, timezone, units and precision | Product and Localization |

**Proposed inheritance model:** application root sets a default effective direction; a page/flow or bounded component may inherit or explicitly override it; a text input or isolated content run can separately control its **content direction** without reversing the field shell. Descendants inherit the nearest relevant UI-direction context unless they have a reviewed exception.

A language toggle may derive a default direction (for example a Persian surface usually RTL and an English surface usually LTR), but **do not conflate locale and direction into one Theme variable** or infer that each mixed-language value changes the entire UI direction. Locale changes must also update translations and appropriate language metadata; merely switching direction is insufficient.

Examples requiring separate scopes:
- A wholly English application can default to LTR.
- A bilingual résumé within an RTL application can use LTR **editor content** while its label, validation and field actions remain in the surrounding RTL layout.
- An English job-posting flow within an RTL application may need an LTR sub-scope. **Exactly where that sub-scope starts relative to App Shell/Header/Navigation remains an explicit product decision, not defined here.**

**Implementer handoff (not a public Karbon API claim):** use actual document/element direction semantics so nested contexts and portals/overlays retain their effective direction; pair with appropriate language metadata. Verify how the app, overlay mount point and component library propagate context in runtime. Do not assume a `theme.direction` API exists.

## Logical layout model

Use logical names for direction-sensitive placement. For horizontal writing in the current RTL/LTR modes:

| Concept | RTL | LTR |
| --- | --- | --- |
| inline-start / Start | right | left |
| inline-end / End | left | right |
| block-start | top | top |
| block-end | bottom | bottom |

- Use **Start / End** for regions and positions whose meaning follows reading direction (App Shell, leading/trailing actions, padding, alignment, pane anchoring, breadcrumb progression).
- Prefer **inline-start / inline-end** and **block-start / block-end** in spatial contracts; `leading/trailing` is useful for component content roles.
- Reserve **Left / Right** for deliberately physical geometry, e.g. Popover `Side=Left/Right`, a data axis or an explicit physical icon asset. Never silently rename existing physical component properties to logical ones.
- Do **not** reverse semantic source/DOM order just to draw mirrored columns. The layout may reflect direction, but reading/focus order must remain meaningful.

**Tailwind mapping guidance (implementation adapter; not proof of the installed Karbon version):** where supported, choose logical utilities such as `ps-` / `pe-`, `ms-` / `me-`, `start-` / `end-`, `border-s` / `border-e`, `rounded-s` / `rounded-e`, and `text-start` / `text-end` rather than duplicated RTL/LTR overrides. Use `gap` for inter-item spacing. Logical CSS equivalents include `padding-inline-start`, `margin-inline-end`, `inset-inline-start`, and `border-inline-end`. Confirm exact Tailwind version, mappings and component DOM in Karbon before runtime handoff. Flex/Grid child order still requires authoring and keyboard review; utilities alone do not make arbitrary compositions bidi-correct.

No new spacing, radius, responsive breakpoint, Light/Dark, or direction-specific token is approved here. Existing values stay owned by their token catalogs.

## Mirroring and icons

**Mirror semantics, not every vector.** Classify the **use** of an icon or visual element before choosing the displayed asset:

| Meaning category | Shared rule | Examples / boundary |
| --- | --- | --- |
| Logical navigation/progression | Select orientation for the effective relevant direction | Back, Forward, submenu chevron, previous/next flow |
| Logical alignment/indent | Present the direction-relative meaning | Align Start/End, increase/decrease logical indent |
| Physically or intrinsically meaningful | Preserve physical orientation | Clock, camera, search, calendar, check, close, geographic illustrations |
| Data/temporal/media semantics | Follow the data or control contract, **not** generic UI mirroring | Charts, time axes, timelines, media playback, undo/redo |
| Brand/identifying asset | No automatic mirroring | Logo, logotype, wordmark, recognized symbol |

**Practical authoring:** preserve existing physical `Icon/chevron_left`, `Icon/chevron_right`, `Icon/arrow_left`, `Icon/arrow_right` and other stable asset identities. The **owning component** chooses the appropriate physical asset for a semantic action and direction; avoid global CSS `scaleX(-1)` / blanket icon flips. No new universal semantic-icon component, icon variants or per-direction icon library is required without demonstrated repeated need.

Existing Figma icon instance colors **must still be overridden by the consuming component/screen** using the appropriate semantic foreground token. This is an independent, already-verified [Iconography](../visual/iconography.md) authoring rule; direction never changes token meaning.

## Composition and component boundaries

- **App Shell and Side Navigation:** Start/End positions are logical; preserve existing responsive/navigation decisions. The English-flow App Shell boundary is unresolved.
- **Drawer:** Start/End side placements are logical; Bottom is a physical bottom sheet; floating corner is an anchoring position, not an automatic animation direction.
- **Menu:** a submenu prefers logical End, with collision-aware flipping; arrow key open/close follows the owning Menu contract.
- **Breadcrumb:** the hierarchy remains semantic; the current item is at logical End. Do not mirror the slash as an asset.
- **Popover:** physical Top/Bottom/Left/Right `Side` and logical Start/Center/End `Align` are intentional and coexist.
- **Tables/lists/List–Detail:** visual pane/order depends on semantics, accessible reading order and the pattern contract; do not adopt draft List–Detail Figma examples as approved universal architecture.
- **Form fields:** label, helper/error, affordance placement and leading/trailing geometry follow the effective *field layout* direction; content can independently be RTL, LTR or automatically isolated when unknown. Directional controls remain accessible.
- **Date/Time:** preserve [Segmented Field Editing](segmented-field-editing.md): a time's HH:mm(:ss) stays a physically LTR ordered, isolated value even in RTL. Date segment order, calendar and digit policy remain owned by Date Picker / Localization.
- **Overlays:** verify that an overlay mounted outside the triggering container still receives the intended effective direction and retains its semantic relationships; do not assume that physical portal mounting preserves inherited direction.

A component or pattern owns detailed icon choices, keyboard behavior, trigger/hit-area semantics, focus return, scroll constraints and data decisions. This foundation defines no new component-specific API or forced variant.

## Mixed-direction text and formatting

- UI layout direction and **paragraph/input direction** are different. An LTR entry within an RTL field should not move the Label, Helper, Error or trailing trigger without a separate UI-direction override.
- Known LTR runs (email, URL, code, hashes and Latin identifiers) need an isolated LTR context. Unknown user-generated strings need bidi isolation / auto direction as appropriate. Do not manually reverse punctuation or inject invisible bidi marks where semantic isolation can be used.
- Bidi isolation must apply to individual dynamic values inside localized sentences.
- Display formatting for quantity, number, phone, date, time, unit and percentage follows the **type and product locale policy**; it does not change automatically because the surrounding UI becomes LTR.
- Text truncation should follow logical end of the text/value without discarding full accessible names; validate mixed punctuation and ellipsis in both directions.

The detailed content contract, HTML examples and unresolved numeral/calendar/timezone decisions belong to [Localization](../content/localization.md).

## Keyboard, focus, motion and accessibility

- Preserve meaningful reading, DOM and sequential focus order in mirrored compositions. Directional CSS layout alone must not produce a misleading assistive-technology sequence.
- Never globally reverse Left/Right keyboard controls. Use the *owning interaction model*: spatial adjacency, progression, native text caret behavior, Menu submenu navigation or slider's numeric semantics as appropriate.
- Maintain correct language metadata, accessible naming, focus return, landmark ordering and overlay relationships through direction changes.
- Direction-sensitive motion follows the semantic attachment/progression edge **when that motion is already defined by the component**. Do not create universal motion durations/easing here; shared Motion is still TBD. Honor reduced motion.
- Normative requirements remain in [Keyboard Navigation](../../accessibility/keyboard-navigation.md), [Responsive and Zoom](../../accessibility/responsive-and-zoom.md), [Structure and Navigation](../../accessibility/structure-and-navigation.md), and [Focus Management](../../accessibility/focus-management.md). This document does not redefine Focus styling.

## Figma authoring contract (proposed)

- Represent the effective direction at **composition/page-example level first**, with clear `RTL` and `LTR` example labels. Keep canonical shared component-set identities, existing token usage, shared styles and existing slots.
- For a directional component, build only the **minimum evidence-backed LTR example** and compare it to its existing RTL instance. Do not add `Direction` to every component's Variant set.
- No universal Directionality Variable Collection/Mode is introduced. Variables cannot alone recompose Auto Layout, text and icons.
- Keep logical `Start/End` names for direction-dependent slots/regions, but retain physically meaningful `Left/Right` names where their owning contract requires them.
- Use actual independent text-direction examples (including Persian label plus LTR entered value) and verify layout, truncation, punctuation, icon swap, state and nested overlay direction.
- Figma is editable **visual evidence**, not proof of DOM/ARIA behavior, language switcher implementation or Tailwind/Storybook parity.
- Preserve reviewed masters; record any proven RTL/LTR composition discrepancy with its owning component instead of globally changing assets.

## Audit coverage and outstanding decisions

**2026-10-24 representative Figma inspection:** App Shell, Side Navigation, Drawer, Layout, Breadcrumb, Menu, Popover, Data Table, Select, Autocomplete, Tabs, Date Picker, Time Picker, Number Input, Icons, and List–Detail. The library did not expose a universal direction collection/mode and the sampled component sets did not have an RTL/LTR variant axis. RTL authoring predominates; this **does not certify LTR behavior**.

| Topic | Status | Owner / required evidence |
| --- | --- | --- |
| Root/page/field direction inheritance | Design direction accepted for exploration; proposed contract under review | Design System owner |
| RTL/LTR in one component/token family | Preserve reviewed logical-model choices | Design Language / Figma |
| Icon mirroring matrix | Foundation classification proposed; exact icon use stays with components | Design System owner + icon/component audit |
| Tailwind logical utilities and runtime context propagation | Unverified implementation, **not a runtime API claim** | Karbon/Frontend when requested |
| English flow and surrounding App Shell direction | **TBD — explicitly deferred** | Product owner |
| Exact locale support, digits, calendar, time zone, currency | **TBD by product and locale** | Product / Localization |
| Full LTR coverage in all current component masters | **Open QA**, not assumed drift | Figma component owners |
| Data-axis reversal, carousel, slider, drag/drop edge cases | Owning component/pattern review required | Component / pattern owners |
| Shared Motion durations, easing, transition recipes | **TBD**; preserve reviewed local Drawer exceptions | Motion owner |
| Runtime DOM, screen reader, keyboard and portal behavior | Out of current design-phase scope | Karbon/Storybook when requested |

## Review checklist

- [ ] Preserve existing approved component-specific RTL/LTR exceptions.
- [ ] Confirm meaningful Start/End vs physical Left/Right in each authored composition.
- [ ] Test application default, local flow override and LTR editor inside RTL field independently.
- [ ] Confirm that direction does not silently change calendar, number, time zone, or data semantics.
- [ ] Select navigation icons semantically; never blanket-mirror assets.
- [ ] Validate RTL and LTR text length, bidi isolates, ellipsis, focus/reading order and overlay anchoring.
- [ ] Use linked Figma instances and approved semantic token overrides; do not proliferate direction variant axes.
- [ ] Record unresolved product decisions rather than choosing a universal answer.
- [ ] Keep exact runtime claims subject to live Karbon/Storybook evidence.

## Live references

- [Figma · Directionality HOS-56 review playground (editable QA examples, not a master)](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=25157-37)
- [Figma · App Shell](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24549-36)
- [Figma · Side Navigation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24604-40457)
- [Figma · Drawer](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24608-36)
- [Figma · Date Picker](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=60-0)
- [Figma · Time Picker](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24862-45799)
- [Figma · Icons](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=15068-360607)
