---
id: design-system.reference.component-mapping
collection: design-system
type: reference
title: Design-to-Code Component Mapping
summary: Registry contract for mapping stable Figma component identities to runtime components and Storybook; records current verified mappings and gaps.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: 2026-10-19
related:
  - design-system.reference.figma
  - design-system.reference.code
  - design-system.reference.storybook
---

# Design-to-Code Component Mapping

This registry prevents AI and humans from guessing runtime component APIs from Figma names.

A mapping is considered verified only when both sides are supported by their owning live sources.

## Retrieval and evidence boundary

This file is a **large design-to-code mapping evidence register**, not a fully populated runtime parity registry. Start from the [Component Mapping Lookup Index](component-mapping-index.md), find the exact component's `###` heading and read only that subsection.

- Treat verified Figma IDs/keys as **design identity evidence only**. An unregistered runtime source is not `verified` because a design has been handed off.
- The owning Code package, compiled API, tests and Storybook build must be verified separately before asserting runtime parity or shipment.
- Historical snapshots and PR-status notes are evidence recorded at the time; do not treat them as live issue/PR state unless rechecked.
- This register is for cross-source evidence and unresolved matches, not a replacement for component usage/semantic rules.

## Mapping fields

For each mapped component record:

```text
Design System component
Figma file key
Figma component key
Figma node ID
Code repository
Code package
Runtime component/API identifier
Figma property → code prop mapping
Storybook stable story/docs identifier
Mapping mechanism
Last verified
Known mismatch/gap
```

`Mapping mechanism` may be Figma Code Connect or another explicit registry. The mechanism is less important than having a stable, reviewable mapping.

## Current mapping registry

### Progress Circle and Loading pattern — HOS-46 final design contract

| Field | Verified design source / boundary |
|---|---|
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Loading pattern presentation | [Loading · Pattern](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24144-128998) · page `370:0`, moved under Patterns |
| Loading ownership | Usage pattern; **no separate public Loading component or wrapper**. Compose Progress Circle / Indeterminate directly; context owns busy state and announcements |
| Removed sources (historical only) | Old Loading set `3238:28455` and its 9 masters removed after all consumers migrated and instance count reached zero. Old key `14302ada5f73ab107d80509082cb3cb79ec4ca0f` is not a live source |
| Progress Circle presentation | [Progress Circle / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24203-116) · page `24201:379` |
| Progress Circle public set | `24200:460` · key `fa4ad066cca165f8869d86b8d8133b41d89a4bd3` · 12 valid variants: 3 sizes × (Indeterminate Active + Determinate Active / Success / Error); no Color axis |
| Determinate authoring | Only Active Determinate exposes nested `Progress value`: 0 / 25 / 50 / 75 / 100%. Success/Error use complete static geometry, with no editable percentage or rotation. Runtime renders actual validated values |
| Private geometry sources | `_Progress Circle / Track / Small` `3172:28703` (original base set/key `b7204e59832cad521eb94064e060623fb2fb189e` retained); Medium `24200:311`; Large `24200:336`; 5 snapshots each |
| Preserved geometry masters | Original Small `3172:28675`, Medium `24149:1205`, Large `3165:28654` remain the 25% sources; existing rotation links retained |
| Private rotation | `_Progress Circle / Rotation` `3165:28659` · original key `6155930ad6dade6abebb70ad047b1fa9078e9c31` · 12 variants, Size × Phase; four-phase prototype reference |
| Button dependency | All 160 Loading=True masters directly use `Progress Circle / Indeterminate / Small / Active` source `24200:361`, 16px; `Button → Progress Circle` |
| Other migrated consumers | Three File Uploader spinner sources, current Loading/Circle examples and slot content directly use Progress Circle; inherited Button/File Uploader instances follow their original parent sources |
| Button colors | All 160 Loading=True masters use `surface/disabled` neutral background, no Style border, `line/default` track and `line/accent` arc; original dimensions and focus treatment retained. Busy styling takes visual precedence; Disabled and busy semantics remain distinct |
| Visual contract | Editable Stroke; line/default track; line/accent Active (including 100%), line/success and line/error terminal rings; flat endpoints and full opacity. No new tokens or scope changes |
| Legacy Inline outcomes | Unused legacy set `24149:1204` removed after verifying zero consumers; no outcome family remains under Loading |
| Contracts | [Loading pattern](../design-system/patterns/loading-and-progress.md) · [Progress Circle](../design-system/components/progress-circle.md) |
| Runtime / Storybook / Code Connect | Unregistered / unverified; no production animation, reduced-motion or assistive-technology test claim |
| Figma last verified | 2026-10-19 |

### Skeleton — HOS-47 design handoff (Figma verified; runtime unregistered)

| Field | Verified design source / boundary |
|---|---|
| DS component | **Skeleton**, contract: [`../design-system/components/skeleton.md`](../design-system/components/skeleton.md) |
| Figma file / page | `rROD8ctH9UfPGAMrRrOzHe` / `Skeleton` page `24146:46` |
| Presentation | [Skeleton / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24146-47) · node `24146:47` |
| Public component set | `Skeleton` · node `24146:62` · key `d38438dc508671b18e814db895f0cab0cc13b95e` |
| Text primitive | `Shape=Text` · node `24146:56` · key `b04c95bd011ad7a840ba9c83a16a6d6ba4cf8a3f` |
| Block primitive | `Shape=Block` · node `24146:58` · key `9ebaeb10b3d3b5dd8a5b046d35ba3f7378591e75` |
| Circle primitive | `Shape=Circle` · node `24146:60` · key `5d32bf679bc931e3a2bc253a5175a88df5c8d95e` |
| Authoring contract | One `Shape` axis, three primitives. Width/height are geometry. Text reference is Body/SM 24px line box / 12px bar; Circle remains square. No public animation-phase or interaction-state axis |
| Color / radius | Existing Semantic `utility/skeleton-base` and `utility/skeleton-shimmer`; Text Small, Block Medium by default, Circle Full |
| Motion design | One intended `animate-skeleton` utility; left-to-right 1800ms linear Shimmer, 60% feathered band, 50% center intensity; immediate 150ms ease-out content reveal; static/direct reduced-motion treatment |
| Visual / motion reference | [Playground sequence](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24212-63) · `24212:63`; [native Motion preview](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24212-110) · `24212:110` |
| Motion TBD | Revisit duration, easing, reveal and related parameters after shared DS Motion foundations are completed; current values remain the v1 handoff target |
| Runtime repository/package/API | **Unregistered / unverified for Skeleton**. The class name is an intended contract, not an observed exported API; no Angular selector/props are inferred |
| Storybook / executed tests | **Unregistered / unverified**. Native Figma authoring is design evidence, not production execution or accessibility conformance |
| Mapping mechanism / verified | Explicit design-source registry, **2026-10-19**; exact Figma-to-code property mapping awaits an owning runtime source |
| Known gap | Comprehensive existing-product consumer migration audit remains separate; preview gradients are derived Semantic snapshots, not proof of live runtime theming |

### Dialog — HOS-42 design handoff (Figma verified; runtime unregistered)

