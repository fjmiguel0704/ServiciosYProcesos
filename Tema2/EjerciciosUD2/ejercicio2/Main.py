from SumaRecorreNumeros import sumaNumeros
from multiprocessing import *
import time

if __name__ == "__main__":
    inicio = time.time()
    pool = Pool(processes=3)
    numero = [(3, ), (4, ), (5, )]

    resultado = pool.starmap(sumaNumeros, numero)

    pool.close
    fin = time.time()
    print(resultado)
    print("Todos los procesos han terminado")
    print(fin - inicio)