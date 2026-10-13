# AI Agent Platform

A FastAPI backend for user accounts and user-owned AI agent configurations.

## Features

- User registration and username/password login
- JWT bearer authentication
- CRUD operations for authenticated users' agents
- PostgreSQL persistence with SQLAlchemy
- Database schema migrations with Alembic
- Interactive API documentation through Swagger UI

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)
- Docker Desktop, or a compatible PostgreSQL instance

## Local setup

1. Create your local environment file:

   ```bash
   cp .env.example .env
   ```

2. Edit `.env`. Set a unique local `DB_PASSWORD` and a private `SECRET_KEY`. Generate a key with:

   ```bash
   python -c "import secrets; print(secrets.token_urlsafe(48))"
   ```

   Never commit the real `.env` file or share production credentials.

3. Install dependencies and start PostgreSQL:

   ```bash
   uv sync
   docker compose up -d
   ```

4. Apply migrations:

   ```bash
   uv run alembic upgrade head
   ```

5. Start the API:

   ```bash
   uv run uvicorn app.main:app --reload
   ```

The API listens on `http://127.0.0.1:8000`; Swagger UI is available at `http://127.0.0.1:8000/docs`.

Compose maps the host port from `DB_PORT` (default `5434`) to PostgreSQL's container port `5432`. The app's `DB_HOST` should normally be `localhost` when running the API on the host. If the API runs inside Compose, use the service name `postgres` instead.

## Security

- Never commit `.env`, database passwords, JWT signing keys, or production credentials.
- Use different random secrets for development, staging, and production.
- Store production secrets in your deployment platform's secret manager.
