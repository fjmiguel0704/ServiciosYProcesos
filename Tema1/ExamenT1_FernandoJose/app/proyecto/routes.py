from flask import *
from flask_jwt_extended import jwt_required
from utls.functions import *

rutaFicheroProyecto = "app/ficheros/proyecto.json"
rutaFicheroDepartamento = "app/ficheros/departamento.json"

proyectoBP = Blueprint('proyecto', __name__)

@proyectoBP.get("/")
def get_proyectos():
    proyectos = leeFichero(rutaFicheroProyecto)
    return jsonify(proyectos)

@proyectoBP.post("/")
def add_proyecto():
    proyectos = leeFichero(rutaFicheroProyecto)
    if request.is_json:
        proyecto = request.get_json()
        proyecto["id"] = find_next_idProyecto(proyectos)
        if proyecto["id"] == rutaFicheroDepartamento[id]:
            proyectos.append(proyecto)
            escribeFichero(proyectos)
            return proyecto, 201
        return {"El id departamento no existe"}
    return {"El formato debe ser Json"}, 415

@proyectoBP.delete("/")
@jwt_required()
def eliminar_proyecto(id):
    proyectos = leeFichero(rutaFicheroProyecto)
    for proyecto in proyectos:
        if proyecto["id"] == id:
            proyectos.remove(proyecto)
            escribeFichero(proyectos)
            return "{}", 200
    return {"El proyecto no existe"}, 404
    