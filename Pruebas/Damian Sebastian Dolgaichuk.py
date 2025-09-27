#Primer Parcial – Programación 1
#Enunciado
#La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las
#copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que
#utilice listas paralelas (una para titulos[] y otra para ejemplares[]). Cada título debe estar
#vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas.
#Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario
#elija salir.
#Requisitos y Restricciones Técnicas
#• Estructuras Permitidas: Debes usar un bucle while para navegar por las opciones del
#menú hasta que el usuario elija salir. Se debe utilizar una estructura case (o su
#equivalente con if/elif/else) para el menú, así como estructuras condicionales y
#secuenciales de Python. Se permiten funciones para validar cadenas de texto como
#lower(), upper() o isdigit().
#• Estructuras Prohibidas: Está estrictamente prohibido usar excepciones, clases,
#diccionarios, funciones de creación propia y estructuras de datos avanzadas. Si se
#utilizan, la calificación máxima será de 10%.
#• Listas Paralelas: Las listas titulos[] y ejemplares[] deben estar sincronizadas, de modo
#que el título en un índice corresponda a la cantidad de copias en el mismo índice de la
#otra lista
#Ejemplo:
#• títulos[] = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
#• ejemplares[] = [5, 3, 7]
#En este ejemplo, "El Señor de los Anillos" tiene 5 copias, "Orgullo y Prejuicio" tiene 3 copias,
#y "Matar un Ruiseñor" tiene 7 copias.
#Requerimientos del Menú
#1. Ingresar títulos → Para agregar los títulos iniciales de los libros, el usuario indica la
#cantidad inicial.
#2. Ingresar ejemplares → Para agregar una cantidad de copias para cada título.
#3. Mostrar catálogo → Muestra todos los libros y su stock actual.
#4. Consultar disponibilidad → Busca un título específico y muestra cuántos ejemplares
#hay.
#5. Listar agotados → Muestra los títulos que tienen 0 ejemplares.
#6. Agregar título → Permite añadir un nuevo libro y sus ejemplares disponibles al
#catálogo, respetando la sincronía de los índices en las listas.
#7. Actualizar ejemplares (préstamo/devolución) → Permite modificar el stock de un
#libro, elegido por el usuario, para registrar préstamos o devoluciones.
#- Préstamo -> Disminuye en 1 la cantidad de ejemplares del libro seleccionado,
#si hay unidades suficientes.
#- Devolución -> Aumenta en 1 la cantidad de ejemplares del libro seleccionado.
#8. Salir → Termina la ejecución del programa.
#Entregables
#El estudiante deberá subir el archivo del programa en lenguaje Python a la plataforma
#institucional. NO SUBIR UN REPOSITORIO DE GITHUB. SOLO SUBIR EL ARCHIVO.PY
#El código debe cumplir con:
#• Todas las funcionalidades solicitadas reflejadas en el menú.
#• Buena ejecución sin errores.
#• Nomenclatura clara en el nombre de las variables.
#• Legibilidad general y buenas prácticas de codificación.
#Rúbrica de Evaluación
#Código Criterio Peso Descripción detallada
#C1 Correctitud
#Funcional
#50% Evalúa que todas las funcionalidades del sistema
#estén implementadas y funcionen correctamente:
#• Agregar título: se añade a titulos[] y ejemplares[]
#manteniendo la correspondencia de índices y
#evitando duplicados.
#• Consultar disponibilidad: muestra correctamente
#los ejemplares para un título válido.
#• Listar agotados: muestra títulos con ejemplares = 0.
#• Préstamo / Devolución: ajusta correctamente el
#stock.
#• Mostrar catálogo: lista todos los títulos con su
#stock.
#C2 Cumplimiento de
#Restricciones
#20% Evalúa el respeto de las limitaciones de diseño:
#• Uso exclusivo de listas paralelas.
#• Mantener títulos con ejemplares = 0 en el catálogo.
#• No usar diccionarios, clases, funciones ni
#estructuras avanzadas.
#• Sincronía permanente entre titulos[] y ejemplares[].
#C3 Interacción y
#Validación
#10% Evalúa la robustez de la interacción con el usuario:
#• Validar que el título no sea vacío.
#• Validar que las cantidades sean enteros y positivas
#(o cero si corresponde).
#• No permitir prestar más de lo disponible.
#• Verificar la existencia del título antes de cualquier
#operación.
#• Menú persistente hasta elegir salir.
#• Manejo de opciones inválidas con mensajes claros.
#C4 Estructura y
#Legibilidad
#10% Evalúa la calidad del código:
#• Variables descriptivas.
#• Indentación consistente.
#• Flujo claro y ordenado.
#• Mensajes coherentes y consistentes para el usuario.
#C5 Casos de Prueba /
#Cobertura
#5% Evalúa la consideración de casos normales y
#extremos en las pruebas:
#• Pruebas con títulos y ejemplares válidos.
#• Título con ejemplares = 0.
#• Intento de préstamo mayor que el disponible.
#• Título inexistente en cualquier operación.
#Programación 1
#C6 Gestión de Casos
#Borde
#5% Evalúa el manejo de escenarios críticos:
#• Préstamo cuando no hay ejemplares disponibles.
#• Préstamo con cantidades negativas o excesivas.
#• Devoluciones inválidas (cantidades negativas).
#• Operaciones sobre títulos inexistentes o vacíos
#Total 100%
#Fecha de Entrega: 30/11/2023

