from fastapi import APIRouter
from typing import List
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate

# Fake storage for now
tasks = []
task_id = 1

def create_task(task: TaskCreate):
    global task_id
    task_data = task.model_dump()
    task_data["id"] = task_id
    task_id += 1
    tasks.append(task_data)
    return task_data

def get_tasks():
    return tasks

def delete_task(task_id: int):
    global tasks

    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted_task = tasks.pop(i)
            return deleted_task
    
    return None

def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            update_data = task_update.model_dump(exclude_unset= True) # Only include fields user provided
            task.update(update_data)
            return task
        
    return None