import requests

url = "https://jsonplaceholder.typicode.com/users/1/todos"

dict = {'id':203, 'userId':2, 'title': 'Hacer tareas', 'completed': False}
response = requests.post(url, json=dict)

print ("Código de estado: ", response.status_code)
print(response.json())