---
id: design-system.component.dialog
collection: design-system
type: component
title: Dialog
summary: Canonical design contract for modal, blocking task dialogs, including dismiss/focus, responsive presentation and scroll.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: 2026-10-19
related:
  - design-system.reference.component-mapping
  - design-system.foundation.responsive-layout-spec
  - design-system.accessibility.focus-management
  - design-system.accessibility.keyboard-navigation
  - design-system.accessibility.screen-reader-semantics
---

# Dialog

> **HOS-42 / Design handoff ready.** These are approved **intended behaviors**, not assertions that a runtime component, Storybook story or accessibility tests already exist. Figma is the editable design source; Code/Storybook must independently establish implementation and test status.

## Purpose and boundaries

Dialog provides a **modal, blocking** interaction scope for a short, focused task that requires a decision or completion before returning to the page. In this Design System **Dialog** is the component name and the current v1 is **always modal**. Non-modal Dialog is not part of v1; `modal` is a semantic behavior, not a second component.

Use **Dialog** for focused informational content, short forms, edits and content review. Prefer the dedicated **Confirmation Dialog** for confirming consequential actions and **Alert Dialog** for urgent, blocking notification and recovery; ordinary low-priority feedback belongs in Notification/Toast. Prefer a dedicated page or flow for navigation-heavy, long, multi-step work. Use Notification for passive feedback, Popover for lightweight contextual content, and Drawer/Side Sheet for an anchored panel or preserving more underlying context.

**Confirmation**, **destructive confirmation**, **unsaved changes** and **form in Dialog** remain usage **patterns**, not visual Size/Type variants of general Dialog. Figma has separate **Confirmation Dialog** (`Intent=Default/Danger`) and **Alert Dialog** (`Severity=Warning/Error`) component families. **These specialized families are standalone Figma components** that share this document's visual/behavioral rules; they do **not** embed the generic Dialog, and there is **no shared Base/Shell component in Figma**. No shared semantic or spacing token is duplicated or created for them. An urgent, interruptive alert may use `role="alertdialog"` when its content genuinely warrants it; a routine confirmation remains `role="dialog"`. Bottom Sheet is a **presentation pattern**, not a Dialog Size or an automatic Drawer sub-type. Do not add `Type=Alert/Destructive/Confirmation` to the Figma Component Set.

## Anatomy and visual contract

The modal overlay consists of an inert underlying page, a semantic **backdrop** using `semantic/utility/overlay` and an accessible Dialog shell. The shell owns required Title, optional Description, optional Close Button, native Body Slot and optional Footer Slot. Backdrop is not baked into the Figma shell master.

- Shell uses semantic default surface, **Radius/Large = 12px**, **no shadow** and no shell outline. **Shell padding is zero.** Padding belongs to the Header, Body and Footer sections and is bound to existing spacing variables. No new shell/base or component-specific spacing tokens are needed.
- Title: existing Figma text style `Heading/LG` (**18px / 28px**, Bold). Short supporting Description: `Body/Compact/SM` (**14px / 20px**) and the existing public semantic token **`fg/secondary`**. Do not create additional color variables or alias a component-only token for this. Use a more prominent semantic foreground for important consequences if hierarchy/legibility demands it; preserve adequate contrast.
- **Close Button** is a distinct component: `40 × 40px` operable area, `Radius/Medium = 6px`, visible cross approximately 13px, all required hover/focus states, accessible name **«بستن»**. In RTL it is absolutely positioned **12px in Regular / 8px in Mobile from the physical top and left**, outside the Header Auto Layout. Mirror placement when a genuine LTR layout is supported.
- Body and Footer are Figma native Slots: product content and canonical Button instances, never fixed "type" variants. Keep Heading/Description out of scrollable Body.
- **`Overflow fade` is a Figma-only Boolean preview property (default `false`).** Its 48px alpha gradient mask is applied over a **solid public `surface/default` Semantic fill** so both Light and Dark resolve correctly without hard-coded white or a new component token. The mask and surface are grouped behind the same exposed Boolean, anchored to the bottom of the Body viewport with stretch/bottom constraints and independent of Body scrolling. **Runtime does not receive a manual `overflowFade` prop**: derive presence from actual Body overflow and scroll position, hide it when nothing remains below or at the scroll end, and use `pointer-events: none` on the visual overlay.
- The visual Footer uses canonical Buttons. Regular example actions use **Button/Small (32px)**; Narrow authoring examples use **Button/Medium (40px)**. The runtime must not infer touch/pointer capabilities from viewport width: minimum target size and capability-specific accessibility remain separate rules.
- In RTL, action order keeps the Primary/Danger action on the physical **left** of the adjacent Secondary/Cancel action (reading end). Do not flip labels or action semantics without a reason.

