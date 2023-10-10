def maximoNumeros (numero1, numero2):
    if numero1>numero2:
        return numero1
    else:
        return numero2
    
numero1 = int (input("Introduce el primer número: "))
numero2 = int (input("Introduce el segundo número: "))
print("El número mayor es: ")
print(maximoNumeros(numero1, numero2))