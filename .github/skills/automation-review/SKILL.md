---
name: automation-review
description: Review automated tests for correctness, determinism, isolation, maintainability, assertions and appropriate test-level selection.
argument-hint: "[test file or test suite]"
---

# Automation Review

Check:
- correct test level,
- meaningful assertions,
- determinism,
- isolation,
- test-data management,
- readability,
- maintainability,
- failure diagnostics,
- appropriate reuse,
- no arbitrary sleeps,
- no hidden dependencies,
- no redundant coverage.

Red flags:
- weak assertions,
- excessive E2E,
- shared mutable data,
- retry masking,
- huge Page Objects,
- implementation-detail assertions.
