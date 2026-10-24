---
id: design-system.component.file-uploader
collection: design-system
type: component
title: File Uploader
summary: Canonical Carbon-derived file selection and drag-and-drop design contract, with native File list Slot, file-level feedback and verified Figma sources.
knowledge_state: verified
document_maturity: final
design_status: ready-for-dev
design_maturity: handoff-ready
status: reviewed
owner: Design System team
last_reviewed: '2026-10-20'
related:
  - design-system.component.progress-bar
  - design-system.component.progress-circle
  - design-system.pattern.loading-and-progress
  - design-system.reference.component-mapping
  - design-system.accessibility.forms
  - design-system.accessibility.dynamic-content-and-feedback
  - content.pattern.loading-and-progress
  - content.pattern.error
topics:
  - file-uploader
  - file-item
  - dropzone
  - upload
  - rtl
  - accessibility
  - validation
---

# File Uploader — HOS-39

> **Final design contract; ready for implementation/sandbox handoff, not production certified.** This specification describes the **original Carbon component now canonical in Figma**, NOT the archived single-size pilot. The original Carbon component identities and composition are preserved; subsequent token-compliance visual refinements are documented in the 2026-10-20 section below. No actual upload endpoint, runtime API, Storybook story, keyboard behavior or assistive-technology result has been verified. These are implementation acceptance requirements, not claims of working code.

## Purpose, composition and boundaries

File Uploader lets a user choose one or more files, optionally drag them into a target, and inspect the selected files and their independent statuses. It owns the **entry area** and composes a **File list** of File Items.

- **File Uploader**: selection entry point, label/constraints, enabled/disabled treatment and nested list visibility.
- **Dropzone**: optional alternative pointer drop target; **never the only input method** and not a second upload-state owner.
- **File Item**: one file's name, visually identifiable loading/outcome/error and associated permitted action(s). A file-level failure must not mark other files failed.
- **Progress Circle / Indeterminate / Active**: directly supplies the 16px spinner in all three File Item `State=Loading` sources. Loading remains a File Item state and a [usage pattern](../patterns/loading-and-progress.md), not a separate spinner component or a real percentage.
- **Progress Bar**: shared component for trustworthy determinate or indeterminate continuous progress, when needed.
- **Attachment / Image Uploader**: passive already-stored attachment or crop/preview-specific flow, respectively; not automatically a File Uploader state.
- **Inline feedback**: field/batch-wide error that cannot be localized to one File Item; use the Content System error pattern instead of painting all files red.

Selection constraints, upload network timing, virus/security validation, remote deletion, persistence and cancellation semantics are owned by the **consuming product and runtime**. They are not Design System defaults.

## Canonical Figma authoring (verified)

[Open actual Carbon File Uploader documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24020-785)

| Actual Figma master | ID | Verified structure |
| --- | --- | --- |
| Public `File uploader` | `5465:294860` | **15 variants**: Type × Size × supported State |
| Internal `_File uploader file item` | `3199:35182` | **18 variants**: Size × 6 presentational States |
| Internal `_File uploader - Drag and drop box states` | `3183:29103` | **4 states**, original Carbon |
| Internal `_File uploader file list item` | `4188:102462` | **1 native `File list` Slot**, ID `24003:831` |
| Figma presentation | `24020:785` | Actual masters in §01/§03, six connected Playground examples |
| Superseded HOS-39 pilot | `23907:394` | Archived experiment; **not** an API/source for Carbon |

Public properties: `Type` = Default / Drag and drop; `Size` = Large / Medium / Small; `State` = Enabled / Disabled (plus Skeleton only where provided for Drag and drop); `Label text` and `Desc. text` are Text; `Files` is Boolean for list visibility. Do **not** invent separate runtime `Mode`, `UploadStatus`, `FileCount` or `DragReject` props from these names.

Internal File Item: `Size` (L/M/S), `State` (Uploaded, Loading, Success, Focus, Error short, Error long), and `File name`, `Short desc.`, `Long desc.` Text properties. Internal Dropzone: Enabled, Drag + Hover, Focus and Disabled, with editable `Helper text`. These are original presentational variants, not evidence of network behavior.

The File list has **one** shared `File list` authoring Slot containing exactly **three existing source-linked File Item examples**. Designers can add, replace and remove items; do not add a count variant. In the source these three items measure **L 160px / M 136px / S 112px** total height. These are *Figma specimens*, never files automatically present in the consuming product.

### Copy and default visuals

- Public helper default: **«فایل موردنظر را انتخاب کنید.»** No assumed type, size or count limit.
- Dropzone instruction: **«فایل را اینجا بکشید و رها کنید یا روی «انتخاب فایل» کلیک کنید»**. The explicit Browse action must work without dragging. The instruction does not establish that the whole region is clickable.
- Where a product has verified format, byte-size or count limits, replace the generic helper with the actual relevant constraints *before selection*. A generic Carbon example such as “500KB, jpg/png” **must not ship as an unverified product policy**.
- Error copy must describe a **known** failure and, if available, a supported recovery: e.g. «فرمت این فایل پشتیبانی نمی‌شود. فایل دیگری انتخاب کنید.» Do not assert network causes or recovery guarantees without evidence.
- Original Carbon Button styles and Dropzone composition remain; the File Item radius is now 6px Medium (previously 4px) and the passive item surface is now surface/muted. These are deliberate DS refinements, not imports from the archived pilot. The pilot's 12px/176px Dropzone, Drag-reject, illustration TBD, and XS Cancel/Retry choices are **not silently migrated**.

