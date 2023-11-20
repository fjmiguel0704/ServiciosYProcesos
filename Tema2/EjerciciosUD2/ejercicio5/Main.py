from SumaRecorreNumeros import sumaNumeros
from multiprocessing import *

if __name__ == "__main__":
    process1 = Process(target=sumaNumeros, args=(10,20))
    process2 = Process(target=sumaNumeros, args=(15,5))
    process3 = Process(target=sumaNumeros, args=(5,10))
    process1.start()
    process2.start()
    process3.start()
    process1.join()
    process2.join()
    process3.join()
    print("Todos los procesos han terminado")