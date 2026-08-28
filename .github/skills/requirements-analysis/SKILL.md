---
name: requirements-analysis
description: Analyze business requirements and refine a Story into clear, observable and testable business behavior without introducing technical implementation.
argument-hint: "[Story]"
---

# Requirements Analysis

Use this skill when analyzing or refining business requirements and Acceptance Criteria.

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

When an Acceptance Criterion is ambiguous or incomplete, identify the specific missing information rather than inventing expected behavior.

## Scope

Explicitly distinguish:

IN SCOPE:
...

OUT OF SCOPE:
...

## Business Dependencies

Identify dependencies that affect business behavior or scope.

Consider:

- other business processes;
- dependent business rules;
- actors or roles;
- upstream or downstream business activities;
- prerequisites.

Do not introduce technical dependencies.

## Ambiguity and Conflicts

Identify:

- missing information;
- contradictory requirements;
- unclear terminology;
- undefined outcomes;
- unclear ownership or responsibility;
- assumptions that materially affect behavior.

Do not silently resolve ambiguity or conflicts.

Mark unresolved decisions as:

OPEN

For significant open decisions, provide:

- question;
- why it matters;
- reasonable alternatives;
- recommendation.

## Reasoning Classification

Clearly distinguish:

FACT:
...

INFERENCE:
...

PROPOSAL:
...

DECISION:
OPEN

Do not present an inference or proposal as an approved business decision.

## Traceability

Maintain traceability:

Business Requirement
→ Story
→ Business Rule
→ Acceptance Criterion

Acceptance Criteria must remain connected to the business requirement they verify.

If an Acceptance Criterion cannot be traced to an approved business requirement, identify the issue rather than inventing justification.

## Boundary

This skill defines:

- how business requirements are analyzed;
- how business behavior is clarified;
- how scope and dependencies are identified;
- how Acceptance Criteria are assessed.

It does not define:

- system architecture;
- APIs;
- database structures;
- implementation details;
- test implementation.

Those concerns belong to the relevant downstream role.
