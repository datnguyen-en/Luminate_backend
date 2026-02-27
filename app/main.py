from fastapi import FastAPI
from app.api.tasks import router as tasks_router
from app.db.database import Base, engine
from app.models import Task



app = FastAPI()

app.include_router(tasks_router)

Base.metadata.create_all(bind=engine)