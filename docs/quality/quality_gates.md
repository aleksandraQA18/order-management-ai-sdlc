# Quality Gates

## Goal

Prevent a merge from being considered complete without sufficient
automated evidence.

## Pull Request Gate

Every PR should run at minimum: 1. backend checks 2. frontend checks 3.
API tests relevant to changed scope 4. E2E tests relevant to changed
scope where applicable 5. test report generation

## Required Gate Conditions

-   build succeeds
-   required automated tests pass
-   no critical test failures
-   no lint/type-check failures
-   test artifacts are retained
-   no known blocker/high-severity issue introduced without explicit
    decision

## Merge Gate

The default branch must require the CI workflow to pass before merge.

## Post-Merge Gate

Every merge to the main branch triggers the full regression suite.

## Nightly / Extended Gate

Optional later: - broader E2E suite - security smoke tests -
dependency/security checks - flaky test detection

## Important

Do not start with dozens of gates. Add them as the project grows.

## Future Quality Metrics

-   pass rate
-   flaky test rate
-   test duration
-   escaped defects
-   critical risk coverage
-   change failure rate
-   mean time to feedback
