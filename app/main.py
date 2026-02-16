from fastapi import FastAPI

app = FastAPI(title="Namu AI - Bem-estar Assistant")

@app.get("/")
def health_check():
    return {"status": "ok"}
