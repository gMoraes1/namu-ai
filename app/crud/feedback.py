from sqlalchemy.orm import Session
from app.models.feedback import Feedback

def create_feedback(
    db: Session,
    recommendation_id: int,
    rating: int,
    comment: str | None
) -> Feedback:
    feedback = Feedback(
        recommendation_id=recommendation_id,
        rating=rating,
        comment=comment
    )
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    
    return feedback