from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any
from app.services.chat.vet_bot import VetBot
from app.api.deps import get_current_user, get_db
from sqlalchemy.orm import Session
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()
vet_bot = VetBot()

@router.post("/chat", response_model=ChatResponse)
async def chat_with_vet(
    chat_request: ChatRequest,
    current_user: Dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Chat with the AI vet assistant
    """
    # Get the latest pet metrics for context
    # You can modify this based on your database schema
    pet_data = db.query(PetMetrics).filter(
        PetMetrics.user_id == current_user["id"]
    ).order_by(PetMetrics.timestamp.desc()).first()
    
    if not pet_data:
        pet_data = {}  # Fallback to empty data if no metrics found
    
    response = await vet_bot.chat(
        message=chat_request.message,
        pet_data=pet_data.__dict__ if pet_data else {}
    )
    
    return ChatResponse(response=response)