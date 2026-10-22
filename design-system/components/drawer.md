---
id: design-system.component.drawer
collection: design-system
type: component
title: Drawer
summary: TBD Drawer component scope and design contract; distinguish modal/non-modal side surfaces from Dialog and responsive pane layouts.
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.component.dialog
  - design-system.foundation.responsive-layout
  - design-system.accessibility.focus-management
---

# Drawer

> **HOS-53 · Design specification ready for development review, not evidence of a deployed implementation.** Size maxima, responsive sizing, modal dismissal/focus, scroll Fade and local motion recipe are defined below. Figma is the editable visual source; Code/Storybook must independently establish implementation, actual APIs and test status. Existing `unverified / scaffold` metadata is retained until owner-reviewed PR merge and maturity gates.

## Purpose and boundary

**Drawer** is a temporary viewport-edge overlay used for contextual editing, filters, inspection, and larger supplemental tasks that should retain the underlying page as context. Unlike **Side Pane**, Drawer is not a persistent page region; Side Pane belongs to App Shell/layout composition. A responsive shell may replace a persistent Side Pane with a Drawer, but this does not make them one component.

Prefer **Dialog** for short, focused blocking decisions and brief forms where a centered, content-height surface is appropriate. Prefer **Popover** for small trigger-anchored interactions and **a full page** for complex, multi-step work. **Bottom Sheet** is a separate presentation pattern, not an automatic Drawer mode.

Navigation from the Start edge belongs to **Side Navigation / App Shell**, not general-purpose Drawer v1.

## Placement and modality

- General-purpose Drawer v1 opens at logical **End only**: **physical left in RTL**, **physical right in LTR**.
- `Start` is intentionally not a Drawer placement choice. There is **no Placement / Direction variant or public placement prop** in the current design.
- Drawer v1 is designed as a **modal temporary overlay**. The backdrop is a separate overlay-composition layer bound to the public semantic token `semantic/utility/overlay`, not a child of the Figma Drawer master.
- When modal, the page behind the active Drawer is visually obscured and must also be inert to interaction. Non-modal Drawer remains out of scope for v1.
- Opening/closing is a runtime/prototype behavior, **not an Enabled/Opened visual variant**.

## Anatomy and visual construction

1. **Shell** — `surface/default`, **Radius/None = 0px**, no shadow by default, zero shell padding. The temporary panel attaches directly to its viewport edge.
2. **Header** — separate section using existing `Heading/LG` Title, optional `Body/Compact/SM` Description with `fg/secondary` and an 8px Title–Description gap. Optional regular Icon Button action(s) may share the title band. Header and Footer follow shared Dialog visual conventions but are **not standalone shared Figma components**.
3. **Close Button** — a real instance of the **same `Close Button / Default`** component used by Dialog, with five existing states (Enabled, Hover, Active, Focus, Disabled), 40×40px target, `Radius/Medium`, accessible name **«بستن»**. It is a **sibling of Header**, absolutely positioned at physical **top 12px / left 12px in RTL**, mirrored to physical right in LTR. **12px applies in both regular and narrow Drawer**; this deliberately differs from the Dialog Mobile 8px inset. The header reserves room for the Close target. In RTL it visually shares the title band on the left, opposite the right-aligned heading.
4. **Header extension** — optional native Figma Slot for **peer-section Tabs**, Search, a task-level Toolbar or another appropriate composition beneath the Heading row. The current **Figma example reuses the canonical `Tabs / Default` component**, with two `Text` Tab Items (`عمومی` and selected `پیشرفته`), rather than custom action buttons masquerading as a tablist. Tabs remain visible when the associated Content panel scrolls; select Tabs only for actual peer content sections, not filters or view-mode switches. This is not an additional Drawer Type.
5. **Content** — required native Slot; the **only vertically scrolling section** when content exceeds available height.
6. **Footer** — optional native Slot; stays outside Content scrolling and accepts canonical Button actions, status/help, or other appropriate content. Example regular buttons are Small (32px); narrow example buttons are Medium (40px). Preserve the Dialog action hierarchy: Primary to the physical left of adjacent Secondary in RTL.
7. **Overflow fade** — a Figma-only 48px alpha fade Boolean (default `false`) inherited from the Dialog visual, derived automatically from Body overflow in runtime.

