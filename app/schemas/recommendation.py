from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Activity(BaseModel):
    name: str = Field(..., min_length=2)
    description: str = Field(..., min_length=5)
    duration: str = Field(..., description="Ex: 20 minutos")
    category: str = Field(..., description="Ex: alongamento, mindfulness, cardio")


class RecommendationCreate(BaseModel):
    user_id: int
    context: Optional[str] = Field(
        None,
        description="Contexto adicional do usuário, ex: estou com dor nas costas"
    )


class RecommendationResult(BaseModel):
    activities: List[Activity]
    reasoning: str
    precautions: Optional[str] = None

class RecommendationResponse(RecommendationResult):
    id: int
    user_id: int
    context: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
