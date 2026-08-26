---
name: docker
description: Build reproducible Docker and Docker Compose environments for local development and CI.
argument-hint: "[Docker task]"
---

# Docker

Principles:
- one concern per service where practical,
- explicit configuration,
- health checks where useful,
- deterministic startup,
- no secrets in images,
- understandable Dockerfiles.

Use Docker Compose for the MVP.
