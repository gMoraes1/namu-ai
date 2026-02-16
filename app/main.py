from fastapi import FastAPI
from app.database import engine, Base
from app.models import recommendation, feedback

app = FastAPI(title="Namu AI - Bem-estar Assistant")
Base.metadata.create_all(bind=engine)

