---
id: design-system.component.date-picker
collection: design-system
type: component
title: Date Picker
summary: Unified segmented date field with optional Calendar; Calendar Off supports manual date entry, Calendar On adds an accessible calendar selection surface.
knowledge_state: verified
document_maturity: draft
owner: Design System team
related:
  - design-system.component.text-input
  - design-system.component.dialog
  - design-system.accessibility.forms
  - design-system.accessibility.focus-management
  - design-system.accessibility.keyboard-navigation
  - design-system.accessibility.component-authoring-contract
topics:
  - date-picker
  - date-input
  - calendar
  - date-field
  - date-selection
  - rtl
  - focus
  - localization
  - responsive
  - accessibility
---

# Date Picker

> **HOS-49 — design contract for review.** Figma's unified Date Picker and Calendar Day Cell sources were rechecked on 2026-10-24. Their visual design, component placement, semantic tokens, and representative desktop/mobile compositions are complete. Real parser, browser keyboard and screen-reader behavior, responsive collisions, and Karbon/Storybook parity have **not** been executed or certified. Document maturity remains **draft** until owner review; Figma authoring properties are not confirmed runtime APIs.

## Purpose and component boundary

**Date Picker is the only public single-date field component.** It always supports manually editing year/month/day segments. Its **Calendar Boolean** switches between two supported uses:

- **Calendar Off (manual entry):** segmented date editing without Calendar trigger or popup. Use when users know and type an exact date (including historical/document dates).
- **Calendar On (default):** the same segmented field plus an independently focusable trailing Calendar trigger and a selectable Calendar surface. Use when visual date browsing is helpful.

Do **not** maintain an independent public Date Input master. The previous [Date Input](date-input.md) document and Figma source are **legacy compatibility references** for existing consumers only. The former Date Input functionality is now `Date Picker / Calendar=false`. Do not replace this date field with a generic Text Input and a decorative Calendar icon.

Date Picker is **not** Date Range, Time Picker, Date-Time Picker, timezone chooser, Menu, or a general-purpose Popover. The calendar is a specialized selection widget; the floating-surface rules are composed without turning this component into generic Popover content.

## Canonical Figma and authoring contract

- [Date Picker — live component and documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24764-3047), page **Date Picker**.
- [Date Picker — public component set](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24703-8942), `24703:8942`.
- [Calendar Day Cell](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24747-2862), `24747:2862`.
- [Calendar Surface](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24748-2810), `24748:2810`.
- [Mobile composition with shared Dialog](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24838-990).

There are **24** public variants: `Size = Small | Medium | Large` × `State = Default | Hover | Focus | Error | Error focus | Disabled | Read only | Read only focus`, with **Medium / Default** as the Figma default. **Calendar is a Boolean authoring property, not a Variant axis**, so switching manual-only and calendar-enabled entry must not double the 24-variant set. There is no `State=Focus+Open`, `Filled` variant axis, or public Range axis.

| Figma authoring property | Purpose |
|---|---|
| `Calendar` (Boolean, default **True**) | **Controls both the Calendar icon and Calendar popup availability**; `False` = manual date entry, no trigger or popup. Figma authoring of a design capability; runtime option naming must be confirmed. |
| `Open` (Boolean) | Controls **only the inner popup content**; it has no visible effect if `Calendar=False`, `Disabled` or `Read only`; **not a required runtime prop** |
| `Filled` (Boolean) | Previews a populated date; **Figma-only** |
| `Placeholder` (Text) | Empty-state localized format/placeholder sample |
| `Year`, `Month`, `Day` (Text) | Independently editable Figma visuals for **one** date |
| `Active segment` (Instance Swap) | Year / Month / Day highlight in Figma; **Figma-only** |
| `Show label` (Boolean) | Hides the visible label only when another accessible-name mechanism exists |
| `Show supporting` (Boolean) | Shows the ordinary supporting region |
| `Supporting text` (Text) | Contextual helper **or** format hint |
| `Error text` (Text) | Text feedback for Error / Error focus |

Nested canonical **Field label** owns `Label`, `Required`, `Show info`. The painted date control is now **inline in the Date Picker master**, as in Select; an unnecessary nested Date Field Base is no longer an active dependency. The `Calendar` Boolean is bound to the direct 16px Calendar icon and the outer Calendar slot; the separate `Open` Boolean is bound to the nested popup content. Therefore **Calendar Off always hides the popup even if Open=True**. Runtime derives open state from interaction and must not treat `Year`, `Month`, and `Day` as unrelated committed values.

## Anatomy, placement and visual rules

