from flask_jwt_extended import jwt_required
from  app.funciones.funciones import *

from flask import *

rutaFicheroLibro = "../ejercicio2/ficheros/libro.json"

libroBP = Blueprint('libro', __name__)

# Funcion que devuelve el proximo numero de id correspondiente
def find_next_id():
    libros = leeFichero(rutaFicheroLibro)
    # Guardamos el id maximo como 0
    max = libros[0]["id"]
    # Recorremos los libros en la lista libros uno a uno
    for libro in libros:
        # Comprobamos si el id es mayor al maximo
        if libro["id"] > max:
            # y lo sobreescribimos
            max = libro["id"]
    # devovemos el valor de ese id sumandole 1
    return max+1

@libroBP.get('/')
# Funcion que devuelve la lista de libros
def get_libro():
    libros = leeFichero(rutaFicheroLibro)
    return jsonify(libros)

@libroBP.get("/<int:id>")
# Funcion que devuelve un libro 
def get_libroId(id):
    libros = leeFichero(rutaFicheroLibro)
    # Recorremos los libros en la lista libros
    for libro in libros:
        # Si el id del libro es igual al que se desea buscar
        if libro['id'] == id:
            # Devuelve el libro
            return libro, 200
    # Devuelve un error al no encontrarse el libro
    return {"error": "Libro not found"}, 404

@libroBP.post("/")
@jwt_required()
# Funcion agregar libro
def add_libro():
    libros = leeFichero(rutaFicheroLibro)
    # Comprobamos si la petición está formato json
    if request.is_json:
        # Guardamos el formato JSON en una variable
        libro = request.get_json()
        # Le asignamos un nuevo id
        libro["id"] = find_next_id()
        # Añadimos el nuevo libro a la lista
        libros.append(libro)
        escribeFichero(rutaFicheroLibro, libros)
        # Devolvemos el libro en formato diccionario
        return libro, 201
    # Error en caso de no ser formato json
    return {"error": "Request must be JSON"}, 415

@libroBP.put("/<int:id>")
@libroBP.patch("/<int:id>")
@jwt_required()
# Funcion para modificar un libro
def modify_libro(id):
    libros = leeFichero(rutaFicheroLibro)
    # Comprobamos si la petición está formato json
    if request.is_json:
        # Guardamos el formato JSON en una variable
        newLibro = request.get_json()
        # Cogemos de nuestra lista de libros, el libro concreto a modificar, buscamos su id
        for libro in libros:
            if libro["id"] == id:
                # Modificamos todos los atributos del libro por los nuevos
                for element in newLibro:
                    libro[element] = newLibro[element]
                escribeFichero(rutaFicheroLibro, libros)
                # Devolvemos el libro en formato diccionario
                return libro, 200
    # Error en caso de no ser formato json
    return {"error": "Request must be JSON"}, 415

@libroBP.delete("/<int:id>")
@jwt_required()
# Funcion que elimina un recurso
def delete_libro(id):
    libros = leeFichero(rutaFicheroLibro)
    # Buscamos en la lista libros el id del recurso a eliminar
    for libro in libros:
        if libro['id'] == id:
            libros.remove(libro)
            escribeFichero(rutaFicheroLibro, libros)
            # Si se encuentra el libro, se devuelve el libro vacío
            return {}, 200
    # Si no se encuentra, se devuelve un error
    return {"error": "Libro not found"}, 404