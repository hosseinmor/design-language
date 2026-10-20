---
id: design-system.component.progress-bar
collection: design-system
type: component
title: Progress Bar
summary: Continuous operation-progress component with measured determinate values, public Figma Indeterminate variants, and explicit success/error feedback.
knowledge_state: verified
document_maturity: final
design_status: ready-for-dev
design_maturity: handoff-ready
status: reviewed
owner: Design System team
last_reviewed: '2026-10-20'
related:
  - design-system.component.progress-indicator
  - design-system.pattern.loading-and-progress
  - content.pattern.loading-and-progress
  - design-system.accessibility.dynamic-content-and-feedback
  - design-system.reference.component-mapping
topics:
  - progress
  - progress-bar
  - determinate
  - indeterminate
  - feedback
  - accessibility
  - rtl
---

# Progress Bar

> **Document status: Final — HOS-37.** The **Determinate / Indeterminate / Success / Error** design contract and corresponding public Figma variants are ready for development handoff. In Figma, Indeterminate is a **static visual reference**, not verified animation. "Final" applies to the documented design contract, not to finished runtime code, production motion, or tested accessibility.

## Purpose

Progress Bar shows the advancement of an identifiable **continuous, asynchronous operation**. It helps users understand either the reliable completed proportion or the fact that processing is still underway.

Use cases include uploading a resume, processing applications in a batch, or preparing a report.

### Component boundaries

| Need | Use | Why |
| --- | --- | --- |
| Known completed proportion of one operation | **Progress Bar — Determinate**, or **[Progress Circle](progress-circle.md)** for compact circular presentation | Actual completed amount can be compared to a total |
| Operation ongoing; completed proportion unknown | **Progress Bar — Indeterminate** or an appropriate Loading pattern | No trustworthy percentage exists |
| Current position in a known sequence of workflow steps | **Progress Indicator / Stepper** | Represents ordered workflow states, not a continuous proportion |
| Short/local busy feedback without meaningful linear operation progress | **[Loading pattern](../patterns/loading-and-progress.md)** using Progress Circle / Indeterminate | An inline or localized busy indicator is sufficient |
| Historical sequence of events | **Timeline** | Describes what occurred and when |
| Capacity, static KPI, score, confidence, or rating | **Not Progress Bar** | Not progress through an ongoing operation |

Do not invent a fixed time threshold for choosing circular activity feedback versus a Progress Bar. The amount of useful progress/context, not a universal duration, drives the choice. The [Loading pattern](../patterns/loading-and-progress.md) composes Progress Circle / Indeterminate directly; Loading is not a separate component. Runtime behavior still requires implementation validation.

## Modes and status semantics

Mode describes **knowledge of progression**. Outcome describes **what happened to the operation**. These are conceptual concerns; Figma's existing `State` / `Progress` axes are not a runtime API.

### Determinate — supported in the public Figma component

- Render measured advancement based on a real total and a real completed value.
- A determinate runtime control must accept **arbitrary valid numeric progress**, not only the illustrated percentages in Figma.
- Conceptually, when `max > min`, normalized proportion is `(value - min) / (max - min)`. Render it within 0–100% of the visual track.
- The default conceptual percentage domain may be 0–100. A product using other units (count or bytes) must provide a valid min/max/value relationship.
- For missing, invalid, or unreliable values, do **not** display a fabricated percentage. Use an indeterminate/busy presentation when that is the true state; do not silently treat unknown as 0%.
- Visible numeric progress text is **optional** and must be based on the same true source as the measured segment. Do not show a visual percentage that disagrees with the rendered progress length.
- A long-running action may remain determinate even when its measured progress is temporarily unchanged. Do not fake incremental advancement to reassure users.

