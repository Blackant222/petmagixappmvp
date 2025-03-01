# Last modified: 2025-03-01 12:54:23 by Blackant222
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HabitBase(BaseModel):
    name: str
    description: Optional[str] = None
    frequency: str
    is_completed: bool = False
    streak: int = 0
    user_id: int
    pet_id: int

class HabitCreate(HabitBase):
    pass

class HabitUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    frequency: Optional[str] = None
    is_completed: Optional[bool] = None
    streak: Optional[int] = None

class HabitInDB(HabitBase):
    id: int
    created_at: datetime
    updated_at: datetime
    last_modified_by: str

    class Config:
        from_attributes = True