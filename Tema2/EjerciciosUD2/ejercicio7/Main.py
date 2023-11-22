from multiprocessing import *
from Funciones import sumaNumeros, leeNumFichero 

if __name__ == '__main__':
    queue = Queue()

    p1 = Process(target=sumaNumeros, args=(queue,))
    p2 = Process(target=leeNumFichero, args=(queue,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Todos los procesos han terminado")   