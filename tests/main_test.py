

from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "UP"
    assert data["service"] == "Heart Disease Prediction API"


    #def test_basic():
    #assert 1 + 1 == 2