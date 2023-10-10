numero = int(input('Introduce un número entero positivo: '))
def esPrimo(num):
    primo = True
    for i in range (2, num):
        if num%i == 0:
            primo = False
            break
    if primo:
        print("Es primo")
    else:
        print("No es primo")
esPrimo(numero)