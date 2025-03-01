from typing import Dict, Any, List
import httpx
from app.core.config import settings
from app.services.ai_service import AIService

class VetBot:
    def __init__(self):
        self.system_prompt = """You are an expert veterinarian AI assistant for PetMagix. 
        You provide helpful, accurate advice about pet health, but always remind users to 
        consult a real veterinarian for serious issues. You have access to the pet's 
        health data and can reference it in your responses.
        
        Key responsibilities:
        - General pet health advice
        - Basic symptom checking
        - Diet and nutrition tips
        - Exercise recommendations
        - Preventive care information
        
        Never prescribe medication or make definitive diagnoses."""

    async def get_pet_context(self, pet_data: Dict[str, Any]) -> str:
        """Creates context about the pet from available data"""
        return f"""Pet Information:
        - Weight: {pet_data.get('weight', 'Unknown')}kg
        - Activity Level: {pet_data.get('activity_level', 'Unknown')}
        - Recent Diet: {pet_data.get('diet', 'Unknown')}
        - Hydration: {pet_data.get('hydration', 'Unknown')}ml
        - Recent Symptoms: {pet_data.get('symptoms', 'None reported')}
        - Last Updated: {settings.CURRENT_TIMESTAMP}"""

    async def chat(self, message: str, pet_data: Dict[str, Any]) -> str:
        try:
            pet_context = await self.get_pet_context(pet_data)
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://api.x.ai/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {settings.XAI_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "grok-2-latest",
                        "messages": [
                            {"role": "system", "content": self.system_prompt},
                            {"role": "user", "content": f"Pet Context:\n{pet_context}\n\nUser Question: {message}"}
                        ],
                        "max_tokens": 500,
                        "temperature": 0.7
                    },
                    timeout=15.0
                )
                
                if response.status_code == 200:
                    return response.json()['choices'][0]['message']['content']
                    
        except Exception as e:
            print(f"Vet Bot Error: {str(e)}")
            
        return "I apologize, but I'm having trouble connecting right now. Please try again later or contact our support team."