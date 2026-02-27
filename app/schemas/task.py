from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    duration: int # in min
    deadline: datetime
    priority: int = 1

class TaskResponse(TaskCreate):
    id: int

class TaskUpdate(BaseModel):
    title: str | None = None
    duration: int | None = None
    deadline: datetime | None = None
    Priority: int | None = None

# Optional so you can update preferred 

