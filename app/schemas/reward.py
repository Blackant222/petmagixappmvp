# Last modified: 2025-03-01 12:54:23 by Blackant222
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RewardBase(BaseModel):
    name: str
    description: Optional[str] = None
    points_required: int = 0
    is_redeemed: bool = False
    user_id: int

class RewardCreate(RewardBase):
    pass

class RewardUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    points_required: Optional[int] = None
    is_redeemed: Optional[bool] = None

class RewardInDB(RewardBase):
    id: int
    created_at: datetime
    updated_at: datetime
    last_modified_by: str

    class Config:
        from_attributes = True