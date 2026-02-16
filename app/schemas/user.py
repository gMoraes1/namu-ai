from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional
from datetime import datetime

class ExperienceLevel(str, Enum):
    iniciante = "iniciante"
    intermediário = "intermediário"
    avançado = "avançado"


class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    age: int = Field(..., ge=0, le=120)
    goals: List[str] = Field(..., min_items=1)
    restrictions: Optional[str] = None
    experience_level: ExperienceLevel

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
