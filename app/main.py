from fastapi import FastAPI
from app.routers import project_router, task_router
import app.create_tables

app = FastAPI()

app.include_router(project_router, prefix="/projects", tags=["projects"])
app.include_router(task_router, prefix="/tasks", tags=["tasks"])

