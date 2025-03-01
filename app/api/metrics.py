# Last modified: 2025-03-01 12:20:16 by Blackant222
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.deps import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.models.metric import Metric
from app.schemas.metric import MetricCreate, MetricUpdate, MetricInDB, AIInsight
from app.services.ai_service import AIService

router = APIRouter()

@router.post("/", response_model=MetricInDB)
async def create_metric(
    metric: MetricCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_metric = Metric(**metric.dict(), last_modified_by=current_user.username)
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    
    # If it's a weight metric, get AI insights
    if metric.metric_type == "weight":
        pet_data = {
            "id": metric.pet_id,
            "weight": metric.value,
            "unit": metric.unit,
            "timestamp": "2025-03-01 12:20:16"
        }
        
        insights = await AIService.get_insights(pet_data)
        
        # Store insights as a new metric
        insight_metric = Metric(
            pet_id=metric.pet_id,
            user_id=current_user.id,
            metric_type="ai_insight",
            value=1.0,
            notes=str(insights),
            last_modified_by="AI System"
        )
        db.add(insight_metric)
        db.commit()
    
    return db_metric

@router.get("/pet/{pet_id}", response_model=List[MetricInDB])
async def read_pet_metrics(
    pet_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    metrics = db.query(Metric).filter(
        Metric.pet_id == pet_id,
        Metric.user_id == current_user.id
    ).offset(skip).limit(limit).all()
    return metrics

@router.post("/ai/insights", response_model=AIInsight)
async def get_ai_insights(
    pet_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Get latest metrics for the pet
    metrics = db.query(Metric).filter(
        Metric.pet_id == pet_id,
        Metric.user_id == current_user.id
    ).order_by(Metric.created_at.desc()).limit(10).all()
    
    pet_data = {
        "id": pet_id,
        "metrics": [metric.to_dict() for metric in metrics],
        "timestamp": "2025-03-01 12:20:16"
    }
    
    insights = await AIService.get_insights(pet_data)
    return {"insights": insights}
