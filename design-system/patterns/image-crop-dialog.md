---
id: design-system.pattern.image-crop-dialog
collection: design-system
type: pattern
title: Image Crop Dialog
summary: Draft modal composition of the Image Cropper inside the existing general Dialog.
knowledge_state: unverified
document_maturity: draft
design_status: provisional
owner: Design System team
related:
  - design-system.component.dialog
  - design-system.component.image-cropper
  - design-system.accessibility.focus-management
topics:
  - image
  - crop
  - dialog
  - pattern
---

# Image Crop Dialog

> **Draft composition, not a new Dialog component or type.**

## Composition

Use the reviewed **general Dialog** (`Dialog / Default`) with its native Body and Footer slots. Insert an Image Cropper **instance** in Body; preserve the Dialog's Header, Close Button, overlay, semantic surface, width rules, Footer action instances, focus containment and safe-exit contract. Do not detach or duplicate the Dialog shell. The crop interface does not own modal opening, dismissal or an API for backdrop behavior.

[Live Figma pattern and linked Dialog specimen](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=25179-37): Dialog instance `25179:44`, Body Slot `I25179:44;24039:430`, nested Cropper instance `25179:101`. The regular example uses the medium Dialog source `24036:292`; it does not claim mobile authoring completeness.

## Actions and focus

Use the Dialog's existing labeled primary action for **confirming the proposed crop** and a safe secondary **cancel**. Confirm only after an image and valid crop exist. Do not conflate confirming the crop with successful network upload; transfer timing and persistence belong to the consuming product.

Closing, Escape and Cancel must use Dialog's single safe-exit path, including its unsaved-changes guard when appropriate; backdrop click does not dismiss by default. Focus moves inside on open, remains contained, and returns to the invoking control on exit or a logical survivor when necessary. The Cropper viewport and Zoom Slider own their respective visible-focus indicators according to the shared Focus Management contract.

## Open questions

- Is a changed crop considered dirty, and does abandoning it require confirmation in each product flow?
- Does crop confirmation commit a local preview, return transformation metadata, produce a new binary, or initiate upload? **No default is asserted here.**
- Narrow/mobile layout, constrained height/overflow, and gesture behavior are not yet demonstrated in Figma; resolve before design handoff.
- Crop failure/retry and whether the Dialog remains open on image processing failure require product/runtime evidence.
