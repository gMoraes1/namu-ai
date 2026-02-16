from sqlalchemy import Column, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base

class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    context = Column(Text)

    activities = Column(JSONB, nullable=False)
    reasoning = Column(Text, nullable=False)
    precautions = Column(Text)

    created_at = Column(TIMESTAMP, server_default=func.now())   

    user = relationship("User", back_populates="recommendations")   
    