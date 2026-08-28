---
name: frontend-implementation
description: Implement approved frontend behavior from the Story and Implementation Map using the existing frontend architecture, conventions and APIs without inventing product behavior.
argument-hint: "[Story]"
---

# Frontend Implementation

Use this skill when implementing frontend changes assigned to `FE`.

## Inputs

Use:

- approved Story;
- approved Acceptance Criteria;
- approved System Analyst analysis;
- approved Implementation Map;
- approved QA Quality Contract;
- approved UI Design Artifact when applicable;
- existing frontend source code;
- existing frontend tests;
- frontend documentation;
- repository conventions.

Treat approved requirements and decisions as the source of product behavior.

## Implementation Flow

1. Inspect the relevant existing frontend code before changing it.
2. Identify the components, routes, state, services and dependencies affected by the Implementation Map.
3. Understand existing conventions and reusable patterns.
4. Identify the smallest maintainable implementation that satisfies the approved behavior.
5. Implement only the frontend changes assigned to `FE`.
6. Integrate with approved API contracts and existing frontend abstractions.
7. Preserve existing behavior outside the approved Story scope.
8. Run relevant frontend checks.
9. Review the resulting diff for unintended changes.
10. Record implementation evidence and deviations.

## Existing Code

Prefer existing:

- components;
- hooks;
- services;
- state management;
- routing;
- validation patterns;
- error handling;
- styling conventions;
- test utilities.

Do not introduce a new pattern when an appropriate existing pattern already exists without a justified reason.

Do not refactor unrelated code.

## Scope

The Implementation Map is the boundary of frontend work.

If implementation reveals that another component, service or backend change is required:

- stop the affected work;
- record the issue as `OPEN`;
- explain the impact;
- request human review.

Do not silently expand the Story scope or modify the Implementation Map.

## API Integration

Use only approved API behavior and contracts.

If the existing API differs from the approved contract:

- do not invent a new contract;
- do not silently adapt the product behavior;
- record the mismatch as `OPEN`;
- explain the impact;
- request human review.

Use existing frontend API integration patterns where appropriate.

## UI Boundary

When a UI Design Artifact is provided:

- treat the approved artifact as the source of UI/UX requirements;
- implement the defined layout, components, states and interactions;
- preserve the approved behavior;
- do not introduce intentional UX changes without human approval.

If the design is ambiguous, incomplete or conflicts with approved business/system requirements:

- do not guess;
- record the issue as `OPEN`;
- request human review.

Do not treat the UI Design Artifact as authorization to change business behavior.

## Code Quality

The implementation should:

- follow repository conventions;
- remain maintainable;
- avoid unnecessary abstraction;
- avoid duplicated logic where an existing abstraction is appropriate;
- preserve type safety;
- handle relevant loading, success and error states;
- avoid unrelated refactoring.

Choose the simplest implementation that satisfies the approved requirements.

## Documentation

Identify whether implementation requires documentation changes.

Use:

NO_CHANGE

UPDATE_EXISTING

NEW_DOCUMENT

Do not document unapproved behavior.

## Evidence

Record evidence for:

- implemented frontend changes;
- relevant checks;
- test execution;
- build or static checks;
- deviations and limitations.

Never claim a check passed unless it actually ran.

## Boundary

This skill defines how to implement approved frontend behavior.

It does not define:

- business requirements;
- system architecture;
- UX/design decisions;
- QA verification strategy;
- backend implementation.

Those concerns belong to the relevant role or artifact.