**Figma authoring decision (v1, verified 2026-10-19):** Retain the `0%`, `25%`, `50%`, `75%`, and `100%` design-time `Progress` presets as **illustrative snapshots**; do not create a variant for every possible percentage. Figma's component property model in this file exposes no numeric Value property. Testing direct nested segment geometry overrides did **not** provide a reliable editable numeric percentage in a component instance. Consequently, the current public component does **not** support exact arbitrary-percentage authoring in Figma. Do not label a 50% visual as “37%” or treat these presets as measured data. A precise one-off illustration needs separate, explicitly non-canonical visual composition and review, not a claimed Progress Bar instance API. **Runtime must accept and render actual validated numeric values, including 1%, 37%, 99% and 100%.** The lack of a numeric Figma property is intentionally **not** a development blocker.

### Indeterminate — implemented as static public Figma variants

Use Indeterminate when an operation is active but its completed proportion, remaining work, or ETA **cannot be measured reliably**.

**Required contract:**

- Communicate ongoing activity, **not how much work is complete**.
- Do **not** show a numeric percentage, completed/total count, guessed step, or invented time remaining.
- Give the user enough context to identify the action and object, for example «در حال آماده‌سازی گزارش…».
- An animated moving segment can reinforce busy feedback, but its motion must not be interpreted as measured progress or a promise of completion.
- When reduced-motion preferences are active, preserve the busy meaning using readable status text without motion-dependent information.
- Switch to Determinate only when trustworthy values become available. Switch to Success/Error only after the operation actually reaches that outcome.

**Figma status (2026-10-15):**

- The nested `_Progress bar track item` retains `Progress=Indeterminate` in **Small 4px** and **Big 8px**; no internal Track master was duplicated.
- The public `Progress bar` now exposes **five** `State=Active, Progress=Indeterminate` variants: `Default/Small`, `Default/Big`, `Inline/Small`, `Inline/Big`, and `Indent/Big`. These match currently supported Active size/alignment combinations; `Indent/Small` was not invented.
- Each Indeterminate master nests its corresponding Track and preserves linked Label/Helper text authoring where present. Indeterminate is a **Progress axis value**, not a separate Mode axis.
- **Verified in Figma:** component links, both sizes, available alignment treatments, RTL/Persian Playground, neutral Track stroke, accent **static segment**, and absence of numeric progress copy. The segment must move appropriately at runtime, not act as a static 25% claim.
- **Runtime QA needed:** actual animation, reduced-motion handling, accessible progress naming/value/announcements, and long/mixed-script responsive behavior.

### Completion and settled outcomes — aligned with Progress Circle

Measured advancement stays **Active / line/accent through 100%**. The normal measured sequence is Active partial → Active 100% → optional stable Success or Error once the actual result is known. There is no mandatory completion delay or automatic green state at 100%.

Success/Error are complete, static result treatments; they are not indeterminate or partially filled running states. A complete Error track does not assert successful transfer of all data: if work fails early, stop activity and report the actual failure without animating a fabricated numeric value to 100%. Keep truthful values distinct from terminal outcome presentation and announcements.

Figma now includes five Active 100% parents matching the five supported size/alignment combinations, plus a private 100% track for each size. Success/Error retain the Bar's existing supporting text/icons; the compact Circle intentionally has no message slot or built-in icon.

## Current Figma implementation — verified source

Figma: [Progress bar / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23867-126381)

| Source | Verified identifier |
| --- | --- |
| File | `[DS] Job Vision NEXT` — `rROD8ctH9UfPGAMrRrOzHe` |
| Page | `Progress bar` — `8930:400384` |
| **Public component set** | `Progress bar` — node `12603:272925`; component key `1d9983588bb228a44ca2b3af89195bd1e2b51c9d` |
| **Nested track set** | `_Progress bar track item` — node `12603:273022`; component key `b765a10f45d8d3ad69489a266bc6e623ba94d5b1` |
| Presentation | `Progress bar / Documentation` — node `23867:126381`, 1600px shared presentation system |

