from app.services import task_services
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    return task_services.create_task(task)

@router.get("/tasks", response_model=List[TaskResponse])
def get_tasks():
    return task_services.get_tasks()

@router.delete("/tasks/{task_id}", response_model=TaskResponse)
def delete_task(task_id: int):
    deleted = task_services.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate):
    updated = task_services.update_task(task_id, task_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated
