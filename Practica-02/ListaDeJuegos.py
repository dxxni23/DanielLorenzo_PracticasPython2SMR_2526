############ PRACTICA 02 ############

#---Solución---#

Lista_De_Juegos = [['Catan', 4], ['Dixit', 2], ['Virus', 6], ['Carcassonne', 3]]
Eleccion = ""


while Eleccion != "h":
    print("----------- EL GAME ----------")
    print("a) Añadir un Nuevo Juego")
    print("b) Mostras la Lista")
    print("c) Mostras los juegos ordenados alfabeticamente, de la Z a la A")
    print("d) Mostrar los juegos ordenados por número de unidades (menor a mayor)")
    print("e) Elimina el Juego")
    print("f) Aplicar Mantenimiento")
    print("g) Prestación de Juego")
    print("h) Salir")
    Eleccion = input("-----¿Que Opción Eliges?-----: ")

    if Eleccion == "a":
        Nombre = int(input("Introduce el Nombre del Nuevo Jugo: "))
        Unidades = int(input("Introduce el Número de Unidades: "))
        Lista_De_Juegos.append(Nombre,Unidades)

    elif Eleccion == "b":
        print("La Lista de Juegos es: ", Lista_De_Juegos)
    
    elif Eleccion == "c":
        Lista_De_Juegos_Ordenada_Alfabeticamente = sorted(Lista_De_Juegos , key=lambda x: x[0], reverse=True)
        print(Lista_De_Juegos_Ordenada_Alfabeticamente)
    
    elif Eleccion == "d":
        Lista_De_Juegos_Ordenada_menorAmayor = sorted(Lista_De_Juegos, key=lambda x: x[1])
        print(Lista_De_Juegos_Ordenada_menorAmayor)

    elif Eleccion == "e":
        print(Lista_De_Juegos)
        Juego_Borrar = input("Introduce el juego que quieres borrar: ")
        for elemento in Lista_De_Juegos:
            if elemento[0].lower() == Juego_Borrar.lower():
                Juego_Borrar.append(elemento)
            for i in Juego_Borrar:
                Lista_De_Juegos.remove(i)

    elif Eleccion == "f":
        for x in range(len(Lista_De_Juegos)):
            if Lista_De_Juegos[x][1]<3:
                Lista_De_Juegos[x][1] = Lista_De_Juegos[x][1] + 2

    elif Eleccion == "g":
        print("La Lista de Juegos es: ", Lista_De_Juegos)
        Juego_Prestado = input("Introduce el juego que quieres: ")
        for elem in Lista_De_Juegos:
            if elem[0].lower() == Juego_Prestado.lower():
                encontrado = True
                if elem[1] == 0:
                    print("No quedan unidades de ese juego.")
                else:
                    elem[1] -= 1
                    print("Juego prestado correctamente. Quedan", elem[1], "unidades.")

    elif Eleccion == "h":
        print("Saliste Del programa")

    else:
        print("Opción No Valida")
