import requests

BASE_URL = "https://api.example.com"

def test_users_schema():
    # Call API endpoint to fetch users
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200  # Validate status code

    data = response.json()  # Convert response to JSON

    # Validate top-level structure
    assert isinstance(data, dict)
    assert "users" in data
    assert isinstance(data["users"], list)

    # Validate structure of first user object
    if data["users"]:
        user = data["users"][0]
        assert "id" in user
        assert "name" in user
        assert "email" in user