```text
Date Picker
├── Canonical Field label (Label / Required? / Info?)
├── Date control
│   ├── Segmented Date Input content (Year / Month / Day)
│   └── Trailing affordances, in logical End position
│       ├── Calendar icon (only if Calendar On and interactive; absent when Off/Read only)
│       └── Error icon (Error states; outermost when Calendar Off)
├── One supporting region (Helper OR format hint; Error replaces both)
└── Calendar selection surface (only if Calendar On and opened)
    ├── Month and year header + navigation
    ├── Weekday headings
    └── Calendar Day Cell grid
```

| Field Size | Control height | Inline padding |
|---|---:|---:|
| Small | 32px | 12px |
| Medium (default) | 40px | 16px |
| Large | 48px | 16px |

**Field Family:** `6px · Medium` radius and the canonical [Select](select.md) trailing-Chevron spacing pattern. Calendar is a **direct 16×16px icon instance within the field's Auto Layout**, with **no extra 24px or 32px wrapper or padding**. Its physical left inset in RTL is **12px in Small**, **16px in Medium/Large**. Field content gap matches Select: **4px in Small** and **8px in Medium/Large**, each bound to the shared Spacing variable. In Error and Error focus, the **16px Calendar icon remains leftmost**, and the **16px Error status icon sits immediately to its right** (toward the editable date). Both icons use the same Auto Layout gap; the content region shrinks automatically and must not overlap either icon. In Read only / Read only focus, hide the Calendar icon and reclaim the reserved space. The visual icon does not alone define the button's accessible pointer target: the runtime must provide an independently keyboard-operable trigger with a sufficient hit area **without adding visual inset or changing the spacing**. The calendar icon is non-directional and must not rotate upon opening. The action is not a fake affordance embedded in an inaccessible text input. The implementation must provide an actual keyboard-operable action with an accessible name and sufficient pointer target.

**Calendar header composition:** Previous/Next month controls are **instances of the existing [Icon Button](icon-button.md) component**, using `Style=Ghost`, `Size=Medium` (40×40px), and canonical `Icon/chevron_right` / `Icon/chevron_left` swaps appropriate to RTL. Do **not** create a separate Month Navigation Component Set or use a label-hiding Button workaround. The Month/Year label and two buttons are a frame **within Calendar Surface**, not a second independent Month-Year master. Preserve keyboard-operable labels for Previous/Next month in implementation; Figma instance names alone are not accessible labels.

**Figma source structure:** the canonical Date Picker now owns the painted Field Control **directly in each of its 24 variants**, matching Select's Field anatomy. This enables one `Calendar` Boolean to control the icon and popup while allowing the segmented content region to **expand automatically** when the icon is absent. The former three-size Date Field Base and 24-variant Date Input remain archived in Legacy for existing instances; they are **not active public sources**. The reusable internal Date Segment Focus master remains because it shares three focus-highlight positions without multiplying the public variant axes.

**Fluid field and fixed calendar width (RTL):** The Date Picker **field has no fixed Max Width**. Its Figma master is authored at a 288px **sample width**, not a maximum. When placed inside a resizing Auto Layout container, the entire field (Label, Control, Supporting/Error) stretches to the available inline width; `Calendar=false` also reclaims the trigger width. The date Placeholder is text-aligned **right** and the segmented value group is anchored to the **right side of its expanding content region**; Label and Supporting/Error text are also right-aligned in RTL. Individual segment numerals remain centered within their own edit targets. No element should retain a hard-coded 288px **field** constraint.

**Desktop Calendar:** the calendar **selection panel itself retains a fixed 288px width**, independent of field width, and its **right edge aligns to the field's right edge in RTL** (the logical inline-start alignment for this pattern). The popup remains outside the field's Auto Layout flow and does not affect field sizing. A field narrower than 288px may visually overhang on the left; runtime positioning must shift/flip as needed to stay within the **viewport**, rather than force the field to become 288px wide. The surface uses `surface/raised`, `12px · Large` radius, governed floating shadow, and **4px** vertical anchor gap. Fit to available viewport space, flip/shift when needed, preserve usable zoom/reflow, and avoid double wrapping in an independent Popover shell. An anchored selection panel is not automatically a modal Dialog.

**Mobile:** use the shared **Dialog** mobile composition (canonical `Size=Small / Viewport=Mobile` example) with the same Calendar source, not a second manually invented calendar shell. A modal mobile presentation requires correct focus scope, dismiss mechanism and restoration under the [Dialog](dialog.md) and [Focus Management](../../accessibility/focus-management.md) contracts. Figma demonstrates composition, **not tested responsive breakpoints or runtime modality**.

