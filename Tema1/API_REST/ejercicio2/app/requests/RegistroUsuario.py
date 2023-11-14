import requests

api_url = "http://localhost:5050/users"

dict = {"usuario": "Yeri", "contraseña": "buenas"}

response = requests.post(api_url, json=dict)

print(response.status_code)
print(response.json())