The Figma source has **30 public variants** (25 preserved and 5 Active 100% additions) and **16 nested Track variants**. Under the [Figma Component Presentation Guideline](../../integrations/figma-component-presentation.md), the **original public Component Set** (unchanged node ID/key) is physically placed in the presentation's **01 · Component set** section and the **original internal Track Component Set** in **03 · Anatomy & composition**. Both canonical sources retain all their variants, token bindings, and connected instances. Their variants have a more compact two-column *canvas arrangement*, not new APIs or duplicate sources. **02 · Playground** uses actual source-linked instances. Superseded IBM/Carbon documentation artboards and the redundant instance-only visual matrix/anatomy copies were removed. Source keys establish design identity; they do not prove library publication, Code Connect, or implementation.

### Actual authoring properties

| Component | Property | Existing values/type |
| --- | --- | --- |
| Parent | `Size` | `Small` (4px), `Big` (8px) |
| Parent | `Alignment` | `Default`, `Inline`, `Indent` |
| Parent | `State` | `Active`, `Success`, `Error` |
| Parent | `Progress` | `0%`, `25%`, `50%`, `75%`, `100%`, `Indeterminate`, `Success`, `Error` |
| Parent | Text | `Label text`, `Helper text`, `Success text`, `Error text` |
| Nested Track | `Size` | `Small` (4px), `Big` (8px) |
| Nested Track | `Progress` | `0%`, `25%`, `50%`, `75%`, `100%`, `Success`, `Error`, `Indeterminate` |

**Do not assume a full Cartesian variant matrix.** In particular, `State`, `Progress`, `Alignment`, and `Size` have only the 30 authored parent combinations. `Indeterminate` is an option of the existing `Progress` axis, not a separate Mode. There is no separate `Value`, `Show helper`, or `RTL` parent property. Hide any unneeded copy through supported instance authoring/layer visibility rather than assuming a Boolean property exists.

### Anatomy

```text
Progress bar (public)
├── Label (+ status icon on outcome variants)
├── _Progress bar track item (nested)
│   ├── Neutral Track stroke
│   └── Colored progress Stroke segments (when applicable)
└── Helper / Success message / Error message
```

`Default` places text around the bar; `Inline` uses a horizontal arrangement; `Indent` is another documented authoring arrangement. These are **layout choices**, not operation modes. Preserve the existing layout semantics in implementation only where the product uses them.

**Text resilience (Figma-verified 2026-10-17):** Default and Indent parent variants use content-hug vertical sizing with height-autoresizing Label/Helper; longer Persian strings can wrap and increase the component's height without clipping. Inline keeps a compact 20px row; its Label is fixed width and single-line truncated with an ending ellipsis. The presentation Playground includes **real source-linked long-Persian and mixed-script instances** demonstrating both strategies. In runtime, the full operation name must remain available to assistive technology even if visually truncated; do not depend on a tooltip alone for the accessible name.

### Visual and token contract

| Role | Token / approved treatment |
| --- | --- |
| Neutral/unfilled Track | `line/default` — **Stroke**, never Fill |
| Active progress segment, including 100% and static Indeterminate | `line/accent` — **Stroke**, never Fill |
| Complete Success segment | `line/success` — **Stroke**, never Fill |
| Complete Error segment | `line/error` — **Stroke**, never Fill |
| Construction | Both unfilled Track and colored segments use **inside bottom Stroke** with weight **4px Small / 8px Big**; colored segments have **no Fill** |
| Success icon / message | `fg/success` |
| Error icon / message | `fg/error` |
| Label | `fg/primary` |
| Ordinary helper | `fg/secondary` |

