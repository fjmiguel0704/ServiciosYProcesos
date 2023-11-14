import requests

api_url = "http://localhost:5050/autor/2"
dict = {"apellidos": "Jimenez Dominguez"}
response = requests.patch(api_url,json=dict)

print("Codigo de estado: ", response.status_code)

print(response.json())