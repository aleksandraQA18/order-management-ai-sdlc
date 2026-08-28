# Defect Catalog

This document is the ground truth for controlled defect injection experiments.

## Rules

- Each defect has a unique ID.
- Keep this catalog separate from normal agent context when evaluating detection.
- Do not disclose expected detection results to the agents being evaluated.
- Do not change the expected behavior after detection unless the experiment itself changes.
- Record evidence for every detection claim.

## Defect Template

### DEF-XXX — [Short Name]

| Field | Value |
| --- | --- |
| Category | |
| Severity | `Critical / Major / Minor` |
| Layer | `FE / BE / API / Integration / E2E / Cross-cutting` |
| Component | |
| Introduced in | |
| Status | `PLANNED / INJECTED / DETECTED / FIXED / VERIFIED` |

### Expected Behavior

...

### Injected Incorrect Behavior

...

### Injection Point

...

### Expected Detection Opportunities

| Stage | Expected to detect? | Rationale |
| --- | --- | --- |
| BA | `YES / NO` | |
| SA | `YES / NO` | |
| QA analysis | `YES / NO` | |
| Developer tests | `YES / NO` | |
| Dev Reviewer | `YES / NO` | |
| QA verification | `YES / NO` | |
| QA Reviewer | `YES / NO` | |
| CI | `YES / NO` | |
| Logs / observability | `YES / NO` | |
| E2E | `YES / NO` | |

### Actual Detection

| Event | Stage | Evidence | Timestamp | Finding ID |
| --- | --- | --- | --- | --- |
| | | | | |

### Fix

| Field | Value |
| --- | --- |
| Fix PR | |
| Fixed in commit | |
| Verification evidence | |
| Date fixed | |

### Experiment Notes

...

---

## Initial Defect Set

Start with a small, diverse set rather than maximizing defect count.

Recommended initial categories:

- validation defect;
- incorrect business rule;
- API contract defect;
- error-handling defect;
- regression defect;
- UI behavior/design deviation;
- persistence/data defect;
- insufficient or misleading automated test.

Do not inject multiple defects that are likely to be indistinguishable during detection until the basic experiment is working.
