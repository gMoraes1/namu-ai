from sqlalchemy.orm import Session
from app.models.recommendation import Recommendation

def create_recommendation(
    db: Session,
    user_id: int,
    context: str | None,
    activities: list,
    reasoning: str,
    precautions: str | None
) -> Recommendation:
    recommendation = Recommendation(
        user_id=user_id,
        context=context,
        activities=activities,
        reasoning=reasoning,
        precautions=precautions
    )
    db.add(recommendation)
    db.commit()
    db.refresh(recommendation)
    return recommendation       

def get_recommendations_by_user(db: Session, user_id: int):
    return (
        db.query(Recommendation)
        .filter(Recommendation.user_id == user_id)
        .order_by(Recommendation.created_at.desc())
        .all()
    )                      