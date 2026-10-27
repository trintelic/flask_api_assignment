from app import app

client = app.test_client()


def test_hello():
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello, world!"


def test_sum():
    response = client.post("/sum", json={"numbers": [1, 2, 3]})

    assert response.status_code == 200
    assert response.get_json()["sum"] == 6
