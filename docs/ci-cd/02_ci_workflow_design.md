# CI/CD Workflow Design

## Workflow A --- Pull Request

Trigger: - `pull_request` to `main`

Stages:

``` text
Checkout
  ↓
Install dependencies
  ↓
Lint + typecheck
  ↓
Build
  ↓
Start test dependencies
  ↓
API tests
  ↓
E2E tests
  ↓
Upload reports
```

## Workflow B --- Main Regression

Trigger: - `push` to `main`

Stages:

``` text
Checkout
  ↓
Build
  ↓
Start isolated environment
  ↓
API regression
  ↓
E2E regression
  ↓
Upload reports
  ↓
Quality Gate
```

## Workflow C --- Optional Nightly

Trigger: - scheduled

Possible scope: - extended regression - security checks - dependency
checks - longer-running tests

## Failure Handling

When tests fail: - preserve report, - preserve screenshots/traces where
available, - expose failure in workflow summary, - fail the job.

Do not make the pipeline green by retrying failures indefinitely.

Retries should be limited and used only as a diagnostic/temporary
mechanism.

## Quality Principle

A green pipeline means the defined automated checks passed. It does not
mean the software is defect-free.

The QA agent remains responsible for interpreting evidence against
business risk.
