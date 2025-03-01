import httpx
from typing import List, Dict, Any
from app.core.config import settings
from datetime import datetime

class AIService:
    @staticmethod
    async def get_insights(pet_data: Dict[str, Any]) -> List[str]:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://api.x.ai/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {settings.XAI_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "grok-2-latest",
                        "messages": [{
                            "role": "user",
                            "content": f"Analyze this pet's health data and provide insights: {pet_data}"
                        }],
                        "max_tokens": 150
                    },
                    timeout=10.0
                )
                
                if response.status_code == 200:
                    return response.json()['choices'][0]['message']['content'].split('\n')
                    
        except Exception as e:
            print(f"AI API Error: {str(e)}")
            
        # Fallback insights
        return [
            f"Your pet's current weight is {pet_data.get('weight', '0')}kg",
            "Maintain regular exercise and healthy diet",
            "Consider scheduling a regular vet check-up",
            f"Analysis timestamp: {settings.CURRENT_TIMESTAMP}"
        ]