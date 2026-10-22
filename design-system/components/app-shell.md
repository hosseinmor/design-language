---
id: design-system.component.app-shell
collection: design-system
type: component
title: App Shell
summary: Draft Karbon App Shell composition contract for viewport-based Figma variants, optional logical regions, and a nested Page Container with one native content slot.
knowledge_state: unverified
document_maturity: draft
owner: Design System team
related:
  - design-system.foundation.responsive-layout
  - design-system.foundation.responsive-layout-spec
  - design-system.token.layout.catalog
---

# App Shell

> **Status — design candidate, pending owner review.** This document records the approved discussion scope and the current experimental Figma composition. It is **not** a verified Karbon runtime API, a shipped component, or a resolution of legacy Responsive Layout documentation conflicts.

## Purpose

App Shell composes stable, cross-page application chrome around a designer-owned main content area. It gives a designer a reusable page starting point without detaching Header/Navigation or adding a Page Container manually.

Use it for application screens with shared Header, edge panes or app-level Footer. A single-purpose interstitial may use a simpler page pattern instead. This is a composite **design-time Figma component**; its exact runtime abstraction and framework API remain implementation-owned.

## Anatomy and ownership

```text
App Shell / Viewport = xs | md | lg
├── Header                    [existing nested instance; optional]
├── Body                      [auto layout]
│   ├── End Pane              [logical end; optional]
│   ├── Main Region           [fills remaining width; no page gutter]
│   │   └── Page Container    [nested instance]
│   │       └── Content       [ONE native slot; designer-owned]
│   └── Start Pane            [logical start; optional]
└── App Footer                [app-level, optional]
```

In RTL, Start Pane appears on the **right** and End Pane on the **left**. This relationship reverses in LTR; region names are always logical, not physical.

App Shell owns chrome, region presence and their relative layout. Main Region fills the available area. **Page Container owns centering, width constraint and horizontal gutter**. The Content slot has no independent second page-gutter layer. Product page content, including its own local Flex/Grid, is owned by the consuming design. App Footer is shared app chrome, not a page-local form action bar.

## Designer-facing choices

| Property | Kind | Values | Notes |
|---|---|---|---|
| `Viewport` | Figma variant | `xs`, `md`, `lg` | Designer selects manually for the intended viewport |
| `Header` | Boolean | On / Off | Controls shared Header visibility |
| `Start Pane` | Boolean | On / Off | Controls logical start region |
| `End Pane` | Boolean | On / Off | Controls logical end region |
| `App Footer` | Boolean | On / Off | Controls app-level Footer |
| Container `Mode` | Exposed nested variant | `Contained` / `Fluid` | Default `Contained`; `Fluid` removes its max-width constraint |
| Container `Reference` | Exposed nested variant | `sm` / `md` / `lg` / `xl` / `2xl` | Determines the design-time Tailwind v3 max-width and gutter step; designer changes manually when needed |
| Container `Content` | Native slot | Arbitrary page content | Exactly one content slot, nested in Page Container |

The App Shell's three design-time viewport ranges are:

- `xs`: widths below 768 px.
- `md`: widths from 768 px through 1023 px.
- `lg`: widths of 1024 px and above.

These labels are **Figma App Shell variants**, **not** the Tailwind `xs:`/`sm:` utility system. Tailwind v3 base screen values (640, 768, 1024, 1280, 1536 px) are the target for the separate responsive-foundation reconciliation. The current `main` Layout Token Catalog still contains a legacy conflicting numeric contract; do not claim the two sources already agree.

A shared Figma Boolean property has one default across the Component Set, rather than different defaults by `Viewport`. The current Figma candidate defaults `Start Pane = false`; provided `md` and `lg` playground instances explicitly enable it. Whether to change this default or provide compositional presets is open.

## Responsive behavior

The viewport variant chooses the matching Header presentation and the page-region geometry. The available Main Region and nested Container resize with Figma Auto Layout. Navigation and secondary panes can occupy persistent space in larger layouts; smaller layouts may instead require a separate overlay/drawer interaction pattern. **Enabling a pane Boolean is not evidence that its compact overlay behavior is finished.**

