from sqlalchemy import create_engine    
from sqlalchemy.orm import Session
from sqlalchemy.orm import session_maker, declarative_base


DATABASE_URL = "sqlite:///./luminate.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = session_maker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()