| Field | Verified design source / boundary |
|---|---|
| DS component | **Dialog** (modal dialog v1), canonical contract: [`../design-system/components/dialog.md`](../design-system/components/dialog.md) |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma presentation | [Dialog / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24058-9) · node `24058:9` |
| Figma component set | `Dialog / Default` · node `24036:267` · key `b8bd11b06f27bac00225857315e0cb4f4c0887f7` |
| Size / Viewport axes | Five authored combinations: `Size=Small/Medium/Large/XL` with `Viewport=Regular` (400/560 default/800/960px max widths) plus `Size=Small, Viewport=Mobile` (328px design example). Under 768px layout adapts responsively at runtime; `Mobile` is not a hardware mode or public density prop. |
| Shared authoring properties | `Title`, `Description`, `Description visible`, `Dismissible`, `Body / Slot`, `Footer / Slot`, and **`Overflow fade` Boolean (Figma preview only; default `false`)**. Size and Viewport are authoring axes, not runtime user-selectable appearance APIs. |
| Anatomy | Title and supporting description; native Body/Footer Slots; canonical shared Buttons; independent Close Button |
| Close Button set | `Close Button / Default` · node `24046:476` · key `c19c7786bdbb03e1ad13695db575d5d7478e0d34`; 40px operable area, 5 states, Radius Medium 6px; physical top/left in RTL: **12px Regular / 8px Mobile** |
| Former Narrow Figma preset | `Dialog / Narrow preset` · node `24087:129096` · key `70787797b38b3976da888be932b8cfdee90e897b`; **already linked to the canonical `Size=Small, Viewport=Mobile` source**. Compatibility composition only; do not add a sixth variant or delete until linked consumers are checked |
| Responsive | **Shell padding 0.** General: Regular inline 24px / Mobile inline 16px, Header inset to clear RTL Close 64px, Footer top **24px Regular / 16px Mobile**. Confirmation/Alert: Regular inline/top 32px / narrow inline/top 24px. Body-only scrolling, 16px min viewport gutters; 768px layout boundary. Mobile actions use Button/Medium (40px), Regular example Button/Small (32px). |
| Design behavior | Backdrop uses `semantic/utility/overlay` and never dismisses by default; Escape safe-cancels, unsaved edits guarded; focus trapped/restored; scroll only Body. The **48px bottom fade** uses an **alpha-gradient mask applied to `surface/default` Semantic solid fill**, with bottom/stretch constraints. Figma `Overflow fade` Boolean is for preview only. At runtime, show fade only when more Body content remains below, hide at bottom/no overflow, and set `pointer-events: none`. No extra color tokens or runtime `overflowFade` toggle. |
| Alert vs confirmation | Independent Figma Confirmation Dialog and Alert Dialog components share behavior rules, **not a nested Dialog or Figma Base**. `alertdialog` semantic role only when urgency warrants it; confirmation and destructive remain intent patterns |
| Legacy | `Modal` set node `4080:55366`, key `dbb168637e13405605604dd1ca479f298735c348`, retained for migration; not the new canonical source |
| Design status | **Handoff-ready Figma and intended design/accessibility contract**; no proof of coded behavior/shipping |
| Runtime repository/package/API | **Unregistered / unverified**; exact props, events, DOM and focus library must not be guessed |
| Storybook / executed tests | **Unregistered / unverified**; implementation acceptance checklist is in `dialog.md` |
| Cross-foundation note | Canonical GitHub Responsive ruler disagrees with recent Figma Tailwind v3 foundation at sm/lg/2xl; both agree at 768px, which is the Dialog threshold. Foundation reconciliation is a separate task |
| Figma last verified | 2026-10-19 |

Figma component keys and names above are verified on the live source. This is **not** a verified Figma-to-code mapping without registered owning runtime/Storybook identities.

### Confirmation Dialog — standalone Figma component (review draft)

| Field | Current verified design source |
|---|---|
| Main component set | `Confirmation Dialog / Default` · node `24144:1108` · key `13645b3dea156f24f6c84e12a463c4b15b448bb4` |
| Presentation | [Confirmation Dialog](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24147-56) |
| Variants | `Intent=Default/Danger`; canonical Primary/Secondary (Danger Primary for destructive) |
| Content | Title/Description (short consequence belongs in Description), `Show body` false by default, optional native Body Slot and Footer Slot |
| Visual rules | Independent Shell in Figma, zero shell padding and no nested Dialog/Base. Existing semantic tokens. Header top/inline Regular 32px, Narrow 24px; optional Body top 16px; Footer top/inline/bottom Regular 32px, Narrow 24px (explicit content-to-actions gap). Title/Description gap 8px |
| Semantics | Ordinary confirmation uses `dialog`, explicit safe Cancel and Escape path; avoid blanket `alertdialog` |
| Status | Figma design review draft, **not** registered runtime/Storybook or production-ready |

### Alert Dialog — standalone Figma component (review draft)

| Field | Current verified design source |
|---|---|
| Main component set | `Alert Dialog / Default` · node `24144:128997` · key `19c4b10ed481dfda38bec782e2e5fa762294db25` |
| Presentation | [Alert Dialog](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24147-203) |
| Variants | `Severity=Warning/Error`; canonical **24px icon is an in-flow child of the RTL Title Row** (physical right of title), gap 8px, bound to existing public `fg/warning` / `fg/danger` tokens; no absolute icon |
| Content | Title, required short message in Description, optional hidden native Body Slot, native Footer Slot (acknowledge or retry/cancel examples) |
| Visual rules | Independent Shell in Figma, zero shell padding and no nested Dialog/Base. Existing semantic tokens. Header top/inline Regular 32px, Narrow 24px; optional Body top 16px; Footer top/inline/bottom Regular 32px, Narrow 24px (explicit content-to-actions gap). Title/Description gap 8px |
| Semantics | `alertdialog` only when an urgent modal interruption is warranted; ordinary notifications remain inline or Toast |
| Status | Figma design review draft, **not** registered runtime/Storybook or production-ready |

### File Uploader — final Carbon design source (runtime unverified)

| Field | Verified Figma source |
| --- | --- |
| DS component | File Uploader (Carbon-derived) |
| Figma presentation (canonical) | `24020:785` — 1600px _Docs structure |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Original public component set | `File uploader` — `5465:294860` — **15 variants** (Type × Size × State) |
| Public variant axes | Type: Default / Drag and drop; Size: Large / Medium / Small; State: Enabled / Disabled; Drag and drop also Skeleton |
| Public authoring | Text: Label text, Desc. text; Boolean: Files (file-list visibility) |
| Default copy | `Desc. text`: «فایل موردنظر را انتخاب کنید.»; Dropzone `Helper text`: «فایل را اینجا بکشید و رها کنید یا روی «انتخاب فایل» کلیک کنید». No hard-coded file limits. |
| Design status | **Final (Figma + component contract)**, not runtime-verified and not production-released |
| Original internal File Item set | `_File uploader file item` — `3199:35182` — **18 variants** (6 states × 3 sizes) |
| Original internal Dropzone state set | `_File uploader - Drag and drop box states` — `3183:29103` — **4 states** |
| Original File List master | `_File uploader file list item` — `4188:102462` — **one native `File list#23998:0` Slot** |
| File List default content | Exactly **three existing source-linked File Item instances**, original IDs preserved, hidden duplicates removed; no fixed count variant |
| Presentation arrangement | Original public set in §01; all three original internal masters in §03; **six** source-linked scenarios in §02 (one/multiple, RTL error, disabled, mixed states, long filename) |
| Figma published component keys | Not independently verified in this audit; node IDs and instance links verified |
| Runtime / code props | **Unregistered / unverified** |
| Storybook and executed tests | **Unregistered / unverified** |
| Design handoff | **Ready for development/sandbox** with finalized design contract; runtime/API, validated product policies, executed accessibility/network tests still pending |

[Open canonical Carbon presentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24020-785)

**Superseded exploratory source, retained for comparison (not canonical):** HOS-39 pilot documentation `23907:394`, Uploader `23905:614` (4 variants), File Item `23903:127017` (5), Dropzone `23905:565` (6). All are archived visually in the Figma Archive; their runtime behavior/illustration proposals must **not** be read as properties of the Carbon master. No consumer components were detached or force-migrated.

### Button

