from queue import Queue

def leeNumFichero(queue):
    rutaArchivo="ejercicio3/numeros.txt"
    with open(rutaArchivo,'r') as archivo:
        for numero in archivo:
            numeros = numero.split(",")
            queue.put((int(numeros[0]), int(numeros[1])))
    queue.put(None, None)

def sumaNumeros (queueNumeros):
    resultado=0
    while True:
        numeros = queueNumeros.get()
        if (numeros[0] == None):
            break
        if (numeros[0] > numeros[1]):
            numeros = (numeros[1], numeros[0])
        for i in range (numeros[0], numeros[1]+1):
            resultado+=i
        print (resultado)
