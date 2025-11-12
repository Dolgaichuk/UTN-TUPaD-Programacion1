
import csv
import os

def normalizar_titulo(titulo):
    return ' '.join(titulo.split()).strip()
# Cargar el catálogo desde un archivo CSV
def cargar_catalogo(ruta_csv):
    # Inicializar el catálogo
    catalogo = {}
    # Verificar si el archivo existe
    if os.path.exists(ruta_csv):
        # Leer el archivo CSV y cargar los datos en el catálogo
        with open(ruta_csv, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            # Cargar los datos en el catálogo
            for fila in lector:
                # Normalizar y validar los datos
                titulo_raw = fila.get('TITULO', '').strip()
                # Normalizar el título
                titulo = normalizar_titulo(titulo_raw)
                # Validar el título y la cantidad
                cantidad_str = fila.get('CANTIDAD', '').strip()
                # Convertir cantidad a entero, manejando posibles errores
                cantidad = int(cantidad_str) if cantidad_str.isdigit() else 0
                # Agregar al catálogo si el título es válido
                if titulo:
                    catalogo[titulo.lower()] = {'titulo': titulo, 'cantidad': cantidad}
    # Retornar el catálogo cargado
    return catalogo
# guardar el catálogo en un archivo CSV
def guardar_catalogo(catalogo, ruta_csv):
    # Escribir los datos del catálogo en el archivo CSV
    with open(ruta_csv, mode='w', newline='', encoding='utf-8') as archivo:
        # Crear un escritor CSV
        campos = ['TITULO', 'CANTIDAD']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        # Escribir cada libro en el archivo
        for libro in catalogo.values():
            escritor.writerow({'TITULO': libro['titulo'], 'CANTIDAD': libro['cantidad']})
# validar título
def validar_titulo(titulo, catalogo):
    # Normalizar el título
    titulo_norm = normalizar_titulo(titulo)
    # Verificar si el título está vacío o ya existe en el catálogo
    if not titulo_norm:
        print("El título no puede estar vacío.")
        return False
    if titulo_norm.lower() in catalogo:
        print("El título ya existe en el catálogo.")
        return False
    return True
# validar cantidad
def validar_cantidad(cantidad_str):
    cantidad_str = cantidad_str.strip()
    # Verificar si la cadena está vacía
    if not cantidad_str:
        print("La cantidad no puede estar vacía.")
        return None
    cantidad = int(cantidad_str)
    if cantidad < 0:
        print("La cantidad no puede ser negativa.")
        return None
    return cantidad
# ingresar múltiples títulos
def ingresar_titulos(catalogo, ruta_csv):
    # Pide al usuario la cantidad de títulos a ingresar
    while True:
        n_str = input("¿Cuántos títulos desea ingresar? ").strip()
        if n_str.isdigit():
            n = int(n_str)
            break
        print("Por favor, ingrese un número válido.")
    # Ingresar cada título y su cantidad
    for _ in range(n):
        # Validar y normalizar el título
        while True:
            titulo = input("Ingrese el título del libro: ")
            if validar_titulo(titulo, catalogo):
                titulo_norm = normalizar_titulo(titulo)
                break
        # Validar la cantidad
        while True:
            cantidad_str = input("Ingrese la cantidad de ejemplares: ")
            cantidad = validar_cantidad(cantidad_str)
            # Verificar si la cantidad es válida
            if cantidad is not None:
                break
            # Solicitar nuevamente la cantidad si no es válida
        catalogo[titulo_norm.lower()] = {'titulo': titulo_norm, 'cantidad': cantidad}
    # Guardar el catálogo actualizado
    guardar_catalogo(catalogo, ruta_csv)
    print("Títulos ingresados y guardados correctamente.")
# ingresar ejemplares a un título existente
def ingresar_ejemplares(catalogo, ruta_csv):
    titulo = input("Ingrese el título del libro para agregar ejemplares: ").strip()
    clave = normalizar_titulo(titulo).lower()
    # Verificar si el título existe en el catálogo
    if clave not in catalogo:
        print("El título no existe en el catálogo.")
        return
    # Solicitar la cantidad de ejemplares a agregar
    while True:
        cantidad_str = input("Ingrese la cantidad de ejemplares a agregar: ")
        cantidad = validar_cantidad(cantidad_str)
        if cantidad is not None:
            break
    # Actualizar la cantidad de ejemplares    
    catalogo[clave]['cantidad'] += cantidad
    guardar_catalogo(catalogo, ruta_csv)
    print(f"Se han agregado {cantidad} ejemplares a '{catalogo[clave]['titulo']}'.")
# mostrar catálogo

def mostrar_catalogo(catalogo):
    if not catalogo:
        print("El catálogo está vacío.")
        return
    print("Catálogo de libros:")
    #
    for libro in catalogo.values():
        print(f"Título: {libro['titulo']}, Cantidad: {libro['cantidad']}")
# consultar disponibilidad
def consultar_disponibilidad(catalogo):
    # Normalizar el título
    titulo = input("Ingrese el título del libro para consultar disponibilidad: ").strip()
    clave = normalizar_titulo(titulo).lower()
    # Verificar si el título existe en el catálogo
    if clave in catalogo:
        cantidad = catalogo[clave]['cantidad']
        print(f"El libro '{catalogo[clave]['titulo']}' tiene {cantidad} ejemplares disponibles.")
    else:
        print("El título no existe en el catálogo.")
# listar títulos agotados
def listar_agotados(catalogo):
    agotados = [libro for libro in catalogo.values() if libro['cantidad'] == 0]
    if not agotados:
        print("No hay títulos agotados.")
        return
    print("Títulos agotados:")
    
    for libro in agotados:
        print(f"Título: {libro['titulo']}")
# agregar nuevo título
def agregar_titulo(catalogo, ruta_csv):
    # Normalizar el título
    while True:
        titulo = input("Ingrese el título del libro a agregar: ")
        if validar_titulo(titulo, catalogo):
            titulo_norm = normalizar_titulo(titulo)
            break
    # Validar la cantidad inicial
    while True:
        cantidad_str = input("Ingrese la cantidad inicial de ejemplares: ")
        cantidad = validar_cantidad(cantidad_str)
        if cantidad is not None:
            break
    #    
    catalogo[titulo_norm.lower()] = {'titulo': titulo_norm, 'cantidad': cantidad}
    guardar_catalogo(catalogo, ruta_csv)
    print(f"El título '{titulo_norm}' ha sido agregado con {cantidad} ejemplares.")
# actualizar ejemplares para préstamo o devolución
def actualizar_ejemplares(catalogo, ruta_csv):
    titulo = input("Ingrese el título del libro para actualizar ejemplares: ").strip()
    clave = normalizar_titulo(titulo).lower()
    # Verificar si el título existe en el catálogo
    if clave not in catalogo:
        print("El título no existe en el catálogo.")
        return
    # Solicitar acción: préstamo o devolución
    accion = input("¿Desea realizar un préstamo (p) o una devolución (d)? ").strip().lower()
    if accion == 'p':
        if catalogo[clave]['cantidad'] > 0:
            catalogo[clave]['cantidad'] -= 1
            guardar_catalogo(catalogo, ruta_csv)
            print(f"Préstamo realizado. Quedan {catalogo[clave]['cantidad']} ejemplares de '{catalogo[clave]['titulo']}'.")
        else:
            print("No hay ejemplares disponibles para préstamo.")
    elif accion == 'd':
        catalogo[clave]['cantidad'] += 1
        guardar_catalogo(catalogo, ruta_csv)
        print(f"Devolución realizada. Ahora hay {catalogo[clave]['cantidad']} ejemplares de '{catalogo[clave]['titulo']}'.")
    else:
        print("Acción no válida. Use 'p' para préstamo o 'd' para devolución.")
# mostrar menú
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
# función principal
def main():
    ruta_csv = 'catalogo_libros.csv'
    catalogo = cargar_catalogo(ruta_csv)
    # Bucle principal del programa
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ").strip()
        match opcion:
            case '1':
                ingresar_titulos(catalogo, ruta_csv)
            case '2':
                ingresar_ejemplares(catalogo, ruta_csv)
            case '3':
                mostrar_catalogo(catalogo)
            case '4':
                consultar_disponibilidad(catalogo)
            case '5':
                listar_agotados(catalogo)
            case '6':
                agregar_titulo(catalogo, ruta_csv)
            case '7':
                actualizar_ejemplares(catalogo, ruta_csv)
            case '8':
                print("Saliendo del programa. ¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")
#
if __name__ == "__main__":
    main()

    

















































































































































































