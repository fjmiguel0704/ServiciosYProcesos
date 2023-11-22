from queue import Queue

def leeNumFichero(tuberia):
    rutaArchivo="ejercicio3/numeros.txt"
    with open(rutaArchivo,'r') as archivo:
        for numero in archivo:
            numeros = numero.split(",")
            tuberia.send(numeros[0], numeros[1])
        tuberia.send(None, None)
    

def sumaNumeros (tuberiaNumeros):
    resultado=0
    while True:
        numeros = tuberiaNumeros.recv()
        if (numeros[0] == None):
            break
        if (numeros[0] > numeros[1]):
            numeros = (numeros[1], numeros[0])
        for i in range (numeros[0], numeros[1]):
            resultado+=i
        print (resultado)