| Field | Current value |
|---|---|
| DS component | Button |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Button / Default` |
| Figma component key | `be5d0d9cd5fdd02f9d7afa1e371c2f2a23acb329` |
| Figma node ID | `1854:1776` |
| Figma variant properties | `Style / Size / State / Loading` |
| Figma content properties | `Button text / Start Icon / End Icon / Swap Start Icon / Swap End Icon` |
| Figma styles | `Brand / Primary / Secondary / Tertiary / Ghost / Danger Primary / Danger Tertiary / Danger Ghost` |
| Figma sizes | `Extra Small 28 / Small 32 / Medium 40 / Large 48` |
| Figma states | `Enabled / Hover / Active / Focus / Disabled` |
| Loading representation | `False / True`, separate from interaction State; directly uses Progress Circle / Indeterminate / Small, 16px, State=Active, line/default track + line/accent arc on surface/disabled (HOS-46); no Loading wrapper |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer code prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Button design identity and current Figma property model are verified. Runtime API, Storybook identity, and Figma-to-code prop mapping remain deliberately unverified because the owning runtime Design System repository/package and Storybook source are not yet registered. Track that source gap through the integration contract rather than guessing from Figma.


### Icon Button

| Field | Current value |
|---|---|
| DS component | Icon Button |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Icon Button / Default` |
| Figma component key | `f9b7af4bd9afaf768ae955c51ccddd29833c5ca7` |
| Figma node ID | `22685:1410` |
| Figma variant properties | `Style / Size / State` |
| Figma content properties | `Icon` instance swap |
| Figma styles | `Brand / Primary / Secondary / Tertiary / Ghost / Danger Tertiary / Danger Ghost` |
| Figma sizes | `Extra Small 28 / Small 32 / Medium 40 / Large 48` |
| Figma states | `Enabled / Hover / Active / Focus / Disabled` |
| Icon size | Fixed `18px` |
| Tooltip contract | Required for operable Icon Buttons on hover/focus; Tooltip does not replace the accessible name |
| Loading / Selected | Not part of the current Icon Button contract |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer code prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Icon Button design identity and current Figma property model are verified. Its accessible-name, Tooltip, sizing, destructive-action, and state boundaries are defined in `../design-system/components/icon-button.md`. Runtime API, Storybook identity, Tooltip composition strategy, and Figma-to-code prop mapping remain deliberately unverified until the owning runtime Design System source is registered.



### Menu

| Field | Current value |
|---|---|
| DS component | Menu |
| Knowledge document | `../design-system/components/menu.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Menu / Default` |
| Figma component key | `5b8278235b0cefb99927a2507739afb15ace8f3b` |
| Figma node ID | `17332:167748` |
| Figma variant properties | `Size / Layout` |
| Figma content properties | `Content` native SLOT |
| Variant count | `8 = 4 Size × 2 Layout` |
| Figma sizes | `Extra Small 28 / Small 32 / Medium 40 / Large 48` item baseline; default `Medium` |
| Menu layouts | `Simple / Complex`; default `Simple`; Simple collapses leading, Complex reserves a `16px` leading column across items; default Complex authoring content shows the shared Start icon |
| Menu width | `160px min / 200px default / 320px max` |
| Menu surface | `surface/raised + Shadow/Floating + 12px Large radius` |
| Menu Item set | `Menu Item / Default` |
| Menu Item key | `77d84f9c0d0377652a87f13ef915c65412655073` |
| Menu Item node ID | `17332:167436` |
| Menu Item variants | `40 = 4 Size × 5 State × 2 Tone` |
| Menu Item states | `Default / Hover / Active / Focus / Disabled` |
| Menu Item tones | `Default / Danger`; Disabled is State and visually overrides Tone |
| Menu Item content properties | `Label / Leading / Checked / Show start icon / Start icon / Show shortcut / Shortcut / Submenu` |
| Submenu depth | JV v1 authoring supports `Root Menu → one child Submenu` only; no submenu trigger inside the child submenu |
| Submenu composition | Child surface reuses `Menu / Default`, matches parent Size, keeps independent `160–320px` width, uses 2px surface gap, opens toward logical End and may flip on collision |
| Menu Item anatomy | Flat direct children: `Trailing + Label + Leading`; no active nested Menu Item Content component |
| Leading rule | `Leading=false` collapses the Start column; `Leading=true` reserves `16px`; Leading/Trailing containers are transparent; Menu Layout controls the default composition |
| Width ownership | Menu owns `160–320px` shell width; Menu Item has no independent min/max width and fills the Menu content slot |
| Icon color override | Shared icon components keep a fixed base color; Menu Item explicitly overrides icons by Tone/State: Default → `fg/primary`, Danger → `fg/danger`, Disabled → `fg/disabled`; re-check after icon swap |
| Group Label | `Menu Group Label / Default`, node `23038:129820`, key `ae3dbe7236e339083cccd60ad047306201c0f6c6` |
| Divider | `Menu Divider / Default`, node `23038:129822`, key `8cb217e111f87fa16785890815d769083ac7e5ec` |
| Legacy migration assets | `Legacy / Menu Item Content` key `3c4735684b5eb1146dab273119bcc59dbceee8aa`; `Legacy / Keyboard shortcut` key `e2113c87df4d0d02d41477f4c706fb6b30a6437a`; `Legacy / Overflow menu` key `89d20a2413e0b877ce2d9c358ce75bb903155bfb`; retained Overflow Open uses an absolute Menu overlay, `clip content = false`, 2px trigger gap, and unchanged trigger bounds |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-23 |

The Menu design identity, action/command boundary, Size × Layout model, flat Menu Item anatomy, Size × State × Tone Menu Item model, one-level submenu composition/depth, grouping helpers, RTL geometry, semantic visual treatments, width/truncation rules, and accessibility contract are verified in `../design-system/components/menu.md`. Runtime API, exact DOM/focus implementation, overlay/positioning engine, Storybook identity, and Figma-to-code prop mapping remain deliberately unverified until the owning runtime source is registered.

### Menu Button

| Field | Current value |
|---|---|
| DS component | Menu Button |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Menu Button / Default` |
| Figma component key | `166f62776a8c17f3ccdc9f4891892fcd380be68c` |
| Figma node ID | `22930:811` |
| Figma variant properties | `Size / Open` |
| Variant count | `8 = 4 Size × 2 Open` |
| Figma content properties | `Menu content` native SLOT; exposed nested `Trigger / Button` |
| Figma sizes | `Extra Small 28 / Small 32 / Medium 40 / Large 48` |
| Default trigger | Canonical Button / Tertiary; approved Menu Button styles: Primary / Tertiary / Ghost |
| Open representation | `Open=True` maps Trigger to Active + chevron-up; Menu remains outside trigger layout |
| Anchor gap | `2px` per shared contextual-surface rule |
| Loading | No top-level Loading state; loading content belongs inside Menu |
| Menu size alignment | Extra Small / Small / Medium / Large map 1:1 to canonical Menu 28 / 32 / 40 / 48 |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-20 |

The Menu Button design identity, Button composition, native Menu Slot, Size × Open matrix, 2px anchoring rule, RTL geometry, and Menu Button accessibility contract are verified in `../design-system/components/menu-button.md`. Runtime popup API, exact prop names, collision/portal implementation, and Storybook identity remain unverified.


### Combo Button

| Field | Current value |
|---|---|
| DS component | Combo Button |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Combo Button / Default` |
| Figma component key | `c6f34b8a4294241844d10349881d8264b1c072eb` |
| Figma node ID | `22932:134187` |
| Figma variant properties | `Style / Size / Open` |
| Variant count | `24 = 3 Style × 4 Size × 2 Open` |
| Figma styles | `Primary / Secondary / Tertiary` |
| Figma sizes | Heights: `Extra Small 28 / Small 32 / Medium 40 / Large 48`; current default widths: `98 / 118 / 134 / 150px` (Divider adds zero layout width) |
| Composition | Shared `Unified shell / Wrapper` (horizontal Auto Layout) containing canonical `Menu Trigger / Icon Button` + 1px semantic `Divider` Rectangle + canonical exposed `Primary Action / Button`; native `Menu content` SLOT is a direct child of the public Combo variant, out of layout |
| Inter-segment treatment | Canonical Buttons touch with **zero gap**. The non-interactive Divider is a **1px visible Rectangle positioned ABSOLUTE** at `Trigger.width − 1px`, centered vertically, height `control height − 16px`, and **0px layout width**. Wrapper is Hug-width. Semantic fills: Primary `line/inverse`, Secondary `line/emphasis`, Tertiary `line/default`. No child joining strokes. Tertiary retains 1px outside-aligned `line/default` border on Wrapper |
| Open representation | Only Menu Trigger maps to Active + chevron-up; Primary Action state remains independent |
| Anchor gap | `2px` |
| Loading | Owned by nested Primary Action; no outer Loading axis |
| RTL | Primary Action logical Start/right; Menu Trigger logical End/left |
| Menu size alignment | Extra Small / Small / Medium / Large map 1:1 to canonical Menu 28 / 32 / 40 / 48 |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-10-17; 24/24 canonical variants and 13 Playground instances passed structural and visual-state QA |

