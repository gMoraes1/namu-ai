from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json

from app.database import get_db
from app.schemas.recommendation import (
    RecommendationCreate,
    RecommendationResponse,
    RecommendationResult,
)
from app.schemas.feedback import FeedbackCreate, FeedbackResponse
from app.crud import recommendation as recommendation_crud
from app.crud import user as user_crud
from app.crud import feedback as feedback_crud
from app.models.recommendation import Recommendation

from app.service.llm_service import generate_response
from app.utils.prompt_builder import build_prompt


router = APIRouter(prefix="/recommendations", tags=["recommendations"])


@router.post("/", response_model=RecommendationResponse)
def create_recommendation(
    payload: RecommendationCreate,
    db: Session = Depends(get_db)
):
    user = user_crud.get_user_by_id(db, payload.user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    prompt = build_prompt(user, payload.context)
    raw_response = generate_response(prompt)

    try:
        parsed = json.loads(raw_response)
        validated = RecommendationResult(**parsed)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error parsing LLM response: {str(e)}"
        )

    recommendation = recommendation_crud.create_recommendation(
        db=db,
        user_id=payload.user_id,
        context=payload.context,
        activities=[a.model_dump() for a in validated.activities],
        reasoning=validated.reasoning,
        precautions=validated.precautions,
    )

    return recommendation


@router.post("/{recommendation_id}/feedback", response_model=FeedbackResponse)
def add_feedback(
    recommendation_id: int,
    payload: FeedbackCreate,
    db: Session = Depends(get_db),
):
    recommendation = db.query(Recommendation).filter(
        Recommendation.id == recommendation_id
    ).first()

    if not recommendation:
        raise HTTPException(status_code=404, detail="Recommendation not found")

    feedback = feedback_crud.create_feedback(
        db=db,
        recommendation_id=recommendation_id,
        rating=payload.rating,
        comment=payload.comment,
    )

    return feedback
