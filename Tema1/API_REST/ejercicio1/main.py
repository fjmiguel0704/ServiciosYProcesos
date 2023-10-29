from funciones import * 
url = "https://jsonplaceholder.typicode.com/posts"
opcion = 1

while opcion!=0:
    print ("Selecciona una opción")
    print ("1. Mostrar todas las publicaciones")
    print ("2. Mostrar una publicación concreta")
    print ("3. Añadir una nueva publicación")
    print ("4. Modificar todos los datos de una publicación")
    print ("5. Modificar un dato concreto de una publicación")
    print ("6. Eliminar una publicación")
    print ("0. Salir del programa")

    opcion = int(input())

    if opcion == 1:
        # Mostrar todas las peticiones
        getAllPosts(url)

    elif opcion == 2:
        numeroPubli = int (input("Introdice un número de publicación (1-100): "))
        getPost(url, numeroPubli)

    elif opcion == 3:
        userId = int (input("Introduce el id de usuario: "))
        id = int (input("Introduce el id: "))
        title = input("Introduce el título de la publicación: ")
        body = input("Introduce el cuerpo de la publicación: ")
        addPost (url, userId, id, title, body)

    elif opcion == 4:
        idModificar = int (input("Introduce el id del recurso a modificar: "))
        url = "https://jsonplaceholder.typicode.com/posts/" + str(idModificar)
        newUserId = int (input("Introduce el nuevo id de usuario: "))
        newId = int (input("Introduce el nuevo id: "))
        newTitle = input("Introduce el nuevo título de la publicación: ")
        newBody = input("Introduce el nuevo cuerpo de la publicación: ")
        modAllPost(url, newUserId, newId, newTitle, newBody)

    elif opcion == 5:
        idMod = int (input("Introduce el id del recurso a modificar: "))
        url = "https://jsonplaceholder.typicode.com/posts/" + str(idMod)
        opcionCampo = 0
        print ("1. userId")
        print ("2. id")
        print ("3. title")
        print ("4. body")
        opcionCampo = int (input("¿Qué desea modificar?: "))

        if opcionCampo == 1:
            campoModificar = "userId"
            nuevoDato = int (input("Introduce el nuevo id de usuario: "))
        elif opcionCampo == 2:
            campoModificar = "id"
            nuevoDato = int (input("Introduce el nuevo id: "))
        elif opcionCampo == 3:
             campoModificar = "title"
             nuevoDato = input("Introduce el nuevo título de la publicación: ")
        elif opcionCampo == 4:
            campoModificar = "body"
            nuevoDato = input("Introduce el nuevo cuerpo de la publicación: ")

        modOnePost(url, campoModificar, nuevoDato)

    elif opcion == 6:
        idEliminar = int (input("Introduce el id del recurso a eliminar: "))
        url = "https://jsonplaceholder.typicode.com/posts/" + str(idEliminar)
        delPost (url)