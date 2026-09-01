---
name: backend-implementation
description: Implement approved backend API, service, and application behavior using existing architecture and the smallest safe change.
argument-hint: "[Story]"
---

# Backend Implementation

Implement only the approved BE scope.

## Flow

1. Read relevant approved requirements, System Analysis, Implementation Map, and API contracts.
2. Inspect affected code and existing patterns.
3. Search for reusable services, repositories, schemas, validators, and utilities.
4. Make the smallest safe change.
5. Validate relevant behavior.
6. Review the final diff.

## API Contract

Do not guess or change endpoints, methods, request/response fields, status codes, validation, error payloads, or auth/authz behavior.

If required contract information is missing or conflicting, report `OPEN`.

## Business Logic

Implement approved business rules and invariants. Preserve established error-handling patterns and avoid leaking internal or sensitive details.

## Reuse

Search before creating new backend abstractions. Prefer reuse or extension when it preserves architecture and behavior.

## Dependencies

Avoid unnecessary dependencies. Add one only when materially required by the Story and compatible with the project.

## Scope

No frontend changes, unrelated refactoring, invented behavior, or unapproved contract/architecture changes.

## Validation

Run only relevant checks. Never bypass or weaken a failing check.

## Output

Report:
- changes;
- checks/tests and results;
- `OPEN` issues or deviations.
