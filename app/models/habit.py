# Last modified: 2025-03-01 12:37:01 by Blackant222
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.base import TimeStampedBase
from datetime import datetime

class Habit(TimeStampedBase):
    __tablename__ = "habits"

    name = Column(String(100))
    description = Column(String(500))
    frequency = Column(String(50))  # daily, weekly, monthly
    is_completed = Column(Boolean, default=False)
    streak = Column(Integer, default=0)
    
    # Foreign Keys
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="habits")
    pet = relationship("Pet", back_populates="habits")
    metrics = relationship("Metric", back_populates="habit", cascade="all, delete-orphan")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        self.last_modified_by = "Blackant222"