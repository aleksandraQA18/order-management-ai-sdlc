---
name: frontend-implementation
description: Implement approved frontend behavior using existing project patterns and the smallest safe change.
argument-hint: "[Story]"
---

# Frontend Implementation

Implement only the approved FE scope.

## Flow

1. Read approved BA/SA requirements and relevant contracts.
2. Inspect affected frontend code.
3. Search for reusable components, hooks, services, utilities, and API clients.
4. Identify the smallest safe change.
5. Implement using existing project patterns.
6. Run relevant validation.
7. Review the diff for scope and unintended changes.

## API Boundary

Use only approved API/system contracts.

Do not guess:

- endpoints;
- methods;
- request/response fields;
- status codes;
- error payloads;
- state transitions.

If required contract information is missing or conflicting, report `OPEN`.

## Reuse

Before creating a new component, hook, service, utility, or API client, search for an existing equivalent.

Prefer reuse or extension when it preserves current architecture and behavior.

## Scope

- Do not modify backend behavior.
- Do not add unrelated refactoring.
- Do not change approved requirements.
- Do not invent behavior.
- Prefer the smallest safe change over broad cleanup.

## Validation

Run only relevant checks for the changed frontend code.

Never weaken, remove, or bypass a failing check merely to obtain a passing result.

## Output

Report briefly:

- implemented changes;
- tests/checks run and result;
- `OPEN` issues or deviations.

Do not add unrelated documentation or analysis.