### Focus, errors and disabled treatment

- Default `surface/default` + `line/default` 1px.
- Hover / Focus border `line/emphasis` 1px.
- **Focus is not an extra border:** the canonical Text Input **two-layer semantic Effect** renders `focus/default` 2px with a 1px offset. It must not change control dimensions.
- Error uses `line/error` 2px and `fg/error` text. Error focus preserves both error border/message and the independent focus effect.
- Disabled uses `surface/disabled`, `line/disabled`, `fg/disabled`; neither date segments nor Calendar action should be operable.
- Read only uses `line/muted`, retains readable content and its focus treatment where appropriate, but must not offer a misleading editable/open action.
- The active date segment highlight is an editing context **inside** the content, not the outer control's focus ring.

**Segment authoring:** Day, Month, and Year live in one physical RTL-aware **Auto Layout** group rather than absolute-positioned text layers. Use the canonical **2px Spacing token** between the five segment/separator items; each date-part text is centered in its editable segment wrapper, with the active-segment backdrop painted **behind** the glyphs. Placeholder/filled content lives **inside the inline Field Control's Auto Layout content region**; it is not an unrelated absolute overlay of the former internal Field Base. Switching Calendar Off must reclaim Calendar icon space without shifting the field border or Focus effect.

**No** `surface/brand` for selected calendar days. The selected Cell uses `surface/accent-emphasis` (`surface/accent-emphasis-hover` when hovered) and `fg/on-color`. Ordinary day text uses `fg/primary`, adjacent-month text `fg/tertiary`, and disabled day text `fg/disabled`. Focus remains the distinct `focus/default` semantic role. Interactive hover uses `surface/transparent-hover`.

## Calendar Day Cell and single-date selection

The source `Calendar Day Cell` has **16 variants** from three orthogonal visual axes:

| Axis | Values | Meaning |
|---|---|---|
| `Interaction` | Default / Hover / Focus / Disabled | Local interaction/focus treatment |
| `Selection` | None / Selected | Whether this day is the selected date |
| `Month` | Current / Adjacent | Month relationship in the displayed grid |
| `Today` | Boolean authoring | Marks actual current date independently of Selection |
| `Day` | Text authoring | Locale-formatted day label |

**Today is not necessarily Selected.** Selected, Focus, and Today can coexist; the Figma source preserves combined appearance without a long opaque State list. The runtime must derive these properties from the actual calendar date and selection model, not blindly expose all combinations as valid application props.

Keep one selected date, with at most one calendar day marked selected at a time. Disabled dates remain unavailable to commit. A currently displayed adjacent-month day can be rendered or interacted with only according to the consuming calendar policy; no adjacent-date selection rule should be guessed from the visual source. `Disabled + Selected` and nonsensical Today combinations require runtime guards. Range-start, range-middle and range-end visuals **do not belong** to the Single Date Cell contract.

## Date value and input behavior

**Both Calendar modes use one date-only committed value and a recoverable segmented editing draft.** Empty, incomplete and temporarily invalid year/month/day segments are editing drafts, not new committed dates. A valid complete date is committed once; manual editing and calendar selection must never maintain conflicting date values.

- Year, Month and Day segments always remain manually editable in either Calendar mode. When `Calendar=False`, **there is no calendar action, no popup and no opening behavior**. When On, focusing the text control alone **does not** automatically open the popup.
- Typing and full-date paste use the same localized parser and validation; supported Persian/Arabic/Latin numerals normalize internally. An incomplete draft does not commit an invalid calendar date.
- A valid calendar day selection commits **one date value**, updates the segmented display, and closes the Calendar when the single-date selection action completes. An invalid/unavailable day does not commit.
- Product/Form supplies requiredness, initial date, min/max, unavailable-date predicates and validation timing/copy. Avoid variants for arbitrary dates, limits or error categories.
- Date-only values must not shift day because of time-zone or UTC-midnight conversion. Calendar system, display format, digit set and weekday order are **locale/product configuration**, not a fixed product-wide Gregorian or Jalali default in this component.
- A product-owned optional **Clear** action may be added when clearing is meaningful and permitted. It must not displace/confuse the Calendar action or silently clear a required date. The current public Figma design does **not** include Clear as a confirmed default.
- Today shortcut, presets, multi-month calendars, Date Range and Timezone are **not** included in Single Date v1 by default.

## Opening, keyboard and focus management

This is a **composite date-field + calendar** widget, requiring stronger behavior than a generic Text Input.

### Separate focusable trigger (Calendar On only)

