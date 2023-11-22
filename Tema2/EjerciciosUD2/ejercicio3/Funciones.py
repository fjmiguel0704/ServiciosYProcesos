from queue import Queue

def leeNumFichero(queue):
    rutaArchivo="ejercicio3/numeros.txt"
    with open(rutaArchivo,'r') as archivo:
        for numero in archivo:
            queue.put(int (numero))
    queue.put(None)

def sumaNumeros (queueNumeros):
    resultado=0
    while True:
        numeros = queueNumeros.get()
        if (numeros == None):
            break
        for i in range (1, numeros+1):
            resultado+=i
        print (resultado)
