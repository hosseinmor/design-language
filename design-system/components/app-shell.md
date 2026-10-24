---
id: design-system.component.app-shell
collection: design-system
type: component
title: App Shell
summary: Draft Karbon App Shell composition contract for responsive chrome, logical Start and End regions, and a Page Container-owned native content slot.
knowledge_state: unverified
document_maturity: draft
owner: Design System team
related:
  - design-system.component.side-navigation
  - design-system.component.drawer
  - design-system.foundation.responsive-layout
  - design-system.foundation.responsive-layout-spec
  - design-system.token.layout.catalog
---

# App Shell

> **Status — audited Figma design candidate, pending runtime review.** This document describes the live Figma source after the 2026-10-24 audit. It is not a shipped runtime API and does not claim Storybook parity. The Page Container and optional Layout Content responsibilities are now reconciled in Figma.

## Purpose

App Shell composes stable application chrome around designer-owned page content. Use it for application screens that share a Header, logical navigation, optional supplementary Drawer, and optional app-level Footer. A single-purpose interstitial or marketing page may use a simpler page pattern.

App Shell owns region placement and visibility. It does not own product content, navigation items, Drawer content, responsive breakpoint tokens, or runtime interaction implementation.

## Anatomy and ownership

```text
App Shell
├── Header                              [linked instance; optional]
├── Body                                [horizontal composition on md/lg]
│   ├── End Region
│   │   └── Drawer                      [linked instance; optional]
│   ├── Main Region                     [fills remaining width; no page gutter]
│   │   └── Page Container              [linked responsive layout primitive]
│   │       └── Content                 [one native page-content slot]
│   │           └── Layout / Content    [optional inner max-width helper]
│   └── Start Region
│       └── Side Navigation             [linked instance; optional]
└── App Footer                          [optional placeholder region]
```

Start Region and End Region are conceptual layout regions, not components. Do not introduce `Start Pane` or `End Pane` wrappers. In RTL, logical Start is right and logical End is left; in LTR they mirror.

| Owner | Responsibility |
|---|---|
| App Shell | Region order, region visibility, mobile temporary-surface composition, remaining Main width |
| Side Navigation | Navigation destinations, item density, Compact/Expanded presentation |
| Drawer | Drawer header, actions, content, footer, Display and modal behavior contract |
| Page Container | Responsive width, centering, page gutter, and the primary Content slot |
| Layout / Content | Optional narrower inner max-width; no gutter or visual styling |
| Consuming product | Page content, local grids, route semantics and product-specific minimum usable width |

Main Region adds no horizontal page padding. Page Container is the only owner of page gutter and the primary native Content slot. Designers place content directly in that slot by default. Add Layout / Content only when the design needs a narrower reading or working width. Drawer and Side Navigation keep their independent native slots; those are not extra page-content slots.

## Live Figma source

- [App Shell component set](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24550-497)
- [App Shell presentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24829-43466)
- [Mobile responsive Playground](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24988-3726)
- [Side Navigation source](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24631-180)
- [Drawer source](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24677-486)
- [Page Container source](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24549-41)
- [Layout Content source](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23437-83)

The App Shell presentation follows [Figma component presentation guidance](../../integrations/figma-component-presentation.md): 00 Header, 01 canonical Component Set, 02 Playground, 03 Anatomy and composition, and 04 Usage and handoff. The canonical Component Set remains in section 01; Playground examples are instances.

## Component API

### Variant axes

| Property | Values | Contract |
|---|---|---|
| `Viewport` | `xs`, `md`, `lg` | Manual Figma authoring preset; it does not switch automatically from frame width |
| `Navigation` | `Compact`, `Expanded` | Controls 64px/256px persistent navigation on md/lg; ignored visually on xs |

The set intentionally retains all six `Viewport × Navigation` combinations. Both xs variants render the same 256px temporary navigation. `xs / Expanded` is a compatibility alias, not a distinct mobile visual state.

The audit found one `xs / Expanded` instance and it exists only in the archived QA area. Deleting that source would nevertheless leave a partial two-axis matrix and make variant switching less predictable. A true five-state model would require either a breaking combined `Layout` axis or separate mobile and desktop components. Both alternatives add migration cost and reduce the current simple API. Keep six variants until an owner explicitly approves a migration plan; do not delete a single xs source as an isolated cleanup.

### Boolean properties

| Property | Default | Contract |
|---|---:|---|
| `Header` | `true` | Shows shared Header |
| `Side Navigation` | `false` | Shows persistent md/lg navigation or temporary xs navigation |
| `End Drawer` | `false` | Shows linked Drawer as Inline on md/lg or Overlay on xs |
| `App Footer` | `true` | Shows app-level Footer placeholder |

`End Pane` was renamed to `End Drawer` in Figma. The component-property identity suffix (`#24550:13`) was preserved, and audited instance values survived the rename.

### Exposed nested authoring

Page Container, Drawer and Side Navigation remain linked instances and remain exposed so designers can reach their native slots. This also exposes nested layout properties that App Shell already owns:

