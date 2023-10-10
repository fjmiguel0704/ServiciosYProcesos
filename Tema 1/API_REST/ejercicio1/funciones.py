import requests

def getAllPosts(url):
    response = requests.get(url)
    if response.status_code == 200:
        lista = response.json()
    for diccionario in lista:
        for clave in diccionario:
            print (clave, ":", diccionario[clave])
        print()
#s
def getPost(url, numPubl):
    response = requests.get(url+"/"+str(numPubl))
    if response.status_code == 200:
        diccionario = response.json()
        for clave in diccionario:
            print(clave, ":", diccionario[clave])
            print()
    else:
        print("La petición no ha terminado correctamente. Código: ", response.status_code)

