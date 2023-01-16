import requests

#BASE = "http://127.0.0.1:5000/"

data = {
    "band_name": "ACDC",
    "band_genre": "Rock",
    "gigs": 100,
    "rating": 4
}

response = requests.post("http://127.0.0.1:5000/bands", json=data)

if response.status_code == 201:
    print("201!")
    print(response.json())
else:
    print("Error:", response.status_code)

response = requests.get("http://127.0.0.1:5000/bands/1")

if response.status_code == 200:
    print("200!")
    print(response.json())
else:
    print("Error:", response.status_code)