## Design behavior contract (normative)

### Entry, file count and disabled state

1. **Browse works for all enabled entry types**. Drag and drop is an enhancement for capable environments, never a mandatory path. Keyboard and touch must retain Browse.
2. **Single versus multiple is a consuming-product selection policy**, not a `Size` or file-count variant. A single-file flow must not silently replace an existing file. Use an explicit Remove/Replace path approved by the product. Multi-file flows may append only up to real configured limits.
3. **No implicit upload timing**. A file may be merely selected until submit, or transfer may start immediately, depending on the product. Never label a selected file as successfully uploaded unless a trusted source confirms success.
4. **Disabled** prevents new selection and drag/drop. Existing uploaded files may remain visible as a separate content policy; the legacy Carbon disabled specimen hides the list, so consumers needing visible saved files must explicitly compose that state rather than assuming Carbon's disabled variant provides it.
5. **Duplicate files**: default to preserving existing selections; do not silently replace or deduplicate without product policy. If rejected by a known rule, identify the affected file and provide a viable next step.

### File lifecycle and mapping to Carbon

| Logical/runtime state | Intended behavior | Current Carbon representation / caveat |
| --- | --- | --- |
| Selected / pending | File accepted locally for this flow; transfer not necessarily started | `Uploaded` is a **legacy visual label only** and must not be interpreted as server success |
| Uploading | Transfer actually underway | `Loading`; spinner is indeterminate only, no invented percentage |
| Uploaded / success | A trusted product/backend result establishes success | `Success`, or an approved persisted-file presentation |
| Validation error | File rejected by an enforced type/size/count/security rule | `Error short` or `Error long` based on **content length**, not error category |
| Upload error | An attempted transfer failed | `Error short` or `Error long` with a truthful transfer-failure message |
| Focus | Keyboard interaction state; **not a lifecycle step** | `Focus` is purely interaction feedback |
| Canceled | Transfer interrupted on request, only if supported | **No Carbon state in v1**; requires a separate product/runtime decision |

State names above are a *semantic mapping for implementers*, **not verified runtime prop names**. The two Error length variants must never become separate error codes.

### Remove, Retry, Cancel and Progress

- **Remove**: only when the product permits removing that file. Remove-before-upload discards a local selection; removing an already persisted file may require a different authorized operation. Neither one necessarily cancels a running transfer.
- **Retry**: show only when a failed attempt can genuinely be repeated from preserved file data. Preserve unrelated successful files and show any real result. The original Carbon error Item has no approved dedicated Retry button; until such a control is implemented, a supported re-selection path is acceptable.
- **Cancel**: the earlier experimental pilot explored a Ghost/XS «لغو» action, but the canonical Carbon `Loading` source does **not** contain it. **Do not render an inert Cancel** or mislabel Remove as Cancel. An explicit Cancel + post-cancel outcome is a separate optional enhancement requiring runtime capability.
- **Progress**: show actual measured amount via the shared Progress Bar (determinate) only where the product exposes valid loaded and total bytes; otherwise the existing spinner/indeterminate pattern is appropriate. Announce important transition milestones, not every percentage-point update.
- **Error recovery**: a field-level upload failure must not erase other files; if a file is retained for retry, do not claim its bytes are available after reload unless the product guarantees that.

### Error ownership and validation timing

- On file selection/drop, validate the enforced limits available locally, then apply authoritative server validation. `accept` is only a hint, not authoritative security validation.
- **During drag**, the browser may not expose enough file information to decide accept/reject. Carbon's `Drag + Hover` is not a promise that a file will be accepted. The archived pilot's Drag-reject is **out of v1 scope** until its capability is verified.
- **After drop/selection**, type/size and per-file violations belong on the affected File Item. File transfer error also belongs to that File Item. A batch/field-level problem belongs to associated inline field feedback.
- Format, maximum bytes, count, duplicate/replacement policy and requiredness are configured by product, **not by the shared design system**; do not invent values in Figma examples or error messages.

### Responsive, RTL and accessibility acceptance criteria

