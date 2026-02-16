import requests

try:

    data = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

    response = requests.post(
        "https://api.restful-api.dev/objects",
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
