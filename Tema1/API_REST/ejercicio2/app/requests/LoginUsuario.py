import requests

api_url = "http://localhost:5050/users/"

token = 'token_creado'
headers = {'Authorization' : 'Bearer ' + token}
response = requests.get(api_url, headers=headers)


if(response.status_code == 200):
    lista = response.json()
    for element in lista:
        for clave in element:
            print(clave,": ", element[clave])
        print()
else:
    print("La peticion no ha terminado correctamente ", response.status_code)