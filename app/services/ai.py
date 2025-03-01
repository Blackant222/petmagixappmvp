from typing import Optional
from app.models.pet import PetMetrics

async def get_ai_response(message: str, pet_metrics: Optional[PetMetrics] = None) -> str:
    """
    Get AI response for pet-related queries.
    
    Args:
        message: The user's message/question
        pet_metrics: Optional pet metrics data to provide context
        
    Returns:
        str: AI-generated response
    """
    # For now, return a simple response
    # TODO: Implement actual AI integration
    return (
        "Thank you for your question. As a veterinary AI assistant, I recommend consulting "
        "with a veterinarian for specific medical advice. However, I can provide some general "
        "information about pet care and wellness."
    )