import pytest
import requests

BASE_URL = "https://api.example.com"

@pytest.mark.parametrize("endpoint, expected_status", [
    ("/health", 200),
    ("/bad-request", 400),
    ("/unauthorized", 401),
    ("/server-error", 500),
])
def test_status_codes(endpoint, expected_status):
    # Send request to different endpoints
    response = requests.get(f"{BASE_URL}{endpoint}")

    # Validate expected HTTP status code
    assert response.status_code == expected_status
