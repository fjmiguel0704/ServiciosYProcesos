import requests

url = "https://jsonplaceholder.typicode.com/todos/6"

dict = {'userId':5}
response = requests.patch(url, json=dict)

print ("Código de estado: ", response.status_code)
print(response.json())