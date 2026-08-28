---
name: code-review
description: Critically review a pull request against approved requirements, architecture, implementation boundaries, tests and repository evidence. Produce evidence-based, actionable findings without implementing fixes.
argument-hint: "[Pull Request / Story]"
---

# Code Review

Use this skill when reviewing a developer Pull Request.

## Purpose

Evaluate whether the implementation is correct, appropriately scoped, maintainable and sufficiently verified.

The goal is not to find the largest possible number of comments.

The goal is to identify meaningful problems that are supported by evidence.

## Evidence Hierarchy

Evaluate the implementation in this order:

1. Approved business requirements and Acceptance Criteria.
2. Approved System Analyst analysis and Implementation Map.
3. Approved API and data contracts.
4. Existing architecture and repository conventions.
5. Existing and changed tests.
6. CI and other execution evidence.
7. General engineering principles.

Do not treat personal preference as a requirement.

## Review Process

For each significant change:

1. Understand the intended behavior.
2. Identify the evidence supporting that behavior.
3. Inspect the relevant implementation and surrounding code.
4. Inspect affected tests and existing coverage.
5. Consider how the change can be incorrect despite appearing to work.
6. Check boundaries, failure paths and existing behavior.
7. Check for regression risk.
8. Check whether the implementation introduces unnecessary complexity.
9. Determine whether a finding is supported by evidence.
10. Report only meaningful findings.

## Adversarial Review

Actively challenge the implementation.

Ask:

- What could make this implementation incorrect?
- Which approved requirement could be violated?
- What happens at meaningful boundaries?
- What happens with invalid input?
- What happens when a dependency fails?
- What existing behavior could regress?
- Is an assumption unsupported?
- Could the implementation create a data-integrity or security problem?
- Could the tests pass while the intended behavior is still broken?

Do not invent hypothetical problems without a credible mechanism or evidence.

## Scope Review

Check whether the PR:

- implements the approved Story;
- contains all required implementation changes;
- avoids unrelated changes;
- avoids speculative functionality;
- avoids silently changing approved contracts;
- respects the Implementation Map.

Flag scope creep when it has meaningful impact.

## Architecture Review

Check compatibility with:

- approved System Analysis;
- Implementation Map;
- existing architecture;
- established repository patterns.

Do not request refactoring solely because another design is personally preferred.

If the PR requires an architectural decision not covered by approved analysis, report the gap and request Human/appropriate-role review.

## Regression Review

Consider the impact on existing behavior.

Inspect:

- changed shared code;
- callers and consumers;
- state transitions;
- validation;
- error paths;
- contracts;
- persistence behavior;
- affected existing tests.

A regression finding should identify a plausible affected behavior and supporting evidence.

## Test Review

Review developer-owned unit/component tests for:

- meaningful behavior coverage;
- correct assertions;
- deterministic execution;
- appropriate isolation;
- appropriate test data;
- unnecessary mocking;
- missing important coverage.

Do not require tests merely to increase test count.

Do not replace QA-owned API, integration or E2E testing with developer tests.

## Finding Quality

A finding should normally contain:

- severity;
- location;
- problem;
- evidence;
- impact;
- recommendation.

Do not report a finding unless it is supported by code, requirements, tests, architecture or other available evidence.

Prefer a small number of high-value findings over a large number of speculative or stylistic comments.

## Severity

Use:

- `BLOCKER` — prevents safe merge or creates critical risk.
- `HIGH` — significant functional, security, data-integrity or regression risk.
- `MEDIUM` — meaningful defect or maintainability problem that should be addressed.
- `LOW` — limited impact issue with a concrete reason for change.
- `INFO` — useful observation that does not require a change.

Severity must reflect impact, not personal preference.

## False Positives

Before reporting a finding, challenge it:

- Is the behavior actually required?
- Is the behavior actually incorrect?
- Is there evidence?
- Could an existing contract intentionally allow it?
- Am I reporting a preference rather than a defect?

If evidence is insufficient, do not report the issue as a finding.

## Review Outcome

The reviewer may recommend:

- `APPROVE`
- `CHANGES_REQUESTED`
- `COMMENT`

The reviewer does not perform the fix.

The reviewer does not make final merge decisions.

Human approval remains authoritative.

## Escalation

Escalate when:

- requirements are ambiguous or conflicting;
- Implementation Map is insufficient;
- an API or data contract appears incorrect;
- an architectural decision is required;
- scope must change;
- evidence is insufficient to determine correctness.

Mark the issue as requiring Human or appropriate-role review rather than inventing a decision.

## Boundary

This skill does not:

- implement fixes;
- modify requirements;
- modify architecture;
- modify the Implementation Map;
- define QA strategy;
- implement API/integration/E2E tests;
- approve its own changes.
