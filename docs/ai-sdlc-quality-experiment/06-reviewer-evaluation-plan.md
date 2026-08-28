# AI Reviewer Evaluation Plan

## Purpose

Evaluate Dev Reviewer and QA Reviewer as systems under test.

The objective is not to prove that one model is universally better. The objective is to measure performance under controlled repository-specific conditions.

## Evaluation Dataset

Create controlled PRs containing known issues.

Suggested cases:

- missing validation;
- regression;
- incorrect API contract;
- weak assertion;
- misleading automated test;
- missing error handling;
- UI deviation;
- scope creep;
- false-positive case.

Each case must have a ground-truth expected finding.

## Reviewer Inputs

The reviewer should receive the same normal context available in production-like operation:

- Story;
- relevant repository context;
- changed files/diff;
- AGENTS.md;
- applicable skills;
- test results;
- implementation evidence.

Do not expose the ground-truth defect catalog.

## Evaluation Criteria

### Detection

Did the reviewer identify the known problem?

### Evidence

Did the reviewer cite concrete code, test, requirement or repository evidence?

### Correctness

Is the finding technically and functionally correct?

### Severity

Is the severity reasonable?

### Actionability

Does the recommendation explain what should be investigated or changed?

### False Positives

Did the reviewer report a problem that is not actually a defect?

### Duplication

Did the reviewer report the same underlying issue multiple times?

## Finding Format

Recommended reviewer finding:

| Field | Value |
| --- | --- |
| Severity | `BLOCKER / MAJOR / MINOR / OBSERVATION` |
| Location | |
| Finding | |
| Evidence | |
| Risk / Impact | |
| Recommendation | |

## Model Comparison

If different models are evaluated, keep the experiment conditions as equal as possible.

Record:

- model;
- model/version if available;
- prompt/instructions version;
- skills version;
- repository commit;
- PR;
- date;
- findings.

Compare:

- detection rate;
- precision;
- false positives;
- severity accuracy;
- evidence quality;
- actionability;
- consistency.

Do not conclude that a model is better based on a single PR.

## Quality Gate

A reviewer should not be considered successful merely because it found many issues.

A high-quality reviewer should:

- detect meaningful defects;
- avoid unsupported findings;
- provide evidence;
- distinguish severity appropriately;
- avoid noise;
- remain consistent across similar cases.

## Human Validation

Human review remains the final authority for evaluating reviewer findings.
