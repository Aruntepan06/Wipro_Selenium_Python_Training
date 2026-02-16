import requests

try:
    data = {
        "category": "Platform",
        "name": "Arun",
        "rating": "Mature",
        "releaseDate": "2012-05-04",
        "reviewScore": 85
    }

    # make a PUT request to update videogame with id 0
    response = requests.put(
        "https://videogamedb.uk:443/api/v2/videogame/1",
        json=data
    )

    print(response)

    # check if the status code is 200 OK
    if response.status_code == 200:
        print("Status code is 200 OK")
        result = response.json()
        print(result)
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
