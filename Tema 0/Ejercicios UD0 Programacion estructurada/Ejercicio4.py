import random


aleatorio = random.randint(1, 100)
numero = int(input("Introduce el número a adivinar: "))
while numero!=aleatorio and numero>=0:
    if numero < aleatorio:
        print ("EL número es menor al que se intenta adivinar")
    else:
        print("EL número es mayor al que se intenta adivinar")
    numero = int(input("Introduce el número a adivinar: "))

if numero==aleatorio:
    print("Has acertado")
else:
    print("Te has rendido, el número era: ", aleatorio)