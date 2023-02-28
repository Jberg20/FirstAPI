import requests

BASE = "http://127.0.0.1:5000/"

# Add a new band to the database
data = {
    "band_name": "ACDC",
    "band_genre": "Rock",
    "gigs": 100,
    "rating": 4
},
{
    "band_name": "King Crimson",
    "band_genre": "Progressive Rock",
    "gigs": 10,
    "rating": 3
}

response = requests.post(BASE + "bands", json=data)

if response.status_code == 201 or 200:
    print("Successfully added band!")
else:
    print("Error:", response.status_code)

# Get the band with ID 1
response = requests.get(BASE + "bands/1")

if response.status_code == 200:
    print("Successfully retrieved band!")
    print(response.json())
else:
    print("Error:", response.status_code)
