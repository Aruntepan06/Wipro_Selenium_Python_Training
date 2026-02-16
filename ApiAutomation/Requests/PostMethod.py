import requests

try:
      
    data = {
        "category": "Platform",
        "name": "Mario",
        "rating": "Mature",
        "releaseDate": "2012-05-04",
        "reviewScore": 85
    }

    response = requests.post(
        "https://videogamedb.uk:443/api/v2/videogame",
        json=data
    )

    print("POST Response:", response)

    if response.status_code == 200:
        print("POST Status code is 200 OK")
        result = response.json()
        print("POST Data:", result)
    else:
        print(f"POST Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
