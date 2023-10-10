def comprobarVocal (letra):
    esVocal = False
    if letra == "a" or letra == "e" or letra == "i" or letra== "o" or letra == "u": 
        esVocal = True
    return esVocal

letra = input("Introduce una letra: ")
letraMin = letra.lower()
print("Es voval" if comprobarVocal(letraMin) else "No es vocal") 