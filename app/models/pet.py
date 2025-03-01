from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
from app.db.base_class import Base

# TimeStampedBase - Base class to handle created_at, updated_at, and last_modified_by fields
class TimeStampedBase(Base):
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_modified_by = Column(String(50))

# PetMetrics Class
class PetMetrics(TimeStampedBase):
    __tablename__ = "pet_metrics"

    id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, ForeignKey("pets.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    weight = Column(Float)
    activity_level = Column(String)
    eating_habits = Column(String)
    last_checkup = Column(DateTime(timezone=True))

    # Relationships
    pet = relationship("Pet", back_populates="metrics")
    user = relationship("User", back_populates="pet_metrics")

# Pet Class
class Pet(TimeStampedBase):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    species = Column(String(50))
    breed = Column(String(50))
    age = Column(Float)
    weight = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="pets")
    habits = relationship("Habit", back_populates="pet", cascade="all, delete-orphan")
    metrics = relationship("PetMetrics", back_populates="pet", cascade="all, delete-orphan")
    
    # Custom init method to handle timestamps and modification tracking
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        self.last_modified_by = "Blackant222"