- **Do not render or expose the Calendar trigger when Calendar is Off.** The trailing Calendar control, when enabled, is a real button or an equivalent semantic action; it has a meaningful accessible name (e.g. `انتخاب تاریخ`), appropriate expanded/controlled relationships, and a target that meets the pointer contract.
- Click, Enter or Space on this action opens the Calendar; clicking/editing the date segments does **not** open it. Opening the panel does not overwrite an incomplete editing draft.
- When opened, focus moves predictably to the selected date if usable, or to an appropriate initial date (often today, if enabled). The exact fallback when today is disabled/out of bounds is a runtime acceptance case.

### Calendar navigation

A keyboard-operable calendar grid must support logical focus and date navigation, including:
- Arrow movement between enabled/selectable dates, respecting the displayed week and RTL visual order.
- Home/End to relevant week boundaries and appropriate PageUp/PageDown month navigation where the chosen accessible calendar pattern supports them.
- Month/year navigation through clearly labeled controls; announce the visible period when it changes.
- Enter/Space to choose an enabled day when focused; distinguish the selected date from keyboard focus and Today.
- Escape to dismiss without changing committed value, then return focus to the Calendar trigger or another logically appropriate originating control. Outside-click dismissal must likewise not silently commit a draft.
- No focus trap for a **non-modal** desktop panel; modal mobile Dialog has its own contained focus and restoration rules.

Implement these as a tested accessible calendar pattern rather than guessing role/keyboard attributes from static Figma variants. If the runtime chooses a particular ARIA grid/dialog implementation, verify that its chosen focus model actually works with RTL, mixed numerals, keyboard, screen readers and viewport changes.

### Supporting content and validation

Under the control, **Error > explicit helper > generated locale Format Hint > nothing**. The Figma component has exactly one `Show supporting`/`Supporting text` authoring slot; do not stack Helper and Format Hint. While invalid, show actionable `Error text` with correct programmatic association. Validation is ordinarily triggered on blur or submit/commit per Product/Form policy, not every partial keystroke.

## Accessibility acceptance and evidence

Reference [Accessible Forms](../../accessibility/forms.md), [Focus Management](../../accessibility/focus-management.md), [Keyboard Navigation](../../accessibility/keyboard-navigation.md), [Dialog](dialog.md), the [Component Accessibility Authoring Contract](../../accessibility/component-accessibility-authoring-contract.md), and the [Accessibility Testing](../../accessibility/testing.md) gate.

**Before claiming accessibility or runtime readiness**, verify:
- overall field and individual segment labels; calendar trigger name/role/state and focus order;
- visible `:focus-visible` with error/selected/today contexts; no border-only Focus or layout shift;
- correct supporting/error associations, invalid/required feedback and announcements;
- keyboard-only type/paste/open/navigate/select/dismiss; focus restoration, grid boundaries, disabled dates, month changes and mobile Dialog;
- screen-reader date/day/month announcements, selected/current/disabled semantics, RTL/LTR, mixed-script input and correct localized digit output;
- 200% zoom, mobile soft keyboard, target sizes, touch interaction, floating collision and Product × Appearance contrast.

Figma screenshots and component-property counts do **not** prove completed browser, parser, screen-reader or Storybook QA.

## Known gaps and implementation boundary

- Final product rules for Jalali/Gregorian, localized formatting/parsing and ambiguous pasted dates remain to be supplied/approved by the consuming products. The shown March 2021 sample is illustrative only.
- Confirm initial focused date and adjacent-month selection when min/max or unavailable dates affect the grid.
- The exact runtime framework API, parser implementation, ARIA mechanism, automated stories and tests have **not been reviewed**. Do not infer Angular selectors or public inputs/outputs from Figma property names.
- Mobile Dialog is a live **design composition**, not evidence of working modal focus or touch/zoom behavior.
- Date Range and Time Picker/Date-Time Picker are different contracts and follow-on HOS-49 work.

## Live source and handoff state

**Figma:** single public Date Picker set `24703:8942` (24 variants) and Calendar Day Cell `24747:2862` on the official **Date Picker** page; checked 2026-10-24. Legacy Date Input master `24779:839` and Date Field Base `24662:227` are retained under internal compatibility sources for migration; no separate public Date Input page remains.

**Karbon / Storybook:** [karbon.jvoffice.ir](https://karbon.jvoffice.ir/) is the runtime reference site, but **no matching implementation export or executed parity, keyboard, screen-reader or responsive tests have been verified** for this component.

**Review gate:** Design System owner review, registry and link validations, and the triggered accessibility knowledge gate are required before merging or changing document maturity.