The Combo Button design identity, shared Wrapper + semantic Divider architecture, preserved canonical Button/Icon Button instance links and native Menu Slot, Style × Size × Open matrix, independent segment behavior, 2px anchoring, RTL geometry, Loading boundary and accessibility contract are documented and Figma-verified in `../design-system/components/combo-button.md`. Runtime component/API, Storybook identity, and exact Figma-to-code property mapping remain unverified.


### Tooltip

| Field | Current value |
|---|---|
| DS component | Tooltip |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Tooltip / Default` |
| Figma component key | `e29f8f48a0b3ec52f9490d4a9c101df5fba9d769` |
| Figma node ID | `22773:127299` |
| Figma variant properties | `Side / Align` |
| Figma content properties | `Text` |
| Figma matrix | `4 Sides × 3 Alignments = 12 variants` |
| Anatomy | Inverse Surface + text; no caret / arrow |
| Anchor offset | Fixed `2px` Surface-to-trigger gap |
| Visual roles | `surface/inverse + fg/on-inverse`; no border; no shadow |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer code prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

Tooltip design identity, arrowless anatomy, placement matrix, RTL mapping, 2px anchor offset, and Icon Button consumer contract are verified. Runtime delay, collision/flip, portal/layering, package/API identity, Storybook identity, and Figma-to-code mapping remain deliberately unverified until the owning runtime source is registered.


### Accordion

| Field | Current value |
|---|---|
| DS component | Accordion |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component | `Accordion` |
| Figma component key | `649891c2bfc1413f60f04011bc71a05576d12738` |
| Figma node ID | `22821:129502` |
| Figma content properties | `Items` native SLOT |
| Items Slot | 1+ children, zero gap, preferred/allowed content = `Accordion Item` |
| Default authoring content | 3 collapsed Accordion Item instances; count is not fixed |
| Group behavior | Multiple-open default; Single-open explicit runtime option; both allow all-collapsed |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

### Accordion Item

| Field | Current value |
|---|---|
| DS component | Accordion Item / standalone Disclosure |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Accordion Item` |
| Figma component key | `2728144865f9616dd66228719b4fb71936e3062a` |
| Figma node ID | `22794:548` |
| Figma variant properties | `Size / State / Expanded / Indicator position` |
| Variant count | 48 |
| Figma content properties | `Title / Content` |
| Content | Native Figma SLOT with editable default Body text; accepts arbitrary frames/text/component instances |
| Figma sizes | `Large 48 / Medium 40 / Small 32` minimum Trigger heights |
| Figma states | `Enabled / Hover / Focus / Disabled`; Active is runtime-only |
| Indicator position | `Start / End`; in RTL Start=right and End=left |
| Composition | Same Item may be used alone as Disclosure or inside Accordion Items Slot |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

Accordion and Accordion Item design identities, native Slot composition, visual state model, RTL geometry, and current Figma property models are verified. Runtime API, exact DOM/animation implementation, Storybook identity, and Figma-to-code property mapping remain deliberately unverified until the owning runtime Design System source is registered.

### Link

| Field | Current value |
|---|---|
| DS component | Link |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Link / Default` |
| Figma component key | `f31eac5461a0d8a608089f696b3b1402590be8a9` |
| Figma node ID | `22920:125581` |
| Figma variant properties | `Style / Size / State` |
| Variant count | `27 = 3 Style × 3 Size × 3 Figma State` |
| Figma content properties | `Link text / End icon / Swap end icon` |
| Figma styles | `Default / Subtle / Inverse` |
| Figma sizes | `Small 12/16 / Medium 14/20 / Large 16/24`; Medium default |
| Figma states | `Enabled / Hover / Focus`; Active is runtime-only and visually matches Hover |
| Background | Transparent component and Label wrapper in every variant |
| Underline behavior | Enabled none; Hover / Active / Focus underlined at runtime |
| Figma underline implementation | Responsive 1px label-width helper; Enabled opacity 0, Hover/Focus opacity 1; runtime uses real text-decoration |
| Icon geometry | Optional End icon only; fixed `18px`, `8px` label gap |
| Deliberate exclusions | No Underline axis, Start icon, Disabled, Visited, Bold, or legacy Inline axis |
| Inline / multiline Figma authoring | Native Text range using Link semantic token + persistent underline; inherits surrounding typography |
| Legacy Figma component | `Link / Legacy`, node `3245:28722`; migration only |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer code prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Link design identity, Style × Size × State Figma model, transparent anatomy, semantic token mapping, state-driven underline behavior, End-icon geometry, and native-Text inline/multiline authoring boundary are verified in `../design-system/components/link.md`. Runtime API, Storybook identity, and Figma-to-code prop mapping remain deliberately unverified until the owning runtime Design System source is registered.


### Breadcrumb

| Field | Current value |
|---|---|
| DS component | Breadcrumb |
| Knowledge document | `../design-system/components/breadcrumb.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component | `Breadcrumb` |
| Figma component key | `b0fb38288d8b84e0ff6e1d5ded6eeb31574581fa` |
| Figma node ID | `22973:282463` |
| Figma content properties | `Items` native SLOT |
| Default authoring content | 3 visible Breadcrumb Item instances |
| Items Slot | min 2 children; preferred/allowed content = `Breadcrumb Item / Default`; default content visible on insertion |
| Breadcrumb Item set | `Breadcrumb Item / Default` |
| Breadcrumb Item key | `e0fcea8c52b6deb183c6d2c4624243875ae21425` |
| Breadcrumb Item node ID | `22986:407` |
| Breadcrumb Item variants | `Type = Link / Current / Overflow` |
| Breadcrumb Item content property | `Current label` |
| Link composition | canonical `Link / Subtle / Medium`; interaction states delegated to Link |
| Overflow composition | canonical `Icon Button / Ghost / Extra Small`; popup/menu behavior delegated to owning runtime pattern |
| Current page | always present, non-interactive, semantic current-page item |
| Layout | single-line; 8px Items Slot gap; deep paths use Root / Overflow / Parent / Current |
| Legacy Figma | `Breadcrumb / Legacy` and `Breadcrumb Item / Legacy`; migration/reference only |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names or overflow algorithm from Figma |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Breadcrumb design identity, Item composition, Link/Icon Button reuse, current-page treatment, single-line truncation/collapse model, RTL behavior, native Slot authoring, and accessibility contract are verified in `../design-system/components/breadcrumb.md`. Runtime API, exact DOM/popup implementation, collapse measurement algorithm, Storybook identity, and Figma-to-code mapping remain deliberately unverified until the owning runtime Design System source is registered.


### Inline Notification

| Field | Current value |
|---|---|
| DS component | Inline Notification |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Inline Notification` |
| Figma component key | `eb09e1db167646902904f70dfd4e3a194a8a265d` |
| Figma node ID | `22838:3046` |
| Figma variant properties | `Status` |
| Figma content properties | `Message / Description / Show description / Action / Dismissible / Action content` |
| Variant count | 4 = Info / Success / Warning / Error |
| Action composition | Native `Action content` SLOT; current preferred components are shared Link and Tertiary Small Button |
| Dismiss composition | Shared `Icon Button / Ghost / Medium`, absolute top-left in RTL |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Inline Notification design identity, severity matrix, content anatomy, native Action Slot, RTL dismiss geometry, typography, and semantic token mapping are verified in `../design-system/components/notification.md`.

### Toast

| Field | Current value |
|---|---|
| DS component | Toast |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Toast` |
| Figma component key | `5c164a8b212650d4e9e322a9088fbc4fc4e7628f` |
| Figma node ID | `22839:3058` |
| Figma variant properties | `Status / Contrast` |
| Figma content properties | `Title / Message / Show title / Action / Dismissible / Timeout indicator / Action content` |
| Variant count | 8 = 4 Status × 2 Contrast |
| Contrast | `Normal / High`; High is inverse-surface treatment, not severity |
| Action composition | Native `Action content` SLOT; Normal defaults to Default Link, High defaults to Inverse Link |
| Dismiss composition | Shared `Icon Button / Ghost / Medium`, absolute top-left in RTL |
| Elevation | `Shadow/Floating` |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Toast design identity, Status × Contrast matrix, native Action Slot, timeout-indicator capability, RTL dismiss geometry, typography, elevation, and semantic token mapping are verified in `../design-system/components/notification.md`. Exact runtime timing, queue/stack behavior, placement, announcement behavior, and High-Toast Button treatment remain unverified.


