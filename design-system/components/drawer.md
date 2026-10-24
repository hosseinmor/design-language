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

# Drawer — unified panel family

> **HOS-53 · proposed design contract, subject to owner review.** This document expands the existing Drawer in Figma. It does **not** introduce a separate Floating Panel or Bottom Sheet component family. It defines intended design behavior, not verified Karbon/Storybook APIs or executed runtime tests. Its `unverified / scaffold` metadata is deliberately preserved until governance approval and necessary accessibility evidence.

## Purpose and boundary

Drawer is the reusable **panel surface and anatomy** for side panels, edge overlays, fixed-corner floating panels, and simple bottom sheets. The shared visual structure consists of Header, optional actions, optional Header Extension, required vertically scrollable Content and optional Footer. A presentation wrapper decides whether it participates in page layout, overlays it, or floats over it.

- **Inline** occupies real layout space and responds to App Shell / host width changes. It is not an overlay.
- **Overlay** is edge-attached and opens above content, from a logical inline edge or the bottom.
- **Floating** is a nonmodal, fixed-corner surface offset from viewport edges. It does not participate in layout and is **not draggable** in this scope.
- **Bottom Sheet** is `Display=Overlay` with `Placement=Bottom`; it is not a new Size, Drag variant or separate component.
- The existing **Side Navigation** remains navigation. A Drawer placed at Start is not automatically navigation, and the App Shell still owns navigation hierarchy and persistent page layout.
- Use **Dialog** for focused, short blocking tasks and **Popover** for a small trigger-anchored interaction. Use a dedicated page for complex, tall multi-step workflows.

## Valid combinations (curated, not a Cartesian product)

| Display | Placement / anchor | Modal | Backdrop | Width/height contract |
| --- | --- | --- | --- | --- |
| `Inline` | `Start` / `End` | **Never** | **Never** | Contributes its selected inline width to parent layout; height follows host region |
| `Overlay` | `Start` / `End` | `true` or `false` | Only when modal | Side-panel max widths `Default=400px`, `Large=640px`, constrained by viewport; visual viewport height |
| `Overlay` | `Bottom` | `true` or `false` | Only when modal | Viewport/host inline width; **content-driven sheet height**, capped by visual viewport—not the 400/640 values |
| `Floating` | Logical viewport **corner**: `block-start/end` × `inline-start/end`; example `bottom-end` | **Never** in current use | **Never** | Independent floating surface, 400px reference/max in current design; host constrains viewport |
| Optional `Minimized` state | Inherits previous Display and anchor/placement identity for restoration | No active modal trap/backdrop while minimized | None while minimized | Small nonblocking restoration surface, not a `Size` or `Display` |

`Top` Overlay, free dragging, snapping, variable bottom-sheet stops, swipe-to-dismiss and a public arbitrary-size axis are **out of scope**. Do not multiply all axes into Figma variants or create combinations not listed here.

**Placement ≠ presentation ≠ modality.** RTL maps `Start` to right and `End` to left; LTR reverses these. For Floating, the corner is an *anchoring geometry*, **not** an edge-entry animation direction. `Bottom` means a sheet attached to the viewport bottom when Display is Overlay; it is not a side-panel width choice.

## Shared anatomy and Figma authoring model

