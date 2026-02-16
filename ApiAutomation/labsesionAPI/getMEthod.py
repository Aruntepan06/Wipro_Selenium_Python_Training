import requests

try:
    response = requests.get("https://api.restful-api.dev/objects")
    print(response)


    if response.status_code == 200:
        print("Status code is 200 OK")

       
        data = response.json()
        print(data)

    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
