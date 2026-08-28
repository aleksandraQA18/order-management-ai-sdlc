---
name: frontend-ui-implementation
description: Implement an approved Human-provided UI Design Artifact in the frontend while preserving approved business and system behavior.
argument-hint: "[Story with UI Design Artifact]"
---

# Frontend UI Implementation

Use this skill when a Story contains an approved UI Design Artifact and the frontend must implement it.

## Source of Truth

The approved UI Design Artifact is the source of truth for defined UI and UX behavior.

Use it together with:

- approved Acceptance Criteria;
- approved System Analyst analysis;
- approved Implementation Map.

The design does not override approved business requirements or system constraints.

## Design Interpretation

Inspect the artifact and identify:

- page or screen structure;
- layout;
- visual hierarchy;
- components;
- content;
- states;
- interactions;
- validation behavior;
- loading behavior;
- success and error states;
- responsive behavior when defined;
- accessibility-related requirements when defined.

Implement what is explicitly defined.

Do not infer additional product behavior from visual appearance alone.

## Existing Design Patterns

Before creating UI:

- inspect existing application components;
- reuse established components and patterns;
- follow existing spacing, typography, styling and interaction conventions;
- avoid creating duplicate UI primitives.

If the artifact intentionally differs from existing conventions, follow the approved artifact for the Story unless doing so conflicts with approved requirements.

## States

Do not implement only the ideal state when the approved design defines additional states.

Consider all states explicitly represented by the artifact, such as:

- initial;
- loading;
- validation error;
- server error;
- empty;
- success;
- disabled.

If a required state is not defined and cannot be determined from approved requirements, mark it as `OPEN` rather than inventing behavior.

## Responsive Behavior

Implement responsive behavior only when:

- it is explicitly defined by the artifact; or
- it follows an already established application-wide convention.

Do not invent new responsive behavior that changes product behavior.

## Accessibility

Preserve existing accessibility conventions and implement explicitly defined accessibility requirements.

Do not claim accessibility compliance solely because semantic HTML was used.

## Conflicts

If the UI Design Artifact conflicts with:

- Acceptance Criteria;
- approved business behavior;
- approved System Analyst analysis;
- approved API behavior;

do not choose one silently.

Record:

- the conflict;
- affected behavior;
- implementation impact;
- proposed resolution if useful.

Mark the issue `OPEN` and request human decision.

## Visual Deviations

If implementation cannot reproduce an approved design because of technical constraints:

- document the deviation;
- explain the reason;
- describe the impact;
- request human review when the deviation changes the approved UX.

Do not silently replace the approved design with a different design.

## Boundary

This skill defines how to implement an approved UI design.

It does not define:

- how the UI should be designed;
- business requirements;
- architecture;
- backend implementation;
- QA strategy.
