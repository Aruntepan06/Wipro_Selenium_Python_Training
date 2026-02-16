import requests

try:
    response = requests.delete(
        "https://videogamedb.uk:443/api/v2/videogame/0"
    )

    print(response)

    if response.status_code == 200:
        print("Delete successful (200 OK)")

    elif response.status_code == 204:
        print("Delete successful (204 No Content)")

    elif response.status_code == 404:
        print("Error: Resource not found (404)")

    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