- Change Compact/Expanded with the outer App Shell `Navigation` axis, not nested Side Navigation `Compact`.
- Do not change nested Drawer `Display`; App Shell sets Inline on md/lg and Overlay on xs.
- Do not change nested Page Container `Reference` independently of the selected App Shell viewport preset.
- Layout / Content is not part of the App Shell master. Designers may add it inside Page Container Content only when a narrower max-width is intentional.

Figma cannot conditionally hide parent-owned nested controls while keeping their slots discoverable. Treat those values as authoring rules, not additional consumer choices.

## Responsive model

Use the canonical semantic ranges from [Responsive Layout](../../foundations/visual/responsive-layout/guideline.md): narrow below 768px, regular from 768px to below 1400px, and wide from 1400px. App Shell `xs`, `md`, and `lg` are manual authoring presets intended to represent those ranges; they are not token names and do not select themselves automatically.

### xs / narrow

#### Temporary Navigation

- Uses the existing Side Navigation instance, always Expanded at 256px.
- Anchors to logical Start: right in RTL, left in LTR.
- Starts immediately below the 56px Header.
- Backdrop starts below Header; Header and its toggle remain outside the backdrop.
- The linked Header-menu `Open=true` variant occupies the same 48×56 position as the hamburger. The Figma overlay is a design-time technique and must not produce two runtime buttons.
- Main width does not change.
- This surface is navigation, not a modal dialog. A backdrop alone does not imply `aria-modal=true`.

`Header=false` with `Side Navigation=true` is an invalid xs authoring combination because the close trigger disappears while the backdrop still begins at 56px. Keep Header on whenever temporary Navigation can open.

#### Modal End Drawer

- Uses the existing Drawer with `Display=Overlay`.
- Anchors to logical End: left in RTL, right in LTR.
- Backdrop covers the full viewport, including Header.
- Width follows the tested Figma rule `min(viewport − 32px, 400px)`: 288px at 320, 358px at 390, and 400px from 432px upward.
- Main width does not change.
- Drawer native Header-actions, Content and Footer slots remain available.

Only one temporary surface may be open. If End Drawer is requested while Navigation is open, runtime closes Navigation before opening the modal Drawer. Figma Booleans cannot enforce this mutual exclusion; when both are true, End Drawer currently paints above Navigation and the state must be treated as invalid.

### md and lg / persistent composition

Side Navigation is inline at 64px Compact or 256px Expanded. End Drawer is a linked 400px Inline Drawer. Both subtract from Main Region.

Use 640px as the current App Shell handoff guardrail for a generally usable Main Region, not as a new global token:

- Compact Navigation + Drawer requires at least `64 + 400 + 640 = 1104px` host width.
- Expanded Navigation + Drawer requires at least `256 + 400 + 640 = 1296px` host width.

Below those thresholds, close or collapse one panel, or use a product-reviewed overlay policy. Do not allow the auto-layout result to reduce Main to an unusable sliver merely because the composition is technically possible.

## Verified responsive geometry

The following measurements come from temporary live instances created for this audit and removed after inspection.

| Preset / width | Compact Main | Compact + Drawer | Expanded Main | Expanded + Drawer |
|---|---:|---:|---:|---:|
| md / 768 | 704 | 304 | 512 | 112 |
| md / 900 | 836 | 436 | 644 | 244 |
| md / 1024 | 960 | 560 | 768 | 368 |
| lg / 1280 | 1216 | 816 | 1024 | 624 |
| lg / 1400 | 1336 | 936 | 1144 | 744 |
| lg / 1440 | 1376 | 976 | 1184 | 784 |

The 1280 test intentionally stress-tested the lg source even though 1280 belongs to the current regular semantic range. This reinforces that Figma presets are manual references, not automatic breakpoint logic.

Mobile width tests at 320, 390, 600 and 767px confirmed that Navigation stays 256px at Start, Drawer follows its 32px-backdrop/max-400 rule, both backdrops stretch horizontally, and Main width remains unchanged.

## Height, scrolling and Footer

Runtime intent is a minimum-viewport-height, content-driven document:

- Short content fills at least the viewport.
- Long content grows the document; Footer follows content.
- Header and Footer are not sticky by default.
- Body, Main, Page Container and Content do not become independent scrollports by default.
- Modal End Drawer owns its internal overflow behavior and locks background scroll according to the [Drawer contract](drawer.md).

The Figma representation does not fully model that contract:

- Source reference heights are xs 844px, md 820px and lg 900px. They are canvas references, not tokens or runtime constants.
- xs cannot shrink to the required 700px test height; a request for 700px remains clamped to 844px.
- At 900px, mobile backdrops and panels stretch to 900px correctly.
- Long native-slot content is preserved across `lg → xs` variant switching, but the App Shell instance root remains at its reference height while Body, Main and Footer extend outside the reported root bounds.
- Fresh long-content instances show the same root-bound limitation. Header/Footer toggles do not repair it.

No clean master-only correction was found. Lowering or removing the reference minimum fixes one short screenshot but loses the useful short-page viewport floor; fixing the root height makes long content fixed or clipped. Do not add a Height variant for this design-tool limitation.

