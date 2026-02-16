import requests

try:
    # Make A Get Request To A API Eendpoint
    response = requests.get("https://videogamedb.uk:443/api/v2/videogame")
    print(response)

    # Check if the status code is 200
    if response.status_code == 200:
        print("Status code is 200 OK")

        # Parse the json file
        data = response.json()
        print(data)

    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
