import pytest

from app import app, TASKS


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client


def test_home_returns_http_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_returns_json(client):
    response = client.get("/")
    assert response.is_json


def test_home_returns_expected_tasks(client):
    response = client.get("/")
    assert response.get_json() == [
        {"id": 1, "title": "Estudar Docker"},
        {"id": 2, "title": "Criar o pipeline"},
    ]


def test_tasks_constant_has_two_items():
    assert len(TASKS) == 2
