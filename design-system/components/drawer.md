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

> **HOS-53 · Figma design baseline approved for this scope; component handoff is not yet complete.** The live editable source defines the visual component, whereas this document records the selected design decisions and their unresolved boundaries. Public runtime API, actual responsive sizing, interaction tests, motion values and Storybook parity have **not** been verified. The existing \`knowledge_state: unverified\` / \`document_maturity: scaffold\` metadata remains unchanged until the remaining gates are complete and the owner approves promotion.

## Purpose and boundary

**Drawer** is a temporary viewport-edge overlay used for contextual editing, filters, inspection, and larger supplemental tasks that should retain the underlying page as context. Unlike **Side Pane**, Drawer is not a persistent page region; Side Pane belongs to App Shell/layout composition. A responsive shell may replace a persistent Side Pane with a Drawer, but this does not make them one component.

Prefer **Dialog** for short, focused blocking decisions and brief forms where a centered, content-height surface is appropriate. Prefer **Popover** for small trigger-anchored interactions and **a full page** for complex, multi-step work. **Bottom Sheet** is a separate presentation pattern, not an automatic Drawer mode.

Navigation from the Start edge belongs to **Side Navigation / App Shell**, not general-purpose Drawer v1.

## Placement and modality

- General-purpose Drawer v1 opens at logical **End only**: **physical left in RTL**, **physical right in LTR**.
- \`Start\` is intentionally not a Drawer placement choice. There is **no Placement / Direction variant or public placement prop** in the current design.
- Drawer v1 is designed as a **modal temporary overlay**. The backdrop is a separate overlay-composition layer bound to the public semantic token \`semantic/utility/overlay\`, not a child of the Figma Drawer master.
- When modal, the page behind the active Drawer is visually obscured and must also be inert to interaction. Non-modal Drawer remains out of scope for v1.
- Opening/closing is a runtime/prototype behavior, **not an Enabled/Opened visual variant**.

## Anatomy and visual construction

1. **Shell** — \`surface/default\`, **Radius/None = 0px**, no shadow by default, zero shell padding. The temporary panel attaches directly to its viewport edge.
2. **Header** — separate section using existing \`Heading/LG\` Title, optional \`Body/Compact/SM\` Description with \`fg/secondary\` and an 8px Title–Description gap. Optional regular Icon Button action(s) may share the title band. Header and Footer follow shared Dialog visual conventions but are **not standalone shared Figma components**.
3. **Close Button** — a real instance of the **same \`Close Button / Default\`** component used by Dialog, with five existing states (Enabled, Hover, Active, Focus, Disabled), 40×40px target, \`Radius/Medium\`, accessible name **«بستن»**. It is a **sibling of Header**, absolutely positioned at physical **top 12px / left 12px in RTL**, mirrored to physical right in LTR. **12px applies in both regular and narrow Drawer**; this deliberately differs from the Dialog Mobile 8px inset. The header reserves room for the Close target. In RTL it visually shares the title band on the left, opposite the right-aligned heading.
4. **Header extension** — optional native Figma Slot for a secondary toolbar row, Search, Tabs, or other composition. It is not an additional Drawer Type.
5. **Content** — required native Slot; the **only vertically scrolling section** when content exceeds available height.
6. **Footer** — optional native Slot; stays outside Content scrolling and accepts canonical Button actions, status/help, or other appropriate content. Example regular buttons are Small (32px); narrow example buttons are Medium (40px). Preserve the Dialog action hierarchy: Primary to the physical left of adjacent Secondary in RTL.

**Close versus other actions:** The dedicated Close Button is not a replaceable generic icon action; it always means safe dismissal. Refresh/Reset/Edit/More use standard Icon Buttons and their own accessible names. The v1 master has one optional sample header action (\`Show header action\`); a future arbitrary multi-action header should be composed through an explicitly designed actions slot rather than a proliferation of Boolean variants. Existing **Header extension Slot** supports a toolbar below the title row.

**Section spacing in current Figma sample:** regular inline padding is 24px for Header, Content and Footer; narrow preview uses 16px. A physical-left Header reservation prevents the Close hit target overlapping the Title. For current design examples, Close is 12px from both top and physical left in RTL. These are editable design facts, not a claim about a tested responsive runtime.

## Sizing and responsive status — intentionally TBD

**No final width model is approved.** The live Figma source is a single resizable Main Component and has **no Size variant axis**. The **400px and 640px** widths are only representative design samples. Do not implement them as fixed \`Default / Large\` presets or impose a maximum without another explicit sizing decision.

A **360px narrow** example illustrates adapting the Drawer to the available viewport, with 16px section inline padding and 40px footer buttons. Exact fluid behavior, maximum/minimum width, thresholds, extreme narrow viewport rules and any public sizing API remain **TBD**. Do not create an independent breakpoint system. Do not automatically convert the Drawer to Bottom Sheet.

Drawer is an edge-attached viewport-height surface in the design examples. Respect actual visual viewport and safe-area constraints in runtime; the header and footer must remain usable when zoom/reflow reduce available height. A Figma viewport sample is not proof of these runtime constraints.

## Overflow, scroll and separators

- Header and Footer remain outside the scrolling Content. The background page must not scroll while a modal Drawer is active.
- \`Content / Slot\` in Figma has vertical overflow enabled; long-form playground content exercises the slot.
- A contextual **Divider or 48px edge fade** should be shown only when useful to communicate more available content, never as an unconditional decoration. The final Drawer-specific separator/fade treatment and whether to reuse Dialog's fade presentation remain **TBD**. Do not expose an arbitrary \`overflowFade\` public prop in anticipation of that decision.
- Avoid uncontrolled nested scroll containers and prevent content or focus targets being hidden underneath Footer actions.

## Dismissal and task safety — intended design, runtime unverified

- Visible Close requests **safe dismissal**. \`Show close=false\` only removes the visible affordance; a legitimate Cancel/Back/exit path must remain for an interruptible task.
- **Escape** should route to the same safe exit and never submit or destroy data.
- **Backdrop click does not dismiss by default**; background controls must not receive the click.
- Unsaved edits require a **single guard** across Close, Escape, Cancel and navigation; users explicitly choose whether to discard. Avoid accidental data loss from overlay dismissal.
- Swipe-to-dismiss is not part of the v1 design.
- The opening/closing transition moves from/to logical End. Duration, easing and final motion tokens remain **TBD**, while reduced-motion preference must be respected.

These are **intended design behaviors**, not assertions about a deployed Drawer.

## Accessibility acceptance criteria

For the proposed **modal** version, implementation and tests must establish:

- Accessible dialog semantics appropriate to the temporary task (\`role="dialog"\`; \`aria-modal="true"\` only when background is truly inert), with visible Title supplying \`aria-labelledby\` and concise Description optionally supplying \`aria-describedby\`.
- Focus placed logically inside when opened; Tab/Shift+Tab contained within the active interaction scope; visual focus indicator present; portalled controls treated as belonging to the active Drawer.
- Focus returned to the invoking element if still available, otherwise to a logical surviving target.
- Keyboard access to Close, header actions and Footer controls; an accessible Close name **«بستن»**.
- Safe Escape and unsaved-change dismissal behavior; correct screen-reader content announcements.
- Scroll/reflow usability with long Persian content, 200% zoom, narrow viewports and reduced-motion enabled.

The shared [Focus Management](../../accessibility/focus-management.md) foundation remains normative. **None of the above tests is marked executed by the Figma design review.**

## Figma source and examples

- [Drawer / Default · original Main Component](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24608-37) — existing source identity preserved, not a rebuilt detached copy.
- [Drawer / Documentation · HOS-53](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24636-458) — one current presentation with the actual master and linked examples.
- [Close Button / Default](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24046-476) — shared with Dialog; its source was not modified for Drawer.

Verified design sample coverage: RTL End for contextual editing and filters, a 640px toolbar/long-content form, a 360px narrow presentation, and a no-Footer composition. All five preview Drawer instances remain connected to the same Main Component. Three actual Figma native Slots are present: **Header extension**, **Content**, **Footer**. Existing \`Show close\`, \`Show description\`, \`Show header action\`, \`Show header extension\` and \`Show footer\` Boolean properties are exposed. Visual QA does not imply runtime functionality.

## Known gaps and handoff state

**Still unresolved:** final width/size API and responsive boundaries, exact overflow edge indication, detailed animation tokens, actual dismissal and focus behavior, light/dark and extreme-reflow runtime validation, Storybook/code mapping and tests.

**HOS-53 remains in progress** until these acceptance gates are resolved or explicitly scoped into separately tracked work with owner approval. The current Figma **visual/component authoring design** is accepted for this bounded baseline. No Code/Storybook implementation or parity claim is made.