### Section-owned spacing (Figma final design rule)

**All three shells have `padding: 0` and `itemSpacing: 0`.** They own only surface, radius, width, and responsive/scroll boundaries; Header, Body and Footer own their padding. Figma components remain independent—**no shared Base Component**—and use existing Spacing variables. A row below describes `top / inline (left-right) / bottom` padding.

| Component and viewport | Header | Body (optional) | Footer | Gap from last content to actions |
|---|---|---|---|---|
| General Dialog / Regular | `24 / 24* / 0` | `16 / 24 / 0` | `24 / 24 / 24` | 24px via Footer top |
| General Dialog / Mobile | `16 / 16* / 0` | `16 / 16 / 0` | `16 / 16 / 16` | 16px via Footer top |
| Confirmation & Alert / Regular | `32 / 32 / 0` | `16 / 32 / 0` | `32 / 32 / 32` | 32px via Footer top |
| Confirmation & Alert / Narrow | `24 / 24 / 0` | `16 / 24 / 0` | `24 / 24 / 24` | 24px via Footer top |

`*` In the **general Dialog with a visible Close Button**, Header uses a **64px physical-left inset** in RTL to clear its `40×40px` hit target at `left:12px; top:12px` in Regular and `left:8px; top:8px` in Mobile; the physical right inset is 24px Regular / 16px Mobile. This is a Header-only override, not shell padding. Follow the direction contract if implementing a genuine LTR layout.

- The 8px **Title → Description** gap is internal to the Heading group for all variants. Content in short Confirmation/Alert dialogs goes in Description by default; Body remains hidden unless extra structured content is present.
- The Footer owns the separation from whichever content section precedes it. Do **not** add a second 24px/32px gap on the parent or on the Body's bottom: this would double the spacing. If there is **no Footer**, add bottom space to the final visible content section (e.g. Body bottom 24px Regular / 16px Narrow in general Dialog).
- Alert Dialog: **Icon is an actual child of the Title Row**, not an absolute sibling of Header. The RTL row is `[Title (flex), Alert icon (24px)]` with an **8px gap**; Title is right-aligned and shares Heading/LG. Description is its own line underneath, aligned with the Header's right edge. Icons and their colors reuse canonical icon components and existing public `fg/warning` / `fg/danger` variables.
- At viewport height limits, keep Header/Footer outside the scroll container and scroll only Body. When Body is hidden, the Footer's top padding still supplies exactly one content-to-actions gap: **16px generic Mobile, 24px generic Regular or specialized narrow, and 32px specialized Regular**. This is intended runtime behavior; visual Figma checks do not constitute executed scroll/a11y tests.

### Size and responsive choices

| Authoring Size | Preferred maximum shell width | Intended use |
|---|---:|---|
| Small | 400px | Brief notice/confirmation |
| Medium (default) | 560px | Typical short interaction |
| Large | 800px | Larger focused form/composition |
| XL | 960px | Wider content that genuinely needs space |

