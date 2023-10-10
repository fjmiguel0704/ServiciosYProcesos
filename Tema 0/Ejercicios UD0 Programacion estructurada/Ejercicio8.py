numero = int (input("Introduce un número: "))
for contador in range (numero+1):
    print(' '*(numero-contador)+'* '*contador)