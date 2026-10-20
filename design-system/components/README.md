# Components

Component documents are **decision contracts**, not complete copies of Figma or code.

A component page should answer, as briefly as the component allows:

1. What is it for?
2. When should it be used or avoided?
3. What meaningful choices/variants exist?
4. What non-obvious behavior and states matter?
5. What composition/content constraints matter?
6. What accessibility behavior is specific to this component?
7. What is still unsupported or unresolved?
8. Where are the live Figma and code/Storybook sources?

## Documentation depth

Use complexity-driven depth:

```text
Simple/native component
→ compact contract

Stateful/native-based component
→ add meaningful state and validation behavior

Composite/custom component
→ document the full interaction/focus/keyboard contract
```

Do not fill sections mechanically when they add no decision value.

## Keep out of the component page by default

- generated prop/API tables;
- every Figma property and permutation;
- raw token-value catalogs;
- obvious pixel values already owned by tokens/Figma;
- implementation test code;
- completed migration history.

Reference the live source instead.

Existing long-form component documents can be simplified opportunistically when they are next reviewed; no bulk rewrite is required solely for consistency.
