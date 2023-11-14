import requests

api_url = "http://localhost:5050/users/"

dict = {"nombre": "Fernando", "contraseña": "12345"}

response = requests.post(api_url, json=dict)

print(response.status_code)
print(response.json())