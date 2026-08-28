---
name: backend-implementation
description: Implement approved backend and service changes assigned to BE using the existing architecture, approved API contracts and Implementation Map.
argument-hint: "[Story]"
---

# Backend Implementation

Use this skill when implementing backend changes assigned to `BE`.

## Inputs

Use:

- approved Story;
- approved Acceptance Criteria;
- approved System Analyst analysis;
- approved Implementation Map;
- approved QA Quality Contract;
- existing backend/service source code;
- existing backend tests;
- relevant architecture and repository documentation;
- repository conventions.

Treat approved requirements and decisions as the source of backend behavior.

## Implementation Flow

1. Inspect the relevant existing backend code before changing it.
2. Identify affected services, modules, dependencies and boundaries.
3. Understand existing implementation and architectural conventions.
4. Identify the smallest maintainable implementation satisfying the approved behavior.
5. Implement only backend changes assigned to `BE`.
6. Integrate with approved API contracts.
7. Implement required business logic and error handling.
8. Apply approved data/persistence changes through the appropriate skill.
9. Preserve existing behavior outside the approved Story scope.
10. Run relevant backend checks.
11. Review the resulting diff for unintended changes.
12. Record implementation evidence and deviations.

## Existing Code

Prefer existing:

- services;
- modules;
- domain logic;
- repositories;
- validation;
- error handling;
- configuration;
- dependency patterns;
- test utilities.

Do not introduce a new pattern when an appropriate existing pattern already exists without a justified reason.

Do not refactor unrelated code.

## Scope

The Implementation Map is the boundary of backend work.

If implementation reveals that another component, frontend change or architectural change is required:

- stop the affected work;
- record the issue as `OPEN`;
- explain the impact;
- request human review.

Do not silently expand the Story scope or modify the Implementation Map.

## API Contracts

Implement only approved API behavior and contracts.

Verify:

- endpoint behavior;
- request handling;
- response behavior;
- validation;
- status codes;
- relevant error behavior.

If the existing API differs from the approved contract:

- do not invent a new contract;
- record the mismatch as `OPEN`;
- explain the impact;
- request human review.

Do not use this skill to define API tests. API test implementation remains outside the BE Developer scope.

## Business Logic

Implement approved business rules and invariants.

Do not infer new business behavior from implementation convenience.

If a rule is ambiguous or contradictory:

- do not guess;
- record the issue as `OPEN`;
- request human review.

## Error Handling

Preserve established error-handling patterns.

Ensure approved failure behavior is represented where required.

Do not expose internal implementation details or sensitive information through API errors.

Do not introduce generic error handling that hides meaningful failures.

## Dependencies

When adding or changing dependencies:

- prefer existing repository dependencies where suitable;
- avoid unnecessary dependencies;
- consider compatibility and maintenance impact;
- record meaningful dependency changes.

Do not introduce infrastructure changes outside the approved scope.

## Code Quality

The implementation should:

- follow repository conventions;
- remain maintainable;
- preserve type safety where applicable;
- minimize duplication;
- avoid unnecessary abstraction;
- avoid unrelated refactoring;
- preserve behavior outside the approved change.

Choose the simplest implementation that satisfies the approved requirements.

## Evidence

Record evidence for:

- implemented backend changes;
- relevant checks;
- unit tests;
- build/static checks where applicable;
- deviations and limitations.

Never claim a check passed unless it actually ran.

## Boundary

This skill defines how to implement approved backend behavior.

It does not define:

- business requirements;
- system architecture;
- API test strategy;
- integration/E2E test implementation;
- QA verification strategy;
- frontend implementation.
