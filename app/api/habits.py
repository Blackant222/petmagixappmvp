# Last modified: 2025-03-01 12:40:45 by Blackant222
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.deps import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.models.habit import Habit
from app.schemas.habit import HabitCreate, HabitUpdate, HabitInDB
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=HabitInDB)
async def create_habit(
    habit: HabitCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_habit = Habit(**habit.dict(), last_modified_by=current_user.username)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit

@router.get("/", response_model=List[HabitInDB])
async def read_habits(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    habits = db.query(Habit).filter(
        Habit.user_id == current_user.id
    ).offset(skip).limit(limit).all()
    return habits

@router.put("/{habit_id}/complete", response_model=HabitInDB)
async def complete_habit(
    habit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    habit = db.query(Habit).filter(
        Habit.id == habit_id,
        Habit.user_id == current_user.id
    ).first()
    
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    habit.last_completed = datetime.utcnow()
    habit.streak += 1
    habit.last_modified_by = current_user.username
    db.commit()
    db.refresh(habit)
    return habit