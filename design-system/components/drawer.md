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
- **Header:** Title uses `Heading/LG` (28px line height); optional Description uses `Body/Compact/SM` (20px line height) with `fg/secondary` and an 8px Title–Description gap. A **single horizontal Auto Layout TOP-aligns** the action group (including Close) and flexible Heading. The Title starts alongside Close, while Description, when present, **extends downward below Title** without moving Close or recentering the action row. **With no Description and one visible Close, the Header is 60px** (12px top + 40px control + 8px bottom). **With one-line Description it is 76px** (12 + 56 + 8); naturally increase height if text wraps or localization requires. These are measured Figma design baselines, not height variants. Resume Assistant shows Title only; supporting context belongs in Content.
- **Header actions and Close:** Header uses one Auto Layout group: (1) the **canonical Dialog Close Button** (40×40px, accessible «بستن») under the independent `Show close` visibility property, and (2) a single **native `Header actions / Slot`** for any other action—Minimize, Dock/Undock, Refresh, etc.—composed from **canonical Icon Button** instances (40×40px Medium in examples). The two old `Show minimize` and `Show header action` Booleans **are removed**. Designers insert/remove or swap actions **inside the Slot**; there is no proliferation of Boolean axes or source variants. Foundation 8px spacing aligns adjacent actions. RTL positions the group on the physical left, with the Close at the outer edge; LTR mirrors the group. Regular Figma Header section padding is **top 12px / physical left 12px / physical right 24px / bottom 8px**. The Close target remains aligned to the top 12px in RTL, **inside Auto Layout**, not absolutely positioned. If Close is hidden, only intended Slot content remains; empty Slots must not reserve an extra control. Close requests end/cancel; Minimize only suspends presentation. Never display them redundantly if they yield the same outcome. Action Focus comes from the canonical outer `Focus/Default` treatment, **never a Border change**.
- **Header Extension:** optional native Slot for canonical Tabs, Search or context Toolbar. Header and extension remain outside scrolling Content. The current Figma example uses a **real linked `Tabs / Default`** source, not fake controls.
- **Content:** required **native Slot**; the only scroll container when necessary. Long-form overflow can use the same 48px semantic alpha Fade from Dialog. The Figma `Overflow fade` Boolean is a **preview affordance**, not a manually-set runtime flag.
- **Footer:** optional native Slot, canonical Buttons/actions/status; remains outside Content scrolling. No unnecessary permanent Divider or double spacing.
- **Optional Minimize:** a canonical Icon Button added into `Header actions / Slot`, independent of Display and **not a Drawer Boolean**. The Figma resume-assistant example uses a **328×64px compact restore launcher** instead of a second full panel header: semantic surface, `Radius/Large`, `Shadow/Floating`, linked canonical `Icon/AI resume`, a single-line Title and secondary active-conversation status, plus an explicit canonical `Button/Small` labelled «بازکردن». The launcher is a small **composition**, not a fifth Display/Size Variant or standalone Floating Panel. Its whole surface is not an additional competing action; the clearly labelled Restore Button is the operable control. The **session/content state is not destroyed**.

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

### Current Figma construction evidence

The live canonical source is one editable **Drawer** Component Set with four curated variants, **four true native Slots** (Header actions, Header extension, Content and Footer), original Dialog Close Button and Foundation-bound typography, colors, spacing, radius and elevation. The two `Show minimize` / `Show header action` booleans have been removed. All secondary Header controls are instances of the existing **Icon Button** inside Header actions Slot; the Close Button remains separately controlled by `Show close`.

The Figma Header row is **TOP-aligned** across all source variants. Compact Title + Close is **60px** high; Title + one-line Description + Close is **76px** high. Description adds height *below* Title; no separate Height or Description Size axis is needed. The [two live linked Header specimens](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24936-792) demonstrate both states.

Both Playgrounds use editable system components, not flattened screenshots: **Text Input**, **Checkbox**, **Tabs**, **Button**, **Icon Button**, **Close Button**, and the existing linked **Side Navigation** in App Shell. Section captions are right-aligned Persian and representative example cards follow RTL visual order. The assistant's Floating and Inline instances reference **the same reusable demo-session content source**, containing a real Text Input draft composer and Primary Send Button. The derived Main Region is a real 776px editable resume form with two Text Inputs and Primary Save Button beside a 400px Inline panel; the six App Shell source variants were not altered.

