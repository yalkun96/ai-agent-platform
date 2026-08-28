# AI Agent Platform

A modular backend platform for orchestrating AI agents that can break a user request into specialized tasks, execute them through dedicated agents, and combine the results into a final response.

## Overview

The goal of the project is to build an extensible AI automation platform where different agents can collaborate on a single task.

Example workflow:

```text
User request
     |
     v
Orchestrator
     |
     +----------------+----------------+----------------+
     v                v                v                v
 Research Agent   Coding Agent    Testing Agent    Reporting Agent
     |                |                |                |
     +----------------+----------------+----------------+
                              |
                              v
                       Final result
```

## Current Stack

- **Python 3.13+**
- **FastAPI** — API layer
- **PostgreSQL** — persistent data storage
- **SQLAlchemy 2.0** — ORM / database access
- **Alembic** — database migrations
- **Pydantic / Pydantic Settings** — validation and configuration
- **Uvicorn** — ASGI server
- **uv** — Python package and environment management

## Architecture

The project follows a modular, layered backend architecture designed to keep API, business logic, data access, and infrastructure concerns separated.

```text
app/
├── api/          # API routes and dependencies
├── core/         # Configuration and application infrastructure
├── schemas/      # Pydantic request/response schemas
├── services/     # Business logic
├── repositories/ # Data access layer
├── agents/       # AI agent implementations
└── tasks/        # Background task orchestration

models/           # Database models
alembic/           # Database migrations
```

## Project Goals

- Build a reliable orchestration layer for multiple AI agents
- Keep agents modular and independently extensible
- Support asynchronous task execution
- Persist tasks, agents, executions, and results
- Provide a clean API for submitting and tracking jobs
- Add authentication and authorization
- Integrate multiple LLM providers
- Containerize the application for local and production environments

## Development

Clone the repository and create a Python environment with `uv`:

```bash
git clone https://github.com/yalkun96/ai-agent-platform.git
cd ai-agent-platform
uv sync
```

Create your local environment file from `.env.example` and configure the PostgreSQL connection.

Run the API:

```bash
uv run uvicorn app.main:app --reload
```

API documentation is available through FastAPI at `/docs` when the application is running.

## Status

This project is actively being developed. The architecture is being built incrementally, with the focus on clean separation of concerns, extensibility, asynchronous execution, and production-oriented backend practices.

## Author

**Yalkun Mametov**

Python Backend Developer