These are **content capacity choices**, not breakpoint names or unconditional fixed widths. Display width must remain fluid, bounded by the selected maximum and **at least 16px** viewport gutters on both sides. Never overflow to preserve a requested Size; if XL still requires a large complex workflow, reconsider Dialog.

Use `narrow` below the shared **768px** viewport boundary; regular at/above 768px. The **generic content/form Dialog** uses **24px Regular / 16px Mobile section inline padding**. The **dedicated Confirmation and Alert Dialog** components use **32px Regular / 24px Narrow section inline padding**. This difference is assigned by component responsibility and available viewport, **not** a freely selectable density/spacing property. Figma defines a **`Viewport` authoring axis** with five valid combinations only: `Size=Small/Medium/Large/XL, Viewport=Regular` and `Size=Small, Viewport=Mobile` (328px source). This is not an eight-variant matrix. `Mobile` labels the visual design below the 768px breakpoint; it is **not** hardware detection or a public runtime density prop. The former `Dialog / Narrow preset` is **already a linked instance of `Size=Small, Viewport=Mobile`** and remains solely for compatibility with existing linked examples; remove it only after checking consumers. The actual component should adapt to available viewport/host width at runtime rather than exposing a user-selectable Narrow switch. Current supported Figma previews: widths 320/360/390px; also validate boundary 767/768px.

**Foundation discrepancy note (non-blocking for Dialog):** Current Figma `Responsive Layout Foundation / Tailwind v3` uses sm=640, lg=1024, 2xl=1536, while current GitHub Responsive Layout specification still lists legacy ruler sm=544, lg=1012, xxlarge=1400. Both agree on `medium/md=768`, the only global threshold Dialog consumes. Do **not** silently rewrite the foundation or invent a second breakpoint scale in code. Resolve the larger foundation migration separately with its owner.

## Dismissal and task safety

- The Figma **Dismissible** Boolean controls the **visible Close affordance**. `false` means no X; it does **not** authorize a keyboard trap or removal of the explicit safe Cancel/Back option. For a decision-driven confirmation, a visible safe action is always available.
- **Escape** dismisses a normal, cancellable Dialog via the same safe-exit path as Close. In an ordinary or destructive confirmation without X, Escape invokes the **safe Cancel** path, not the destructive action. Respect any active unsaved-change guard. An uninterruptible operation with no safe exit should not be represented as an indefinite focus-trapping Dialog; it requires a specifically justified alternative flow.
- **Backdrop click never dismisses by default.** It does not trigger submit or silently discard edits. Clicks/keyboard interaction with the obscured page must not reach underlying controls.
- **Unsaved changes:** all exit sources (Close, Escape, visible Cancel/Back, navigation) funnel through **one guard**. If dirty, ask whether to discard/keep editing; keep the user's data until a deliberate destructive decision. Do not discard on Escape or backdrop. Do not open arbitrary nested dialogs: use one coordinated confirm flow and preserve focus management.
- Submitting a form or starting an async operation must not immediately remove the user's recovery path if it fails. Prevent duplicate submissions, retain error state/context, and define safe cancellation for pending work at the product layer.

## Keyboard, focus and accessibility

The runtime **must** implement and verify these behaviors (design approval does not mean tests have passed):

- **Semantics:** active shell exposes `role="dialog"` and `aria-modal="true"` **only if** backdrop/background are visibly obscured and actually inert. Visible title supplies `aria-labelledby`; short helpful description may supply `aria-describedby`. For multi-paragraph or structured content avoid announcing a huge combined description. Exceptionally urgent alert pattern uses `role="alertdialog"` with appropriate description.
- **On open:** focus moves inside. Short informational Dialog → Close or acknowledgement; short form → first valid input; destructive irreversible confirmation → **least destructive Cancel**; extensive/structured content → programmatically focus title/start with `tabindex="-1"` without adding a permanent Tab stop or shifting the start off-screen. Do not focus the shell itself as a generic fallback.
- **While open:** Tab and Shift+Tab cycle through visible enabled controls *inside* the active Dialog, including nested popovers/portalled controls in its interaction scope; focus indicator remains visible. Background is inert to pointer, keyboard and assistive technology, not merely visually dimmed.
- **On close:** focus returns to the invoking control if still mounted/appropriate; otherwise moves to a logical surviving target, e.g. the next item after deletion. Never strand focus on an unmounted element or inert backdrop.
- **Stacking:** no nested Dialog by default. If a truly exceptional blocking alert must stack, only the topmost dialog owns focus/interactions; the previous level resumes only after closing the alert.

