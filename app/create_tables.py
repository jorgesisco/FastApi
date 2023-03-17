from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, DATABASE_URL
from app.models import project_model, task_model

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables for your models
Base.metadata.create_all(bind=engine)
