import pytest
import requests

@pytest.fixture
def base_url():
    # Provide base API URL
    return "https://api.example.com"

@pytest.fixture
def auth_token(base_url):
    # Login and generate auth token
    response = requests.post(
        f"{base_url}/auth/login",
        json={"username": "test_user", "password": "test_pass"}
    )
    return response.json()["token"]  # Return token to dependent fixtures

@pytest.fixture
def user(base_url, auth_token):
    # Create user using base_url and auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(
        f"{base_url}/users",
        json={"name": "Chain User", "email": "chain@example.com"},
        headers=headers
    )
    user = response.json()

    yield user  # Provide user to test

    # Cleanup: delete user after test finishes
    requests.delete(f"{base_url}/users/{user['id']}", headers=headers)


def test_user_chain(user):
    # Validate user object received from fixture chain
    assert "id" in user
