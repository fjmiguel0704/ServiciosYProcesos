import requests

api_url = "http://localhost:5050/autor"

dict = {"dni": "29566530D", "nombre": "Juan", "apellidos": "Jimenez Rodriguez"}

response = requests.post(api_url, json=dict)

print(response.status_code)
print(response.json())