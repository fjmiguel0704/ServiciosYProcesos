import requests

def getAllPosts(url):
    response = requests.get(url)
    if response.status_code == 200:
        lista = response.json()
    for diccionario in lista:
        for clave in diccionario:
            print (clave, ":", diccionario[clave])
        print()
        
def getPost(url, numPubl):
    response = requests.get(url+"/"+str(numPubl))
    if response.status_code == 200:
        diccionario = response.json()
        for clave in diccionario:
            print(clave, ":", diccionario[clave])
            print()
    else:
        print("La petición no ha terminado correctamente. Código: ", response.status_code)

def addPost(url, idUsuario, id, titlePost, bodyPost):
    todo = {"userId":idUsuario, "id":id, "title": titlePost, "body":bodyPost}
    response = requests.post(url, json=todo)
    if response.status_code == 201:
        diccionario = response.json()
        for claves in diccionario:
            print(claves, ":", diccionario[claves])
    else:
        print("La petición no ha terminado correctamente. Código: ", response.status_code)

def modAllPost (url, newUserId, newId, newTitle, newBody):
    todo = {"userId": newUserId, "id": newId, "title": newTitle, "body": newBody}
    response = requests.put(url, json=todo)
    if response.status_code == 200:
        diccionario = response.json()
        for claves in diccionario:
            print(claves, ":", diccionario[claves] )

    else:
        print("La petición no ha terminado correctamente. Código: ", response.status_code)

def modOnePost (url, campoModificar, nuevoDato):
    todo = {campoModificar: nuevoDato}
    response = requests.patch(url, json=todo)
    if response.status_code == 200:
        diccionario = response.json()
        for claves in diccionario:
            print(claves, ":", diccionario[claves] )

    else:
        print("La petición no ha terminado correctamente. Código: ", response.status_code)

def delPost (url):
    response = requests.delete(url)
    if response.status_code == 200:
        diccionario = response.json()
        for claves in diccionario:
            print(claves, ":", diccionario[claves])
    else:
        print("La petición no ha terminado correctamente. Código: ", response.status_code)