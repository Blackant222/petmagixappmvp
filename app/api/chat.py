from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.deps import get_db, get_current_user
from app.models.user import User
from app.models.pet import PetMetrics
from app.services.ai import get_ai_response
from pydantic import BaseModel
import uuid

router = APIRouter(prefix="/vet", tags=["vet"])

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    message_id: str

@router.post("/chat", response_model=ChatResponse)
async def chat_with_vet(
    chat_request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        # Get pet metrics if available
        pet_metrics = db.query(PetMetrics).filter(
            PetMetrics.user_id == current_user.id
        ).first()

        # Get AI response
        response = await get_ai_response(
            message=chat_request.message,
            pet_metrics=pet_metrics
        )

        return ChatResponse(
            response=response,
            message_id=str(uuid.uuid4())
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing chat request: {str(e)}"
        )