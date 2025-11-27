
Opcion_Elegida = ""
Elegir = 0
Lista_Catalogo =  [["Inception", "pelicula", "thriller", 5, 2010], 
                   ["One Piece", "serie", "anime", 4, 1999], 
                   ["La La Land", "pelicula", "romantica", 4, 2016], 
                   ["Stranger Things", "serie", "fantastica", 5, 2016], 
                   ["Superbad", "pelicula", "comedia", 4, 2007], 
                   ["La Comunidad del Anillo", "pelicula", "fantastica", 5, 2001]] 


while Opcion_Elegida != "d":

    print("----SALESIX----")

    print("a) Ver catálogo") 
    print("b) Filtrar por género") 
    print("c) Cambiar puntuación") 
    print("d) Salir") 

    Opcion_Elegida = input("Introduce la Opción que Quieras Elegir: ").lower()

    if Opcion_Elegida == "a":

        print("Elige una opción 1 / 2 / 3")
        print("1 / Catalogo Ordenado por Orden Alfabetico: ")
        print("2 / Catalogo Ordenado por Año: ")
        print("3 / Salir")

        while Elegir != 3:
            Elegir = int(input("Introduce la Opción que Quieras: "))
            if Elegir == 1:
                print("Catalogo Ordenado por Orden Alfabetico: ")
                Catalogo_Alfabetico = sorted(Lista_Catalogo, key=lambda x: x[0])
                print(Catalogo_Alfabetico)
            elif Elegir == 2:
                print("Catalogo Ordenado por Año: ")
                Catalogo_Año = sorted(Lista_Catalogo, key=lambda x: x[4], reverse=True)
                print(Catalogo_Año)
            elif Elegir == 3:
                print("Saliste")
            else:
                print("Opción no Valida")

    elif Opcion_Elegida == "b":
        Filtro_de_Genero = input("Introduce el Genero que Quieras: ")
        for i in Lista_Catalogo[2]:
            Genero_Igual = Filtro_de_Genero
            if Genero_Igual == i:
                print(Genero_Igual)
            else:
                print("No Hay Películas de ese Género")

    elif Opcion_Elegida == "c":
        PeliculaSerie_Para_Punturar = input("Introduce el Nombre de la Película / Serie, que quieres puntuar: ")



    elif Opcion_Elegida == "d":
        print("--- Saliste ---")

    else:
        ("Opción No Valida")
