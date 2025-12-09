# fastapi-microservice-template

Modular **FastAPI** microservice built with **clean architecture**, **Test-Driven Development (TDD)**, and production-ready API patterns. This repo is a small template I use to practice building backend services in Python.

## Features
- Simple CRUD API for managing `tasks` (create, list, update, delete).
- Layered structure: `routers`, `schemas`, and `services` to keep code modular.
- Basic health check endpoint for uptime monitoring.
- Example unit tests using `pytest` and `httpx` to demonstrate TDD.
- Async FastAPI endpoints ready to be extended with real database/storage.

## Tech Stack
- Python 3.11+
- FastAPI
- Uvicorn (ASGI server)
- Pydantic
- Pytest + httpx (API testing)

## Project Structure
fastapi-microservice-template/
├── app/
│ ├── main.py
│ ├── api/
│ │ ├── init.py
│ │ ├── routes_tasks.py
│ ├── models/
│ │ ├── init.py
│ ├── schemas/
│ │ ├── task.py
├── tests/
│ ├── test_tasks.py
├── requirements.txt
└── README.md


## Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/mirzamuhammaddaniyal-eng/fastapi-microservice-template.git
cd fastapi-microservice-template
```

```bash
# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

```bash
# 3. Install dependencies
pip install -r requirements.txt
```

```bash
# 4. Start the FastAPI server
uvicorn app.main:app --reload
```

Visit:
```
http://127.0.0.1:8000
```

Health check:
```
/health
```
