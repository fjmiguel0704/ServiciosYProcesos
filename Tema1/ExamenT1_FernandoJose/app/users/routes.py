import bcrypt
from flask import *
from flask_jwt_extended import create_access_token 
from app.utls.functions import *

rutaFicheroUsuarios = "app/ficheros/users.json"

usersBp = Blueprint("users", __name__)

@usersBp.post("/")
def registroUsuario():
    usuarios = leeFichero(rutaFicheroUsuarios)
    if request.is_json:
        usuario = request.get_json()
        contraseña = usuario["contraseña"].encode("utf-8")
        salt = bcrypt.gensalt()
        hashContraseña = bcrypt.hashpw(contraseña, salt).hex()
        usuario["contraseña"] = hashContraseña
        usuarios.append(usuario)
        escribeFichero(rutaFicheroUsuarios, usuarios)
        token = create_access_token(identity=usuario["usuario"])
        return {"token" : token}, 201
    return {"Debe ser formato Json"}, 415

@usersBp.get("/")
def loginUsuario():
    usuarios = leeFichero(rutaFicheroUsuarios)
    if request.is_json:
        usuario = request.get_json()
        nombreUsuario = usuario ["usuario"]
        contraseña = usuario["contraseña"].encode("utf-8")
        for unUsuario in usuarios:
            if unUsuario["usuario"] == nombreUsuario:
                unaContraseña = unUsuario["contraseña"]
                if bcrypt.checkpw(contraseña, bytes.fromhex(unaContraseña)):
                    token = create_access_token(identity=nombreUsuario)
                    return {"token":token}, 200
                else:
                    return {"No autorizado"}, 401
        return {"Usuario no encontrado"}
    return {"Debe ser formato Json"}