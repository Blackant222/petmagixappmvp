# Last modified: 2025-03-01 12:39:05 by Blackant222
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.base import TimeStampedBase
from datetime import datetime

class Reward(TimeStampedBase):
    __tablename__ = "rewards"

    name = Column(String(100))
    description = Column(String(500))
    points_required = Column(Integer, default=0)
    is_redeemed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="rewards")