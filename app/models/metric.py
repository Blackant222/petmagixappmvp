# Last modified: 2025-03-01 12:39:05 by Blackant222
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.models.base import TimeStampedBase
from datetime import datetime

class Metric(TimeStampedBase):
    __tablename__ = "metrics"

    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    value = Column(Float)
    unit = Column(String(20))
    notes = Column(String(500))
    recorded_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    pet = relationship("Pet", back_populates="metrics")
    habit = relationship("Habit", back_populates="metrics")
    user = relationship("User", back_populates="metrics")