import requests

# 1
r = requests.get("https://jsonplaceholder.typicode.com/users")
r.raise_for_status()
for u in r.json():
    print(u["name"], u["email"])

# 2
r = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": 2})
r.raise_for_status()
print(len(r.json()))

# 3
payload = {"title": "hello", "body": "world", "userId": 1}
r = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
print(r.status_code)
assert r.status_code == 201

# 4
# data=  -> form-encoded (or raw body) like application/x-www-form-urlencoded
# json=  -> sends JSON body and sets Content-Type: application/json automatically

# 5
r = requests.get("https://jsonplaceholder.typicode.com/users")
if r.status_code != 200:
    raise requests.HTTPError(f"Bad status: {r.status_code}", response=r)

# 6
r = requests.get("https://jsonplaceholder.typicode.com/users")
r.raise_for_status()
for u in r.json():
    print(u["username"].upper())

# 7
try:
    r = requests.get("https://jsonplaceholder.typicode.com/users", timeout=2)
    r.raise_for_status()
    print("OK")
except requests.exceptions.Timeout:
    print("Timeout happened")

# 8
s = requests.Session()
r1 = s.get("https://httpbin.org/cookies/set", params={"mycookie": "123"})
r2 = s.get("https://httpbin.org/cookies")
print(r2.json())

# 9
with open("sample.txt", "w") as f:
    f.write("hello")
with open("sample.txt", "rb") as f:
    r = requests.post("https://httpbin.org/post", files={"file": f})
print(r.json())

# 10
r = requests.get("https://jsonplaceholder.typicode.com/posts")
r.raise_for_status()
with open("posts.json", "w", encoding="utf-8") as f:
    f.write(r.text)
