# Quality Reporting and Dashboard

## Purpose

Present the results of the AI-SDLC quality experiment in a form that demonstrates both application quality and process effectiveness.

## Dashboard Sections

### Executive Summary

Show:

- total known defects;
- detected defects;
- missed defects;
- detection rate;
- defects escaping the quality gate;
- average/median TTD;
- average/median TTF.

### Detection by Stage

Display the number of defects first detected by:

- BA;
- SA;
- QA;
- developer tests;
- Dev Reviewer;
- QA verification;
- QA Reviewer;
- CI;
- logs;
- E2E;
- post-gate.

### Detection by Category

Group defects by:

- validation;
- business logic;
- API;
- integration;
- UI;
- regression;
- data/persistence;
- test quality;
- other.

### Severity Distribution

Show:

- Critical;
- Major;
- Minor.

Compare injected severity with detected severity where relevant.

### AI Reviewer Performance

Separate:

#### Dev Reviewer

- detection rate;
- precision;
- false positives;
- severity accuracy;
- missed known defects.

#### QA Reviewer

- detection rate;
- precision;
- false positives;
- severity accuracy;
- missed known defects.

### Escaped Defects

For every escaped defect show:

- defect ID;
- severity;
- where it escaped;
- where it was eventually detected;
- why earlier stages did not detect it;
- corrective action.

## Trend Reporting

As the experiment grows, compare:

- experiment run;
- defect category;
- reviewer/model version;
- detection stage;
- detection rate;
- false positive rate.

Do not compare results across materially different experiment conditions without documenting the difference.

## Defect Detail

Every known defect should be drillable to:

`Defect → Story → PR → evidence → detection → fix → verification`

## Presentation Goal

The report should answer:

1. What defects were introduced?
2. Which were detected?
3. Where were they detected?
4. Which were missed?
5. How reliable were the AI reviewers?
6. What did the logs and CI tell us?
7. What weaknesses exist in the SDLC?
8. What changed after process improvements?
