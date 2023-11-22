from SumaRecorreNumeros import sumaNumeros
from multiprocessing import *

if __name__ == "__main__":
    with Pool (processes=3) as pool:
        pool.starmap(sumaNumeros, [(10,20),(15,5),(5,10)])

    print("Todos los procesos han terminado")