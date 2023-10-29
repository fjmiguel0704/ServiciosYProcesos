from  utils.funciones import *

from flask import Blueprint, jsonify, request

rutaFicheroAutor = "app/ficheros/autor.json"
rutaFicheroLibro = "app/ficheros/libro.json"

autorBP = Blueprint('autor', __name__)

def find_next_id():
    autores = leeFichero(rutaFicheroAutor)
    max = autores[0]["id"]
    for autor in autores:
        if autor["id"] > max:
            max = autor["id"]

    return max+1

@autorBP.get('/')
def get_autor():
    autores = leeFichero(rutaFicheroAutor)
    return jsonify(autores)

@autorBP.get("/<int:id>")
def get_autor(id):
    autores = leeFichero(rutaFicheroAutor)
    for autor in autores:
        if autor['id'] == id:
            return autor, 200
    return {"error": "Autor not found"}, 404

@autorBP.post("/")
# definimos la función correspondiente
def add_autor():
    autores = leeFichero(rutaFicheroAutor)
    # Comprobamos si la petición cumple con el formato json
    if request.is_json:
        # Guardamos el formato JSON
        autor = request.get_json()
        # Le asignamos un nuevo id
        autor["id"] = find_next_id()
        # Añadimos el nuevo país a nuestra lista
        autores.append(autor)
        escribeFichero(rutaFicheroAutor, autores)
        # Devolvemos el país en formato diccionario y 201
        return autor, 201
    # Si la petición no cumple con el formato JSON
    return {"error": "Request must be JSON"}, 415

@autorBP.put("/<int:id>")
@autorBP.patch("/<int:id>")
# definimos la función correspondiente
def modify_autor(id):
    autores = leeFichero(rutaFicheroAutor)
    # Se comprueba si la petición que nos ha llegado cumple con el formato json
    if request.is_json:
        # Creamos una variable donde guardamos el formato JSON, que coincide con un diccionario
        newAutor = request.get_json()
        # Tenemos que coger de nuestra lista de países, el país concreto a modificar, para lo cual
        # habrá que buscarlo por su id
        for autor in autores:
            if autor["id"] == id:
                # Modificamos todos los atributos del país con los nuevos valores indicados en el json
                for element in newAutor:
                    autor[element] = newAutor[element]
                escribeFichero(rutaFicheroAutor, autores)
                # Devolvemos el país en formato diccionario y el código 200 para indicar que se ha modificado
                return autor, 200
    # Si la petición no cumple con el formato JSON devuelve un mensaje de error y el código 415
    return {"error": "Request must be JSON"}, 415

@autorBP.delete("/<int:id>")
# Se debe añadir como parámetro de entrada el id que se 
# indica en la dirección
def delete_autor(id):
    autores = leeFichero(rutaFicheroAutor)
    # Como hay que eliminar un país concreto, tendremos que buscar 
    # en la lista el id del país que se ha indicado en la petición
    for autor in autores:
        if autor['id'] == id:
            autores.remove(autor)
            escribeFichero(rutaFicheroAutor, autores)
            # Si se encuentra el país, se devuelve el país ya vacío más el código 200
            return {}, 200
    # Si no se encuentra, se devuelve mensaje de error y código 404
    return {"error": "Autor not found"}, 404

# Lista de jugadores por su equipo
@autorBP.get("/<int:id>/libro")
def get_libros(id):
    lista = []
    libros = leeFichero(rutaFicheroLibro)
    for libro in libros:
        if libro['id'] == id:
            lista.append(libro)
    if len(lista) > 0:
        return lista, 200
    else:
        return {"error": "No libros of this Autor"}, 404

if __name__ == '__main__':
    autorBP.run(debug=True, host='0.0.0.0', port=5051)