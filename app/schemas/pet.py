# Last modified: 2025-03-01 12:54:23 by Blackant222
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PetBase(BaseModel):
    name: str
    species: str
    breed: Optional[str] = None
    age: Optional[float] = None
    weight: Optional[float] = None
    user_id: int

class PetCreate(PetBase):
    pass

class PetUpdate(BaseModel):
    name: Optional[str] = None
    species: Optional[str] = None
    breed: Optional[str] = None
    age: Optional[float] = None
    weight: Optional[float] = None

class PetInDB(PetBase):
    id: int
    created_at: datetime
    updated_at: datetime
    last_modified_by: str

    class Config:
        from_attributes = True