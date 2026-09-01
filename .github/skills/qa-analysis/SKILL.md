---
name: qa-analysis
description: Define the minimum risk-based verification strategy and Quality Contract for a Story across API, integration, and E2E levels.
argument-hint: "[Story]"
---

# QA Analysis

Convert approved requirements and system analysis into the minimum verification needed for sufficient quality confidence.

## Inputs

- approved BA Analysis and Acceptance Criteria;
- approved System Analyst Analysis;
- relevant UI Design Artifact;
- relevant implementation, tests, and CI evidence when available.

Read only what is relevant to the Story.

## Flow

1. Map Acceptance Criteria to observable behavior.
2. Identify material risks using impact and likelihood.
3. Define Verification Targets for behaviors/risks requiring evidence.
4. Select the lowest sufficient test level:
   - `API`: API behavior, validation, contracts, errors.
   - `INTEGRATION`: real infrastructure, persistence, service boundaries, cross-component behavior.
   - `E2E`: critical user journeys/cross-system behavior not sufficiently covered below.
5. Define minimum evidence and automation mode.
6. Derive focused regression scope from changed components, dependencies, contracts, and critical journeys.
7. Produce the Quality Contract.

## Risk Rules

Use `HIGH`, `MEDIUM`, or `LOW`, based on impact and likelihood.

Report only material risks. Keep rationale short and evidence-based.

## Verification Targets

Format:

`VT-XX: [observable behavior] | AC: [AC-XX] | Risk: [R-XX] | Level: [API/INTEGRATION/E2E] | Evidence: [minimum evidence]`

Create targets only where verification provides meaningful confidence.

## Test-Level Rules

Prefer the lowest sufficient level.

Use integration testing when real infrastructure behavior is part of the risk; use Testcontainers when appropriate.

Use E2E only for critical journeys or behavior that lower levels cannot sufficiently verify.

Do not repeat the same verification at multiple levels without a risk-based reason.

## Automation

For each target choose:
- `AUTOMATED`
- `MANUAL`
- `NOT_REQUIRED`

State only a short rationale. Do not prescribe framework-level implementation.

## Regression

Keep regression focused on changed behavior and its dependencies. Require full regression only when risk justifies it.

## BDD

BDD is optional. Use it only when examples materially clarify critical business behavior, high-risk rules, meaningful negative behavior, or important cross-component flows.

## Quality Contract

```text
## QA Quality Contract

### Verification Targets
- VT-01: ...

### Risk
- R-01: HIGH — ...

### Test Levels
- API: ...
- INTEGRATION: ...
- E2E: ...

### Required Evidence
- ...

### Regression Scope
- ...

### Quality Gate
- PASS criteria: ...
- FAIL criteria: ...
- OPEN conditions: ...
```

The Quality Contract defines minimum evidence, not every possible test.

## Output

Produce exactly:

```text
# QA Analysis

## Risks
- R-01: [LOW/MEDIUM/HIGH] — [short rationale]

## Verification Targets
- VT-01: [observable behavior] | AC: [AC-XX] | Risk: [R-XX] | Level: [API/INTEGRATION/E2E] | Evidence: [minimum evidence]

## Coverage Gaps
- [material gap, or None identified]

## Automation Strategy
- VT-XX: [AUTOMATED/MANUAL/NOT_REQUIRED] — [short rationale]

## Regression Scope
- [focused scope, or None beyond current verification]

## QA Quality Contract

### Verification Targets
- VT-01: ...

### Risk
- R-01: ...

### Test Levels
- API: ...
- INTEGRATION: ...
- E2E: ...

### Required Evidence
- ...

### Regression Scope
- ...

### Quality Gate
- PASS criteria: ...
- FAIL criteria: ...
- OPEN conditions: ...
```

Do not add sections.

## Constraints

- Start from approved requirements, not implementation assumptions.
- Do not redefine requirements or prescribe implementation.
- Do not invent risks, targets, or tests.
- Keep analysis minimal and proportional to risk.
