---
name: ci-cd
description: Design and review GitHub Actions CI/CD pipelines, test execution, quality gates, artifacts, staging and release flow.
argument-hint: "[CI/CD task]"
---

# CI/CD

PR:
checkout → dependencies → lint/typecheck → build → API tests → required E2E → reports

Main:
merge → build artifact → staging → smoke → regression → release gate

Rules:
- fail loudly,
- preserve evidence,
- avoid unlimited retries,
- isolate test environments,
- enforce required checks through repository rules.