- **Shell:** semantic `surface/default`, zero shell padding; sections own spacing.
- **Header:** Title uses `Heading/LG`; optional Description uses `Body/Compact/SM` with `fg/secondary`, at an 8px vertical gap. The Header contains **one horizontal Auto Layout row**, with a content-sized action cluster on the physical left in RTL and a flexible right-aligned Heading. The containing Header section sizes vertically. The cluster reflows as actions appear or disappear; visible actions must not overlap, leave dead reserved Close space or push Title off the shell. Resume Assistant shows Title only; supporting context lives in Content, not a repeated header Description.
- **Header actions and Close:** reuse the original **Dialog Close Button** (40×40px, accessible «بستن») and canonical Ghost Icon Buttons. Their shared **Auto Layout action cluster** is ordered physically left-to-right in RTL as **Close → Minimize → Dock/Undock** with a Foundation 8px gap and 40px action targets; use the correct mirrored logical order in LTR. Header section padding is 12px top/physical-left, 24px physical-right and 16px bottom in the regular Figma baseline. Close retains its 12px physical corner inset, **without independent absolute positioning**; if hidden, remaining actions fill that space automatically. Close requests end/cancel; Minimize only suspends presentation. Do not display both when they lead to identical results. Action focus uses the canonical outer `Focus/Default` effect, **not** a border-state imitation.
- **Header Extension:** optional native Slot for canonical Tabs, Search or context Toolbar. Header and extension remain outside scrolling Content. The current Figma example uses a **real linked `Tabs / Default`** source, not fake controls.
- **Content:** required **native Slot**; the only scroll container when necessary. Long-form overflow can use the same 48px semantic alpha Fade from Dialog. The Figma `Overflow fade` Boolean is a **preview affordance**, not a manually-set runtime flag.
- **Footer:** optional native Slot, canonical Buttons/actions/status; remains outside Content scrolling. No unnecessary permanent Divider or double spacing.
- **Optional Minimize:** a canonical Icon Button action, independent of Display. The Figma resume-assistant example uses a **328×64px compact restore launcher** instead of a second full panel header: semantic surface, `Radius/Large`, `Shadow/Floating`, linked canonical `Icon/AI resume`, a single-line Title and secondary active-conversation status, plus an explicit canonical `Button/Small` labelled «بازکردن». The launcher is a small **composition**, not a fifth Display/Size Variant or standalone Floating Panel. Its whole surface is not an additional competing action; the clearly labelled Restore Button is the operable control. The **session/content state is not destroyed**.

### Curated Figma variants

The existing **Drawer** Component Set was extended in place, retaining its prior Default and Large Overlay source IDs. It now has only the following authored variants:

| Display | Size | Figma source meaning |
| --- | --- | --- |
| Overlay | Default | 400px maximum **side** panel reference |
| Overlay | Large | 640px maximum **side** panel reference |
| Inline | Default | width-contributing side pane; host may resize |
| Floating | Default | fixed-corner nonmodal panel using shared slots and foundation shadow |

There is no Floating Panel component, no Bottom Sheet Size axis, and no cross-product of `Display × Placement × Modal × Minimized` in Figma. Bottom and corner choices live in **composition Playgrounds**. Modal is a **behavioral contract** coordinated with backdrop, focus and underlying inertness; a Figma Boolean that merely toggles a dark rectangle would be misleading.

**Token treatment (current Figma):** Overlay side and Inline use `Radius/None` and no shadow. Floating uses **`Radius/Large = 12px` + `Shadow/Floating`** with `surface/default`. Bottom Sheet uses top corners `Radius/Large`, bottom corners `Radius/None` at the attached edge. A minimized floating presentation reuses `surface/raised` and `Shadow/Floating`. Inline may use a semantic `line/default` separator to distinguish itself from Main Region; do not simulate a focus ring using border changes. All interactive controls use the shared **`Focus/Default` outer focus ring**.

### Spacing and sizing

For side-pane examples, use **24px section inline padding Regular** and **16px Narrow**, relying on the existing 768px shared breakpoint. Do not treat the breakpoint as user-selectable Size. Overlay side height follows the dynamic visual viewport. Inline height is provided by the hosting App Shell region. Floating has a fixed **corner inset** using the shared 16px spacing value; its 600px design specimen is **not** a new public height token.

The simple Bottom Sheet occupies the available mobile inline width, chooses a useful content-driven height capped by the dynamic visual viewport and safe area, and scrolls **only Content** when necessary. The current 390×340px Figma example illustrates a content-appropriate sheet and does not establish a public fixed sheet-height contract.

