import requests

api_url = "http://localhost:5050/departamento/1"

dict = {"nombre": "Fisica", "responsable": "Fernando"}

response = requests.put(api_url, json=dict)

print(response.status_code)
print(response.json())