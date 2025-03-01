# Last modified: 2025-03-01 12:35:27 by Blackant222
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.models.base import TimeStampedBase
from datetime import datetime

class Pet(TimeStampedBase):
    __tablename__ = "pets"

    name = Column(String(50), index=True)
    species = Column(String(50))
    breed = Column(String(50))
    age = Column(Float)
    weight = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="pets")
    habits = relationship("Habit", back_populates="pet", cascade="all, delete-orphan")
    metrics = relationship("Metric", back_populates="pet", cascade="all, delete-orphan")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        self.last_modified_by = "Blackant222"