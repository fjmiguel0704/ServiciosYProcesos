def menu():
    print("¿Qué desea hacer?")
    print("1. SUMAR")
    print("2. RESTA")
    print("3. MULTIPLICACIÓN")
    print("4. DIVISIÓN")

def calculadora(num1, num2, opc):
    resultado = 0
    switch = {
        1: num1+num2,
        2: num1-num2,
        3: num1*num2,
        4: num1/num2
    }
    return switch.get(opc)



numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
menu()
opcion = int (input("Seleccione una opción: "))
print(calculadora(numero1, numero2, opcion))