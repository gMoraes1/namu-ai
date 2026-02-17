import requests
from app.core.config import get_settings

settings = get_settings()

def generate_response(prompt: str) -> str:
    url = f"{settings.OLLAMA_BASE_URL}/api/generate"
    payload = {
        "model": settings.LLM_MODEL,
        "prompt": prompt,
        "stream": False,
        "keep_alive": "5m",
        "options": {
            "num_predict": 300
        }
    }
    response = requests.post(url, json=payload, timeout=180)

    if response.status_code != 200:
        raise Exception(f"LLM API error: {response.status_code} - {response.text}")     
    data = response.json()
    return data["response"]