import requests

api_url = "http://localhost:5050/autor/2"
response = requests.delete(api_url)

print("Codigo de estado: ", response.status_code)

print(response.json())