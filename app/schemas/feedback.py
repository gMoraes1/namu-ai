from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class FeedbackCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = Field(None, max_length=1000)

class FeedbackReponse(BaseModel):
    id: int
    recommendation_id: int
    rating: int
    comment: Optional[str]
    created_at: datetime    

    class Config:
        from_attributes = True