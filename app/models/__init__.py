# Last modified: 2025-03-01 12:40:45 by Blackant222
from sqlalchemy.orm import relationship
from app.models.base import Base, TimeStampedBase
from app.models.user import User
from app.models.pet import Pet
from app.models.habit import Habit
from app.models.metric import Metric
from app.models.reward import Reward

# Set up relationships after all models are imported
User.pets = relationship("Pet", back_populates="user", cascade="all, delete-orphan")
User.habits = relationship("Habit", back_populates="user", cascade="all, delete-orphan")
User.metrics = relationship("Metric", back_populates="user", cascade="all, delete-orphan")
User.rewards = relationship("Reward", back_populates="user", cascade="all, delete-orphan")

Pet.habits = relationship("Habit", back_populates="pet", cascade="all, delete-orphan")
Pet.metrics = relationship("Metric", back_populates="pet", cascade="all, delete-orphan")

__all__ = [
    "Base",
    "TimeStampedBase",
    "User",
    "Pet",
    "Habit",
    "Metric",
    "Reward"
]