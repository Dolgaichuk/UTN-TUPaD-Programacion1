#Persistencia (CSV)
#● El programa carga el catálogo desde un archivo CSV al iniciar (si existe) y guarda los 
#cambios cada vez que se modifica el inventario.
#● Formato sugerido del CSV (con encabezado):
#○ Columnas: TITULO,CANTIDAD
#Ejemplo:
#TITULO,CANTIDAD
#El Señor de los Anillos,5
#1984,0
#Ficciones,3
#Interacción por menú (flujo general)
#● Al iniciar, se muestra un menú numerado y se solicita una opción.
#● El menú debe repetirse (bucle while) hasta elegir Salir.
#● Luego de cada operación que cambie datos, el programa debe persistir el catálogo en 
#el CSV y mostrar un mensaje de confirmación.
#Funcionalidades obligatorias del menú
#1. Ingresar títulos (múltiples): permite cargar varios libros de una vez, el usuario indica la 
#cantidad de libros que quiere cargar. Por cada libro, pedir TITULO (no vacío, no 
#duplicado) y CANTIDAD (>= 0).
#2. Ingresar ejemplares: sumar una cantidad a un título existente.
#3. Mostrar catálogo: listar todos los libros con su stock actual.
#4. Consultar disponibilidad: buscar un TITULO y mostrar cuántos ejemplares hay 
#disponibles.
#5. Listar agotados: mostrar solo los títulos con CANTIDAD == 0.
#6. Agregar título: alta de un libro individual (validar duplicados) con su cantidad inicial.
#7. Actualizar ejemplares (préstamo/devolución):
#○ Préstamo: restar 1 solo si CANTIDAD > 0.
#○ Devolución: sumar 1.
#8. Salir: finalizar la aplicación.
#Reglas de negocio y validaciones

#● Títulos: no se aceptan vacíos; comparar sin sensibilidad a mayúsculas y normalizando 
#espacios.
#● Cantidades: deben ser enteros >= 0 al cargar/editar.
#● Préstamos: no permitir valores negativos (si está en 0, informar al usuario).
#● Mensajes claros: informar siempre si una operación fue exitosa o rechazada y el 
#motivo.
#Requisitos y restricciones técnicas
#● Obligatorio:
#○ Bucle while para el menú.
#○ match/case para direccionar opciones (Python 3.10+).
#○ Funciones para modularizar (cargar/guardar CSV, validar entradas, buscar 
#títulos, etc.).
#○ Estructuras: listas y diccionarios (estructura principal descrita arriba).
#○ Persistencia en CSV.
#○ Se pueden usar validadores como lower(), upper(), isdigit().
#● Prohibido (penaliza a 10% máximo de nota si se usan): funciones lambdas, 
#excepciones, clases, variables globales.
#Comportamiento esperado (resumen)
#● Si el CSV no existe, iniciar con catálogo vacío.
#● Si el usuario ingresa un título duplicado, rechazar y volver a pedir.
#● Tras agregar/actualizar datos, guardar automáticamente en el CSV.
#● Las búsquedas de títulos deben ser robustas (insensibles a mayúsculas y espacios 
#extra).
#Entregables
#● El estudiante deberá subir un único archivo del programa en lenguaje Python (.py) a la 
#plataforma institucional.
#● NO SUBIR UN REPOSITORIO DE GITHUB. SOLO SUBIR EL ARCHIVO .PY.

