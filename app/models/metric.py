# Last modified: 2025-03-01 12:39:05 by Blackant222
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.base import TimeStampedBase
from datetime import datetime

class Metric(Base, TimeStampedBase):
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

class PetMetric(Base, TimeStampedBase):
    __tablename__ = "pet_metrics"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    metric_id = Column(Integer, ForeignKey("metrics.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    value = Column(Float)
    recorded_at = Column(DateTime, default=datetime.utcnow)

    pet = relationship("Pet", back_populates="pet_metrics")
    metric = relationship("Metric", back_populates="pet_metrics")
    user = relationship("User", back_populates="pet_metrics")
