---
name: frontend-ui-implementation
description: Implement UI behavior from an approved Design Artifact while preserving business and system constraints.
argument-hint: "[Story with UI Design Artifact]"
---

# Frontend UI Implementation

Use only when the Story has an approved UI Design Artifact.

## Flow

1. Inspect the Design Artifact.
2. Identify defined screens, states, interactions, responsive behavior, and relevant accessibility requirements.
3. Inspect existing design-system components and reuse them where appropriate.
4. Implement only specified UI behavior.
5. Validate defined states and interactions.
6. Report material visual or behavioral deviations.

## Boundaries

- The Design Artifact does not override approved business or system requirements.
- Do not invent unspecified UI behavior.
- Do not redesign the product.
- Do not introduce a new design-system pattern when an existing one is suitable.
- Do not perform a separate accessibility or visual-design audit unless assigned.
- Report conflicts between design, requirements, and existing constraints as `OPEN`.

## States

When defined or required by approved behavior, account for relevant:

- loading;
- success;
- empty;
- validation/error;
- disabled;
- responsive states.

Do not invent additional product behavior.

## Output

Report briefly:

- UI behavior implemented;
- relevant validation;
- material deviations or `OPEN` issues.

Do not add unrelated analysis.