## Modal behavior and accessibility

A semantic `Modal` capability must be evaluated with Display:

- **Inline:** always nonmodal; no backdrop, inert background or focus trap. Keyboard and screen reader can continue into the surrounding App Shell.
- **Overlay side / Bottom:** modal or nonmodal. **Modal** requires semantic backdrop, real background inertness, focus containment, initial focus strategy, safe Escape/Close, and return of focus. **Nonmodal** has no backdrop, does not trap focus and does not make page inert; controls remain keyboard-operable and appropriately named.
- **Floating:** nonmodal only for current assistant use; no backdrop and no focus trap. Click and keyboard navigation may reach the underlying page.

Use dialog semantics for modal Overlay when appropriate, with visible Title supplying an accessible name. Do **not** assert `aria-modal=true` unless background is actually inert. Nonmodal surfaces must not fake modal semantics. In all presentations, visible focus is the existing **outer `Focus/Default` ring**, not a stroke/border replacement.

**Dismissal:** Close and Escape request a safe exit. The host owns dirty-state confirmation and preserves edits until explicit discard; backdrop behavior is applicable only when modal, and defaults to **not dismissing**. Minimize does **not** call dismiss, cancel or submit. For a minimized modal Overlay, remove the active backdrop and focus trap while the panel is collapsed; remember its Modal configuration and restore the correct scope/backdrop only on re-expansion. Restore focus logically to the compact trigger or prior task as appropriate.

## Minimize, dock and preserved session

`Minimize` and `Dock/Undock` are **orthogonal capabilities**. They do not generate new `Display` variants or fork the content state:

- **Minimize:** retain current task messages, inputs, unsent draft, validation errors and exact reading/scroll position. Keep persistent state even if expanded DOM presentation is hidden; do not unmount/replace the session by accident. Present only the **compact Restore launcher** (Title + one concise status + existing Button) while minimized—do not reproduce Header actions, Description and Footer in miniature. Close and Minimize may both appear **only when their effects differ**; in the resume assistant example, Close is hidden to avoid a redundant exit action. Restoring returns to the same Display and previous scroll point.
- **Dock Floating → Inline:** move the presentation into the App Shell's Inline `End Pane`, consuming actual layout width and reducing Main Region width. Preserve the **same session object and content**; do not restart the conversation or reset reading position.
- **Undock Inline → Floating:** restore the same session into the chosen fixed logical viewport corner, preserve draft and scroll state; use existing foundations for spacing/elevation.
- **Space gate:** Dock is offered **only if the host App Shell can accommodate the inline pane without violating its Main Region minimum**. In the Figma scenario, `Inline=400 + Navigation=64 + Main min=640`; a 1240px host supports it (776px Main remains), while 980px would leave only 516px and must hide/disable Dock. This is a **scenario constraint**, not a new global breakpoint.
- Both presentations reuse a single linked **Demo content / Resume assistant session** component with the same visible in-progress draft and reading marker; that establishes visual continuity, **not proof of runtime state persistence**.

## Motion, scrolling and responsive constraints

Overlay may animate from its physical attachment edge; side Start/End direction mirrors in RTL/LTR, and Bottom enters vertically from below. Floating's corner is an anchor, not a directional `Placement` animation. Inline changes the App Shell layout; avoid treating it as a modal slide-over. Reduced motion must remove nonessential transition duration and preserve state and focus correctness.

The existing Drawer-local motion numbers (entrance 240ms, exit 200ms, backdrop 180ms, `0ms` reduced motion) apply to the **prior side Overlay recipe only** pending a shared Motion Foundation decision; they are **not automatically applied to Floating/Inline/Bottom** and are not new universal motion tokens.

Content scroll stays within the panel; Header/Extension/Footer remain outside the scrolling region. Re-evaluate scroll fade from actual overflow and offset. For an Inline host, do not create nested viewport scroll locks. Floating and Bottom stay within the visual viewport and safe areas; prevent focused input / Footer controls from being hidden by software keyboards, zoom or text reflow.

