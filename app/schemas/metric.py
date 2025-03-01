# Last modified: 2025-03-01 12:58:05 by Blackant222
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class AIInsight(BaseModel):
    insight: str
    confidence: float
    generated_at: datetime = datetime.utcnow()

    class Config:
        from_attributes = True

class MetricBase(BaseModel):
    value: float
    unit: str
    notes: Optional[str] = None
    pet_id: int
    habit_id: int
    user_id: int
    recorded_at: datetime = datetime.utcnow()

class MetricCreate(MetricBase):
    pass

class MetricUpdate(BaseModel):
    value: Optional[float] = None
    unit: Optional[str] = None
    notes: Optional[str] = None

class MetricInDB(MetricBase):
    id: int
    created_at: datetime
    updated_at: datetime
    last_modified_by: str
    insights: Optional[List[AIInsight]] = []

    class Config:
        from_attributes = True