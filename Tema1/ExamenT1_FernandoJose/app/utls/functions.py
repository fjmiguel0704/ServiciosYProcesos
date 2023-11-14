import json

def leeFichero(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    try:
        data = json.load(archivo)
        archivo.close()
        return data
    except json.JSONDecodeError:
        return []
    
def escribeFichero(nombreArchivo, data):
    archivo = open(nombreArchivo, "w")
    json.dump(data, archivo)
    archivo.close()

def find_next_idProyecto(proyectos):
    return max (proyecto["id"] for proyecto in proyectos) + 1

def find_next_idDepartamento(departamentos):
    return max (departamento["id"] for departamento in departamentos) + 1
