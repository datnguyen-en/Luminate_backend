from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    duration: int # in min
    deadline: datetime
    priority: int = 1

class TaskResponse(TaskCreate):
    id: int