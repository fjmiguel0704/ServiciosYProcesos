import requests

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.delete(url)

print ("Código de estado: ", response.status_code)
print(response.json())