# Programa de gestión de catálogo de libros con persistencia en CSV
import csv
import os   
CATALOGO_CSV = 'catalogo_libros.csv'
def cargar_catalogo():
    catalogo = {}
    if os.path.exists(CATALOGO_CSV):
        with open(CATALOGO_CSV, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                titulo = fila['TITULO'].strip()
                cantidad = int(fila['CANTIDAD'])
                catalogo[titulo.lower()] = {'titulo': titulo, 'cantidad': cantidad}
    return catalogo 
def guardar_catalogo(catalogo):
    with open(CATALOGO_CSV, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ['TITULO', 'CANTIDAD']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for libro in catalogo.values():
            escritor.writerow({'TITULO': libro['titulo'], 'CANTIDAD': libro['cantidad']})   
def validar_titulo(titulo, catalogo):
    titulo = titulo.strip()
    if not titulo:
        print("El título no puede estar vacío.")
        return False
    if titulo.lower() in catalogo:
        print("El título ya existe en el catálogo.")
        return False
    return True
def validar_cantidad(cantidad_str): 
    if not cantidad_str.isdigit():
        print("La cantidad debe ser un número entero no negativo.")
        return None
    cantidad = int(cantidad_str)
    if cantidad < 0:
        print("La cantidad no puede ser negativa.")
        return None
    return cantidad
def ingresar_titulos(catalogo):
    try:    
        n = int(input("¿Cuántos títulos desea ingresar? "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return          
    for _ in range(n):
        while True:
            titulo = input("Ingrese el título del libro: ")
            if validar_titulo(titulo, catalogo):
                break               
        while True:

            cantidad_str = input("Ingrese la cantidad de ejemplares: ")
            cantidad = validar_cantidad(cantidad_str)
            if cantidad is not None:
                break
        catalogo[titulo.lower()] = {'titulo': titulo.strip(), 'cantidad': cantidad}
    guardar_catalogo(catalogo)  
    print("Títulos ingresados y guardados correctamente.")
def ingresar_ejemplares(catalogo):
    titulo = input("Ingrese el título del libro para agregar ejemplares: ").strip()
    clave = titulo.lower()
    if clave not in catalogo:
        print("El título no existe en el catálogo.")
        return
    while True:
        cantidad_str = input("Ingrese la cantidad de ejemplares a agregar: ")
        cantidad = validar_cantidad(cantidad_str)
        if cantidad is not None:
            break
    catalogo[clave]['cantidad'] += cantidad
    guardar_catalogo(catalogo)
    print(f"Se han agregado {cantidad} ejemplares a '{catalogo[clave]['titulo']}'.")        
def mostrar_catalogo(catalogo):
    if not catalogo:
        print("El catálogo está vacío.")
        return
    print("Catálogo de libros:")
    for libro in catalogo.values():
        print(f"Título: {libro['titulo']}, Cantidad: {libro['cantidad']}")  
def consultar_disponibilidad(catalogo):
    titulo = input("Ingrese el título del libro para consultar disponibilidad: ").strip()
    clave = titulo.lower()
    if clave in catalogo:
        cantidad = catalogo[clave]['cantidad']
        print(f"El libro '{catalogo[clave]['titulo']}' tiene {cantidad} ejemplares disponibles.")
    else:
        print("El título no existe en el catálogo.")
def listar_agotados(catalogo):
    agotados = [libro for libro in catalogo.values() if libro['cantidad'] == 0]
    if not agotados:

        print("No hay títulos agotados.")
        return
    print("Títulos agotados:")
    for libro in agotados:
        print(f"Título: {libro['titulo']}") 
def agregar_titulo(catalogo):
    while True:
        titulo = input("Ingrese el título del libro a agregar: ")
        if validar_titulo(titulo, catalogo):
            break
    while True:
        cantidad_str = input("Ingrese la cantidad inicial de ejemplares: ")
        cantidad = validar_cantidad(cantidad_str)
        if cantidad is not None:
            break
    catalogo[titulo.lower()] = {'titulo': titulo.strip(), 'cantidad': cantidad}
    guardar_catalogo(catalogo)
    print(f"El título '{titulo}' ha sido agregado con {cantidad} ejemplares.")    
def actualizar_ejemplares(catalogo):
    titulo = input("Ingrese el título del libro para actualizar ejemplares: ").strip()
    clave = titulo.lower()
    if clave not in catalogo:
        print("El título no existe en el catálogo.")
        return
    accion = input("¿Desea realizar un préstamo (p) o una devolución (d)? ").strip().lower()
    if accion == 'p':
        if catalogo[clave]['cantidad'] > 0:
            catalogo[clave]['cantidad'] -= 1
            guardar_catalogo(catalogo)
            print(f"Préstamo realizado. Quedan {catalogo[clave]['cantidad']} ejemplares de '{catalogo[clave]['titulo']}'.")
        else:
            print("No hay ejemplares disponibles para préstamo.")
    elif accion == 'd':
        catalogo[clave]['cantidad'] += 1
        guardar_catalogo(catalogo)
        print(f"Devolución realizada. Ahora hay {catalogo[clave]['cantidad']} ejemplares de '{catalogo[clave]['titulo']}'.")
    else:
        print("Acción no válida. Use 'p' para préstamo o 'd' para devolución.")
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Ingresar títulos (múltiples)")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")

def main():
    catalogo = cargar_catalogo()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ").strip()
        match opcion:
            case '1':
                ingresar_titulos(catalogo)
            case '2':
                ingresar_ejemplares(catalogo)
            case '3':
                mostrar_catalogo(catalogo)
            case '4':
                consultar_disponibilidad(catalogo)
            case '5':
                listar_agotados(catalogo)
            case '6':
                agregar_titulo(catalogo)
            case '7':
                actualizar_ejemplares(catalogo)
            case '8':
                print("Saliendo del programa. ¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")

if __name__ == "__main__":
    main()

    

















































































































































































