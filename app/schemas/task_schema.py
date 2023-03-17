from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str
    project_id: int

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
