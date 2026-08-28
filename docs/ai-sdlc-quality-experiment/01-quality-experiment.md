# AI-SDLC Quality Experiment

## Purpose

This project is both:

1. an application development project;
2. a controlled experiment evaluating an AI-powered SDLC and its ability to prevent, detect, diagnose and report defects.

The application is the System Under Test (SUT). The SDLC process and its AI agents are the second subject of evaluation.

## Objectives

- Build the application through the defined AI-SDLC workflow.
- Introduce a controlled set of known defects.
- Preserve a private ground truth for those defects.
- Observe where and when defects are detected.
- Collect evidence from tests, CI, logs, GitHub reviews and reports.
- Measure defect detection effectiveness.
- Evaluate false positives and false negatives.
- Evaluate the quality of AI reviewer findings.
- Identify weaknesses in the SDLC process, not only in the application.

## Principles

### Ground truth

Every injected defect must have a unique identifier and a known expected behavior.

The agents being evaluated must not receive the ground-truth catalog as input during normal review.

### Controlled injection

Defects must be introduced deliberately and reproducibly.

Each defect must document:

- defect ID;
- category;
- severity;
- affected layer/component;
- intended incorrect behavior;
- expected correct behavior;
- injection point;
- expected detection opportunities.

### Evidence over claims

A defect is considered detected only when there is concrete evidence showing that the defect was identified.

Examples:

- failing automated test;
- manual verification evidence;
- GitHub reviewer finding;
- CI failure;
- log/observability signal;
- documented QA finding.

### Human remains the final decision maker

AI agents may analyze, implement, review and report. Human decisions remain authoritative.

## Experiment Modes

### Development Mode

Normal application development through:

Human → BA → SA → QA → FE/BE → PR → Review → Verification

### Defect Injection Mode

A known defect is introduced into an otherwise controlled version of the application.

The normal SDLC is then observed without revealing the ground truth to the agents under evaluation.

## Experiment Lifecycle

1. Select a defect from the defect catalog.
2. Record the ground truth.
3. Introduce the defect.
4. Create or update the relevant Story/PR.
5. Run the normal development and review workflow.
6. Collect evidence.
7. Record the first detection point.
8. Record all subsequent detections.
9. Fix the defect.
10. Re-run relevant verification.
11. Record time to detect and time to fix.
12. Update experiment metrics.
13. Evaluate the process.
14. Preserve the result for reporting.

## Success Criteria

The project is successful when it can demonstrate:

- known defects introduced in a controlled manner;
- reliable traceability from defect → detection → evidence → fix;
- measurable detection effectiveness;
- identification of defects missed by individual stages;
- meaningful GitHub reviewer feedback;
- reproducible reports and metrics;
- documented process improvements.

## Out of Scope

This experiment does not attempt to prove that AI can guarantee software quality.

It evaluates the effectiveness of a specific AI-assisted workflow under controlled conditions.
