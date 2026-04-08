from app.app import app


def test_home():
    client = app.test_client()
    response = client.get("/", headers={"Accept": "application/json"})

    assert response.status_code == 200

    data = response.get_json()
    assert data["message"] == "Hello DevOps Engg"


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()
    assert data["status"] == "OK"