- Original Carbon Figma specimens are 288px wide; this is not a fixed product breakpoint. Runtime must handle narrow widths, wrap helper/error text without cropping actions and preserve readable file extensions. No unverified claim is made that the Figma master itself is fluid.
- Align Persian instructions to the product RTL reading order. Isolate mixed RTL/LTR filename segments bidirectionally; visually truncate excessively long filenames where needed but expose the **full accessible name** and provide a non-pointer-only way to retrieve the full filename.
- The file input has a persistent accessible label; actionable errors must be associated with the relevant file/field. Use native input/keyboard semantics and a visible focus indicator. No nested interactive controls within an already-interactive drop target.
- Every active file action needs a unique accessible name including the filename (e.g. «حذف رزومه.pdf»). Disabled/hidden actions must not remain keyboard-operable.
- Announce selection, completed upload, failures and removal with nonintrusive status semantics when focus does not move. A spinner is not itself an adequate announcement of success or failure.
- If selection is required, communicate requiredness visibly/programmatically. Do not clear unrelated valid files after a recoverable error. Respect reduced motion for transitions if introduced.
- **Release/QA matrix:** empty / 1 / 3+ files; Browse and drag/drop; per-file Loading/Success/Validation/Upload failure; different file counts; long Persian/Latin name; 320–360px / zoom; focus, disabled, keyboard-only, screen reader; actual network retry/cancel only when enabled by product.

## Scope and implementation handoff

**Design-approved v1:** existing Carbon Type/Size/State families, actual original button/dropzone styling, native variable-length File List Slot, nonfabricated copy, file-level errors, product-configured limits, a non-drag file picker and the accessibility/validation behavior above. **No new canonical variants** are required merely for content length, count or product policy.

**Excluded from v1**: branded illustration, separate Drag-reject state, generic global upload error state, arbitrary file-count variants, additional Cancel/Retry visual controls from the archived pilot, assumed remote deletion, hard-coded accepted formats or upload endpoints. Future capabilities require specific product scope and cannot be imported just because a Figma draft contains them.

**Verified on October 17, 2026:** canonical component IDs and 15 / 18 / 4 variant counts, one native Slot with three connected default items, six source-linked Playground cases (one file, three files, Persian validation, disabled, mixed file statuses, long filename), standard 1600px Figma presentation, and default text changes. These are **Figma/source checks, not executed runtime/AT tests**.

**Required of implementing team:** map the code API and actual product constraints, wire native input/drop handling, pass the behavioral and accessibility matrix, and record Storybook/code source identities in `component-mapping.md` after verification. Failure in any required runtime criterion blocks production release, **not the Design System design handoff**.

Design knowledge is finalized for review and development use; no claim is made that the component already uploads files in a browser.


## Token compliance and current Figma migration (2026-10-20)

Original component identities and authoring API remain intact: **15 public variants, 18 File Item variants, 4 Dropzone variants, and one File list Slot with three connected specimens**. No component/variant identities or slots were recreated.

### Foundation binding changes

- **131** spacing properties were bound to existing Spacing variables (27 public / 102 File Item / 2 File list).
- **16** Dropzone corners were rebound from deprecated 12px Surface to shared 12px Large, without changing geometry.
- Disabled Dropzone helper was rebound to public **fg/disabled** from an unresolved legacy reference.

### Approved semantic and appearance changes

- **File Item background:** all 18 variants now consume **surface/muted** instead of surface/neutral-muted. The container presents file/status information passively; Remove/other actions remain separate interactive controls.
- **File Item corner radius:** all 18 variants now bind four corners to **6px Medium** (72 radius properties). This intentionally replaces the previous raw 4px radius, but preserves variant identities, widths/heights and file contents.
- **Dropzone Focus:** the existing Focus variant keeps its **1px `line/emphasis`** boundary and adds visible Focus through the shared [Focus Management](../../accessibility/focus-management.md) contract. Drag + Hover remains a separate state. In Figma the Dropzone base is the perceived Focus target; runtime visibility follows the shared Focus Management contract rather than a File-Uploader-specific keyboard/pointer rule. Figma editor/browser visibility still requires acceptance testing.
- **Error message contrast:** the three short 12px failure messages now use **fg/primary**; three long secondary descriptions use **fg/secondary**. Their icon **fg/error** and border **line/error** remain. Earlier fg/error error text was only 3.91:1 in Dark against the newly passive File Item surface.

### Contrast checks and restrictions

Computed from actual JobVision/Cando x Light/Dark Figma alias values on surface/muted:

| Role | Light | Dark |
|---|---:|---:|
| fg/primary | 18.48:1 | 8.83:1 |
| fg/secondary | 7.41:1 | 5.85:1 |
| fg/error icon, non-text | 5.87:1 | 3.91:1 |

The new normal text combinations exceed 4.5:1; the error icon exceeds the 3:1 non-text threshold. Values are identical in the inspected Product mappings. These are **calculated token contrasts**, not browser or assistive-technology test results.

**Focus/default contrast against surface/default:** 4.59:1 Light and 4.31:1 Dark. Against surface/muted in Dark it is **2.85:1**, requiring separate review whenever that backdrop is used for the Focus ring. Do not assert global keyboard/focus compliance merely from the token/style binding.

**Open maintenance and runtime debt:** File Item 7/11/15px optical padding; Dropzone 10/50px local construction; old Transparent/Transparent Paint Styles; actual focus-ring editor/browser rendering; mixed-content, screen-reader and native file input testing; published instance override regression; product appearance visual matrix. The neighboring nine-variant **image uploader** is a separate component with its own migration debt, not part of this scope.

Detailed evidence: File Uploader Token Migration Audit. Foundation/semantic fixes are **applied in Figma**, while runtime, focus and published-consumer QA remain open.
