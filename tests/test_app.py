import pytest
from app import app, members


@pytest.fixture
def client():
    app.config["TESTING"] = True
    members.clear()

    with app.test_client() as client:
        yield client

    members.clear()


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_programs(client):
    response = client.get("/programs")
    assert response.status_code == 200
    assert len(response.json) == 3


def test_add_member(client):
    response = client.post(
        "/members",
        json={"name": "Harsha"}
    )

    assert response.status_code == 201
    assert response.json["name"] == "Harsha"


def test_add_member_without_name(client):
    response = client.post("/members", json={})
    assert response.status_code == 400