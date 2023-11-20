from multiprocessing import *
import time

def suma (num1, num2):
    return num1 + num2

if __name__ == "__main__":
    inicio = time.time()
    pool = Pool(processes=2)
    numeros = [(1,2),(3,4),(5,6),(7,8)]

    resultados = pool.starmap(suma, numeros)

    pool.close
    fin = time.time()
    print(resultados)
    print(fin - inicio)