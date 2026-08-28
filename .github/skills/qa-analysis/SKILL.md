---
name: qa-analysis
description: Analyze Story risk using approved requirements and current system evidence, assess existing test coverage and regression impact, define verification strategy and automation needs, and establish a risk-based QA Quality Contract.
argument-hint: "[Story]"
---

# QA Analysis

Use this skill to perform the detailed QA analysis for the current Story.

## Inputs

Base the analysis on relevant evidence:

- approved business requirements and Acceptance Criteria;
- approved UI Design Artifact, when the Story affects user-facing UI;
- approved BA analysis;
- approved System Analyst analysis;
- current system behavior;
- relevant source code;
- existing automated and manual tests;
- existing test coverage;
- previous defects when available;
- relevant documentation.

Do not rely on the Story in isolation.

## Analysis Flow

Follow this sequence:

1. Understand the approved business behavior.
2. Understand the affected system behavior and components.
3. Inspect relevant existing implementation, tests, and UI Design Artifact when applicable.
4. Inspect relevant existing implementation and tests.
5. Assess existing verification coverage.
6. Identify critical behavior and failure impact.
7. Identify relevant business and technical risks.
8. Apply relevant QA heuristics.
9. Map risks to verification targets.
10. Select the lowest effective test level for each target.
11. Determine automation needs.
12. Assess regression impact and define regression scope.
13. Define required manual verification where appropriate.
14. Define the QA Quality Contract.
15. Define the risk-based quality gate.
16. Record coverage gaps, open questions, and unresolved risks.

## Existing Implementation Analysis

Review relevant implementation to understand current behavior and potential impact.

Consider:

- affected components;
- shared components;
- existing validation;
- business rules implemented in code;
- state transitions;
- error handling;
- integration points;
- consumers of changed behavior.

Use code as evidence of current behavior, not as a replacement for approved requirements.

Do not perform a full code review or prescribe implementation changes.

If implementation contradicts approved requirements, identify the discrepancy and mark it for review.

## Existing Test Analysis

Inspect relevant tests before defining new verification.

Determine:

- which Acceptance Criteria are covered;
- which risks are covered;
- which test levels are represented;
- which tests are affected;
- which tests should be updated;
- which tests remain sufficient;
- which coverage gaps exist;
- whether relevant tests are reliable and deterministic.

Do not duplicate sufficient existing coverage.

Existing tests are evidence of coverage, not proof that behavior is correct.

## Coverage Gaps

Analyze the gap between:

Approved behavior
→ Identified risks
→ Existing verification
→ Required verification

For each meaningful gap determine whether:

- an existing test should be updated;
- a new test is required;
- another verification method is more appropriate;
- no additional verification is necessary.

Do not require coverage solely to increase test count.

## Risk Analysis

Start from behavior and consequences, not test count.

For each relevant risk consider:

- affected behavior;
- potential impact;
- likelihood;
- existing coverage;
- verification required;
- appropriate test level.

Prioritize verification according to risk.

Do not turn hypothetical risks into mandatory requirements without evidence.

## Verification Targets

Define behavior or system properties that require confidence.

Examples:

- critical business flows;
- business rules;
- validation;
- error handling;
- state transitions;
- API behavior;
- data integrity;
- integration points;
- regression-sensitive behavior.

Each important risk should have an explicit verification target or a documented reason why no additional verification is required.

## Test Level Selection

Prefer the lowest effective test level.

Consider:

- unit;
- component;
- API;
- integration;
- E2E;
- manual verification.

Use a higher-level test when lower-level verification cannot provide sufficient confidence.

Use E2E primarily for critical user journeys or cross-component behavior that cannot be effectively verified lower in the stack.

Every selected level should have a reason.

## Automation Strategy

Determine automation needs based on:

- risk;
- repeatability;
- regression value;
- stability;
- maintenance cost;
- execution frequency;
- appropriate test level;
- existing automation.

Prefer extending reliable existing automation over duplicate coverage.

Automation is not required simply to increase test count.

Do not prescribe implementation details.

## Regression Analysis

Analyze what could regress before defining regression scope.

Consider:

- changed components;
- shared components;
- consumers of changed behavior;
- changed business rules;
- changed APIs;
- changed data behavior;
- critical user journeys;
- existing regression coverage;
- previous defects;
- known fragile areas.

Determine:

- what could regress;
- why it could regress;
- what existing tests provide confidence;
- what additional verification is required.

Do not require full regression by default.

## Regression Scope

Define the minimum effective regression verification.

Use:

| Area / Flow | Existing Coverage | Regression Risk       | Required Verification |
| ----------- | ----------------- | --------------------- | --------------------- |
|             |                   | `LOW / MEDIUM / HIGH` |                       |

If no additional regression verification is required, state why.

## Manual Verification

Define manual verification when:

- automation cannot provide sufficient confidence;
- usability or visual behavior is relevant;
- exploratory investigation is required;
- a risk is better assessed manually.

Do not require manual verification when existing automated evidence provides sufficient confidence.

## QA Quality Contract

Define the minimum verification required for the Story.

Use:

| Area                         | Definition |
| ---------------------------- | ---------- |
| Required verification        |            |
| Required automation          |            |
| Required manual verification |            |
| Quality gate                 |            |

The Quality Contract must be traceable to identified risks and existing coverage.

The quality gate must be proportional to the risk.

## Evidence

Support verification decisions with available evidence:

- requirements;
- BA analysis;
- System Analyst analysis;
- source code;
- existing tests;
- test coverage;
- previous defects;
- CI results;
- automated test results;
- manual verification results.

A passing test suite is evidence, not proof that the software is defect-free.

## Open Questions

Mark missing information as:

OPEN

For significant decisions provide:

- question;
- why it matters;
- reasonable alternatives;
- recommendation.

Do not silently resolve ambiguity.

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

Do not present an inference or proposal as an approved decision.

## Boundary

This skill defines:

WHAT needs to be verified

WHY it needs to be verified

WHAT existing evidence already provides confidence

WHERE coverage gaps exist

AT WHICH LEVEL verification should occur

WHETHER automation is appropriate

WHAT regression scope is required

WHAT quality gate is required

It does not define:

HOW tests are implemented

Test implementation belongs to the relevant Developer or dedicated test implementation activity.
