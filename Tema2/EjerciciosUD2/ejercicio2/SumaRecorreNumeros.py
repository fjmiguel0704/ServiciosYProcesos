def sumaNumeros(numero1, numero2):
    resultado = 0
    if numero2>numero1:
        for i in range(numero1, numero2+1):
            resultado+=i
        print ("Suma de numeros es del ",  numero1,  " al ", numero2, " es igual a ", resultado)
    else:
        for i in range(numero2, numero1+1):
            resultado+=i
        print ("Suma de numeros es del ",  numero2,  " al ", numero1, " es igual a ", resultado)
    