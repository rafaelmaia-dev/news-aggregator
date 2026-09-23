<div align="center">

# 📰 News Aggregator

**A self-hosted AI-powered news pipeline that fetches RSS feeds, summarizes articles with an LLM, and delivers them straight to your Telegram.**

[Architecture](#architecture) · [Tech Stack](#tech-stack) · [Quick Start](#quick-start) · [Roadmap](#roadmap)

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Self-Hosted](https://img.shields.io/badge/self--hosted-yes-success)](https://github.com/rafaelmaia-dev/bot_noticias_ia)

</div>

---

## What is this?

**News Aggregator** is an open-source backend project that automates your daily tech news reading.

It runs two independent processes:

- **Worker** — a scheduler that fetches RSS feeds, deduplicates articles, calls the [Groq API](https://groq.com) for LLM summarization, and dispatches formatted summaries to a Telegram chat.
- **API** — a FastAPI REST service that exposes the persisted data for querying, filtering, and feed management (JWT-protected).

Built as a portfolio project to demonstrate clean async backend architecture, containerization, and CI/CD pipelines.

---

## Architecture

```
+----------------------------------------------------------+
|                     Worker Process                       |
|                                                          |
|  APScheduler --> Fetcher --> Parser --> Deduplication    |
|                                              |           |
|                                         PostgreSQL       |
|                                              |           |
|                               Summarizer (Groq API)      |
|                                              |           |
|                          Dispatcher (Telegram Bot API)   |
+----------------------------------------------------------+

+----------------------------------------------------------+
|                      API Process                         |
|                                                          |
|   FastAPI --> Routers --> SQLAlchemy --> PostgreSQL       |
|               (JWT auth for admin endpoints)             |
+----------------------------------------------------------+
```

---

## Tech Stack

| Layer        | Technology                                    |
|--------------|-----------------------------------------------|
| API          | FastAPI + Pydantic v2                         |
| ORM          | SQLAlchemy 2.0 (async) + asyncpg              |
| Database     | PostgreSQL                                    |
| Scheduler    | APScheduler                                   |
| LLM          | Groq API                                      |
| Delivery     | Telegram Bot API                              |
| Testing      | pytest + pytest-asyncio                       |
| Code Quality | SonarCloud + Ruff                             |
| Security     | Trivy (Docker image scanning)                 |
| Container    | Docker + Docker Compose                       |
| CI/CD        | GitHub Actions                                |

---

## Quick Start

**1. Clone the repository and set up your environment:**

```bash
git clone https://github.com/rafaelmaia-dev/bot_noticias_ia.git
cd news-aggregator

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**2. Configure your environment variables:**

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```dotenv
# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/news_aggregator

# Telegram — get your token from @BotFather
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
TELEGRAM_CHAT_ID=your-chat-or-group-id

# Groq — get your key at console.groq.com
GROQ_API_KEY=your-groq-api-key

# Delivery settings
DELIVERY_MODE=digest          # "digest" or "realtime"
DIGEST_SCHEDULE=08:00,18:00   # HH:MM, comma-separated
DIGEST_MAX_ARTICLES=10
```

**3. Run database migrations:**

```bash
alembic upgrade head
```

**4. Start the worker:**

```bash
python -m worker.scheduler
```

> Docker Compose support (API + Worker + PostgreSQL as containers) is coming in Phase 3.

---

## Getting Started (Manual Setup)

> **Prerequisites:** Python 3.11+, PostgreSQL running locally or via Docker.

```bash
# Spin up PostgreSQL quickly with Docker
docker run -d \
  --name news-db \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=news_aggregator \
  -p 5432:5432 \
  postgres:16-alpine
```

Then follow the [Quick Start](#quick-start) steps above.

---

## Roadmap

### Phase 0 — Scaffolding (done)
- [x] Project structure, `.venv`, `requirements.txt`, Alembic, `.gitignore`, MIT License
- [x] `src/config.py` — settings management via Pydantic Settings
- [x] `src/database.py` — async SQLAlchemy engine + session factory

### Phase 1 — Core Pipeline (in progress)
- [ ] SQLAlchemy models: `Feed`, `Article`, `Delivery`
- [ ] Alembic migrations
- [ ] RSS fetcher + parser (`worker/fetcher.py`, `worker/parser.py`)
- [ ] Groq summarizer (`worker/summarizer.py`)
- [ ] Telegram dispatcher (`worker/dispatcher.py`)
- [ ] APScheduler job orchestration (`worker/scheduler.py`)
- [ ] End-to-end deduplication (by URL hash)

### Phase 2 — REST API
- [ ] Pydantic v2 schemas (request/response models)
- [ ] Feed CRUD endpoints (JWT-protected)
- [ ] Article query endpoints (public, with pagination and filters)
- [ ] Automated tests (unit + integration with test database)
- [ ] OpenAPI documentation with examples

### Phase 3 — Containerization
- [ ] Multi-stage Dockerfile for the API
- [ ] Dockerfile for the worker
- [ ] `docker-compose.yml` orchestrating API + Worker + PostgreSQL
- [ ] `.env.example` with all required variables documented

### Phase 4 — CI/CD Pipeline
- [ ] GitHub Actions: lint (Ruff) → tests (pytest) → SonarCloud scan
- [ ] Docker image build step
- [ ] Trivy vulnerability scan on built images
- [ ] Push to GitHub Container Registry
- [ ] Automated deploy on merge to `main`

### Phase 5 — Observability *(stretch goal)*
- [ ] `/health` and `/ready` endpoints
- [ ] Structured JSON logging
- [ ] Prometheus metrics (delivery count, fetch errors)

---

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how to set up your development environment and submit pull requests.

---

## License

This project is licensed under the [MIT License](./LICENSE).
