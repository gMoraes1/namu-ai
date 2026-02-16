from fastapi import FastAPI
from app.database import engine, Base
from app.models import recommendation, feedback
from app.routers import user

app = FastAPI(title="Namu AI - Bem-estar Assistant")
Base.metadata.create_all(bind=engine)

app.include_router(user.router)

