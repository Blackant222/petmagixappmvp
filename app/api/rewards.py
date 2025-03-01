# Last modified: 2025-03-01 12:40:45 by Blackant222
from fastapi import APIRouter

router = APIRouter(prefix="/rewards", tags=["rewards"])

@router.get("/")
async def read_rewards_root():
    return {"message": "Rewards router is working"}

# Last modified: 2025-03-01 12:20:16 by Blackant222
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.deps import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.models.reward import Reward
from app.schemas.reward import RewardCreate, RewardUpdate, RewardInDB
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=RewardInDB)
async def create_reward(
    reward: RewardCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_reward = Reward(**reward.dict(), last_modified_by=current_user.username)
    db.add(db_reward)
    db.commit()
    db.refresh(db_reward)
    return db_reward

@router.get("/", response_model=List[RewardInDB])
async def read_rewards(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    rewards = db.query(Reward).filter(
        Reward.user_id == current_user.id
    ).offset(skip).limit(limit).all()
    return rewards

@router.post("/{reward_id}/claim", response_model=RewardInDB)
async def claim_reward(
    reward_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    reward = db.query(Reward).filter(
        Reward.id == reward_id,
        Reward.user_id == current_user.id
    ).first()
    
    if not reward:
        raise HTTPException(status_code=404, detail="Reward not found")
        
    if reward.status == "claimed":
        raise HTTPException(status_code=400, detail="Reward already claimed")
        
    if current_user.points < reward.points_required:
        raise HTTPException(status_code=400, detail="Insufficient points")
    
    reward.status = "claimed"
    reward.claimed_at = datetime.utcnow()
    reward.last_modified_by = current_user.username
    
    current_user.points -= reward.points_required
    
    db.commit()
    db.refresh(reward)
    return reward
