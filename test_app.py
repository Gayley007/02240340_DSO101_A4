import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home():
    assert 1 + 1 == 2


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Calculator API"


def test_add(client):
    response = client.get("/add?a=3&b=4")
    assert response.status_code == 200
    assert response.get_json()["result"] == 7.0


def test_add_negative(client):
    response = client.get("/add?a=-5&b=3")
    assert response.get_json()["result"] == -2.0


def test_subtract(client):
    response = client.get("/subtract?a=10&b=4")
    assert response.status_code == 200
    assert response.get_json()["result"] == 6.0


def test_subtract_negative_result(client):
    response = client.get("/subtract?a=2&b=9")
    assert response.get_json()["result"] == -7.0


def test_multiply(client):
    response = client.get("/multiply?a=6&b=7")
    assert response.status_code == 200
    assert response.get_json()["result"] == 42.0


def test_multiply_by_zero(client):
    response = client.get("/multiply?a=100&b=0")
    assert response.get_json()["result"] == 0.0


def test_divide(client):
    response = client.get("/divide?a=20&b=4")
    assert response.status_code == 200
    assert response.get_json()["result"] == 5.0


def test_divide_by_zero(client):
    response = client.get("/divide?a=10&b=0")
    assert response.status_code == 400
    assert "error" in response.get_json()
