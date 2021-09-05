import requests
import json

url = "http://localhost:5000"

headers = {}
headers["Content-Type"] = "application/json"

# Registration api
payload = {"name":"gokul","password":"gokul123"}
test_registration = requests.post(url+"/register",json=payload, headers=headers)
print(test_registration.text)


# Login api
test_login = requests.get(url+"/login", auth=('gokul', 'gokul123'))
print((test_login.json())["token"])

# Token
token = (test_login.json())["token"]

# All users list
test_users_get = requests.get(url+"/users")
print(test_users_get.text)

# Create author
headers = {}
headers["Content-Type"] = "application/json"
headers["x-access-tokens"] = token

test_create_author = requests.post(url+"/author", json ={"name":"u jones","book":"u October","country":"Canada"}, headers=headers)

print(test_create_author.text)