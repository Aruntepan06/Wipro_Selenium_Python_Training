import requests
from requests.auth import HTTPBasicAuth

try:

    headers = {
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json"
    }

    data = {
        "name": "Mario"
    }

    response = requests.patch(
        "https://api.restful-api.dev/objects/ff8081819c5368bb019c5599418a0451",
        headers=headers,
        auth=HTTPBasicAuth("username", "password"),
        json=data
    )

    print(response)

    if response.status_code == 200:
        print("Status code is 200 OK")
        result = response.json()
        print(result)
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