### Checkbox

| Field | Current value |
|---|---|
| DS component | Checkbox |
| Knowledge document | `../design-system/components/checkbox.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Checkbox / Default` |
| Figma component key | `af1fdbe97bf103d8ae5e4540d36f4ffb284cc35b` |
| Figma node ID | `3193:29303` |
| Figma variant properties | `Selection / State` |
| Variant count | `9 = 3 Selection × 3 State` |
| Figma content properties | `Label / Show label` |
| Figma selections | `Unchecked / Checked / Indeterminate` |
| Figma states | `Default / Focus / Disabled` |
| Visual size | `20px` Checkbox icon instance; source icon artwork scales proportionally inside the nested instance |
| Label gap | `8px` |
| Selection semantics | Exact local Icons-page components: unchecked node `15087:365340` key `b4b5e8aad25d7be4009568638bc86a3b85a6a185`; checked node `15087:365337` key `a9b3101d611597626af94d5f3a63a08058bbceab`; indeterminate node `15087:365343` key `ae823e542df2e4ac6c644e4ce8b97fe13aaa5b89`; Unchecked = `fg/secondary`, Checked/Indeterminate = `fg/accent` |
| Focus | shared `focus/default` 2px outside ring with 1px gap; independent from selection |
| RTL | logical inline-start control / inline-end label; no Position variant |
| Checkbox Group set | `Checkbox Group / Default` |
| Checkbox Group key | `9c6f915d8bc3399d2f02fd0aad20218757b0749f` |
| Checkbox Group node ID | `23020:127117` |
| Checkbox Group properties | `Direction / Group label / Show group label` |
| Checkbox Group directions | `Vertical / Horizontal` |
| Horizontal group sizing | item instances Hug contents; `16px` inter-item gap |
| Validation | owned by surrounding form-field composition; no Error/Warning Checkbox variants |
| Loading | outside base Checkbox state matrix; use Skeleton composition rather than Skeleton variants |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Checkbox design identity, exact local icon-library sources, Selection × State matrix, 20px icon sizing, first-line/top-aligned multiline behavior, semantic color mapping, focus treatment, flexible-width/multiline behavior, Checkbox Group direction contract, validation/loading boundaries, RTL geometry, Indeterminate semantics, and accessibility contract are verified in `../design-system/components/checkbox.md`. Runtime API, exact DOM/event semantics, Storybook identity, and Figma-to-code prop mapping remain deliberately unverified until the owning runtime Design System source is registered.


### Radio

| Field | Current value |
|---|---|
| DS component | Radio |
| Knowledge document | `../design-system/components/radio.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Radio / Default` |
| Figma component key | `a1e6b8ca998c57f78abd75b97b190aacbd662f44` |
| Figma node ID | `2930:23442` |
| Figma variant properties | `Selected / State` |
| Variant count | `6 = 2 Selected × 3 State` |
| Figma content properties | `Label / Show label` |
| Figma states | `Default / Focus / Disabled` |
| Visual size | `20px` Radio icon instance; source icon artwork scales proportionally inside the nested instance |
| Label gap | `8px` |
| Selection semantics | Exact local Icons-page components: unchecked node `15087:365350` key `c8005abc2598ad492de5ac17df5cfb9dc1a4509b`; checked node `15087:365346` key `5acf2d061791622a49c9826cd671f165d6648f73`; Unselected = `fg/secondary`, Selected = `fg/accent` |
| Focus | shared `focus/default` 2px outside ring with 1px gap; independent from selection |
| RTL | logical inline-start control / inline-end label; no Position variant |
| Radio Group set | `Radio Group / Default` |
| Radio Group key | `8a24b1caa72671235a5c9d26706efcc845f45eee` |
| Radio Group node ID | `2927:28166` |
| Radio Group properties | `Direction / Group label / Show group label` |
| Radio Group directions | `Vertical / Horizontal` |
| Validation | owned by surrounding form-field composition; no Error/Warning Radio variants |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Radio design identity, exact local icon-library sources, Selected × State matrix, 20px icon sizing, first-line/top-aligned multiline behavior, semantic color mapping, focus treatment, flexible-width/multiline behavior, Radio Group direction contract, validation boundary, RTL geometry, and accessibility contract are verified in `../design-system/components/radio.md`. Runtime API, exact DOM/event semantics, Storybook identity, and Figma-to-code prop mapping remain deliberately unverified until the owning runtime Design System source is registered.


### Toggle

