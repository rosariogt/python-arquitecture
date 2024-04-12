import requests

URL = 'http://localhost:8000'

response = requests.get(URL)
HEADERS = { 'accept':'application/json'}

response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    print("Peticion exitosa")

    print(response.content)