from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.recommendation import RecommendationCreate, RecommendationResponse
from app.crud import recommendation as recommendation_crud  
from app.crud import user as user_crud

router = APIRouter(prefix="/recommendations", tags=["recommendations"]) 

@router.post("/", response_model=RecommendationResponse)                    
def create_recommendation(
    payload: RecommendationCreate,
    db: Session = Depends(get_db)
):
    user = user_crud.get_user_by_id(db, payload.user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    mock_activities = [
        {
            "name": "Alongamento leve",
            "description": "Sessão de alongamento para relaxamento muscular",
            "duration": "20 minutos",
            "category": "alongamento",
        }
    ]

    mock_reasoning = "Baseado no perfil do usuario e seus objetivos."
    mock_precautions = "evitar movimentos bruscos e respeitar os limites do corpo." 

    recommendation =  recommendation_crud.create_recommendation(
        db=db,
        user_id=payload.user_id,
        context=payload.context,
        activities=mock_activities,
        reasoning=mock_reasoning,
        precautions=mock_precautions
    )
    return recommendation