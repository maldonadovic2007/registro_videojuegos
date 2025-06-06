#registro de videojuegos: 

videojuegos = []

plataformas = ("pc", "ps5", "xbox series x", "nintendo switch")

while True:
    print("\n---menu de videojuegos ---")
    print("1. ingresar videojuego")
    print("2. ver videojuego")
    print("3. modificar videojuego")
    print("4. eliminar videojuego")
    print("5. salir")

    opcion = input("seleccione una opcion (1-5): ")

    if opcion =="1":
        codigo = input("ingrese el codigo del videojuego: ")
        nombre = input("ingrese el nombre del juego:")
        genero = input("ingrese el genero del videojuego")
        
        print("\nplataformas disponibles:" )
        print ("1. pc")
        print ("2. ps5") 
        print ("3. xbox series x ")
        print ("4. nintendo switch")

        plataforma_codigo = input("selecciones el numero de la plataforma: ")
        plataforma = plataformas[plataforma_codigo - 1 ]

        videojuego = { "codigo": codigo, 
                       "nombre": nombre,
                       "genero": genero,
                       "plataforma": plataforma,
        }
        
        videojuegos.append(videojuego)
        print("videojuego registrado exitosamente")


    elif opcion=="2":
        if len (videojuegos) == 0:
            print("no hay videojuegos registrados: ")
            for v in videojuegos:
                print(f"codigo: {v['codigo']}, nombre: {v['nombre']}, genero: {v['genero']}, plataforma: {v['plataforma']}")
                
    elif opcion=="3":
        codigo = input/("ingrese el codigo del videojuego a modificar: ")
        encontrado = False
        for v in videojuegos:
            if v["codigo"] == codigo:
               v["nombre"] = input ("nuevo nombre: ")
               v["genero"] = input ("nuevo genero: ")

               print("\nplataformas disponibles:" )
               print ("1. pc")
               print ("2. ps5") 
               print ("3. xbox series x ")
               print ("4. nintendo switch")

               plataforma_codigo = input("selecciones el numero de la plataforma: ")
        plataforma = plataformas[plataforma_codigo - 1 ] 
        print("videojuego registrado exitosamente")
        encontrado = True
        break
if not encontrado:
    print("videojuego no encontrado.")

elif opcion=="4":
    
    codigo = input("ingrese el codigo del videojuego a eliminar: ")
    eliminado = False
    for v in videojuegos:
        if v ["codigo"] == codigo:
            videojuegos.remove(v)
            print("videojuego eliminado correctamente: ")
            eliminado = True
            break
        if not eliminado:
            print("videojuego no encontrado.")

        elif opcion =="5":
            print("saliendo del programa")
            break
        else:
            print("opcion no valida")

