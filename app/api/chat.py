from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.deps import get_db, get_current_user
from app.models.user import User
from app.models.pet import PetMetrics
from app.services.ai import get_ai_response
from pydantic import BaseModel
import uuid
from datetime import datetime

router = APIRouter(prefix="/vet", tags=["vet"])

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    message_id: str
    timestamp: datetime = datetime.utcnow()

@router.post("/chat", response_model=ChatResponse)
async def chat_with_vet(
    chat_request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not chat_request.message:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Message cannot be empty"
        )

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
            message_id=str(uuid.uuid4()),
            timestamp=datetime.utcnow()
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing chat request: {str(e)}"
        )