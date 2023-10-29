import requests

url = "https://jsonplaceholder.typicode.com/todos/199"
response = requests.get(url)

print ("Código de estado: ", response.status_code)
print (response.json())