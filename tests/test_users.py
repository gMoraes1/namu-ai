from fastapi.testclient import TestClient
from app.main import app

cliente = TestClient(app)

def test_create_user():
    response = cliente.post(
        "/users",
        json={
            "name": "Teste User",
            "age": 30,
            "goals": ["relaxar"],
            "restrictions": "Nenhuma",
            "experience_level": "iniciante"
        }
    )

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "Teste User"
    assert data["age"] == 30
    assert "id" in data

def test_user_stats():
    response = cliente.post(
        "/users",
        json={
            "name": "Teste User",
            "age": 31,
            "goals": ["relaxar"],
            "restrictions": "Nenhuma",
            "experience_level": "iniciante"
        }
    )

    user_id = response.json()["id"]

    response = cliente.get(f"/users/{user_id}/stats")

    assert response.status_code == 200
    data = response.json()

    assert "total_recommendations" in data
    assert "total_feedbacks" in data
    assert "average_rating" in data