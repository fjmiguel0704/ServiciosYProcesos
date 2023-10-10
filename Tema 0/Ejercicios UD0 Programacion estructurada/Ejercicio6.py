numero = int (input("Introduce un número: "))
multiplicacion = 1
for contador in range (numero, 0, -1):
    multiplicacion*=contador
print(multiplicacion)