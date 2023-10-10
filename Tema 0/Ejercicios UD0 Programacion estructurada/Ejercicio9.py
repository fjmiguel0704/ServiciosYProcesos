
def numerosComprendidos(numero1, numero2):
    comprendidos = int
    if numero1<numero2:
        for i in range(numero1+1,numero2):
            comprendidos = i
            print(comprendidos)
    else:
        for i in range (numero2+1, numero1):
            comprendidos = i
            print(comprendidos)

numero1 = int (input("Introduce el primer número: "))
numero2 = int (input("Introduce el segundo número: "))
numerosComprendidos (numero1, numero2)
