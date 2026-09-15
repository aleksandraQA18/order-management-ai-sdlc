---
name: qa-analysis
description: Produce a concise, automation-first QA Analysis for the current Story and assess existing tests for reuse, extension, correction, or gaps.
argument-hint: "[Story]"
---

# QA Analysis

Produce the QA Analysis defined by the QA Agent.

## Analysis Flow

1. Read the approved BA Analysis and System Analysis.
2. Inspect the relevant implementation and existing tests.
3. Determine what existing tests already cover the Story.
4. Decide which existing tests should be reused, extended, updated, or left unchanged.
5. Identify missing material verification.
6. Choose the most valuable test levels.
7. Decide whether BDD adds communication value.
8. Define regression scope.
9. Define the minimum evidence required by the Quality Contract.

## BDD Scenarios

Use `bdd-scenarios` only when complex business behavior, multiple rules, exceptions, or decision paths make concrete examples useful for shared understanding.

BDD should describe WHAT the system does, not HOW it is implemented.

Do not generate BDD for simple behavior when ordinary verification scenarios are sufficient.

## Automation Tests

Prioritize:
- API tests for backend behavior and contracts;
- integration tests for cross-component behavior and persistence/data integrity;
- E2E only for meaningful user journeys or frontend integration.

For existing tests, explicitly classify relevant coverage as:
- `REUSE`
- `EXTEND`
- `UPDATE`
- `NO_CHANGE`
- `MISSING`

Only include classifications that matter to the current Story.

Include negative and boundary cases when they materially verify the requirements.

## Manual Tests

Include manual verification only when it provides evidence that automation cannot reasonably provide, such as:
- exploratory investigation;
- visual/usability behavior when relevant;
- environment-specific behavior;
- one-off checks that are not worth automating.

Do not invent manual tests just to have manual coverage.

## Test Strategy

Describe the verification approach, not the acceptance criteria again.

State:
- primary test level;
- supporting test levels;
- automation priority;
- whether manual testing adds value.

## Regression

Select the smallest existing behavior set that could realistically be affected.

## Quality Contract

Define the minimum evidence needed to say the Story is adequately verified.

It should answer:

> What must be true before QA can consider this Story verified?

Typical evidence:
- all material verification scenarios have evidence;
- required automated tests pass;
- relevant regression tests pass;
- no material QA gaps remain unresolved.

Do not use a fixed coverage percentage.

## Output

Produce exactly:

### BDD Scenarios
### Automation Tests
### Manual Tests
### Test Strategy
### Regression
### Quality Contract
