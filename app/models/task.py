from sqlalchemy import Column, Integer, String, DateTime
from app.db.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index= True)
    title = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    deadline = Column(DateTime, nullable=False)
    priority = Column(Integer, default=1)

    