**Close versus other actions:** The dedicated Close Button is not a replaceable generic icon action; it always means safe dismissal. Refresh/Reset/Edit/More use standard Icon Buttons and their own accessible names. The v1 master has one optional sample header action (`Show header action`); a future arbitrary multi-action header should be composed through an explicitly designed actions slot rather than a proliferation of Boolean variants. Existing **Header extension Slot** supports a toolbar below the title row.

**Section spacing in current Figma sample:** regular inline padding is 24px for Header, Content and Footer; narrow preview uses 16px. A physical-left Header reservation prevents the Close hit target overlapping the Title. For current design examples, Close is 12px from both top and physical left in RTL. These are editable design facts, not a claim about a tested responsive runtime.

## Sizing and responsive design contract

The approved v1 Figma and intended runtime Size model is **`Default | Large`**. Width values are now **design maxima**, rather than provisional examples:

| Size | Maximum width | Use |
| --- | ---: | --- |
| `Default` (default) | **400px** | Filters, compact contextual edits, simple details |
| `Large` | **640px** | Structured content, richer forms, two-column content where it fits |

**Fluid width:** `inline-size: min(100dvw, selectedMaxWidth)` or equivalent viewport/safe-area constrained behavior. The Size selection is an upper bound, **not a minimum width**. Do not allow viewport-horizontal scrolling or expose an arbitrary width override or resizable edge in v1. A Large Drawer at 360px is 360px wide, not converted to a third Size or Bottom Sheet.

**Narrow:** use the existing **768px** shared breakpoint to switch section inline padding from **24px Regular** to **16px Narrow**. Narrow is **not** a Figma Size or a separately selectable density. The 320px/360px Figma examples are resized `Size=Default` instances; run QA also at 390, 767, 768 and wider sizes. Footer examples use Button/Medium 40px in Narrow; do not infer touch capability from width. Close remains physical 12px from top/left RTL and mirrors for LTR.

**Height:** Drawer fills the **dynamic visual viewport** (`100dvh` or equivalent). Account for safe-area insets and the software keyboard; Header, optional Header Extension and Footer remain visible outside the flexing Content. The page behind the modal is scroll-locked. Collapse any inner multi-column form at insufficient container width. If 200% zoom or short landscape height makes essential actions unusable, replace the dense task with a dedicated page rather than clipping content.

## Overflow, scroll and separators

**Final v1 visual treatment: reuse Dialog's 48px semantic alpha Fade**, not a permanent Divider. The Fade uses an alpha mask over `surface/default`, preserving Light/Dark behavior, at the **bottom of the Content viewport**, immediately above Footer if present. Its visual layer must not intercept clicks or focus (`pointer-events: none`).

- Show Fade **iff** Content vertically overflows **and content remains below** the current scroll position. Hide when content fits and at the scroll end; recompute on scrolling, layout, content changes and resize. Use a ~1px tolerance against rounding flicker.
- The Figma `Overflow fade` **Boolean defaults to false and is preview-only**. It is enabled on the long-content Large example. Runtime must **derive** overflow from actual scroll state; **no public `overflowFade` prop**.
- Only Content scrolls; Header, Header Extension and Footer remain outside its scroll container. Do not scroll the inert page, permit an accidental horizontal scrollbar, or obscure focused fields beneath Footer actions. Avoid uncontrolled nested scrolling.

## Dismissal, modality and task safety — intended design contract

**Modal-only v1.** The obscured page becomes visually dimmed using `semantic/utility/overlay` and **actually inert** for mouse, keyboard and assistive technology; do not apply `aria-modal=true` without real inertness. Non-modal, nested Drawer, Start placement and swipe-to-dismiss are out of scope.

**Unified safe-exit:** Close Button, Escape, Cancel/Back and relevant route changes use one dismiss request. They never submit, clear fields or silently discard unsaved edits. The hosting product owns dirty-state detection and a coordinated confirmation; choosing Keep editing retains fields and focus in Drawer, choosing Discard permits dismissal. If `Show close=false`, a visible safe exit/recovery path is still required. Backdrop click/tap **never dismisses** by default and never passes interaction through.

Open/closed state, portal/stacking and event naming belong to the owning runtime, not to a Figma visual variant. Allow safe cancellation/retry of pending operations; do not lose context on submission error.

### Drawer-local motion recipe

The shared Motion Foundation and Motion Token Catalog remain unapproved. These are therefore **scoped Drawer v1 implementation values**, *not new global motion tokens*:

