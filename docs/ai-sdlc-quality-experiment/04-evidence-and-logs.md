# Evidence and Observability

## Purpose

Create a consistent evidence trail showing what happened during implementation, testing, review and defect handling.

## Evidence Sources

Use:

- Git commits;
- Pull Requests;
- GitHub review comments;
- CI workflow runs;
- automated test results;
- manual verification records;
- application logs;
- API responses;
- screenshots or UI evidence when relevant;
- defect records.

## Evidence Record

For every significant event record:

| Field | Value |
| --- | --- |
| Event ID | |
| Defect ID | |
| Story | |
| Stage | |
| Actor | `Human / BA / SA / QA / FE / BE / Dev Reviewer / QA Reviewer / CI / System` |
| Timestamp | |
| Result | `PASS / FAIL / FINDING / DECISION` |
| Evidence | |
| Related PR/commit | |

## Logging Principles

Application logs should help answer:

- what operation occurred;
- when it occurred;
- which component handled it;
- whether it succeeded or failed;
- what relevant error condition occurred;
- how the event can be correlated with a test or request.

Do not log secrets, passwords, tokens or unnecessary personal data.

## Defect Correlation

Where practical, correlate:

`Defect ID → Story → PR → commit → CI run → test → log event → reviewer finding → fix`

Do not put hidden ground-truth information into production-like logs if doing so would make the experiment invalid.

## Log Quality

A useful log should support diagnosis.

Avoid:

- generic `something went wrong`;
- sensitive data;
- excessive noise;
- logging only the final failure without useful context.

## Evidence Integrity

Never modify evidence to make an experiment appear successful.

If evidence is unavailable, record:

`EVIDENCE NOT AVAILABLE`

Do not infer successful detection from unrelated events.
