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
        # parse the json file
        data = response.json()
        # text of the response file
        print(response.text)
        # content e of the response
        print(response.content)
        #  status code of the response
        print(response.status_code)
        # headers
        print(response.headers)
        # history
        print(response.history)
        # url
        print(response.url)
        # fecth the single header
        content_type = response.headers.get('Content-Type')
        print(content_type)
        result = response.json()
        print(result)
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
