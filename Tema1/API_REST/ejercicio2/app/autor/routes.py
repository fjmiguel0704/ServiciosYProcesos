from  app.funciones.funciones import *

from flask import *

rutaFicheroAutor = "../ejercicio2/ficheros/autor.json"
rutaFicheroLibro = "../ejercicio2/ficheros/libro.json"

autorBP = Blueprint('autor', __name__)

# Funcion que devuelve el proximo numero de id correspondiente
def find_next_id():
    autores = leeFichero(rutaFicheroAutor)
    # Guardamos el id maximo como 0
    max = autores[0]["id"]
    # Recorremos los autores en la lista autores uno a uno
    for autor in autores:
        # Comprobamos si el id es mayor al maximo
        if autor["id"] > max:
            # y lo sobreescribimos
            max = autor["id"]
    # devovemos el valor de ese id sumandole 1
    return max+1

@autorBP.get('/')
# Funcion que devuelve la lista de autores
def get_autor():
    autores = leeFichero(rutaFicheroAutor)
    return jsonify(autores)

@autorBP.get("/<int:id>")
# Funcion que devuelve un autor
def get_autorId(id):
    autores = leeFichero(rutaFicheroAutor)
    # Recorremos los autores en la lista autores
    for autor in autores:
        # Si el id del autor es igual al que se desea buscar
        if autor['id'] == id:
            # Devuelve el autor
            return autor, 200
    # Devuelve un error al no encontrarse el autor
    return {"error": "Autor not found"}, 404

@autorBP.post("/")
# Funcion agregar autor
def add_autor():
    autores = leeFichero(rutaFicheroAutor)
    # Comprobamos si la petición está formato json
    if request.is_json:
        # Guardamos el formato JSON en una variable
        autor = request.get_json()
        # Le asignamos un nuevo id
        autor["id"] = find_next_id()
        # Añadimos el nuevo autor a la lista
        autores.append(autor)
        escribeFichero(rutaFicheroAutor, autores)
        # Devolvemos el autor en formato diccionario
        return autor, 201
    # Error en caso de no ser formato json
    return {"error": "Request must be JSON"}, 415

@autorBP.put("/<int:id>")
@autorBP.patch("/<int:id>")
# Funcion para modificar un autor
def modify_autor(id):
    autores = leeFichero(rutaFicheroAutor)
    # Comprobamos si la petición está formato json
    if request.is_json:
        # Guardamos el formato JSON en una variable
        newAutor = request.get_json()
        # Cogemos de nuestra lista de autores, el autor concreto a modificar, buscamos su id
        for autor in autores:
            if autor["id"] == id:
                # Modificamos todos los atributos del autor por los nuevos
                for element in newAutor:
                    autor[element] = newAutor[element]
                escribeFichero(rutaFicheroAutor, autores)
                # Devolvemos el autor en formato diccionario
                return autor, 200
    # Error en caso de no ser formato json
    return {"error": "Request must be JSON"}, 415

@autorBP.delete("/<int:id>")
# Funcion que elimina un recurso
def delete_autor(id):
    autores = leeFichero(rutaFicheroAutor)
    # Buscamos en la lista autores el id del recurso a eliminar
    for autor in autores:
        if autor['id'] == id:
            autores.remove(autor)
            escribeFichero(rutaFicheroAutor, autores)
            # Si se encuentra el autor, se devuelve el autor vacío
            return {}, 200
    # Si no se encuentra, se devuelve un error
    return {"error": "Autor not found"}, 404

@autorBP.get("/<int:id>/libro")
# Funcion que devuelve la lista de libros según su autor
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