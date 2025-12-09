from fastapi import FastAPI
from app.api.routes_tasks import router as tasks_router

app = FastAPI(title="FastAPI Microservice Template")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])p