| Field | Current value |
|---|---|
| DS component | Toggle |
| Knowledge document | `../design-system/components/switch.md` (legacy path/id retained for compatibility) |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Toggle` |
| Figma component key | `0c632b79747ffac5f05a4f2c762f81ddcb8293d7` |
| Figma node ID | `22928:125569` |
| Figma variant properties | `Size / State / Toggled` |
| Variant count | `24 = 2 Size × 6 State × 2 Toggled` |
| Figma content properties | `Label / Show label` |
| Figma sizes | `Medium 48×24, thumb 18` / `Small 32×16, thumb 10` |
| Figma states | `Default / Hover / Active / Focus / Disabled / Read-only` |
| Off visual | `surface/neutral-muted*` track; fixed white `palette/bw/white` thumb; no persistent border |
| On visual | `surface/accent-emphasis*` track; fixed white `palette/bw/white` thumb |
| Focus | `focus/default` 2px outside ring, independent from On/Off |
| RTL | Authored Off thumb right / On thumb left; runtime mirrors in LTR rather than adding an RTL variant |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-19 |

The Toggle design identity, Size × State × Toggled matrix, label contract, neutral/accent visual treatment, fixed-white Thumb, focus behavior, RTL geometry, motion guidance, and accessibility contract are verified in `../design-system/components/switch.md`. Runtime API, exact DOM/event semantics, Storybook identity, exact motion constants, and Figma-to-code prop mapping remain deliberately unverified until the owning runtime Design System source is registered.


### Content Switcher

| Field | Current value |
|---|---|
| DS component | Content Switcher |
| Knowledge document | `../design-system/components/content-switcher.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Content Switcher` |
| Figma component key | `2d44a4df734823788a122e9a9c73fec3bd6e4ff2` |
| Figma node ID | `23083:1746` |
| Figma variant properties | `Size` |
| Figma content property | `Items` native SLOT |
| Variant count | `3 = Small / Medium / Large` |
| Figma sizes | `Small 32 / Medium 40 / Large 48` total control height; no XS |
| Item content axis | `Content = Text / Icon`; keep one Content value across the control; Icon + Text intentionally unsupported |
| Default authoring content | 3 equal-width Items; exactly one Selected |
| Composition | 2–5 Items; count is Slot composition rather than a variant axis; single-line, no wrap |
| Internal Item set | `_Content Switcher Item`, node `23038:127212`, key `17b39a5fe6a7b1fbd1679202f90e2ca2a45aba35` |
| Item properties | `State / Content / Label / Icon` |
| Item states | `Default / Hover / Active / Focus / Disabled / Selected`; Selected is terminal |
| Size behavior | Parent owns 32/40/48 total height and 28/36/44 Slot height; slotted Items use vertical Fill. No internal Size/Content variable modes. |
| Geometry | Track radius 8px component-local; Item radius canonical `6px · Medium`; 2px inset; 2px Item gap; fixed 16px Item horizontal padding; no divider |
| Track | `surface/inset` |
| Deprecated-token check | No deprecated Radius bindings; no internal Content Switcher Size/Content variable collections |
| Typography | `Label/SM` = Vazirmatn Medium 14/20, aligned with Button Small/Medium/Large |
| Selected | `surface/default + fg/primary` |
| Icon color override | Shared Icons retain purple guard source color; Item overrides Default → `fg/secondary`, Hover/Active/Focus/Selected → `fg/primary`, Disabled → `fg/disabled`; verified to survive Icon swap |
| Responsive | Never wrap; Icon-only only when unambiguous, otherwise use Menu/Select |
| RTL | No RTL/Position variant; compose in logical reading order |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names or DOM/ARIA roles from Figma |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-10-15 |

The Content Switcher design identity, three-size parent model, native Items Slot, State × Content internal Item model, fill-based sizing, Text/Icon boundary, selected treatment, semantic foreground mapping, equal-width composition, responsive rule, RTL behavior, and accessibility contract are verified in `../design-system/components/content-switcher.md`. Runtime API, exact DOM/ARIA and keyboard implementation, Storybook identity, and Figma-to-code property mapping remain deliberately unverified until the owning runtime source is registered.


### Tabs

| Field | Current value |
|---|---|
| DS component | Tabs |
| Knowledge document | `../design-system/components/tabs.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component | `Tabs / Default` |
| Figma component key | `d79023ff7c2575d09ea714814c8d7e75fbac1662` |
| Figma node ID | `23486:300` |
| Figma content property | `Items` native SLOT |
| Canonical appearance | Line only |
| Canonical size | 40px |
| Item spacing | `24px` owned by Tabs; Text/Text + Icon use `0px` inline padding |
| Default width | Text items Hug contents; Icon-only items are `40×40px`; equal-width is a consuming-layout decision, not a variant |
| Composition | Variable item count through Items Slot; exactly one Selected in normal usage; single-line, no wrap |
| Internal Item set | `_Tab Item`, node `23486:299`, key `883007580c6e232e8ca2ba70a64c90ed80b73067` |
| Item variants | `21 = 3 Content × 7 State` |
| Item variant properties | `Content / State` |
| Item content modes | `Text / Text + Icon / Icon only` |
| Item states | `Default / Hover / Active / Focus / Selected / Selected Focus / Disabled` |
| Item content properties | `Label / Icon`; Label remains the accessible-name authoring source for Icon-only |
| Content consistency | One content mode per tablist; do not mix Text / Text + Icon / Icon-only items in one group |
| Interaction treatment | Hover = foreground-only; Active = `fg/primary` + 2px `line/emphasis` bottom indicator; Selected = `fg/primary` + 2px `line/accent` bottom indicator; no Hover/Active backgrounds |
| Shared tablist line | 1px `line/default` |
| Focus | shared `focus/default` outer ring with 1px surface gap; Selected Focus authored explicitly |
| Overflow | no wrap; runtime horizontal scroll/equivalent mechanism; no canonical Previous/Next arrow API |
| Counter | legacy Tag-based counter removed; wait for validated Badge/count primitive and repeated need |
| RTL | no RTL variant; logical reading-order composition |
| Content Switcher boundary | Tabs = peer content panels; Content Switcher / Segmented Control = alternate representations/modes of same content |
| Legacy Figma | old Type/Size/Alignment/Skeleton/Selected-boolean/overflow-arrow models retained under Legacy names for migration only |
| Documentation frame | `Tabs / Documentation`, node `23488:286` |
| Future TBD | Vertical Tabs and Pill-style Tabs are explicitly out of v1; evaluate only after validated product use cases |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names, DOM/ARIA roles, route behavior, activation mode, or overflow algorithm from Figma |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-10-15 |

The Tabs design identity, line-only v1 appearance, native Items Slot composition, Content × State internal Item model, 40px density, zero-inline-padding + 24px parent-gap layout, Text/Text+Icon/Icon-only content modes, selected/focus treatment, overflow rule, Content Switcher/navigation/filter boundaries, RTL behavior, and accessibility contract are verified in `../design-system/components/tabs.md`. Runtime API, exact DOM/ARIA implementation, activation mode, routing integration, Storybook identity, and Figma-to-code mapping remain deliberately unverified until the owning runtime source is registered.

### Chip

