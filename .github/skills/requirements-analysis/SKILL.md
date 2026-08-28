---
name: requirements-analysis
description: Analyze business requirements and refine a Story into clear, observable and testable business behavior without introducing technical implementation.
argument-hint: "[Story]"
---

# Requirements Analysis

Use this skill when analyzing or refining business requirements and
Acceptance Criteria.

## Analysis Flow

Follow this sequence:

1. Identify the business goal and expected business value.
2. Identify the actor or user affected by the requirement.
3. Identify the trigger or condition that starts the behavior.
4. Define the expected business outcome.
5. Identify applicable business rules.
6. Define what is in scope.
7. Define what is explicitly out of scope.
8. Identify business dependencies.
9. Identify exceptions, ambiguity and missing information.
10. Validate the Acceptance Criteria against the identified behavior.

## Requirement Quality

For each requirement and Acceptance Criterion, verify:

- the expected behavior is observable;
- the expected outcome is clear;
- the relevant condition or trigger is clear;
- the behavior can be tested without knowing the implementation;
- business rules are explicit;
- scope is unambiguous;
- dependencies are identified;
- conflicting requirements are identified.

## Acceptance Criteria

Acceptance Criteria should:

- describe observable business behavior;
- represent business intent;
- be independently understandable;
- be testable;
- avoid implementation details.

When an Acceptance Criterion is ambiguous or incomplete, identify the
specific missing information rather than inventing expected behavior.

## Scope

Explicitly distinguish:

```text
IN SCOPE:
...

OUT OF SCOPE:
...
```
