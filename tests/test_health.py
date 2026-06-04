from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_live():
    response = client.get("/api/v1/health/live")
    assert response.status_code == 200
    assert response.json() == {"message": "ok"}


def test_ready():
    response = client.get("/api/v1/health/ready")
    assert response.status_code == 200
    assert response.json() == {"message": "ready"}