## Figma evidence and Playgrounds

- [Drawer Component Set](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24677-486) — canonical shared source, four curated Display/Size combinations.
- [Drawer documentation and Unified Panel scenarios](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24636-458) — original Overlay samples plus new compositions.
- [App Shell](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24549-36) — live source checked for `End Pane`, Main Region flex sizing and Side Navigation. The new Dock/Inline Playground is a **derived composition** using linked Drawer and Navigation instances; it does not silently rewrite the existing App Shell Component Set.
- [Shared Close Button](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24046-476); [canonical Tabs](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23486-300).

The Playgrounds are deliberately split into **02 · Core / Sizes and Slots** and **03 · Product Scenarios**. Core shows a contextual edit built with canonical Text Inputs, filters built with canonical Checkboxes including 320px and 360px narrow examples, a real linked Tabs/long-content Large panel, and a read-only details panel with no Footer. Product Scenarios show a semantic modal side Overlay, a simple 390×340px bottom sheet, RTL Start and composed LTR End nonmodal references, paired Floating and space-consuming Inline resume assistant views, and the compact Minimized launcher. Internal demo content is hosted outside Presentation in a labelled internal-sources frame; the two assistant examples remain linked to that single source. There is no drag, snap-height, or swipe-dismiss affordance.

### Figma audit evidence (2026-10-24)

- Verified all four source variants retain exactly three shared native slots, the Dialog Close Button source, bound semantic surface/radius/elevation, current typography styles and Foundation spacing. Actions use standard Icon Buttons with the existing outer Focus/Default treatment.
- Reviewed Core and Product Scenarios visually. Replaced generic/empty example content with canonical Text Input and Checkbox instances and task-relevant copy. Confirmed the Bottom Sheet is bottom-attached, and Header/Footer remain distinct from scrollable Content.
- The 1240px App Shell integration example gives the Inline panel 400px of actual horizontal layout space, leaving 776px for Main Region; six live App Shell master variants remain unchanged.
- **LTR is illustrated by a composed visual reference**, including a mirrored Close outside the RTL-authored instance; Figma does not currently expose a runtime-verified direction-aware Drawer placement/Close contract. Likewise, shared resume content shows one linked source but does not demonstrate executable Dock/Undock state preservation.
- Internal demo content is not a second public component. Runtime, screen reader, keyboard, focus containment/restoration, modal inertness, viewport/safe-area behavior and Storybook parity are expressly unverified.

## Design QA and future implementation gates

**Design-side inspection required:** source variants and three real native Slot IDs, same typography and spacing variables, no hard-coded alternative colors, tokenized radius and floating shadow, correct RTL/LTR mirroring in the specification, clear nonmodal vs modal semantics, correct vertical scrolling ownership, action differences (Close versus Minimize), and no false Focus-by-Border appearance. Inspect narrow/full-width samples and the direct link from App Shell Inline Pane to reduced Main Region.

**Unverified runtime gates (outside this task):** actual Dock/Undock and Minimize persistence; correct modal focus trap/restoration versus nonmodal free focus; keyboard-only behavior, screen-reader announcements; 320/360px and 200% zoom; Light/Dark rendering; true viewport and software keyboard; scroll fade; reduced motion; real Karbon/Storybook API and integration parity. Do not record these as executed or passing.

## Repository status

The previous [HOS-53 Drawer v1 documentation proposal, PR #14](https://github.com/hosseinmor/design-language/pull/14), was **still open and not merged** at the start of this work, so `main` contained the earlier Scaffold. This new branch is based on `main` and supersedes the End-only/Modal-only restrictions as an **explicit newly proposed change**, not a silent assumption of merge. Owner review, generation of required registry artifacts, CI and merge are still governed by [Change Process](../../governance/change-process.md).