The special LTR specimen is a **visual geometry/reference composition**, not evidence of an executed direction-aware Drawer API. Figma visually represents the same draft and reading position across Dock/Undock; it does not execute or prove preservation at runtime.

## Development handoff and acceptance criteria

This is the **design handoff contract** for implementation review, not evidence of completed runtime work. A frontend owner should implement in the existing Karbon architecture and choose the concrete public API/portal strategy; do **not** invent a second Floating Panel component or infer a backdrop-only modality flag.

| Area | Acceptance for implementation / QA |
| --- | --- |
| **Anatomy** | One reusable panel with four header/body composition Slots. Keep Close a distinct accessible dismiss control; insert/remove optional controls via Header Actions Slot, not separate boolean options. |
| **Header** | Top-align Close and Heading. 12px top + 8px bottom; 60px Title-only/Close, 76px with one-line Description; longer descriptions grow down. No action/title overlap, including multiple controls. |
| **Display/Placement** | Inline occupies parent layout, Overlay attaches to logical Start/End or Bottom, Floating uses a logical viewport corner, no dragging. Mirror Start/End in RTL and LTR. No Bottom Sheet height variant. |
| **Modal** | Only Overlay can be modal in v1. Modal requires actual inert background, semantically labelled dialog, appropriate backdrop and contained/restored focus. Nonmodal Inline/Floating and nonmodal Overlay allow normal page interaction and no focus trap. |
| **Scroll and overflow** | Content alone scrolls; Header, Header Extension and Footer remain visible. Use Dialog's existing semantic 48px fade only when content remains below the scroll position; no focus or pointer interception. |
| **Close vs Minimize** | Close/Escape follow safe exit and unsaved-change guard. Minimize retains conversation, unsent draft, validation and scroll/read position and exposes a compact Restore launcher. Do not duplicate controls that have the same effect. |
| **Dock/Undock** | The resume assistant switches between Floating and App Shell Inline using the **same state**. Dock available only when remaining Main Region satisfies its host's minimum width; design example: 1240 - 400 - 64 = 776px, while 980 - 400 - 64 = 516px is insufficient against 640px minimum. |
| **Responsive/RTL** | Check at 320/360/390/767/768/1024/1280 widths, dynamic viewport/keyboard and 200% zoom; ensure 16px narrow section padding, safe-area compliance, no clipped essential action and meaningful Persian text reflow. |
| **Accessibility** | Verify keyboard-only use, visible external Focus/Default ring (never a border mutation), initial focus, Tab/Shift+Tab handling for modal portals, Escape, disabled/no-space actions, accessible labels, focus restoration, screen reader and reduced-motion behavior. |
| **Handoff evidence** | Review the linked Figma Component Set, Core Playground, Product Scenarios and App Shell demo in this document. Storybook/code parity and the above runtime tests must be verified **by development**; they were not run in this design task. |

### Review boundaries

The reviewed **2528px Figma Presentation** baseline is maintained; the proposed 1600px migration is not silently substituted. In the Presentation, Section 01 contains the actual editable Drawer master; Section 02 contains source-linked Core examples, and Section 03 contains curated product scenarios. An internal demo-content source is explicitly labelled outside the canonical presentation so it cannot be mistaken for a second public component.

Do not treat PR validation or visual inspection as executable Focus, animation, a11y, dark-mode or Storybook evidence. The current metadata stays `unverified / scaffold` until owner review and relevant tests justify promotion; runtime implementation remains out of scope for this design work.

## Repository status

The earlier [HOS-53 End-only/Modal-only proposal, PR #14](https://github.com/hosseinmor/design-language/pull/14) is **superseded by the current unified Drawer proposal**. Do not merge its narrower contract over this work. This branch was created from `main`, which still carried the old Scaffold at creation time; no merge, runtime verification or maturity promotion is implied. Owner review, generation of required registry artifacts, CI and merge are still governed by [Change Process](../../governance/change-process.md).
