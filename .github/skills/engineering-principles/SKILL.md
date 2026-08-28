---
name: engineering-principles
description: Apply practical software engineering principles during code review, including KISS, DRY, YAGNI, separation of concerns, cohesion, coupling and maintainability.
argument-hint: "[Code / Pull Request]"
---

# Engineering Principles

Use this skill to evaluate implementation quality through established software engineering principles.

## Core Principle

Engineering principles are heuristics, not absolute rules.

Do not report a violation simply because code does not visibly follow a named principle.

A finding requires a concrete reason why the current implementation creates meaningful complexity, duplication, coupling, fragility or maintenance risk.

## KISS — Keep It Simple

Prefer the simplest design that correctly satisfies the requirements.

Look for:

- unnecessary layers;
- needless abstractions;
- complicated control flow;
- clever code that obscures behavior;
- configuration that adds complexity without value.

Do not equate simplicity with fewer lines of code.

A slightly longer implementation may be preferable when it is clearer and easier to maintain.

## DRY — Don't Repeat Yourself

Avoid duplication when multiple pieces of code represent the same concept and a suitable abstraction genuinely reduces maintenance cost.

Do not automatically abstract every similar-looking fragment.

Consider whether:

- the duplicated behavior represents the same concept;
- changes would need to be made consistently;
- abstraction would reduce or increase coupling;
- the abstraction would remain understandable.

Prefer intentional duplication over a premature or misleading abstraction.

## YAGNI — You Aren't Gonna Need It

Do not add functionality, abstraction, configuration or extensibility without a current requirement or concrete need.

Look for:

- speculative features;
- unused configuration;
- unnecessary generic frameworks;
- abstractions created for hypothetical future use.

Keep implementation aligned with the approved scope.

## Separation of Concerns

Responsibilities should be separated when combining them creates meaningful coupling or makes behavior difficult to understand, test or change.

Look for:

- business logic mixed with unrelated infrastructure concerns;
- UI concerns leaking into domain logic;
- persistence logic mixed with unrelated business decisions;
- modules with multiple unrelated responsibilities.

Do not split code into arbitrary layers solely to satisfy a pattern.

## Single Responsibility

A component should have a coherent responsibility and a reason to change.

Look for components that combine unrelated responsibilities and therefore become difficult to test or maintain.

Do not interpret Single Responsibility as requiring every function or class to contain only one small operation.

## Cohesion

Prefer components whose behavior belongs together conceptually.

Low cohesion may indicate that a module has accumulated unrelated responsibilities.

## Coupling

Prefer reasonable dependencies between components.

Look for:

- unnecessary knowledge of internal implementation details;
- excessive dependency chains;
- tight coupling to unstable implementation details;
- changes that require unrelated components to change together.

Do not treat all coupling as bad. Some coupling is necessary and intentional.

## Composition Over Unnecessary Inheritance

Prefer composition when inheritance would create unnecessary coupling or fragile hierarchies.

Do not prohibit inheritance when an actual subtype relationship and existing repository conventions justify it.

## Explicit Over Implicit

Prefer behavior that is understandable from the code and its interfaces.

Look for hidden side effects, surprising state changes and implicit dependencies when they create meaningful maintenance or correctness risks.

## Fail Fast

Where appropriate, invalid states and inputs should be rejected early rather than allowed to propagate.

Consider whether delayed failure makes diagnosis harder or can cause data corruption or incorrect behavior.

Do not apply this mechanically where deferred handling is intentional.

## Principle of Least Surprise

Prefer behavior that is consistent with:

- approved contracts;
- existing repository conventions;
- established component behavior.

Flag surprising behavior when it creates a real usability, correctness or maintenance problem.

## Minimize Complexity

Consider:

- cyclomatic complexity;
- deeply nested logic;
- excessive branching;
- unnecessary indirection;
- duplicated decision logic;
- hard-to-follow state management.

Complexity is justified when it represents real domain complexity.

The goal is not to minimize code at any cost.

## Avoid Premature Abstraction

Do not introduce abstractions before there is a demonstrated need.

Prefer a clear concrete implementation when the abstraction has no current benefit.

## Maintainability Over Cleverness

Prefer code that another engineer can understand and safely modify.

Be cautious with:

- obscure language features;
- compressed logic;
- clever one-liners;
- unnecessary metaprogramming;
- abstractions that hide important behavior.

## Principle Interaction

Principles can conflict.

Examples:

- DRY can conflict with KISS.
- abstraction can conflict with maintainability.
- explicit code can be longer than highly generic code.
- strict separation can create unnecessary indirection.

When principles conflict, prioritize:

1. Correctness.
2. Approved behavior and contracts.
3. Maintainability.
4. Simplicity.
5. Consistency with the repository.

## Review Rule

Do not write:

> "This violates DRY."

Write the concrete engineering consequence, for example:

> "The same business rule is implemented independently in three services. A change to the rule would require synchronized updates in all three locations, creating a concrete maintenance and consistency risk."

Engineering principles should explain **why something matters**, not serve as the finding itself.