| Phase | Duration | Easing |
| --- | ---: | --- |
| Entrance from logical End | **240ms** | `cubic-bezier(0,0,0.38,0.9)` |
| Exit toward logical End | **200ms** | `cubic-bezier(0.2,0,0.38,0.9)` |
| Backdrop opacity in/out | **180ms** | `linear` |

RTL End animates from **left**: `translateX(-100%) → 0`; LTR End from **right**: `translateX(100%) → 0`. Reverse for exit; do not animate width or layout. Make background inert immediately upon opening and restore focus only after safe exit completes; handle interrupted/repeated open/close transitions gracefully.

With `prefers-reduced-motion: reduce`, **all transition durations are 0ms**, preserving focus, inertness and semantic state changes. Revisit the numbers if Karbon later approves shared Motion tokens; these local values do not authorize foundation changes.

## Accessibility and development acceptance

These are **required intended behaviors and developer acceptance tests**, not claims of executed runtime QA:

1. Use `role="dialog"`, a visible heading referenced by `aria-labelledby`, optional concise `aria-describedby`; set `aria-modal="true"` **only with a genuinely inert background**. Hidden/closed Drawer must not remain in the tab order or accessibility tree.
2. On open save the invoking control and move focus inside. For a short form focus the first relevant enabled input; for a long structured form focus its title using `tabindex="-1"` rather than the entire dialog wrapper. Keep the beginning of content visible.
3. Trap Tab/Shift+Tab among operable controls inside the active interaction scope, including portalled dropdowns; Close, Header actions and Footer actions remain accessible, with visible `focus/default` styling.
4. On safe close restore focus to the invoking control if still mounted or a logical surviving target; avoid restoring into an inert backdrop. Escape routes through the same dirty-state guard as Close/Cancel.
5. Check Content-only scrolling and Fade's actual overflow detection. Keep focused fields/validation errors unobscured, with fixed Footer visible under dynamic viewport/software keyboard changes.
6. Test both sizes at **320, 360, 390, 767, 768, 1024, 1280 and 1920px**, 200% zoom, Persian long strings, RTL/LTR, Light/Dark, short/long content, with/without Footer, pointer and keyboard.
7. Test rapid open/close, backdrop non-dismissal, failed submission, unsaved-change confirmation, screen-reader title/description announcement, focus restoration and reduced motion (0ms).

The reviewed [Focus Management](../../accessibility/focus-management.md) contract remains normative. The frontend team owns tests in Code/Storybook; Figma cannot certify their results.

## Figma source and examples

- [Drawer · Size Component Set](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24677-486) — editable source with **`Size=Default | Large`**.
- [Drawer `Size=Default` (400px)](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24608-37) — original Main Component ID preserved as this Variant.
- [Drawer `Size=Large` (640px)](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24677-467) — additional Variant in the same Component Set.
- [Drawer / Documentation · HOS-53](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24636-458) — one current presentation with the actual master and linked examples.
- [Close Button / Default](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24046-476) — shared with Dialog; its source was not modified for Drawer.

Verified Figma samples cover RTL End contextual editing and filters, a 640px `Size=Large` long form with **actual linked Tabs in Header Extension** (`عمومی` / selected `پیشرفته`) and the **48px Fade** preview, 320px and 360px resized `Size=Default` Narrow examples, and a Footer-off case. All **six** preview Drawer instances remain linked to the **two-variant Component Set**; the Large form retains its selected Tabs, Footer status and ten field rows. Both variants use three native Slots (Header extension, Content, Footer) and a **Figma-only `Overflow fade` Boolean**. `Show close` and other existing Booleans remain. This is visual QA, not executed runtime QA.

## Handoff status and evidence

**Design contract is ready for frontend implementation review; runtime verification is still required.** Developer teams may build from the approved Figma Size/placement/visual choices and the intended requirements above. Do not describe the component as already implemented, tested, or Storybook-mapped.

Figma visual QA covers six linked examples: three regular Default, a Large long form with 48px Fade, plus 360px and 320px Narrow default examples. Both source variants retain the three native Slots, the Dialog Close Button and existing section tokens. The Figma Set also exposes a **preview-only `Overflow fade` Boolean**; do not mirror it as runtime API.

**Remaining work is engineering verification**: choose exact runtime component signature consistent with code conventions, implement and execute responsive/motion/focus/scroll/dirty-state tests, and confirm Code/Storybook parity. A future shared Motion-token foundation may replace the component-local values. This document retains `unverified / scaffold` metadata until PR owner review, release evidence and repository governance allow maturity promotion.