## Height, scroll and reflow

Dialog uses **content-height (Hug)** until constrained by available visual viewport. Maintain at least **16px vertical safe space** above/below; cap the shell at the remaining viewport height using an equivalent of `max-height: calc(100dvh - 32px)` adjusted for actual safe areas. When content exceeds the cap, **Header and Footer stay visible**, and **only Body scrolls**. Focus must scroll the focused Body control into view without clipping heading or footer. Avoid scrolling the background. If even title + required actions cannot fit at 200% zoom or landscape, use an appropriate full-screen/alternative flow rather than inaccessible clipping.

## Implementation acceptance checklist

- [ ] Four widths 400/560/800/960 with fluid shrinking and 16px minimum gutters; check 320, 390, 767, 768, 1024, 1280 and 1920; long Persian strings / RTL.
- [ ] Shell padding=0 for all three families; verify section-level spacings in the matrix below (and special no-Footer Body bottom space). No public arbitrary `Narrow` density prop. All retain accessible action targets.
- [ ] Short information with X and no Footer; confirmation with no X and explicit safe Cancel; destructive confirmation with correct Danger emphasis; focused form with validation and loading/error.
- [ ] Escape routes to safe exit; Backdrop click does nothing; changes remain intact unless explicitly discarded; Cancel/Close/Escape share the same guard.
- [ ] Initial focus by scenario, Tab/Shift+Tab cycle, visible focus ring, background inertness, focus restoration after cancel/submit/delete.
- [ ] Normal `dialog` semantics, warranted `alertdialog` semantics, title/description read by a screen reader without duplicate huge announcements.
- [ ] Long Body scrolls without moving Header/Footer; actions remain visible at 200% zoom, minimum viewport height, and with software keyboard.
- [ ] RTL/LTR mirroring policy, order and labels of actions; keyboard-only and touch/capability-independent operability.
- [ ] Overlay color and token use checked; no shell Shadow; Close Button states, contrast and target checked.
- [ ] No invented runtime component names, prop/event names, portal implementation, focus-trap library or shipping status from Figma. Register owning code, Storybook and executed tests before claiming runtime verified.

## Live sources and ownership

- [Dialog page and presentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24058-9)
- Main Figma Dialog Component Set: node `24036:267`, key `b8bd11b06f27bac00225857315e0cb4f4c0887f7`.
- [Close Button source](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24046-476), key `c19c7786bdbb03e1ad13695db575d5d7478e0d34`.
- [Narrow preset source](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24087-129096); generic Dialog Figma authoring only.
- [Confirmation Dialog](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24147-56): independent component, Default/Danger, Title/Description, optional Body Slot, Footer actions; Figma draft awaiting separate handoff QA.
- [Alert Dialog](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24147-203): independent component, Warning/Error, **24px icon inline in the RTL Title Row** with an 8px gap (not absolute), short message in Description and optional Body Slot; Figma draft awaiting separate handoff QA.
- Legacy [Modal](modal.md) retained as a redirect; original Figma master is preserved for migration.
- WAI-ARIA APG: [modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) and [alert dialog](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/).
- Runtime repository/package, code API, Storybook mapping and executed tests: **unregistered/unverified**. They require a distinct implementation/QA owner; design is ready for handoff, not declared shipped.
