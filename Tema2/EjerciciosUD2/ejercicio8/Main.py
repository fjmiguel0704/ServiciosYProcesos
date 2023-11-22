from multiprocessing import *
from Funciones import sumaNumeros, leeNumFichero 

if __name__ == '__main__':
    izq, der = Pipe()

    p1 = Process(target=sumaNumeros, args=(izq,))
    p2 = Process(target=leeNumFichero, args=(der,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()


    print("Todos los procesos han terminado")   