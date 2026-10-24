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
App Shell / Viewport = xs | md | lg ; Navigation = Compact | Expanded
├── Header                    [existing nested instance; optional]
├── Body                      [auto layout]
│   ├── End Drawer / Inline [md/lg, optional]
│   ├── Main Region           [fills remaining width; no page gutter]
│   │   └── Page Container    [nested instance]
│   │       └── Content       [ONE native slot; designer-owned]
│   └── Side Navigation      [direct linked instance in logical Start region; optional]
└── App Footer                [app-level, optional]
```

In RTL, logical Start is on the right and End is on the left; in LTR they mirror. Start Pane and End Pane are layout regions, not independent components. In md/lg the real linked Side Navigation and Drawer / Inline are direct children of Body. In xs the regions become App Shell-owned overlay compositions: expanded Side Navigation under the persistent Header, or modal Drawer / Overlay over the entire viewport. Page Container continues to own the main Content slot and horizontal gutter.

App Shell owns chrome, region presence and their relative layout. Main Region fills the available area. **Page Container owns centering, width constraint and horizontal gutter**. The candidate **Figma-only Page Container Master** is located in **Foundations → Layout & responsive** ([source presentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=25010-48), [unchanged master ID](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24549-41)), rather than nested as a canonical source inside the App Shell documentation page. All six App Shell variants continue to reference the same Container source. The existing older `Layout / Container` family (`23437:83`) remains separate pending reconciliation; do not treat these as interchangeable or imply a runtime Container API. The Content slot has no independent second page-gutter layer. Product page content, including its own local Flex/Grid, is owned by the consuming design. App Footer is shared app chrome, not a page-local form action bar.

## Designer-facing choices

| Property | Kind | Values | Notes |
|---|---|---|---|
| `Viewport` | Figma variant | `xs`, `md`, `lg` | Designer selects manually for the intended viewport |
| `Navigation` | Figma variant | `Compact`, `Expanded` | md/lg choose 64/256px persistent Navigation. xs currently has two redundant source variants that both show the same expanded temporary overlay; preserve both IDs pending owner-reviewed reduction to five useful combinations. |
| `Header` | Boolean | On / Off | Controls shared Header visibility |
| `Side Navigation` | Boolean | On / Off | md/lg toggles persistent navigation; xs toggles a 256px expanded temporary navigation below Header, scrim below Header, and linked Header-menu Open=True close icon |
| `End Pane` | Boolean | On / Off | md/lg toggles Drawer / Inline; xs toggles Drawer / Overlay modal with full-viewport backdrop including Header |
| Drawer `Display` | Nested variant | `Inline` md/lg; `Overlay` xs | Determined by App Shell viewport; Floating is not a fallback |
| Drawer `Size` | Nested variant | `Default` | Inline current source 400px; xs Overlay sample width 358px inside 390px viewport is a Figma-only experimental size, not a token |
| Drawer `Content / Slot` | Nested native slot | Arbitrary supplementary/task content | Drawer-specific content, distinct from Main Page Content; Drawer also owns its own Header-actions/Footer slots |
| `App Footer` | Boolean | On / Off | Controls app-level Footer |
| Container `Mode` | Exposed nested variant | `Contained` / `Fluid` | Default `Contained`; `Fluid` removes its max-width constraint |
| Container `Reference` | Exposed nested variant | `sm` / `md` / `lg` / `xl` / `2xl` | Determines the design-time Tailwind v3 max-width and gutter step; designer changes manually when needed |
| Container `Content` | Native slot | Arbitrary page content | The **only main page-content slot**, nested in Page Container |
| Side Navigation `Compact` | Nested design property | `False` / `True` | md/lg: controlled by parent Navigation variant. xs temporary Navigation always uses `Compact=False`/256px, independent of redundant xs Compact/Expanded labels. Avoid direct override on consumer instances. |
| Side Navigation `Size` | Exposed nested variant | `Small` / `Medium` / `Large` | Default `Medium`; controls navigation item density |
| Side Navigation `Items` | Nested native slot | Navigation destinations/groups | Navigation-specific slot, **not** a second page-content slot |

The App Shell's three design-time viewport ranges are:

- `xs`: widths below 768 px.
- `md`: widths from 768 px through 1023 px.
- `lg`: widths of 1024 px and above.

These labels are **Figma App Shell variants**, **not** the Tailwind `xs:`/`sm:` utility system. Tailwind v3 base screen values (640, 768, 1024, 1280, 1536 px) are the target for the separate responsive-foundation reconciliation. The current `main` Layout Token Catalog still contains a legacy conflicting numeric contract; do not claim the two sources already agree.

A shared Figma Boolean property has one default across the Component Set. The Booleans Side Navigation and End Pane default false. md/lg source variants use Compact 64px or Expanded 256px inline Navigation, with Drawer / Inline at End when requested. Both xs variants now use the same 256px expanded temporary Navigation below Header and a separate modal End Drawer Overlay. These xs variants are visually redundant for Navigation; both IDs are intentionally retained pending later simplification. Figma does not automatically select a viewport variant or guarantee only one Boolean is true.

## Responsive behavior

The Viewport variant chooses Header presentation and layout. In md/lg, the parent Navigation variant sets persistent Side Navigation width (64px/256px) and Main Region receives remaining width; End Drawer / Inline consumes 400px when enabled. In xs, the Side Navigation Boolean shows an App Shell-owned expanded 256px temporary panel anchored right in RTL, starting immediately below the 56px Header. Its utility/overlay backdrop begins below the Header, and the existing Header menu Open=True source icon covers the hamburger position. This keeps the Header visibly outside the backdrop. The xs End Pane Boolean instead shows the linked Drawer / Overlay as an intended modal from the logical End (left in RTL), with a full-viewport backdrop covering Header. Neither overlay subtracts from Main width; neither adds a mobile variant to Side Navigation. Runtime focus, dismissal and scroll behavior is not proved by these Figma examples.

Container is optional as a *layout mode choice* (`Contained` / `Fluid`) but is always present as the nested Figma instance, avoiding manual insertion. Fluid is an exceptional wide-workspace composition, not an assumption that every ultrawide page should stretch indefinitely.

The experimental Page Container's **outer component** (not its inner slot) now supports exact Tailwind v3 max-width references when manually selected: `sm=640`, `md=768`, `lg=1024`, `xl=1280`, and `2xl=1536` px. Mode `Fluid` has no cap. The single inner Content slot fills the padded width of that outer Container. The Container is centered **within the remaining Main Region**, after any persistent panes, and the shell itself adds no duplicate page gutter.

Each Container Reference also selects the current Figma `layout/page-gutter` variable mode: `sm/md/lg → Base (16 px)`, `xl/2xl → XL+ (24 px)`. This binding lives in the Container's design-time reference variants rather than being overridden at the App Shell level, so Mode/Reference switches update width and gutter together.

**Important Figma limitation:** changing a frame's width does **not** automatically switch a variant or its breakpoint Reference. App Shell defaults `xs → sm`, `md → md` and `lg → xl` (for a 1440px primary design reference). For 1024–1279px, a designer must change the exposed nested Container `Reference` to `lg`; from 1536px upward, change it to `2xl`. A narrower reference may also be intentionally selected for task-specific constraints. This manual design-tool setting is not an additional runtime API or a new Tailwind breakpoint. A future improvement could reduce this secondary choice, but no automatic breakpoint selection is claimed.

Changing Shell viewport variants must retain the user's Content slot overrides. Changing nested Container mode must also retain them. The same contract applies if a Boolean hides a region. These changes require a visual QA pass for every intended combination, rather than merely a check that properties exist.

### End region — Drawer Inline integration (Figma evidence, 2026-10-24)

The md/lg App Shell variants use the live Drawer / Inline, Size=Default from the linked Figma Drawer set. Both xs variants now use the same Drawer source with Display=Overlay inside an App Shell modal overlay layer, not a standalone End Pane component. The existing End Pane visibility Boolean remains the same property across all variants.

The current Figma Inline Drawer width is **400px**. When both regions are visible at 1440px, the Main Region width is 784px with a 256px Expanded Navigation and 976px with the 64px Compact Navigation. When the Drawer is hidden, the Main region recovers its 400px. In a 900px `md` / Compact example, Main Region is 436px with the Drawer shown. The Page Container remains the sole native **page-content** slot; Drawer owns separate native slots for Drawer Header actions, Content, Footer (and optional Header extension). This is expected composition, not redundant nested Page Container insertion.

**Mobile responsive decision — design candidate (2026-10-24):** The 400px Inline Drawer is unsuitable for 390px xs. The xs End Pane Boolean now displays a linked Drawer / Overlay over a full-viewport utility/overlay backdrop including Header. The 358px panel at 390px is a test width, not a public size. Modal semantics, focus trapping/restoration, Escape/backdrop dismissal and page scroll lock remain runtime QA obligations.

**Figma regression QA:** On the live App Shell composition, toggling `End Pane` off/on retained **both** the Page Content Slot override and the Drawer Content Slot override. Switching parent `Navigation=Expanded → Compact → Expanded` while keeping Drawer visible retained both content regions and recalculated Main Region (784 → 976 → 784px at 1440px). These results verify editable Figma composition only. The [design-language Drawer document on main](drawer.md) is still a **scaffold**; this Figma source must not be represented as approved code/runtime behavior or a reviewed shared Drawer contract.

### xs Header-preserving navigation and modal End Drawer — Figma candidate (2026-10-24)

**Navigation:** Existing Side Navigation source `Compact=False, Size=Medium`, shown as a right-side 256px temporary panel (RTL). Backdrop uses `utility/overlay` and begins *below* the 56px Header; Header remains visually accessible. The existing Header-menu source offers `Open=False/True`; Figma represents open state with the linked `Open=True` icon over the normal hamburger position and an opaque 48×56px surface to avoid double rendering. This design-time layering is **not** an instruction to render two actual buttons in code. Navigation is not automatically an `aria-modal=true` dialog simply because a backdrop is present.

**End Drawer:** Same linked Drawer component with `Display=Overlay`; the Modal backdrop covers Header and document. Current visual reference is 390×844px with Drawer 358px wide, leaving 32px of Backdrop; that width is experimental. Drawer retains its Content and other native slots.

**Design choice:** Both existing xs parent Navigation variants use the same composition because Compact does not apply to the temporary mobile panel. A future owner-reviewed cleanup may reduce App Shell to five useful variants; the six existing Figma variant IDs are **not removed** in this change.

**Interaction contract pending runtime testing:** Keep the real Header toggle keyboard reachable with appropriate expanded/controlled semantics; handle Escape/outside dismiss and focus restoration. While an End Drawer modal is open, use its proper focus management and scroll lock. App Shell should prevent both temporary surfaces opening simultaneously; separate Figma Booleans do not enforce that. The application must also define overlay behavior at narrower widths and zoom/reflow.

[Two current xs linked-instance Playground examples](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24988-3726).

### Six-variant navigation matrix — Figma QA (2026-10-22)

| Viewport | Navigation | Navigation width when shown | Main Region relationship |
|---|---|---:|---|
| xs | Compact | 256px (same as Expanded) | Temporary panel below Header, Main width unchanged; redundant xs variant label retained for compatibility |
| xs | Expanded | 256px | Temporary panel below Header, Main width unchanged |
| md | Compact | 64px | Main Region = available Body width − 64px |
| md | Expanded | 256px | Main Region = available Body width − 256px |
| lg | Compact | 64px | Main Region = available Body width − 64px |
| lg | Expanded | 256px | Main Region = available Body width − 256px |

All six are members of the **existing App Shell Component Set**; three earlier source variant IDs remain and three additional variants were created. Boolean Header/Side Navigation/End Pane/App Footer property references were checked across all variants. Each retains one native Page Container Content slot; Side Navigation retains its separate navigation-specific Items slot.

A live Figma test toggled `Navigation` on `xs/md/lg` consumer examples and checked effective width and Content retention. In md/lg, Main Region reflow was correct; in xs, navigation stays overlaid for exploration. The outer parent-variant solution **passes this design-tool use case** but does not verify Runtime, accessible responsive Drawer or preservation of every product-specific override.

## Height, scrolling and App Footer — design-side default

App Shell is **minimum-viewport-height, content-driven**, not a fixed-height scroller. For short page content it should occupy at least the intended viewport height; as Content grows, Body/Main/Container/Content all grow to accommodate it. A short page with `App Footer=on` places the app-level Footer at the bottom of the minimum viewport. A long page places it **after the content**, regardless of whether persistent panes are present. Turning Header, Side Navigation or End Pane off must not cause content to overlap Footer.

**Default scroll ownership:** scroll the **whole page/document**. Do not make Body, Main Region, Container or the Content slot separate scrollports. Header is **not sticky by default**. App Footer is **not fixed/sticky by default**. Independent pane scrolling, sticky Header/Footer and viewport-contained operational workspaces are **intentional exceptions**, subject to product, responsive and accessibility requirements; they are not additional App Shell variants in this candidate.

The app-level Footer is shared chrome and should not be conflated with a page-local form action bar or sticky action footer. This candidate's Footer is only a structural placeholder (48px in the current Figma test), **not a finalized Footer component or published dimension**.

### Figma height implementation and limitations

- The `Viewport` design references have initial minimum heights `xs=844`, `md=820`, and `lg=900` px; these are **canvas test/reference heights**, not design-system height tokens, CSS breakpoint heights, or runtime constants. For other viewport heights, the designer must adjust the Figma instance's minimum-height behavior as necessary. Runtime's actual viewport units are implementation-owned.
- The Shell root uses a vertically Hugging Auto Layout with a reference `minHeight`; Body and Main Region Hug their content vertically, and the nested Page Container plus its **single** native Content slot are vertically Hugging. This avoids masking long page content with fixed nested frame heights.
- A **locked, empty** `Viewport Balance / Figma only` layer absorbs spare space caused by optional Header/Footer visibility in the minimum-height Figma component. It is a **design-tool representation workaround, not a sixth semantic region or an additional runtime DOM requirement**. Its minimum rendered size may produce a ~1px Figma rounding difference at Footer boundaries; the expected runtime contract remains exact document flow. On footer-disabled pages, any under-filled reference-height area takes the same surface background as Main Region; do not infer a separate content panel.
- Figma prototype scrolling is demonstrated in a separate **fixed viewport Frame** with `overflowDirection=VERTICAL` and clipping. Because Figma can constrain a Hugging nested instance inside that fixed scroll viewport, the prototype instance uses an explicit minimum height matching its current long content for presentation. This workaround does **not** change the reusable App Shell master nor imply that Figma fully simulates CSS `min-height:100vh` / native browser scroll.
- There is no `Scroll`, `Sticky` or `Footer position` variant in the component; adding one requires a distinct reviewed use case.

### Figma height QA (2026-10-22)

- `lg`, short content, Footer off: Shell remains 900px tall, with no internal Body/Main scrolling.
- `lg`, short content, Footer on: Shell remains 900px; Footer sits at its viewport-bottom position (allowing Figma's ~1px spacer artifact).
- `lg`, 1470px content, Footer on: Shell expands to 1582px and Footer follows the content instead of overlapping it.
- `xs`, short content, Footer on: Shell remains 844px; `md`, 1470px content, Footer on: Shell expands to 1574px.
- `lg` with no Header or with both panes plus long content was checked prior to Side Navigation replacement; no separate Body/Main scrollers were introduced. Height was rechecked with directly nested Side Navigation after replacement.
- A fixed 1440×900px viewport was configured to scroll vertically around a long App Shell instance; this is **Figma prototype configuration only**, not a browser accessibility or runtime scroll test.
- Further regression: 1470px Content survived Footer/Header Boolean toggles and `lg → xs → md → lg` variant changes. **Content preservation passed; Shell height propagation after the variant switch failed in `xs/md`**. A fresh `md` long-page instance did expand as expected, so this issue is specific to the switch/override path.

## Accessibility and semantics

The final runtime composition must preserve meaningful Header/Main/Footer and navigation landmarks, logical keyboard and screen-reader reading order in both RTL and LTR, visible focus, and responsive reflow. Hidden panes must not expose focusable off-screen controls. Any overlay pane requires focus entry/return, keyboard dismissal and a reachable mobile navigation trigger. These behaviors **are not verified by this Figma pilot**.

## Known gaps and acceptance

- The **Side Navigation** component is now the live designed Figma component (source ID `24631:180`) directly used in App Shell; the old legacy Right Panel instance and the extra Start Pane Frame were removed from all three App Shell variants. This is a design-source integration, not an approved runtime implementation. Header remains legacy, and responsive Drawer/flyout behavior remains independently unverified.
- End Pane uses a linked Drawer: Inline in md/lg, modal Overlay in xs. App Footer remains a placeholder, and runtime/Storybook parity is not claimed.
- Review default Side Navigation visibility across viewport variants, `md` rail choice, and responsive Drawer/flyout patterns. Figma currently uses one global Boolean default (`false`). Six parent variants are now implemented for both navigation presentations across all three viewports.
- xs mobile overlays are now represented in Figma: Navigation preserves Header, while End Drawer covers the whole viewport. Both Boolean controls should not be true together; mutual exclusion remains an unverified runtime behavior. Modal End Drawer and temporary Navigation require separate focus/keyboard and scroll tests.
- **Nested Compact resizing gap, mitigated:** changing the nested Side Navigation `Compact` value directly on an App Shell consumer instance may retain the old 64px width and squeeze expanded Items. The **supported Figma design-time workflow is now to change the outer `App Shell → Navigation=Compact/Expanded` Variant**. In verified `md` QA at width 900, Main Region changed correctly from 836px to 644px and back; `lg` at width 1440 changed from 1376px to 1184px and back. The page Content Slot was preserved. Figma still exposes the nested `Compact` setting; designers must avoid toggling that nested setting directly until a more reliable API/property exposure solution is found.
- Resolve old responsive breakpoint and container numeric contracts in `foundations/visual/responsive-layout/` and `design-system/tokens/layout/catalog.md` in a reviewed foundation change; do not silently overwrite them.
- The Tailwind v3 width steps, centered Contained/Fluid modes, and reference-based 16/24px gutters were reproduced and tested in the isolated Figma candidate. The remaining design-tool usability gap is that Container `Reference` must be selected manually when a design crosses steps inside the broader App Shell `lg` range; this should be assessed in designer testing.
- Review any designs that specifically require a sticky Header, sticky footer or independently scrolling pane; those are exception patterns, not verified here. Test long-form focus navigation, scroll restoration and zoom/reflow in runtime before a production claim.
- **Figma height recomputation gap:** a freshly created instance with long Content correctly Hugs its height, but switching an *existing* 1470px-long page from `lg` to `xs` or `md` preserved its Slot content while leaving the instance root at the variant's reference minimum height (844/820px), with Footer lower than the reported Shell bounds. This persisted after a new canvas read, so it is **not yet a verified automatic responsive override workflow**. The tested instance was restored to `lg`. Until solved, choose the intended `Viewport` before authoring page content, or manually verify/adjust the instance height after switching. Do not promote this component to final before this usability issue is reviewed.
- Run keyboard/RTL/zoom and complete design/runtime acceptance. No claimed Storybook parity.

### Figma validation completed (2026-10-22)

The single nested native Content slot retained page content through `lg → xs → md → lg`, `Contained → Fluid → Contained`, and `Reference=lg → 2xl → xl`. In width QA, Contained outer caps and centering were verified at 700px (640px), 900px (768px), 1100px (1024px), 1440px (1280px), and 1920px (1536px). At 1920px, Fluid used the full 1920px, while two visible panes left 1384px of Main Region width and the Container respected that smaller available width. Gutter resolved to 16px for `sm/md/lg` and 24px for `xl/2xl` from the existing Figma responsive layout variable collection. These are **Figma visual/structural checks**, not executable CSS or runtime parity proof.

A former instance-level max-width override prevented Fluid/2xl from working even though their variant labels changed; that stale override was cleared, and max-width ownership is now on the Container source variant. The noncanonical QA samples document the verified state.

## Live references

- [Side Navigation / designed Figma component](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24631-180)
- [Drawer / live Figma component set](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24677-486)
- [App Shell / Inline Drawer authoring Playground](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24961-46031)
- [App Shell / Figma candidate component set](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24550-497)
- [App Shell / Playground](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24552-177)
- [App Shell / All six Navigation variants visual comparison](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24814-44967)
- [Page Container / Tailwind candidate](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24549-41)
- [Container / Verified width QA](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24606-40546)
- [App Shell / Height and Footer QA](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24619-1618)
- [App Shell / Vertical page scroll viewport](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24622-2030)
- Karbon Storybook and code: runtime verification not yet performed; cross-source parity deferred.
