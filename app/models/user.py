from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, Enum
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)          
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    goals = Column(ARRAY(String), nullable=False)
    restrictions = Column(Text)
    experience_level = Column(String(50), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp()) 