Container is optional as a *layout mode choice* (`Contained` / `Fluid`) but is always present as the nested Figma instance, avoiding manual insertion. Fluid is an exceptional wide-workspace composition, not an assumption that every ultrawide page should stretch indefinitely.

The experimental Page Container's **outer component** (not its inner slot) now supports exact Tailwind v3 max-width references when manually selected: `sm=640`, `md=768`, `lg=1024`, `xl=1280`, and `2xl=1536` px. Mode `Fluid` has no cap. The single inner Content slot fills the padded width of that outer Container. The Container is centered **within the remaining Main Region**, after any persistent panes, and the shell itself adds no duplicate page gutter.

Each Container Reference also selects the current Figma `layout/page-gutter` variable mode: `sm/md/lg → Base (16 px)`, `xl/2xl → XL+ (24 px)`. This binding lives in the Container's design-time reference variants rather than being overridden at the App Shell level, so Mode/Reference switches update width and gutter together.

**Important Figma limitation:** changing a frame's width does **not** automatically switch a variant or its breakpoint Reference. App Shell defaults `xs → sm`, `md → md` and `lg → xl` (for a 1440px primary design reference). For 1024–1279px, a designer must change the exposed nested Container `Reference` to `lg`; from 1536px upward, change it to `2xl`. A narrower reference may also be intentionally selected for task-specific constraints. This manual design-tool setting is not an additional runtime API or a new Tailwind breakpoint. A future improvement could reduce this secondary choice, but no automatic breakpoint selection is claimed.

Changing Shell viewport variants must retain the user's Content slot overrides. Changing nested Container mode must also retain them. The same contract applies if a Boolean hides a region. These changes require a visual QA pass for every intended combination, rather than merely a check that properties exist.

## Accessibility and semantics

The final runtime composition must preserve meaningful Header/Main/Footer and navigation landmarks, logical keyboard and screen-reader reading order in both RTL and LTR, visible focus, and responsive reflow. Hidden panes must not expose focusable off-screen controls. Any overlay pane requires focus entry/return, keyboard dismissal and a reachable mobile navigation trigger. These behaviors **are not verified by this Figma pilot**.

## Known gaps and acceptance

- Header and navigation instances in the pilot are **legacy, not reviewed final components**. Finalize their responsive behavior before promoting App Shell.
- End Pane and App Footer currently have **design placeholders**, not final canonical implementation.
- Decide Start Pane defaults/presets; test both-pane combinations and compact overlay behavior.
- Resolve old responsive breakpoint and container numeric contracts in `foundations/visual/responsive-layout/` and `design-system/tokens/layout/catalog.md` in a reviewed foundation change; do not silently overwrite them.
- The Tailwind v3 width steps, centered Contained/Fluid modes, and reference-based 16/24px gutters were reproduced and tested in the isolated Figma candidate. The remaining design-tool usability gap is that Container `Reference` must be selected manually when a design crosses steps inside the broader App Shell `lg` range; this should be assessed in designer testing.
- Run keyboard/RTL/zoom and complete design/runtime acceptance. No claimed Storybook parity.

### Figma validation completed (2026-10-22)

The single nested native Content slot retained page content through `lg → xs → md → lg`, `Contained → Fluid → Contained`, and `Reference=lg → 2xl → xl`. In width QA, Contained outer caps and centering were verified at 700px (640px), 900px (768px), 1100px (1024px), 1440px (1280px), and 1920px (1536px). At 1920px, Fluid used the full 1920px, while two visible panes left 1384px of Main Region width and the Container respected that smaller available width. Gutter resolved to 16px for `sm/md/lg` and 24px for `xl/2xl` from the existing Figma responsive layout variable collection. These are **Figma visual/structural checks**, not executable CSS or runtime parity proof.

A former instance-level max-width override prevented Fluid/2xl from working even though their variant labels changed; that stale override was cleared, and max-width ownership is now on the Container source variant. The noncanonical QA samples document the verified state.

## Live references

- [App Shell / Figma candidate component set](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24550-497)
- [App Shell / Playground](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24552-177)
- [Page Container / Tailwind candidate](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24549-41)
- [Container / Verified width QA](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24606-40546)
- Karbon Storybook and code: runtime verification not yet performed; cross-source parity deferred.
