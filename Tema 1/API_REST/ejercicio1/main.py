from funciones import * 
url = "https://jsonplaceholder.typicode.com/posts"
opcion = 1

while opcion!=0:
    print ("Selecciona una opción")
    print ("1. Mostrar todas las publicaciones")
    print ("2. Mostrar una publicación concreta")
    print ("3. Añadir una nueva publicación")
    print ("0. Salir del programa")

    opcion = int(input())

    if opcion == 1:
        # Mostrar todas las peticiones
        getAllPosts(url)

    elif opcion == 2:
        numeroPubli = int (input("Introdice un número de publicación (1-100): "))
        getPost(url, numeroPubli)
