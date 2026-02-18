from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserStatsResponse
from app.crud import user as user_crud
from app.crud import recommendation as recommendation_crud  
from app.schemas.recommendation import RecommendationResponse           
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user=user)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_id(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/{user_id}/recommendations", response_model=List[RecommendationResponse])
def get_user_recommendations(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_id(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return recommendation_crud.get_recommendations_by_user(db, user_id=user_id)     

@router.get("/{user_id}/stats", response_model=UserStatsResponse)
def get_user_stats(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_id(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_crud.get_user_stats_raw(db, user_id=user_id)