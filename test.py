import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "helloworld/Jack/22")
print(response.json())

response = requests.get(BASE + "helloworld/Jack/22")
print(response.json())

