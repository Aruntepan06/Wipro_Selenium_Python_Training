import pytest
import requests

BASE_URL = "https://api.example.com"

@pytest.fixture
def test_user():
    # Create a user before test execution
    create_res = requests.post(
        f"{BASE_URL}/users",
        json={"name": "Test User", "email": "test@example.com"}
    )
    user = create_res.json()  # Store created user data

    yield user  # Provide user data to test

    # Delete user after test completes (cleanup)
    requests.delete(f"{BASE_URL}/users/{user['id']}")


def test_user_creation(test_user):
    # Validate user was successfully created
    assert "id" in test_user