The Track and colored segments have **square ends**. The entire progress path uses Strokes bound to existing `line/*` semantic tokens, consistent with [Progress Circle](progress-circle.md). The neutral Track is drawn by the nested Track component's bottom Stroke; each occupied segment uses a full-height **inside bottom Stroke**, no Fill, and unchanged 0/25/50/75/100/Indeterminate geometry. Figma preserves the source rectangles/spacers, master keys and RTL arrangement. No component-specific color tokens or expanded scopes are required. Foreground `fg/*` tokens remain appropriate for status text/icons rather than the progress path. In Angular, implement these roles as the semantic stroke/border colors; a line-drawing technique may differ as long as the output matches the contract.

### Typography roles — verified in Figma (2026-10-17)

| Text role | Text style | Size / line height | Font weight | Semantic foreground |
| --- | --- | --- | --- | --- |
| Primary operation Label (all alignments) | `Label/SM` | 14px / 20px | Medium 500 | `fg/primary` |
| Ordinary Helper | `Body/Compact/XS` | 12px / 16px | Regular 400 | `fg/secondary` |
| Success message | `Body/Compact/XS` | 12px / 16px | Regular 400 | `fg/success` |
| Error message | `Body/Compact/XS` | 12px / 16px | Regular 400 | `fg/error` |

The operation Label is the primary identifier of the running task; Helper and terminal-state messages are supporting text. **Do not use `Body/Compact/SM` for the operation Label or `Label/XS` for Helper/Success/Error in this component.** Semantic status colors and clear copy, rather than heavier helper typography, distinguish outcomes. Retain existing RTL alignment, Default/Indent multi-line height growth, and the one-line ending ellipsis in Inline variants. This is a typography role correction, **not** a change to font sizes, line heights, component sizes, or the runtime API.

### Figma token-compliance refinement — 2026-10-20

A source-only audit of the **original** `Progress bar` (30 public variants) and `_Progress bar track item` (16 internal variants) verified the current semantic Stroke, Typography and geometry contract. **46** existing shared-scale spacing properties lacked a Figma Spacing variable binding. They were rebound **in place** without modifying numeric values, component IDs/keys, layout dimensions, or the set's existing Figma API:

- **30** public parent `itemSpacing` bindings: **22 × 8px** in Default/Indent and **8 × 16px** in Inline.
- **4 × 16px** `Label + Icon` gap bindings in Success/Error parent variants.
- **12 × 16px** `paddingRight` bindings on Label and Helper frames in Indent variants.

**Outcome-copy correction:** Both existing `Success message text` layers had consumed `fg/secondary`, despite the Status Typography contract above. They now consume **`fg/success`**, preserving Body/Compact/XS and the original text/content geometry. On the normal `surface/default` background, resolved `fg/success` contrast is **5.02:1 Light / 6.98:1 Dark**; `fg/error` is **6.29:1 / 5.91:1**, for both current Product mappings. This is calculated token contrast, not browser/AT certification.

**Final source evidence:** 46/46 active Spacing properties bound, 52/52 Text layers styled, **44/44 internal bottom-inside Strokes** using `line/default` (16), `line/accent` (18), `line/success` (5) and `line/error` (5). Every progress-path Stroke is bottom-only, 4px Small or 8px Big; no progress-path Fill or foreign semantic token remains. The old paint applied to the **Figma Component Set presentation shell** is not part of consumer instances and was excluded from the source audit.

No new variable, variant, mode, success/error runtime behavior or percentage-authoring capability was added. Indeterminate remains a static Figma reference. Light/Dark editor screenshots, published-instance overrides, actual animation, reduced-motion and accessibility testing remain separate runtime/consumer QA gates.

See the dedicated Progress Bar token audit for node IDs, counts and validation details.
## Content and status text

Content rules belong to [Loading and Progress Content](../../foundations/content/patterns/loading-and-progress.md); use its writing rules and machine-readable evaluation where relevant.

