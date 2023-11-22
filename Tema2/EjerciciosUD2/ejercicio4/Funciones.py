from queue import Queue

def leeNumFichero(tuberia):
    rutaArchivo="ejercicio3/numeros.txt"
    with open(rutaArchivo,'r') as archivo:
        for numero in archivo:
            tuberia.send(int (numero))
    tuberia.send(None)

def sumaNumeros (tuberiaNumeros):
    resultado=0
    while True:
        numeros = tuberiaNumeros.recv()
        if (numeros == None):
            break
        for i in range (1, numeros+1):
            resultado+=i
        print (resultado)
