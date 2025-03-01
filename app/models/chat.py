from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    message_id: str
    timestamp: datetime = datetime.utcnow()

class ChatModel(BaseModel):
    id: int
    user_id: int
    pet_id: int
    message: str
    response: str
    timestamp: datetime = datetime.utcnow()

class Chat(BaseModel):
    id: int
    user_id: int
    pet_id: int
    message: str
    response: str
    timestamp: datetime = datetime.utcnow()
