from fastapi import APIRouter
from typing import List
from app.schemas.task import TaskCreate, TaskResponse

router = APIRouter()

# Fake storage for now
tasks = []
task_id = 1

@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    global task_id
    task_data = task.model_dump()
    task_data["id"] = task_id
    task_id += 1
    tasks.append(task_data)
    return task_data

@router.get("/tasks", response_model=List[TaskResponse])
def get_tasks():
    return tasks
