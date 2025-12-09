# fastapi-microservice-template

Modular **FastAPI** microservice built with **clean architecture**, **Test-Driven Development (TDD)**, and production-ready API patterns. This repo is a small template I use to practice building backend services in Python.

## Features

- Simple CRUD API for managing `tasks` (create, list, update, delete).
- Layered structure: `routers`, `schemas`, and `services` to keep code modular.
- Basic **health check** endpoint for uptime monitoring.
- Example **unit tests** using `pytest` and `httpx` to demonstrate TDD.
- Async FastAPI endpoints ready to be extended with real database/storage.

## Tech Stack

- Python 3.11+
- FastAPI
- Uvicorn (ASGI server)
- Pydantic
- Pytest + httpx (API testing)

## Project Structure

```text
fastapi-microservice-template/
├─ app/
│  ├─ main.py
│  ├─ api/
│  │  ├─ __init__.py
│  │  └─ routes_tasks.py
│  ├─ models/
│  │  └─ __init__.py
│  └─ schemas/
│     └─ task.py
├─ tests/
│  └─ test_tasks.py
├─ requirements.txt
└─ README.md
