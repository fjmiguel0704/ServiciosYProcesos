import requests

api_url = "http://localhost:5050/proyecto/1"

dict = {"nombre": "negocio", "descripcion": "buenas", "idDepartamento": 2}

response = requests.post(api_url, json=dict)

print(response.status_code)
print(response.json())