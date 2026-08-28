---
name: qa-analysis
description: Analyze Story risk using approved requirements and current system evidence, define verification strategy, assess existing test coverage and regression impact, determine automation needs, and establish a risk-based QA Quality Contract.
argument-hint: "[Story]"
---

# QA Analysis

Use this skill when analyzing the quality risks and verification needs of the current Story.

## Inputs

Base the analysis on all relevant available evidence:

- approved business requirements and Acceptance Criteria;
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
3. Inspect relevant existing code and tests.
4. Identify existing verification coverage.
5. Identify critical behavior and failure impact.
6. Identify relevant business and technical risks.
7. Apply relevant QA heuristics.
8. Map risks to verification targets.
9. Select the lowest effective test level for each target.
10. Determine which verification should be automated.
11. Assess regression impact and define regression scope.
12. Define required manual verification where automation is insufficient.
13. Define the QA Quality Contract.
14. Define the risk-based quality gate.
15. Identify open questions, coverage gaps and unresolved risks.

## Existing Implementation Analysis

Review relevant existing implementation to understand the actual system behavior and potential impact of the Story.

Consider:

- affected components;
- shared components;
- existing validation;
- business rules implemented in code;
- state transitions;
- error handling;
- integration points;
- consumers of changed behavior.

Use code as evidence of current system behavior, not as a replacement for approved business requirements.

Do not perform a full code review.

Do not prescribe implementation changes.

If the implementation contradicts the approved requirements, identify the discrepancy and record it as a finding requiring review.

## Existing Test Analysis

Before defining new verification, inspect relevant existing tests.

Determine:

- which Acceptance Criteria are already covered;
- which risks are already covered;
- which test levels are represented;
- which tests are affected by the Story;
- which tests should be updated;
- which tests remain sufficient;
- which coverage gaps exist;
- whether relevant tests are stable and deterministic.

Do not create duplicate tests when existing tests provide sufficient confidence.

Existing tests are evidence of coverage, not proof that the behavior is correct.

## Coverage Gaps

Identify meaningful gaps between:

Approved behavior
→ Identified risks
→ Existing verification
→ Required verification

For each gap determine whether:

- an existing test should be updated;
- a new test is required;
- another verification method is more appropriate;
- no additional verification is necessary because the risk is sufficiently covered.

Do not require coverage solely for the purpose of increasing test count.

## Risk Analysis

Start from behavior and consequences, not from test count.

For each relevant risk consider:

- affected behavior;
- potential impact;
- likelihood;
- detectability where useful;
- existing coverage;
- verification required;
- appropriate test level.

Prioritize verification according to risk.

Do not require identical coverage for every Story.

Do not turn hypothetical risks into mandatory requirements without evidence.

## Verification Targets

Verification targets should describe behavior or system properties that require confidence.

Examples include:

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

Select a higher-level test when lower-level verification cannot provide sufficient confidence.

Use E2E primarily for critical user journeys or cross-component behavior that cannot be effectively verified at a lower level.

Every selected test level should have a reason.

## Automation Strategy

Determine whether verification should be automated based on:

- risk;
- repeatability;
- regression value;
- stability;
- maintenance cost;
- execution frequency;
- appropriate test level;
- existing automation.

Prefer extending reliable existing automation over creating duplicate coverage.

Automation is not required simply to increase test count.

Do not prescribe implementation details that belong to Developers.

## Regression Analysis

Analyze regression impact before defining regression scope.

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
- what additional regression verification is required.

Regression scope must be proportional to risk.

Do not execute or require a full regression suite by default.

## Regression Scope

Define the minimum effective regression verification.

Use:

| Area / Flow | Existing Coverage | Regression Risk | Required Verification |
|---|---|---|---|
| | | `LOW / MEDIUM / HIGH` | |

If no additional regression verification is required, state why.

## Manual Verification

Define manual verification when:

- automation cannot provide sufficient confidence;
- usability or visual behavior is relevant;
- exploratory investigation is required;
- a risk is better assessed manually.

Do not require manual verification when automated evidence provides sufficient confidence for the identified risk.

## QA Quality Contract

Define the minimum verification required for the Story.

Use:

| Area | Definition |
|---|---|
| Required verification | |
| Required automation | |
| Required manual verification | |
| Quality gate | |

The Quality Contract must be traceable to identified risks and existing coverage.

The quality gate must be proportional to the risk.

## Evidence

Verification decisions must be supported by available evidence.

Relevant evidence may include:

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
