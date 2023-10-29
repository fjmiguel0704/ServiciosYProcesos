from  utils.funciones import *

from flask import Blueprint, jsonify, request

rutaFicheroLibro = "Tema1/API_REST/ejercicio2/ficheros/libro.json"

libroBP = Blueprint('libro', __name__)

def find_next_id():
    libros = leeFichero(rutaFicheroLibro)
    max = libros[0]["id"]
    for libro in libros:
        if libro["id"] > max:
            max = libro["id"]

    return max+1

@libroBP.get('/')
def get_libro():
    libros = leeFichero(rutaFicheroLibro)
    return jsonify(libros)

@libroBP.get("/<int:id>")
def get_libro(id):
    libros = leeFichero(rutaFicheroLibro)
    for libro in libros:
        if libro['id'] == id:
            return libro, 200
    return {"error": "Libro not found"}, 404

@libroBP.post("/")
# definimos la función correspondiente
def add_libro():
    libros = leeFichero(rutaFicheroLibro)
    # Comprobamos si la petición cumple con el formato json
    if request.is_json:
        # Guardamos el formato JSON
        libro = request.get_json()
        # Le asignamos un nuevo id
        libro["id"] = find_next_id()
        # Añadimos el nuevo país a nuestra lista
        libros.append(libro)
        escribeFichero(rutaFicheroLibro, libros)
        # Devolvemos el país en formato diccionario y 201
        return libro, 201
    # Si la petición no cumple con el formato JSON
    return {"error": "Request must be JSON"}, 415

@libroBP.put("/<int:id>")
@libroBP.patch("/<int:id>")
# definimos la función correspondiente
def modify_libro(id):
    libros = leeFichero(rutaFicheroLibro)
    # Se comprueba si la petición que nos ha llegado cumple con el formato json
    if request.is_json:
        # Creamos una variable donde guardamos el formato JSON, que coincide con un diccionario
        newLibro = request.get_json()
        # Tenemos que coger de nuestra lista de países, el país concreto a modificar, para lo cual
        # habrá que buscarlo por su id
        for libro in libros:
            if libro["id"] == id:
                # Modificamos todos los atributos del país con los nuevos valores indicados en el json
                for element in newLibro:
                    libro[element] = newLibro[element]
                escribeFichero(rutaFicheroLibro, libros)
                # Devolvemos el país en formato diccionario y el código 200 para indicar que se ha modificado
                return libro, 200
    # Si la petición no cumple con el formato JSON devuelve un mensaje de error y el código 415
    return {"error": "Request must be JSON"}, 415

@libroBP.delete("/<int:id>")
# Se debe añadir como parámetro de entrada el id que se 
# indica en la dirección
def delete_libro(id):
    libros = leeFichero(rutaFicheroLibro)
    # Como hay que eliminar un país concreto, tendremos que buscar 
    # en la lista el id del país que se ha indicado en la petición
    for libro in libros:
        if libro['id'] == id:
            libros.remove(libro)
            escribeFichero(rutaFicheroLibro, libros)
            # Si se encuentra el país, se devuelve el país ya vacío más el código 200
            return {}, 200
    # Si no se encuentra, se devuelve mensaje de error y código 404
    return {"error": "Libro not found"}, 404

if __name__ == '__main__':
    libroBP.run(debug=True, host='0.0.0.0', port=5051)