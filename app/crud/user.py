from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import *
from sqlalchemy import text

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()    


def get_user_stats_raw(db: Session, user_id: int):
    query = text(   """SELECT 
            COUNT(DISTINCT r.id) AS total_recommendations,
            COUNT(f.id) AS total_feedbacks,
            COALESCE(AVG(f.rating), 0) AS average_rating
        FROM recommendations r
        LEFT JOIN feedback f ON f.recommendation_id = r.id
        WHERE r.user_id = :user_id
    """ 
    )
    result = db.execute(query, {"user_id": user_id}).mappings().fetchone()


    return {
        "total_recommendations": result.total_recommendations,
        "total_feedbacks": result.total_feedbacks,
        "average_rating": float(result.average_rating)          
    }

    