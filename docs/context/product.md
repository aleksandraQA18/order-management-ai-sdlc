# QA Academy — Product Description

## Product Overview

QA Academy is a web-based e-learning marketplace focused on software testing and QA Engineering.

The platform allows users to discover QA-related courses and educational materials, create an account, purchase courses, and access the courses they have purchased from a personal area.

The product is intentionally focused on **course discovery, purchase, and access to educational content**. It is not intended to be a full Learning Management System in the first version: there is no learning-progress tracking, certification, gamification, or advanced student assessment.

## Target Users

### Learners

People who want to learn or improve software testing and QA Engineering skills, including:

- aspiring QA Engineers,
- manual testers moving toward automation,
- QA Engineers improving their API, automation, or testing skills,
- developers interested in software quality.

### Platform Administrators

Administrators manage the educational catalogue and make courses and their materials available to users.

## Core Business Concept

The platform sells access to digital QA education.

A user can browse the public catalogue and view course information without purchasing a course. Access to the actual course materials is restricted to users who are authenticated and have purchased the corresponding course.

The key business relationship is:

**User → Purchase → Course Access**

A successful purchase grants the user access to the purchased course.

## Main User Journey

1. A visitor opens the QA Academy website.
2. The visitor browses available courses.
3. The visitor opens a course details page and reviews its description, topics, and price.
4. The visitor registers or logs in.
5. The user purchases a course through the checkout process.
6. The payment is processed by a simulated payment service in the initial version.
7. After a successful payment, the user receives access to the purchased course.
8. The course becomes available in the user's **My Courses** area.
9. The user opens the course and accesses its modules and educational materials.

## Core Features

### Authentication

Users can:

- register an account,
- log in,
- log out,
- access authenticated areas of the platform.

### Course Catalogue

Visitors can:

- browse available courses,
- view course titles and descriptions,
- view course details,
- view pricing information.

### Course Access

Authenticated users can access course materials only when they have an active entitlement to the course through a successful purchase.

Users who have not purchased a course must not be able to access its protected materials directly through the UI or API.

### Purchasing

Users can purchase a course through checkout.

The first version uses a simulated payment flow rather than a real payment provider. The payment result determines whether course access is granted.

Possible payment outcomes include:

- successful payment,
- failed payment,
- pending or unavailable payment.

A successful payment grants access. A failed payment must not grant access.

### My Courses

Authenticated users have a personal area showing the courses they have purchased and can access.

The list should contain only courses for which the user has valid access.

### Course Content

A purchased course contains educational materials organized into modules and lessons or other content units.

The first version focuses on content access and presentation rather than tracking learning progress.

## AI Features

AI is an optional supporting capability rather than the foundation of the platform.

The first AI feature is an **AI Course Assistant**. A user who has access to a course can ask questions related to the course material and receive an AI-generated explanation.

The AI assistant should operate within the context of the relevant course and should not be treated as an authoritative source outside that educational context.

Potential future AI capabilities include:

- generating summaries of course materials,
- generating practice questions,
- explaining difficult concepts,
- suggesting related course materials.

AI requests should be triggered explicitly by the user rather than automatically on every page visit, keeping usage and operating costs predictable.

## Business Rules

1. A visitor can browse the course catalogue without being logged in.
2. A user must be authenticated to purchase a course.
3. A user must be authenticated to access purchased course materials.
4. A successful purchase grants access to the purchased course.
5. A failed payment does not grant course access.
6. A user cannot access another user's purchased courses.
7. A course must not appear in **My Courses** unless the user has valid access to it.
8. Course materials are protected resources and must be authorized at the backend level, not only hidden in the frontend.
9. AI course assistance is available only to users who have access to the relevant course.
10. AI-generated content must not be allowed to override the application's authorization or business rules.

## Product Scope — Initial Version

### In scope

- user registration and login,
- public course catalogue,
- course details,
- authentication,
- checkout,
- simulated payment processing,
- orders/purchases,
- course access control,
- My Courses,
- course modules and educational materials,
- AI Course Assistant,
- basic error handling and user feedback.

### Out of scope

- learning-progress tracking,
- quizzes and exams,
- certificates,
- gamification,
- instructor dashboards,
- real payment processing,
- subscriptions,
- mobile application,
- advanced recommendations,
- full LMS functionality.

## Product Goal

The goal of QA Academy is to provide a realistic web application for purchasing and accessing QA Engineering education while creating a technically rich product environment for demonstrating modern software quality practices.

The platform should support reliable authentication, authorization, purchase workflows, protected content, API integrations, and AI-assisted functionality while keeping the initial product scope small enough to develop and maintain as a focused project.