# Biblioteca Escolar - Gestión de Catálogo de Libros
def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")   
    return input("Seleccione una opción (1-8): ")
def validar_entero_positivo(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit() and int(valor) >= 0:
            return int(valor)
        else:
            print("Por favor, ingrese un número entero positivo.")      
titulos = []
ejemplares = []     
while True:
    opcion = mostrar_menu()
    if opcion == '1':
        cantidad = validar_entero_positivo("¿Cuántos títulos desea ingresar? ")
        for _ in range(cantidad):
            titulo = input("Ingrese el título del libro: ").strip()
            while titulo == "" or titulo in titulos:
                if titulo == "":
                    print("El título no puede estar vacío.")
                else:
                    print("El título ya existe en el catálogo.")
                titulo = input("Ingrese un título válido: ").strip()
            titulos.append(titulo)
            ejemplares.append(0)  # Inicializa con 0 ejemplares
        print(f"{cantidad} títulos ingresados exitosamente.")
    elif opcion == '2':
        if not titulos:
            print("No hay títulos en el catálogo. Primero ingrese títulos.")
        else:
            for i in range(len(titulos)):
                cantidad = validar_entero_positivo(f"Ingrese la cantidad de ejemplares para '{titulos[i]}': ")
                ejemplares[i] += cantidad
            print("Ejemplares actualizados exitosamente.")
    elif opcion == '3':
        if not titulos:
            print("El catálogo está vacío.")
        else:
            print("\nCatálogo de Libros:")
            for i in range(len(titulos)):
                print(f"{titulos[i]} - Ejemplares: {ejemplares[i]}")
    elif opcion == '4':
        if not titulos:
            print("No hay títulos en el catálogo.")
        else:
            titulo_buscar = input("Ingrese el título a consultar: ").strip()
            if titulo_buscar in titulos:
                index = titulos.index(titulo_buscar)
                print(f"'{titulo_buscar}' tiene {ejemplares[index]} ejemplares disponibles.")
            else:
                print(f"El título '{titulo_buscar}' no se encuentra en el catálogo.")
    elif opcion == '5':
        agotados = [titulos[i] for i in range(len(titulos)) if ejemplares[i] == 0]
        if agotados:
            print("Títulos agotados:")
            for titulo in agotados:
                print(titulo)
        else:
            print("No hay títulos agotados.")
    elif opcion == '6':
        titulo_nuevo = input("Ingrese el nuevo título del libro: ").strip()
        while titulo_nuevo == "" or titulo_nuevo in titulos:
            if titulo_nuevo == "":
                print("El título no puede estar vacío.")
            else:
                print("El título ya existe en el catálogo.")
            titulo_nuevo = input("Ingrese un título válido: ").strip()
        cantidad_ejemplares = validar_entero_positivo(f"Ingrese la cantidad de ejemplares para '{titulo_nuevo}': ")
        titulos.append(titulo_nuevo)
        ejemplares.append(cantidad_ejemplares)
        print(f"Título '{titulo_nuevo}' agregado exitosamente con {cantidad_ejemplares} ejemplares.")
    elif opcion == '7':
        if not titulos:
            print("No hay títulos en el catálogo.")
        else:
            titulo_actualizar = input("Ingrese el título a actualizar: ").strip()
            if titulo_actualizar in titulos:
                index = titulos.index(titulo_actualizar)
                accion = input("¿Desea (P)réstamo o (D)evolución? ").strip().upper()
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
    elif opcion == '8':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 8.")

        



