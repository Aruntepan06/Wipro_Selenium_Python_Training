import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def auth_token():
    # Generate authentication token once per test session
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"username": "test_user", "password": "test_pass"}
    )
    response.raise_for_status()  # Ensure login request is successful
    return response.json()["token"]  # Return token for reuse in tests


def test_profile(auth_token):
    # Use session token to access protected API
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{BASE_URL}/profile", headers=headers)
    assert response.status_code == 200  # Validate successful access
