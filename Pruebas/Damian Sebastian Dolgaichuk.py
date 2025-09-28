
print("\nBienvenido a la bibliteca de la UTN TUPaD - Gestión de Catálogo de Libros")
titulos = ["HARRY POTTER", "EL SEÑOR DE LOS ANILLOS", "EL PRINCIPITO", "DON QUIJOTE DE LA MANCHA", "CIEN AÑOS DE SOLEDAD"]
ejemplares = [0, 5, 2, 4, 1]
while True:
    print("\nMenú de Opciones:")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")
    valor = input("Seleccione una opción (1-8): ")

    if  menu == '1':
        titulo = ""
        cantidad = int(input("¿Cuántos títulos desea ingresar? "))
        if cantidad > 0:
            for i in range(cantidad):
                # standarizar a mayúsculas y para evitar que se ingresen titulos en Minúsculas
                titulo = str(input("Ingrese el título del libro: ")).upper()
                while titulo == "" or titulo in titulos:
                    if titulo == "":
                        print("El nombre del título no puede estar vacío.")
                    else:
                        print("El título ya existe en el catálogo.")
                    titulo =   str(input("Ingrese un título válido: ")).upper()
                titulos.append(titulo)
                ejemplares.append(0)
            print(f"{cantidad} títulos ingresados exitosamente.")
        else:
            print("Ingrese un número entero positivo.")
    elif menu == '2':
        if not titulos:
            print("No hay títulos en el catálogo. Primero ingrese títulos.")
        else:
            for i in range(len(titulos)):
                cantidad = int(input(f"Ingrese la cantidad de ejemplares para '{titulos[i]}': "))
                if cantidad >= 0:
                    ejemplares[i] += int(cantidad)
                else:
                    print("Cantidad inválida. Se mantiene el valor anterior.")
            print("Ejemplares actualizados exitosamente.")
    elif menu == '3':
        if not titulos:
            print("El catálogo está vacío.")
        else:
            print("\nCatálogo de Libros:")
            for i in range(len(titulos)):
                print(f"{titulos[i]} - Ejemplares: {ejemplares[i]}")
    elif menu == '4':
        if not titulos:
            print("No hay títulos en el catálogo.")
        else:
            titulo_buscar = input("Ingrese el título a consultar: ").upper()
            index = -1
            for i in range(len(titulos)):
                if titulos[i] == titulo_buscar:
                    index = i
                    break
            if index != -1:
                print(f"'{titulo_buscar}' tiene {ejemplares[index]} ejemplares disponibles.")
            else:
                print(f"El título '{titulo_buscar}' no se encuentra en el catálogo.")
    elif menu == '5':
        agotados = [titulos[i] for i in range(len(titulos)) if ejemplares[i] == 0]
        if agotados:
            print("Títulos agotados:")
            for titulo in agotados:
                print(titulo)
        else:
            print("No hay títulos agotados.")
    elif menu == '6':
        titulo_nuevo = str(input("Ingrese el nuevo título del libro: ")).upper()    
        while titulo_nuevo == "" or titulo_nuevo in titulos:
            if titulo_nuevo == "":
                print("El título no puede estar vacío.")
            else:
                print("El título ya existe en el catálogo.")
        cantidad_ejemplares = input(f"Ingrese la cantidad de ejemplares para '{titulo_nuevo}': ")
        while not (cantidad_ejemplares.isdigit() and int(cantidad_ejemplares) >= 0):
            print("La cantidad de ejemplares no puede ser negativa.")
            cantidad_ejemplares = input(f"Ingrese una cantidad válida de ejemplares para '{titulo_nuevo}': ")
        titulos.append(titulo_nuevo)
        ejemplares.append(int(cantidad_ejemplares))
        print(f"Título '{titulo_nuevo}' agregado exitosamente con {cantidad_ejemplares} ejemplares.")
        print(f"Título '{titulo_nuevo}' agregado exitosamente con {cantidad_ejemplares} ejemplares.")
    elif menu == '7':
        if not titulos:
            print("No hay títulos en el catálogo.")
        else:
            titulo_actualizar = str(input("Ingrese el título a actualizar: ")).upper()
            index = None
            # Buscar el índice manualmente en vez de usar .index()
            for i, t in enumerate(titulos):
                if t == titulo_actualizar:
                    index = i
                    break
            if index is not None:
                accion = input("¿Desea (P)réstamo o (D)evolución? ").upper()
                if accion == 'P':
                    if ejemplares[index] > 0:
                        ejemplares[index] -= 1
                        print(f"Préstamo realizado. Ejemplares restantes de '{titulo_actualizar}': {ejemplares[index]}")
                    else:
                        print(f"No hay ejemplares disponibles para '{titulo_actualizar}'.")
                elif accion == 'D':
                    ejemplares[index] += 1
                    print(f"Devolución realizada. Ejemplares actuales de '{titulo_actualizar}': {ejemplares[index]}")
                else:
                    print("Acción inválida. Use 'P' para préstamo o 'D' para devolución.")
            else:
                print(f"El título '{titulo_actualizar}' no se encuentra en el catálogo.")
    elif menu == '8':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 8.") 


        



