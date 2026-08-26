# DevOps Infrastructure Plan --- Order Management AI SDLC

## Goal

Create a reproducible developer and CI environment in which every merge
is automatically verified.

## Target Infrastructure

``` text
GitHub Repository
      |
      +-- Pull Request
      |      |
      |      +-- lint/typecheck
      |      +-- build
      |      +-- API tests
      |      +-- E2E tests
      |      +-- reports
      |      |
      |      +-- required status checks
      |
      +-- merge to main
             |
             +-- full regression
             +-- artifacts
             +-- quality gate
```

## Phase 1 --- GitHub Repository

Create: - repository - `main` protected branch - feature branches - pull
requests - CODEOWNERS later if useful

Recommended branch naming: - `feature/ORD-003-create-order` -
`fix/ORD-004-validation` - `test/ORD-003-api-tests`

Commit style should be clear and small.

## Phase 2 --- Local Docker

Create Docker Compose for: - frontend - backend - PostgreSQL

Requirements: - environment variables from `.env` - `.env.example`
committed - no secrets in Git - health checks where useful -
deterministic startup - documented commands

Example target:

``` bash
docker compose up --build
```

## Phase 3 --- Test Execution Locally

Document one-command execution for: - API tests - E2E tests - full suite

The same commands should be usable in CI.

## Phase 4 --- GitHub Actions

Create separate workflows if that improves clarity:

### `ci-pr.yml`

Runs on pull requests.

Suggested jobs: 1. backend-checks 2. frontend-checks 3. api-tests 4.
e2e-tests 5. publish-test-results

### `regression.yml`

Runs after merge to `main`.

Suggested jobs: 1. build 2. deploy/start test environment 3. full API
suite 4. full E2E suite 5. publish artifacts 6. quality gate

## Phase 5 --- Quality Gate

Make PR checks required in GitHub branch protection.

At minimum: - backend check - frontend check - API test - E2E test where
applicable

A PR cannot merge when required checks fail.

## Phase 6 --- Test Reports

Store as GitHub Actions artifacts: - Playwright HTML report -
JUnit/compatible report if configured - screenshots - traces for
failures

Do not commit generated reports to the repository.

## Phase 7 --- Secrets

Use GitHub Actions Secrets/Variables for CI-specific values.

Never commit: - passwords - tokens - private keys - production
credentials

## Phase 8 --- Database

CI should create a clean PostgreSQL environment for tests.

Preferred initial approach: - ephemeral PostgreSQL service/container per
workflow - migrations run automatically - deterministic seed data - test
cleanup/reset strategy

Avoid sharing a persistent test database between independent CI runs.

## Phase 9 --- Parallelism

Do not optimize for parallel execution until tests are stable.

First: - deterministic - isolated - reproducible

Then optimize duration.

## Phase 10 --- Security Baseline

Later add: - dependency audit - secret scanning - basic SAST if useful -
basic DAST/security smoke tests

Do not turn security tooling into the first infrastructure milestone.

## Suggested CI Evolution

### v0

Build + lint + typecheck.

### v1

API tests.

### v2

Playwright E2E.

### v3

Dockerized CI environment.

### v4

Required PR checks.

### v5

Post-merge full regression.

### v6

Reports + traces + quality metrics.

### v7

Security checks.

## Infrastructure Definition of Done

-   fresh clone can run locally
-   Docker environment starts reproducibly
-   tests run locally with documented commands
-   PR automatically runs checks
-   required checks block merge
-   merge to main triggers regression
-   test reports are retained
-   secrets are not stored in repository
-   CI uses isolated test data
-   failures are diagnosable from artifacts
