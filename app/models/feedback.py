from sqlalchemy import Column, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True)
    recommendation_id = Column(Integer, ForeignKey("recommendations.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)

    created_at = Column(TIMESTAMP, server_default=func.now())

    recommendation = relationship("Recommendation")
    