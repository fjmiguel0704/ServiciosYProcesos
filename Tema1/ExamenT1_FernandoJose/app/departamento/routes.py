from flask import *
from flask_jwt_extended import jwt_required
from app.utls.functions import *

rutaFicheroDepartamento = "app/ficheros/departamento.json"
rutaFicheroProyecto = "app/ficheros/proyecto.json"

departamentoBP = Blueprint('departamento', __name__)

@departamentoBP.get("/<int:id>")
def get_departamentoId(id):
    departamentos = leeFichero(rutaFicheroDepartamento)
    for departamento in departamentos:
        if departamento["id"] == id:
            return departamento, 200
    return {"Departamento no encontrado"}
   
@departamentoBP.get("/<int:id>/proyecto")
def get_proyecto(id):
    lista = []
    proyectos = leeFichero(rutaFicheroProyecto)
    for proyecto in proyectos:
        if proyecto["id"] == id:
            lista.append(proyecto)
    if len(lista) >0:
        return lista, 200
    else:
        return {"No existe proyecto para este departamento"}, 404
    
@departamentoBP.put("/<int:id>")
@jwt_required()
def modificar_departamento(id):
    departamentos = leeFichero(rutaFicheroDepartamento)
    if departamentos ["id"] == id:       
        if request.is_json:
            nuevoDepartamento = request.get_json()
            for departamento in departamentos:
                if departamento["id"] == id:
                    for element in nuevoDepartamento:
                        departamento[element] = nuevoDepartamento [element]
                    escribeFichero(rutaFicheroDepartamento, departamentos)
                    return departamento, 200
        return {"El formato debe ser Json"}, 415
    else:
        if request.is_json:
            departamento = request.get_json()
            departamento["id"] = find_next_idProyecto(departamentos)
            departamentos.append(departamento)
            escribeFichero(departamentos)
            return departamento, 201
        return {"El formato debe ser Json"}, 415

    