- If text is needed, name the operation and object: «در حال بارگذاری رزومه…», not just «لطفاً منتظر بمانید».
- For Determinate, show a percentage/count **only** when verified: «در حال پردازش ۱۸ درخواست از ۳۶ درخواست».
- For Indeterminate, do not invent numbers, timing, or proximity to completion.
- Do not use Success or Error copy until the result is known.
- Only present Cancel, Retry, background continuation, or completion notification when the product supports it.
- Prefer concise helper text with no duplicate status announcement.

## RTL and localization

- Progress Bar belongs to an RTL product context; **0% starts at the logical start (right in RTL)** and a larger determinate value extends toward the left. Do not reverse the **numeric** meaning of progress.
- Label and Helper should align for Persian reading; percentages and mixed Latin/Persian strings must remain readable with correct bidirectional isolation where applicable.
- Match the value text to the localized units and numerals chosen by the product's localization rules. Never hard-code progress values into the layout.
- Figma has **no separate RTL variant**, so QA RTL on real instances and runtime logical properties instead of creating new directional Cartesian axes.

## Motion and interaction

This component is **passive and not keyboard-interactive**. It has no Hover, Pressed, Focus or Disabled operation state.

- Determinate progress-segment transitions must reflect **real progress value changes**, not an independent timer.
- Indeterminate may use a visibly moving segment on a stationary track. The exact timing, curve, and mechanics are **runtime-owned and unverified**.
- When `prefers-reduced-motion: reduce` is active, disable nonessential looping motion and convey the busy state via text/semantics.
- Do not move keyboard focus merely because progress starts or stops.
- The source does not define cancellation or other controls inside the Progress Bar; any action is product-owned.

## Accessibility — required implementation behavior

Use semantic progress exposure appropriate to the measured/unknown status. Because this is not yet tested against a registered runtime source, all items here are **requirements**, not claims of implementation.

| Case | Accessible contract |
| --- | --- |
| Name | Provide an accessible name identifying the action/object; use visible text via `aria-labelledby` where suitable |
| Determinate | Expose `role="progressbar"` or equivalent native semantics, valid `aria-valuemin`, `aria-valuemax`, and measured `aria-valuenow` |
| Unit-heavy values | If numbers alone are unclear, provide true descriptive `aria-valuetext` or associated text; never fabricate a percentage |
| Indeterminate | Expose a named progress indication **without `aria-valuenow`**; do not substitute 0 or a fake value |
| Busy region | Use `aria-busy` for the affected region only when appropriate; do not apply it indiscriminately to the entire application |
| Success / Error | Announce important terminal status without moving focus; color or icon must not be the only indicator |
| Noise | Avoid live-region announcements for every tiny increment; announce meaningful transitions/milestones without duplicate competing live regions |
| Motion | Busy meaning and outcome must remain clear with reduced motion and without relying on animation |
| Focus | No additional Tab stop for a passive progress display |

Follow the canonical [Dynamic Content and Feedback](../../accessibility/dynamic-content-and-feedback.md) requirements for status-announcement strategy. Preserve ordinary reading order and announce outcomes with the least interruptive sufficient mechanism. UI/assistive-technology verification is a development acceptance requirement.

## Acceptance plan — Storybook bypass

