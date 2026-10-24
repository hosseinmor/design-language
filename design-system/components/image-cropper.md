---
id: design-system.component.image-cropper
collection: design-system
type: component
title: Image Cropper
summary: Draft editable crop viewport for an image; composed inside the existing Dialog without owning file transport.
knowledge_state: unverified
document_maturity: draft
design_status: provisional
owner: Design System team
related:
  - design-system.component.dialog
  - design-system.component.file-uploader
  - design-system.accessibility.focus-management
  - design-system.pattern.on-media-controls
topics:
  - image
  - cropper
  - focus
  - zoom
  - figma
---

# Image Cropper

> **Draft — visual Figma source exists; owner review and input/AT validation outstanding.** This document does not establish runtime API, shipped behavior, allowed media formats or upload timing.

## Role and scope

Image Cropper is a reusable **editing surface** for positioning an existing image inside a crop boundary. It does not select, upload, persist or delete files, and does not own dialog dismissal. A consuming image flow composes it with File Uploader and, for a modal editing task, the reviewed general Dialog.

**Preserved contracts:** Do not modify File Uploader's 15-variant public source or its file lifecycle. Do not create a Crop-specific Dialog shell. The general Dialog owns header/footer, focus containment and exit logic. Use the existing legacy Slider instance for zoom; **do not redesign Slider as part of this work**. Shared focus remains governed by `accessibility/focus-management.md`.

## Current editable Figma draft (2026-10-24)

- [Image Cropper page](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=25175-36).
- Public master: `Image Cropper`, component set `25175:135`.
- Current illustrative authoring axes: `Shape=Circle/Rectangle` × `State=Default/Focus` (4 specimens). They are **Figma exploration**, not approved product defaults, verified runtime props or a full state inventory.
- Anatomy: `Crop / Stage` → `Photo / Background`, outside-crop dim, `Crop / Editable preview`, crop boundary and optional rectangular guide. A helper precedes a **linked instance** of existing Slider (`3673:40573`) with sample text overrides. Original Slider component is unchanged.
- The two `State=Focus` specimens apply the existing `Focus/Default` effect style to the perceived crop viewport; do not invent a new Focus token, draw only a modified border, or indicate keyboard focus on the whole composite when the active sub-control is the crop region.
- Image content currently uses an existing illustrative raster asset from the old Image Uploader for component examples. The asset is **not an endorsed placeholder or image requirement**.
- Presentation: `25181:166` contains anatomy, shape/focus samples, usage and open questions. Samples use linked component instances.

## Draft design guidance

Crop viewport and Zoom Slider must be independently identifiable. A single image should remain recoverable while the user is editing its prospective crop. The crop view should convey the area retained and any dimmed excluded area; do not imply that a circular guide necessarily changes the output file format. Editing controls over images must respect the current [On-Media Controls](../patterns/on-media-controls.md) restrictions; avoid unsupported ad-hoc on-image focus/contrast tokens.

Crop-region keyboard operation, focus movement and output-specific behavior require owner review and future runtime tests. The shared `:focus-visible` contract applies; a mouse drag is not itself a reason to show the shared keyboard focus ring.

## Explicit open decisions — do not silently encode

1. Supported aspect ratios (including whether an arbitrary ratio exists); circle versus square **preview and exported shape semantics**.
2. Minimum and maximum Zoom, initial scale, reset behavior, pan constraints, step sizes and touch/mouse/keyboard gestures.
3. How empty/invalid/decoding-failure images appear, and whether rotation or orientation normalization is in scope.
4. Fluid small-screen authoring and constrained viewport/zoom behavior; current Figma specimen is regular-width only.
5. Whether the editing surface needs additional meaningful visual states beyond Default/Focus, and the crop output handoff contract.

## Acceptance before promotion

Validate crop/zoom affordances, responsive containment in a modal, RTL text, correct source-linked Slider, user-overridable image sample, local Focus effect, and no modifications to original File Uploader/Dialog/Slider component identities. Test keyboard-only and assistive-technology operation in the future runtime separately; no runtime parity is claimed.
