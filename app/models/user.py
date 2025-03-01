# Last modified: 2025-03-01 14:05:59 by Blackant222
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.models.base import TimeStampedBase
from datetime import datetime

class User(TimeStampedBase):
    __tablename__ = "users"

    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(200))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    points = Column(Integer, default=0)
    
    # Relationships
    pets = relationship("Pet", back_populates="user", cascade="all, delete-orphan")
    habits = relationship("Habit", back_populates="user", cascade="all, delete-orphan")
    metrics = relationship("Metric", back_populates="user", cascade="all, delete-orphan")
    rewards = relationship("Reward", back_populates="user", cascade="all, delete-orphan")

    def __init__(self, **kwargs):
        if 'password' in kwargs:
            from app.core.security import get_password_hash
            kwargs['hashed_password'] = get_password_hash(kwargs.pop('password'))
        super().__init__(**kwargs)