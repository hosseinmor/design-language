---
id: design-system.pattern.image-upload
collection: design-system
type: pattern
title: Image Upload
summary: Draft composition for image selection, optional crop editing, preview and upload lifecycle.
knowledge_state: unverified
document_maturity: draft
design_status: provisional
owner: Design System team
related:
  - design-system.component.file-uploader
  - design-system.component.image-cropper
  - design-system.pattern.image-crop-dialog
topics:
  - image
  - upload
  - preview
  - avatar
  - pattern
---

# Image Upload

> **Draft composition**, not a new `File Uploader` variant or `Image Uploader` runtime API.

## Ownership and composition

The canonical [File Uploader](../components/file-uploader.md) owns selecting files, optional drag/drop, file list items and file-specific loading/error outcomes. Image Cropper owns visual positioning and crop boundaries. [Image Crop Dialog](image-crop-dialog.md) composes Cropper inside the existing Dialog. Image preview, replace/remove affordances and crop-to-upload sequencing belong to the consuming **pattern/product policy**, not to File Uploader's public `Type/Size/State` axis.

The legacy neighboring Figma `image uploader` 9-variant component (`19337:1420`) is retained pending migration/consumer audit; **do not delete or silently migrate it**. Keep the current File Uploader master, its file list slot, and its original variants unchanged. A custom trigger has **not** been approved or added to File Uploader in this task.

## Illustrative user journey

1. Select a candidate image with an accessible non-drag alternative.
2. When a product requires cropping, open Image Crop Dialog with the candidate image; permit modifying the crop.
3. Confirm the proposed crop or leave by the Dialog's safe Cancel path. Cancel must not silently replace an already saved image.
4. Show pending/selected and actual uploading/success/failure truthfully using File Uploader's existing lifecycle mapping where applicable.
5. Show a persisted image preview, Replace or Remove only according to product permissions and successful storage state.

This is an **example flow**, not a mandatory order or authorization to start transfer automatically. Format, byte limits, requiredness, multi-file policy, rotation, cropping rules and persistence are configured by each product. Browser `accept` is an input hint, not authoritative validation.

[Current Figma composition](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=25179-37): linked Image Crop Dialog, four-step flow explainer and illustrative circle/rectangle crop specimens.

## Distinct use cases

Avatar, employer logo and image-cover applications may share selection/crop mechanics but vary in preview surface, output constraints and replace/remove authorization. Do not create `Avatar/Logo/Cover` File Uploader variants solely for differing presentation. Keep the UI responsible for each image slot in its consuming product/pattern.

## Explicit TBDs and release gate

- Product-specific valid formats/dimensions, crop ratios, output generation and action availability.
- Whether Crop is mandatory/optional, upload starts before/after crop, and what happens to an earlier persisted image on cancel or failure.
- Narrow/mobile flow and uploaded-preview presentation have not been completed in Figma.
- Screen-reader, keyboard, file-picker security, actual uploading and crop output remain unverified until implementation/test evidence exists.

Do not upgrade document maturity or mark Ready for Dev until owner reviews these questions and the Figma composition is reconciled with the approved decisions.
