import bcrypt
from flask_jwt_extended import create_access_token
from  app.funciones.funciones import *

from flask import Blueprint, request

ficheroUsuarios = "../ejercicio2/ficheros/users.json"

usersBP = Blueprint('users', __name__)


@usersBP.post('/')
def registroUsuario():
    usuarios = leeFichero(ficheroUsuarios)
    if request.is_json:
        usuario = request.get_json()
        contraseña = usuario["contraseña"].encode("utf-8")
        salt = bcrypt.gensalt()
        hashPassword = bcrypt.hashpw(contraseña, salt).hex()
        usuario['contraseña'] = hashPassword
        usuarios.append(usuario)
        escribeFichero(ficheroUsuarios, usuarios)
        token = create_access_token(identity=usuario['usuario'])
        return {'token': token}, 201
    return {"error": "Debe ser formato JSON"}, 415

@usersBP.get('/')
def loginUsuario():
    usuarios = leeFichero(ficheroUsuarios)
    if request.is_json:
        usuario = request.get_json()
        nombreUsuario = usuario['usuario']
        contraseña = usuario["contraseña"].encode("utf-8")  
        for userFile in usuarios:
            if userFile['usuario'] == nombreUsuario:
                ficheroContraseñas = userFile['contraseña']
                if bcrypt.checkpw(contraseña, bytes.fromhex(ficheroContraseñas)):
                    token = create_access_token(identity=nombreUsuario)
                    return {'token': token}, 200
                else:
                    return {'error': 'No autorizado'}, 401
        return {'error': 'Usuario no encontrado'}, 404
    return {"error": "Debe ser formato JSON"}, 415