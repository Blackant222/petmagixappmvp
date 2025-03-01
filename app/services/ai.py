from typing import Optional
from app.models.pet import PetMetrics
from app.core.config import settings
import httpx
import json

async def get_ai_response(message: str, pet_metrics: Optional[PetMetrics] = None) -> str:
    """
    Get AI response using XAI API for pet-related queries.
    
    Args:
        message: The user's message/question
        pet_metrics: Optional pet metrics data to provide context
    """
    try:
        # Prepare the context with pet metrics if available
        context = ""
        if pet_metrics:
            context = (
                f"Pet Weight: {pet_metrics.weight}kg, "
                f"Activity Level: {pet_metrics.activity_level}, "
                f"Eating Habits: {pet_metrics.eating_habits}, "
                f"Last Checkup: {pet_metrics.last_checkup}"
            )

        # Prepare the prompt
        prompt = f"""As a veterinary AI assistant, please help with this question.
        User Question: {message}
        Pet Information: {context if context else 'No pet information available'}
        
        Please provide a helpful and professional response."""

        # XAI API endpoint
        url = "https://api.xai.com/v1/chat/completions"  # Replace with actual XAI endpoint
        
        headers = {
            "Authorization": f"Bearer {settings.XAI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "messages": [
                {"role": "system", "content": "You are a veterinary AI assistant providing helpful advice about pet care."},
                {"role": "user", "content": prompt}
            ],
            "model": "grok-2",  # Replace with actual XAI model name
            "temperature": 0.7
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            
            data = response.json()
            return data["choices"][0]["message"]["content"]

    except Exception as e:
        # Fallback response in case of API errors
        return (
            "I apologize, but I'm having trouble connecting to the AI service at the moment. "
            "For urgent matters, please consult with a veterinarian directly. "
            f"Error: {str(e)}"
        )