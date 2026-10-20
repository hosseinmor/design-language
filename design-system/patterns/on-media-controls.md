---
id: design-system.pattern.on-media-controls
collection: design-system
type: pattern
title: On-Media Controls
summary: The current Core token model does not define dedicated Button tokens for
  image or video backgrounds.
knowledge_state: unverified
document_maturity: draft
related: []
design_status: provisional
source_guideline: button-guidelines-v0.6.md
---

# On-Media Controls

## Current Status

The current Core token model does not define dedicated Button tokens for image or video backgrounds.

`static-white` and `static-black` are not valid Core Button tokens in the current model.

## Temporary Rules

Until a formal On-media control pattern is approved:

- Place the Button on a scrim or filled chip with controllable contrast.
- Ghost is not allowed directly over media.
- Outline is allowed only with a scrim and after contrast testing.
- Do not automatically switch the Button color based only on image brightness.
- Manually test every instance that depends on media content.
- Focus must remain visible across both light and dark image regions.

## Token Rule

Do not introduce locally named Core tokens to solve individual media instances.

## Open Questions

- Whether On-media controls require dedicated formal tokens
- Whether media focus requires a two-layer focus ring
- How focus should remain stable over mixed light and dark content
