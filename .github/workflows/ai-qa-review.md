---
name: AI QA Reviewer
description: Run the repository QA Reviewer on pull requests and publish a non-blocking GitHub review.
on:
  pull_request:
    types: [opened, synchronize, reopened]

engine:
  id: codex

model: gpt-5.4

permissions:
  contents: read
  pull-requests: read

imports:
  - .github/agents/qa-reviewer.agent.md

safe-outputs:
  submit-pull-request-review:
    max: 1
    allowed-events: [COMMENT]
  create-pull-request-review-comment:
    max: 10
---

# QA Reviewer CI

Review the current pull request using the imported QA Reviewer agent.

## Review Context

Treat the following as the primary review evidence:

1. The current pull request diff.
2. The Story being implemented.
3. Approved Acceptance Criteria.
4. Approved QA Quality Contract.
5. Approved System Analysis and Implementation Map.
6. Existing tests and changed tests.
7. Available CI/test evidence.

The repository is the source of truth for locating the relevant Story and approved analysis artifacts.

Before recommending additional verification, search for existing evidence and tests. Do not recommend a test simply because an equivalent test is not obvious from the changed files.

Do not infer missing requirements. If required context cannot be found, report an evidence gap rather than inventing it.

## Output Rules

- This is a non-blocking review.
- Never approve the pull request.
- Never request changes.
- Submit at most one GitHub review with event `COMMENT`.
- Create inline comments only for meaningful findings tied to changed lines.
- Distinguish findings, quality risks, learning notes and false positives/non-issues.
- Do not label a test flaky without evidence or a credible mechanism.
- Use the Test Pyramid as a heuristic, not a fixed ratio.
- Do not create comments for stylistic preferences or speculative issues.
- Keep the review concise and educational.
- If there are no meaningful findings, say so explicitly in the review summary.
