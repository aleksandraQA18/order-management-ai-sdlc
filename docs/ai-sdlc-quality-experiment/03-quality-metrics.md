# Quality Metrics

## Purpose

Measure both application quality and the effectiveness of the AI-SDLC process.

Metrics must be based on recorded evidence and the ground-truth defect catalog.

## Core Metrics

### Defect Detection Rate

`detected known defects / total known defects`

Report overall and by detection stage.

### Defect Escape Rate

`known defects not detected before the selected quality gate / total known defects`

Define the quality gate explicitly for every experiment.

### False Positive Rate

`invalid reviewer findings / total reviewer findings`

Apply primarily to AI reviewer evaluation.

### First Detection Stage

For each defect, record the first stage that identified it.

Possible stages:

- BA;
- SA;
- QA analysis;
- developer tests;
- Dev Reviewer;
- QA verification;
- QA Reviewer;
- CI;
- logs/observability;
- E2E;
- post-gate.

### Time to Detect (TTD)

`first detection timestamp - defect injection timestamp`

### Time to Fix (TTF)

`fix timestamp - first detection timestamp`

## Reviewer Metrics

Track separately for Dev Reviewer and QA Reviewer:

- known defects detected;
- known defects missed;
- false positives;
- severity accuracy;
- evidence quality;
- actionable findings;
- duplicate findings.

### Detection Rate

`known defects correctly detected / known defects applicable to reviewer`

### Precision

`valid findings / all reviewer findings`

### Severity Accuracy

Compare assigned severity with the ground-truth severity.

Do not treat severity mismatch as a defect miss unless the reviewer failed to identify the underlying problem.

## Coverage Metrics

Track:

- Acceptance Criteria covered;
- QA verification targets covered;
- regression risks covered;
- automated tests by level;
- meaningful coverage gaps.

Do not use test count as a proxy for quality.

## Process Metrics

Track:

- number of defects introduced;
- number detected before implementation;
- number detected during development;
- number detected by reviewers;
- number detected during QA;
- number escaping the quality gate;
- number requiring human intervention;
- number of `OPEN` decisions caused by ambiguous or conflicting inputs.

## Reporting Requirements

Every metric should be traceable to:

- Story;
- defect ID;
- PR/commit;
- test result;
- reviewer finding;
- log/evidence;
- timestamp.

Avoid metrics that cannot be reproduced from stored evidence.
