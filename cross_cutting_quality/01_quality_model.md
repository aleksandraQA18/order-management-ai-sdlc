# Cross-Cutting Quality Model

Quality Engineering applies to EVERY story.

## Flow

``` text
Business
  ↓
System Analysis
  ↓
QA Risk Analysis
  ↓
Test Design
  ↓
Development
  ↓
Automation
  ↓
CI
  ↓
Quality Gate
  ↓
QA Review
```

## QA Contract

For every story QA should define: - critical business behavior - risks -
verification targets - appropriate test levels - automation
expectations - regression impact - security considerations - quality
gate

## Core Principle

The QA artifact describes **what must be proven and why**, not how the
developer should write the code.

## Developer Agent

May choose: - framework implementation details, - fixture structure, -
helper design, - test code organization, provided the quality contract
is satisfied.

## QA Agent

Must challenge: - missing coverage, - weak assertions, - incorrect test
level, - duplicated tests, - flaky design, - unjustified E2E tests, -
requirements ambiguity, - untested critical risks.

## Evidence

A story is not quality-complete because tests exist. It is
quality-complete when the required evidence exists and the quality gate
passes.