| Field | Current value |
|---|---|
| DS component | Chip |
| Knowledge document | `../design-system/components/chip.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Selectable set | `Chip / Selectable` |
| Selectable key / node | `5571e8e324b47155d7e9fd384aaea289c2e54d89` / `20783:128158` |
| Selectable variants | `20 = 2 Size × 2 Selected × 5 State` |
| Selectable properties | Variant: `Size / Selected / State`; content: `Label` |
| Removable set | `Chip / Removable` |
| Removable key / node | `193062043a2194024cc06c6d45f11b96b4a238b3` / `23124:358` |
| Removable variants | `10 = 2 Size × 5 State` |
| Removable properties | Variant: `Size / State`; content: `Label / Detail / Show detail / Show leading visual / Leading visual`; `Show detail` controls the whole `Detail content` container |
| Removable behavioral capability | Body may be independently actionable; body and trailing Remove are separate runtime interaction/focus targets; Body action is not a Figma variant |
| Removable surface | `surface/accent-muted + line/accent + fg/accent`; Hover/Active preserve the Accent base and layer `surface/transparent-hover/active`; Disabled uses shared selected-disabled treatment |
| Disclosure set | `Chip / Disclosure` |
| Disclosure key / node | `3ba6c8dc36a76632d1569108e024ae47c841a50c` / `20783:534` |
| Disclosure variants | `20 = 2 Size × 2 Applied × 5 State` |
| Disclosure properties | Variant: `Size / Applied / State`; content: `Label / Summary / Show summary`; `Show summary` controls the whole `Summary content` container |
| Disclosure Open | Runtime-only; removed from Figma variants because reviewed Open treatment duplicated Hover visually |
| Disclosure Applied surface | `surface/accent-muted + line/accent + fg/accent`; Hover/Active preserve the Accent base and layer `surface/transparent-hover/active`; Focus preserves base + `Focus/Default` |
| Action set | `Chip / Action` |
| Action key / node | `876535cdb18030fe2d38c6c6221036d770838586` / `23123:125056` |
| Action variants | `10 = 2 Size × 5 State` |
| Action anatomy | Optional add/action icon at logical End — visually left of the label in RTL |
| Action properties | Variant: `Size / State`; content: `Label / Show trailing icon / Trailing icon` |
| Shared states | `Default / Hover / Active / Focus / Disabled` |
| Figma sizes | `Small 32 / Medium 40` |
| Label text style | `Body/Compact/SM` across all four Chip sets |
| Main content gap | `8px` shared spacing variable |
| Secondary content | Disclosure uses `Summary content`; Removable uses `Detail content`; each contains `Divider (·) + value` with `4px` internal gap |
| Summary / Detail property value | Value only; separator is structural and must not be embedded in the property string |
| Radius | shared `Radius / Full` — current Chip visual direction |
| Focus | shared `Focus/Default` outside focus-visible ring |
| Color | Semantic tokens only; every Chip Hover/Active preserves its semantic base and layers `surface/transparent-hover/active`: default-base states use `surface/default`; Selectable Selected, Disclosure Applied, and Removable use `surface/accent-muted + line/accent + fg/accent`; no public Color axis or Chip-specific color tokens |
| Usage mapping | Choice + Direct Filter → Selectable; Faceted/Popover Filter → Disclosure; committed/input value → Removable; add/start available value → Action |
| Visual grammar | `✓ selected at logical Start before label / ▾ disclose / × remove / + add-start` |
| Product-pattern boundary | Selection mode, required/allow-empty, filter composition, tokenized-input behavior, and software Available→Selected layout live at Group/Pattern level |
| Tag boundary | Tag remains passive/descriptive/categorical and owns `tag/{color}/*`; Chip is interactive and must not consume Tag color tokens |
| Legacy Figma | old Carbon-derived Chip sets, Control-chip artifacts, and old Chip Group components are reference-only; published identities preserved where safe |
| Documentation frame | `Chip / Documentation`, node `23143:531`; includes Component Set, Playground, real Disclosure+Popover composition, and migration note |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime props, DOM/ARIA roles, compound-control structure, or popup implementation from Figma |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-09-23 |

The Chip design identity is verified as four capability-specific public component sets that share one visual recipe without a mega Type matrix. Selectable, Removable, Disclosure, and Action contracts, current Full radius, 8px main content gap, separate Divider + Summary/Detail secondary-content anatomy, Accent treatment for Selectable Selected / Disclosure Applied / Removable, shared structured-surface Hover/Active overlays across all Chip families, leading selected check anatomy, Action icon at logical End, focus-visible behavior, RTL anatomy, software lifecycle, Tag/Button/selection-control boundaries, real Disclosure + Popover composition, and legacy migration are documented in `../design-system/components/chip.md`. Runtime API, exact DOM/ARIA implementation, compound Removable structure, Storybook identity, and Figma-to-code property mapping remain deliberately unverified until the owning runtime Design System source is registered.


### Progress Bar (HOS-37)

| Field | Verified Figma source / status |
|---|---|
| DS component | Progress Bar |
| Knowledge document | `../design-system/components/progress-bar.md` — **final design documentation** |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma page | `Progress bar`, node `8930:400384` |
| Parent component set | `Progress bar` |
| Parent key / node ID | `1d9983588bb228a44ca2b3af89195bd1e2b51c9d` / `12603:272925` |
| Parent variants | **30** (25 preserved + 5 Active 100%); `Size=Small/Big`, `Alignment=Default/Inline/Indent`, `State=Active/Success/Error`, `Progress=0%/25%/50%/75%/100%/Indeterminate/Success/Error`; **not all permutations are authored** |
| Parent Text properties | `Label text / Helper text / Success text / Error text`; no public numeric Value property. Figma 0/25/50/75/100 are illustrative presets; runtime must use measured values |
| Nested source | `_Progress bar track item` |
| Track key / node ID | `b765a10f45d8d3ad69489a266bc6e623ba94d5b1` / `12603:273022` |
| Nested Track variants | 16 = `Small/Big` × `Progress=0%/25%/50%/75%/100%/Success/Error/Indeterminate` |
| Geometry | Small 4px, Big 8px; every public variant uses its matching nested Track Size. **Neutral Track and colored segments** all use 4/8px **inside bottom Strokes** with flat ends; no colored path Fill; no source master identity changes |
| Path Stroke tokens | Neutral Track: `line/default`; Active (including 100%/Indeterminate): `line/accent`; complete Success: `line/success`; complete Error: `line/error`. All have `STROKE_COLOR` scope and are bound to Strokes, never segment Fills. Text/icons retain existing `fg/*` roles |
| Indeterminate in public parent | **Verified in Figma** — 5 variants: Default Small/Big, Inline Small/Big, Indent Big. Source-linked nested Track (static visual; do not show numeric percentage). Motion remains runtime-owned |
| Runtime value treatment | True numeric progress is **required in development**, unrestricted by fixed Figma illustrative percentages. No numeric Figma property exists in current component architecture |
| Documentation frame | [Progress bar / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23867-126381), node `23867:126381` |
| Presentation source structure | **01 · Component set** contains the original public Master `12603:272925`; **03 · Anatomy & composition** contains original internal Track Master `12603:273022`; **02 · Playground** holds real linked instances. Compact two-column source-only canvas layout; no source re-creation |
| Presentation cleanup | One 1600px documentation frame on Progress bar page. Two obsolete IBM artboards plus their redundant instance-only visual matrix/anatomy removed; all master node IDs/keys and variants preserved |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — Figma axis labels are not runtime prop names |
| Storybook | **Bypassed for current design handoff** |
| Code Connect | **No registered mapping** |
| Long-text Figma QA | Default/Indent auto-grow vertically for Persian long copy; Inline label is one line with ending ellipsis. Playground contains linked mixed-script and long-text examples |
| Last live Figma verification | **2026-10-19** — all 16 nested and 30 public variants stroke-only path QA passed |

The **original master identities, physical Section 01/03 placement, and authored visual contract** above were verified against the live Figma file. Progress Bar uses the same four line-token roles as Progress Circle, now **implemented as Stroke-only path geometry**. The original old Figma Fill overrides in nested instances have been cleared. Playground examples remain connected to these sources. The public-parent Indeterminate variants are implemented in Figma as **static design states**; the original Inline/Big track-height mismatch and long-copy overflow are corrected. Numeric Figma percentages intentionally remain illustration presets; actual numeric value, Indeterminate animation, reduced motion, and browser/assistive-technology testing remain runtime development responsibilities. See `../design-system/components/progress-bar.md`.

### Progress Indicator (HOS-31)

| Field | Current value |
|---|---|
| DS component | Progress Indicator |
| Knowledge document | `../design-system/components/progress-indicator.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma page | `Progress indicator`, node `521:16785` |
| Parent component set | `Progress indicator` |
| Parent key / node ID | `335d54d47ea28e6329f88a8bb34dc3b2d02e5c77` / `23704:699` |
| Parent variants | `Direction=Horizontal/Vertical` = **2 variants** |
| Parent content property | Native `Items` SLOT shared by both Direction variants; each starts with 3 default Item instances |
| Parent authoring rule | Add/remove Progress Indicator Items inside the slot. When adding a new terminal Item in Figma, enable the previous terminal connector and disable the new terminal connector. Runtime derives sequence length and terminal connector from step data |
| Item component set | `_Progress indicator item` |
| Item key / node ID | `ebd4a7beb03d58ea243faaed501712880ffa2669` / `23704:348` |
| Item variants | `Direction=Horizontal/Vertical × State=Incomplete/Current/Completed/Error/Disabled` = **10 variants** |
| Item content properties | `Label / Helper / Show helper / Show connector` |
| Typography | Label = `Label/SM`; Helper = `Body/Compact/XS`; `Show helper` default = `true` in finalized Figma |
| Text limits | Horizontal Label 1 line / Helper 2; Vertical Label 2 / Helper 3; ending truncation |
| Marker size | 20px |
| Marker assets | Incomplete/Disabled: `Icon / dot mark outline`; Current: `Icon / dot mark`; Completed: `Icon/check_circle_outline`; Error: `Icon/error_outline` |
| Connector | 3px; Current/Completed = `line/accent`; Incomplete/Error/Disabled = `line/default`; none after final Item |
| Error contract | Error replaces Current for the affected step; helper communicates validation/problem detail |
| Responsive contract | No Compact/mobile variant in v1; mobile/narrow breakpoint and minimum supported size = **TBD**; until defined, do not compress Horizontal below usable width; prefer Vertical or a product-level responsive composition |
| Documentation frame | `Progress indicator / Documentation`, node `23730:499` |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified**; do not treat the 3 default Figma slot Items as a runtime limit |
| Property mapping | **Unverified** — do not infer runtime prop names from Figma property labels |
| Storybook | **Bypassed for current handoff** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-10-15 |

Progress Indicator and Item design identities, final Carbon-derived visual contract, state model, RTL authoring behavior, connector termination, helper placement, and text constraints are verified in Figma. Runtime sequence rendering, exact DOM/API, responsive product composition, and accessibility implementation remain development responsibilities. See `../design-system/components/progress-indicator.md`.


### Choice Group

| Field | Current value |
|---|---|
| DS component | Choice Group |
| Knowledge document | `../design-system/components/choice-group.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma page / docs | `Choice Group` node `23226:9` / `Choice Group / Documentation` node `23226:10` |
| Component set | `Choice Group` |
| Component key / node | `a96c066c443021689ce6add1a47be745c8aa160b` / `23229:133` |
| Variants | `12 = 2 Selection × 2 Layout × 3 State` |
| Variant properties | `Selection = Single / Multiple`; `Layout = Horizontal / Horizontal wrap`; `State = Default / Error / Warning` |
| Content properties | `Group label`; `Show group label`; `Required`; `Show info`; `Error message`; `Warning message`; exposed nested `Info / Tooltip`; native `Items` SLOT |
| Items Slot | Minimum 2 children; preferred/allowed content is `Chip / Selectable`; variable count, reorderable/configurable |
| Width | Resize the instance; no Width variant |
| Group label | Select-like label row; `Label/SM`; optional Required marker + Info/Tooltip; logical Start / visual right in RTL |
| Spacing | Shared `8px` token for group→items gap and item gap; shared `4px` token from Items→validation message |
| Runtime-only policy | Required enforcement / allow-empty; validation timing; tooltip open behavior |
| Ownership | Choice Group owns shared label affordances, group validation State/supporting copy, layout, item relationship, and selection mode; each Chip owns Label, Size, Selected, and interaction State |
| Single semantics | At most one selected; optional group may have no selection; Required is enforced/validated at runtime |
| Multiple semantics | Zero, one, or many selected; changing one item does not auto-clear another |
| State visuals | Label remains neutral `fg/secondary`; Choice Group `Error` / `Warning` adds a 16px semantic status icon (`Icon/error_outline` / `Icon/warning_amber`) + `Body/Compact/XS` supporting message with a 4px icon/text gap and `fg/error` / `fg/warning`; nested Chip Hover/Active/Focus/Selected/Disabled visuals remain entirely item-owned |
| RTL | RTL-first. Horizontal uses normal logical-Start/right alignment. Horizontal wrap uses a Figma-only mirrored `Items` slot + counter-mirrored default Chip children while preserving logical source order; no RTL variant. Runtime must not reproduce the transforms and instead uses true RTL flow with logical DOM/reading order |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified** — do not infer runtime prop names or exact DOM/ARIA implementation from Figma |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-10-18 |

The Choice Group design identity, Single/Multiple selection contract, two layout modes (Horizontal / Horizontal wrap), Default/Error/Warning validation states, Select-like Required + Info/Tooltip label anatomy, neutral label + semantic group-level supporting validation copy, native Selectable-Chip Slot composition, resize-owned width, runtime-owned Required enforcement/allow-empty and tooltip-open behavior, RTL-first alignment plus the documented Figma-only wrap-mirror workaround, tokenized 8px/4px spacing, and boundaries with Radio/Checkbox/Select are verified in `../design-system/components/choice-group.md`. Exact runtime API, DOM/ARIA structure, keyboard implementation details, Storybook identity, and Figma-to-code mapping remain deliberately unverified until the owning runtime source is registered.

### Timeline

| Field | Current value |
|---|---|
| DS component | Timeline |
| Knowledge document | `../design-system/components/timeline.md` |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Figma component set | `Timeline` |
| Figma component key | `70716c3cb413b2669f06596426cea18ff7f7c92a` |
| Figma node ID | `23609:126914` |
| Figma variant axis | `Count=1 / 2 / 3 / 4 / 5 / 6`; default = `4`, **design-time only** |
| Figma authoring | 6 nested Timeline Item instances; Count shows a contiguous prefix and automatically terminates Connector on its last Item; no parent Items Slot |
| Timeline Item component set | `Timeline Item` |
| Timeline Item key / node ID | `3d90d9035ecdfe4f210b8602b8d8d93e8f59e7da` / `23509:48` |
| Timeline Item variants | `Density=Default / Compact` |
| Timeline Item text properties | `Title / Timestamp` |
| Timeline Item other properties | `Icon` instance swap; `Show timestamp / Show connector / Show content` Booleans; optional `Content slot` native SLOT |
| Neutral DS marker | `Icon/dot` key `e9def3d417c05352d5f86ed6d7553755399fd22d`, node `23609:9`; 24px icon with a centered 10px dot |
| Default geometry | 24px RTL start Axis; 1px Connector, 8px Marker-to-Connector gap; 4px Title/Timestamp; 16px Default / 12px Compact Header-to-Content |
| Tokens | `fg/primary` title, `fg/tertiary` time, `fg/secondary` default icon, `line/default` Connector; use existing spacing variable aliases |
| Use cases | Onboarding scheduled task groups (one time bucket → one Item with task list); My Applications event history (one event → one Item) |
| Documentation frame | `Timeline / Documentation · Reference` node `23618:417` |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified**; do not treat Figma Count as a runtime list limit or a required `count` prop |
| Property mapping | **Unverified** — design-to-code mapping is not established from Figma property labels alone |
| Storybook | **Bypassed for current handoff**; not required as a design acceptance condition |
| Code Connect | **No registered mapping** |
| Last Figma verification | 2026-10-14 |

Timeline and Timeline Item's **Figma identities** and visual/component contracts are verified. Runtime implementation must consume a dynamic ordered sequence of events of **unbounded length**, render consecutive connectors (but none after the last event), preserve accessible date/event semantics, and keep the Timeline/Stepper boundary. See `../design-system/components/timeline.md` for the Storybook-independent acceptance plan. Figma component keys above are identity values verified in the owning file; they do not on their own prove library publication.

### Data Table (HOS-35)

| Field | Verified Figma source / status |
|---|---|
| DS component | Data Table |
| Figma documentation page | [Data Table / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23522-13721) |
| Figma file key | `rROD8ctH9UfPGAMrRrOzHe` |
| Table component set | `Data Table / Default` |
| Table key / node ID | `30108b6ffc4e291d624fa9d9814d9277989157b8` / `23524:15759` |
| Table axes | `Size=Small/Medium/Large` × `Selection=None/Multiple` = **6 variants** |
| Header Row | `Data Table Header Row / Default`; key `86541d615f5152be8c6a2abbb16a2bd747202814`; node `23523:14084`; **3 variants** |
| Header Cell | `Data Table Header Cell / Default`; key `bea24d39aab0899bfd349a74fa89d798c60341ff`; node `23514:13393`; `Sort=None/Unsorted/Ascending/Descending` (**4**) |
| Row | `Data Table Row / Default`; key `4867a2edce9368611ef103a751be40b0d7ebe637`; node `23522:14296`; **12 = 3 Size × 4 State** |
| Row Item | `Data Table Row Item / Default`; key `18011b70289e5c947472d85885fb764fd4951c26`; node `23600:127401`; **6 = 3 Size × 2 Expanded** |
| Cell | `Data Table Cell / Default`; key `b60904ae0db53964e8b51d9230f07100522f279e`; node `23514:13381`; **3 Size variants** |
| Text Content | `Data Table Text Content / Default`; key `1c1c38a5b01dc81c2b721c08575b14c6cb1eb550`; node `23618:15999`; `Overflow=Truncate/Wrap` (**2**) |
| Text + Description | key `d7e6efee4d300fe04ff6aac62afe132c1b4a0bdb`; node `23577:15033` |
| Disclosure | key `0c7ed32cc1ac80725172dd16c0c79467ecf005cb`; node `23522:13764` |
| Expanded Content | key `eb42940cfaf7543a6393d0fb72737e02cf9a2748`; node `23526:15123` |
| Component doc | [Data Table](../design-system/components/table.md) |
| Runtime / acceptance proposal | [Table runtime contract](../design-system/components/table-runtime-contract.md) |
| Old components | Moved to separate Figma page `Archive / Data Table Legacy`; existing identities retained, V1 not canonical |
| Code repository/package | **Unregistered** |
| Runtime component/API | **Unverified** |
| Property mapping | **Unverified**; do not infer Angular inputs/outputs from Figma property names |
| Storybook | **Unregistered** |
| Code Connect | **No registered mapping** |
| Last live Figma verification | **2026-10-14** |

Figma IDs, keys and composition were verified against live Figma in HOS-35. Runtime source mapping and browser/assistive-technology tests remain explicitly unverified. The Figma pilot is **ready for sandbox implementation**, not a production/canonical runtime certification. The documentation changes remain in Draft PR #86 pending review.

## Rules

- Figma property labels do not automatically become code prop names.
- Figma variant options do not prove equivalent runtime enums/states exist.
- A code component with a similar display name is not a verified mapping by name alone.
- Storybook title/path similarity is not enough; link it to the owning code component.
- Record meaningful mismatches rather than forcing one-to-one parity.
- Component mapping should be maintained as integration metadata, not copied into every component guideline.

## Mapping priority

When runtime sources become available, map high-usage foundation components first:

```text
Button
Text Input
Select / Dropdown
Checkbox / Radio
Modal
Menu / Popover / Tooltip
Tabs
Tag
Data Table
```

Then expand based on product usage and migration risk.
