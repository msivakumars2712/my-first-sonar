from app import create_app
import pytest


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "welcome to my-first-sonar"}
