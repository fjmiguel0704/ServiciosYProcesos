import requests

api_url = "http://localhost:5050/autor/2"

dict = {"dni": "524586524D", "nombre": "Luis", "apellidos": "Jimenez Rodriguez"}

response = requests.put(api_url, json=dict)

print(response.status_code)
print(response.json())