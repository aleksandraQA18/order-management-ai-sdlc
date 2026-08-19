# Story Lifecycle

```text
BACKLOG
  ↓
READY
  ↓
BA
  ↓
ARCHITECTURE / SA
  ↓
QA ANALYSIS
  ↓
READY FOR DEVELOPMENT
  ↓
DEVELOPER
  ↓
PR + CI
  ↓
QA REVIEW
  ↓
QUALITY GATE
  ↓
MERGE
  ↓
STAGING
  ↓
RELEASE
```

## Blocking Rule
An unresolved blocking question means `BLOCKED`. Do not guess.

## QA is Cross-Cutting
Every Story includes, as applicable:
- risk analysis
- verification strategy
- automation
- regression analysis
- security analysis
- quality gate
- QA review

Quality Engineering is not a separate feature.