| Test | Acceptance condition | Verification status |
| --- | --- | --- |
| Public Figma variants | 30 parent variants (including 5 Active 100% and 5 Indeterminate), same component-set ID/key | **Verified in Figma** |
| Nested Figma variants | 16 Track variants, including 100% and Indeterminate Small/Big | **Verified in Figma** |
| Complete line-only Progress path | `line/default` on neutral Track and `line/accent`, `line/success`, `line/error` on colored segments, all inside Strokes at 4/8px thickness, **no segment Fill** | **Verified in Figma** |
| Visual presentation | One 1600px documentation frame with **original** public Master in 01, original Track Master in 03, and five real RTL Playground instances in 02; no stray legacy artboards | **Verified in Figma** |
| Status appearance | Active, Success and Error render with semantic color and supporting text | **Verified in Figma** |
| RTL sample | Representative Persian content and orientation shown | **Verified in Figma** (design only) |
| Numeric dynamic progress | Any validated numeric value maps to matching segment length/value semantics; not limited to fixed Figma percentages | **Required in development** |
| Determinate edge cases | 0%, intermediate, 100%, missing total/invalid input handled truthfully | **Required in development** |
| Indeterminate behavior | No numeric value, named busy state, sensible motion/reduced-motion fallback | **Specified; runtime verification required** |
| Parent Figma Indeterminate | Public `Progress=Indeterminate` includes Default Small/Big, Inline Small/Big, Indent Big; nested Track connected | **Verified in Figma** |
| Parent Figma Indeterminate QA | Both sizes/layouts, Persian RTL and mixed-script truncation samples, no percentage, static segment | **Verified in Figma** (animation still requires runtime QA) |
| Screen-reader semantics | Accurate determinate/unknown progress; terminal states announced; no update spam | **Required in development** |
| Figma overflow composition | Long Persian Label/Helper reflow in Default/Indent; Inline ellipsis stays one line; Playground QA shows unclipped cards | **Verified in Figma** |
| Runtime responsive composition | Long Persian/mixed-script labels remain accessible and readable at actual product widths | **Required in development** |
| Runtime/Storybook | Owning Angular API, tests and Storybook link | **Unregistered / bypassed for design handoff** |

Storybook is **not a prerequisite for the current design handoff**. Product runtime QA, browser and assistive-technology tests remain development responsibilities; they must not be represented as already passing.

## Verified design work and implementation boundary

1. **Done — public Figma:** 30 public variants and 16 nested Track variants; Indeterminate is connected and static in Figma. All neutral and colored progress segments are bound to properly scoped `line/*` Strokes with no segment Fill; visual and structural QA passed across every nested and public variant.
2. **Done — size consistency:** Existing `Inline/Big` 0/25/50 variants were fixed to use the correct **8px Big Track**, preserving all original IDs and keys. Every public parent now embeds a nested Track matching its `Size`.
3. **Done — robust text authoring:** Default/Indent instances grow vertically for long Persian text; Inline is fixed 20px height with a one-line ending ellipsis. The Figma presentation has overflow regression cases.
4. **Decision — exact numeric values in Figma:** v1 intentionally uses illustrative 0/25/50/75/100 snapshots instead of a misleading or combinatorially large numeric variant family. No existing public numeric Figma control is claimed. **Runtime supports arbitrary valid values**, not these presets.
5. **Pending development/runtime verification — [HOS-40](https://linear.app/hossein-mor/issue/HOS-40):** Indeterminate animation and reduced-motion fallback, runtime numeric geometry, Angular component/API registration, accessible name/value/status announcements, responsive content and browser/assistive-technology tests. These are not design-source defects and must be completed in the owning runtime code.


The **Indeterminate Figma state is implemented**. Its Figma visual is a static reference; motion and accessibility implementation are not yet verified.

## Sources and handoff status

- Figma [canonical Progress Bar presentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23867-126381) — editable design source.
- [Design-to-Code Component Mapping](../../integrations/component-mapping.md) — verified design identity, pending runtime mapping.
- [Progress Indicator](progress-indicator.md) — discrete workflow boundary.
- [Loading and Progress Content](../../foundations/content/patterns/loading-and-progress.md) — canonical content constraints.
- [Dynamic Content and Feedback](../../accessibility/dynamic-content-and-feedback.md) — accessible status requirements.
- HOS-37: https://linear.app/hossein-mor/issue/HOS-37/pilot-progress-bar-component-across-figma-and-design-system-knowledge

**Handoff status:** Documentation **final**; Progress Bar Figma composition and content/size QA **ready for development**. Indeterminate is **static in Figma** and Figma numeric presets are **illustrative only**; runtime animation, numeric API, accessibility behavior and tests remain **unverified**. Original 20 variant masters and both component-set identities are preserved.