For Figma authoring, choose the intended Viewport before adding long content, verify the instance bounds manually after content or variant changes, and use a separate fixed viewport frame for prototype scrolling. Runtime must size against the actual viewport and content flow; the Figma root height is not implementation evidence.

## Page Container and Layout Content

The Figma architecture now separates responsive page layout from optional inner content constraint.

### Page Container

- Uses one `Reference` axis: `sm`, `md`, `lg`, `xl`, `2xl`, and `Fluid`.
- Represents the standard Tailwind v3 container progression used by the product layout.
- Owns responsive width, centering, and the token-bound 16/24px page gutter.
- Owns the primary native `Content` slot used by App Shell.
- Runtime should use the existing Tailwind container behavior rather than introduce another public Container abstraction.

### Layout / Content

- Is optional and lives inside the Page Container Content slot.
- Uses one `Max width` axis: `Compact` 400px, `Narrow` 768px, `Standard` 1200px, `Wide` 1320px, and `Fluid`.
- Owns only the selected max-width and centering.
- Does not own page gutter, fill, border, radius, shadow, or internal padding.
- Runtime implements it as an inner max-width constraint; a dedicated public component is not required unless implementation reuse later justifies one.

Place content directly in Page Container by default. Add Layout / Content only when a narrower measure is a deliberate design decision.

## Runtime interaction and accessibility contract

These requirements are implementation acceptance criteria. They are not verified by Figma.

### Temporary Navigation

- Use one real Header toggle with an accessible name that changes between open and close.
- Expose `aria-expanded` and `aria-controls` on that toggle.
- Do not use dialog semantics or `aria-modal=true` merely because a backdrop exists.
- When open, prevent pointer and keyboard interaction with covered Main/Footer content while leaving Header toggle and Navigation operable. The implementation may use scoped inertness, but must not trap focus in hidden or unrelated controls.
- Escape closes Navigation and restores focus to the Header toggle if focus moved into Navigation.
- Selecting a destination closes Navigation before route focus management runs.
- Backdrop click may close Navigation if product policy requires it; keyboard dismissal must never depend on pointer behavior.

### Modal End Drawer

- Follow [Drawer](drawer.md) for role, accessible naming, close control and backdrop-dismiss policy.
- Enter focus deliberately, contain focus while modal, mark outside application regions inert, lock background scroll, and return focus to the invoker on close.
- Escape closes unless a documented blocking workflow owns a stricter rule.
- Opening End Drawer closes temporary Navigation first.

### Shared checks

- Preserve landmark and DOM order for Header, Navigation, Main and Footer in RTL and LTR.
- Hidden regions must not expose focusable controls or stale screen-reader content.
- Test Tab, Shift+Tab, Enter, Space and Escape; visible focus must not be obscured by the Header, panels or viewport edge.
- Test 200% zoom, reflow, screen-reader name/role/state and both text directions.

See [Focus management](../../accessibility/focus-management.md), [Keyboard navigation](../../accessibility/keyboard-navigation.md), [Screen-reader semantics](../../accessibility/screen-reader-semantics.md), [Structure and navigation](../../accessibility/structure-and-navigation.md), and [Responsive and zoom](../../accessibility/responsive-and-zoom.md).

## Presentation decisions

The audited presentation keeps the canonical source in section 01 and uses linked instances in the Playground. It includes:

- all six variants, with `xs / Expanded` labeled as an alias;
- desktop Expanded and Compact examples;
- xs closed, Navigation-open and End-Drawer-open states;
- anatomy and ownership notes;
- responsive Main-width thresholds;
- the Page Container plus optional Layout Content ownership model;
- Figma height limitations; and
- explicit Runtime QA requirements.

Archived QA frames remain outside the canonical presentation. They are not consumer guidance. No production source, variant or linked dependency was deleted during this audit.

## Acceptance status

### Design evidence completed

- Six variants and all linked source identities preserved.
- `End Drawer` property rename verified on real instances with values intact.
- Page Content survives viewport variant switching.
- Side Navigation and Drawer remain linked; native slots remain available.
- Mobile overlay geometry verified at 320, 390, 600 and 767px; heights checked at 700, 844 and 900px.
- Desktop Main geometry verified at 768, 900, 1024, 1280, 1400 and 1440px with Compact/Expanded Navigation and Drawer off/on.
- Header off, Footer off, both xs temporary surfaces, and long-content cases exercised.

### Blocking decisions and Runtime QA

- Decide whether to keep the six-state compatibility matrix long-term or approve a breaking five-state migration.
- Resolve or explicitly accept the Figma instance root-height limitation for long content and sub-844px xs viewports.
- Validate runtime focus, inertness, Escape/backdrop behavior, scroll lock, route-close behavior, RTL/LTR, zoom and screen-reader semantics.
- Verify implementation and Storybook parity; none is claimed here.

The Figma composition is suitable for engineering discussion and implementation planning. It is not yet ready for an unconditional design handoff or merge as a verified contract while runtime acceptance remains open.
