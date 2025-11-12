# Modulo csv: permite leer y escribir archivos CSV
import csv
import os

# Ruta del archivo CSV
CSV_PATH = "paises.csv"

# --- FUNCIONES AUXILIARES DE ENTRADA ---

def validar_entero(prompt):
    """Pide un valor y se asegura de que sea un número entero positivo."""
    
    while True:
        valor_str = input(prompt).strip()
        if not valor_str:
            print("El campo no puede estar vacío.")
            continue
        try:
            valor = int(valor_str)
            if valor < 0:
                print("El valor debe ser positivo o cero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

def mostrar_pais(pais):
    """Muestra los datos de un país de forma legible."""
    print("---------------------------------")
    print(f" -> Nombre: {pais['nombre']}")
    print(f"    Población: {pais['poblacion']:,}")
    print(f"    Superficie: {pais['superficie']:,} km²")
    print(f"    Continente: {pais['continente']}")
    print("---------------------------------")

# --- MANEJO DE ARCHIVOS ---

def cargar_paises():
    """Carga los datos desde el archivo CSV, manejando errores de archivo y formato."""
    paises = []
    if not os.path.exists(CSV_PATH):
        print("Advertencia: Archivo CSV no encontrado. Iniciando con lista vacía.")
        return paises

    try:
        with open(CSV_PATH, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for i, fila in enumerate(lector, 2):
                try:
                    paises.append({
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    })
                except (ValueError, KeyError): # Manejo de errores de formato 
                    print(f"Error de formato en la línea {i}: Datos 'poblacion' o 'superficie' no son números enteros o faltan columnas.")
    except Exception as e:
        print(f"Error crítico al leer el archivo: {e}")
    return paises

def guardar_paises(paises):
    """Guarda los datos en el archivo CSV."""
    try:
        with open(CSV_PATH, "w", newline='', encoding='utf-8') as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(paises)
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")

# --- FUNCIONALIDADES CRUD ---

def agregar_pais(paises):
    """Función para agregar un país con validación de datos."""
    print("\n--- AGREGAR PAÍS ---")
    nombre = input("Nombre del país: ").strip()
    continente = input("Continente: ").strip()

    if not nombre or not continente:
        print("Error: Los campos Nombre y Continente no pueden estar vacíos.")
        return
    
    print("Ingresa la Población (solo números enteros):")
    poblacion = validar_entero("Población: ")
    print("Ingresa la Superficie (solo números enteros):")
    superficie = validar_entero("Superficie (km²): ")

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    print(f"País '{nombre}' agregado correctamente.")

def actualizar_pais(paises):
    """Actualiza solo Población y Superficie de un país existente."""
    print("\n--- ACTUALIZAR PAÍS ---")
    nombre_buscar = input("Nombre exacto del país a actualizar: ").strip()
    
    pais_encontrado = None
    for pais in paises:
        if pais["nombre"].strip().lower() == nombre_buscar.lower():
            pais_encontrado = pais
            break

    if pais_encontrado:
        print(f"País encontrado: {pais_encontrado['nombre']}")
        
        nueva_poblacion = validar_entero("Nueva población (dejar 0 para no cambiar): ")
        if nueva_poblacion > 0:
            pais_encontrado["poblacion"] = nueva_poblacion
        
        nueva_superficie = validar_entero("Nueva superficie (dejar 0 para no cambiar): ")
        if nueva_superficie > 0:
            pais_encontrado["superficie"] = nueva_superficie
            
        print(f"Datos de {pais_encontrado['nombre']} actualizados correctamente.")
    else:
        print(f"País '{nombre_buscar}' no encontrado.")

# --- BÚSQUEDA, FILTRADO Y ORDENAMIENTO ---

def buscar_pais(paises):
    """Busca un país por nombre (coincidencia parcial o exacta)."""
    print("\n--- BUSCAR PAÍS ---")
    nombre_buscar = input("Buscar país (coincidencia parcial): ").strip().lower()
    if not nombre_buscar:
        print("Error: El campo de búsqueda no puede estar vacío.")
        return
        
    
    resultados = [p for p in paises if nombre_buscar in p["nombre"].lower()]
    
    if resultados:
        print(f"Se encontraron {len(resultados)} país(es):")
        for p in resultados:
            mostrar_pais(p)
    else:
        print("No se encontraron coincidencias para la búsqueda.")

def filtrar_paises(paises):
    """Filtra países por continente, rango de población o rango de superficie."""
    print("\n--- FILTRAR PAÍSES ---")
    print("1. Por Continente")
    print("2. Por Rango de Población")
    print("3. Por Rango de Superficie")
    opcion = input("Selecciona una opción de filtrado: ").strip()
    
    
    filtrados = []
    
    if opcion == "1":
        cont = input("Continente: ").strip().lower()
        if not cont:
            print("Error: El continente no puede estar vacío.")
            return
        filtrados = [p for p in paises if cont in p["continente"].lower()]
        print(f"Filtro aplicado por Continente: {cont.title()}")
        
    elif opcion == "2":
        print("Ingresa el rango de Población:")
        min_p = validar_entero("Población mínima: ")
        max_p = validar_entero("Población máxima: ")
        if min_p > max_p:
             print("Error: La población mínima no puede ser mayor que la máxima.")
             return
        filtrados = [p for p in paises if min_p <= p["poblacion"] <= max_p]
        print(f"Filtro aplicado por Población entre {min_p:,} y {max_p:,}")

    elif opcion == "3":
        print("Ingresa el rango de Superficie:")
        min_s = validar_entero("Superficie mínima: ")
        max_s = validar_entero("Superficie máxima: ")
        if min_s > max_s:
             print("Error: La superficie mínima no puede ser mayor que la máxima.")
             return
        filtrados = [p for p in paises if min_s <= p["superficie"] <= max_s]
        print(f"Filtro aplicado por Superficie entre {min_s:,} y {max_s:,} km²")
        
    else:
        print("Opción de filtrado inválida.")
        return
    
    if filtrados:
        print(f"\nSe encontraron {len(filtrados)} resultados:")
        for p in filtrados:
            mostrar_pais(p)
    else:
        print("No se encontraron países que cumplan con el criterio de filtro.")

def ordenar_paises(paises):
    """Ordena países por nombre, población o superficie."""
    print("\n--- ORDENAR PAÍSES ---")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    campo = input("Selecciona el campo a ordenar (1, 2 o 3): ").strip()
    
    if campo == "1":
        clave = "nombre"
    elif campo == "2":
        clave = "poblacion"
    elif campo == "3":
        clave = "superficie"
    else:
        print("Opción de campo inválida.")
        return
        
    orden = input("Ascendente (A) o Descendente (D): ").strip().upper()
    reversa = orden == "D"
    
    
    paises_ordenados = sorted(paises, key=lambda p: p[clave], reverse=reversa)
    
    print("\nLista de países ordenada:")
    for p in paises_ordenados:
        mostrar_pais(p)

# --- ESTADÍSTICAS ---

def mostrar_estadisticas(paises):
    """Calcula y muestra estadísticas: min/max población, promedios y count por continente."""
    print("\n--- ESTADÍSTICAS ---")
    if not paises:
        print("No hay datos cargados para calcular estadísticas.")
        return
        
    
    pais_mayor_poblacion = paises[0] 
    pais_menor_poblacion = paises[0]
    
    for pais in paises:
        if pais["poblacion"] > pais_mayor_poblacion["poblacion"]:
            pais_mayor_poblacion = pais
        if pais["poblacion"] < pais_menor_poblacion["poblacion"]:
            pais_menor_poblacion = pais
    
    
    poblaciones = []
    superficies = []
    for p in paises:
        poblaciones.append(p["poblacion"])
        superficies.append(p["superficie"])
    
    # Promedios calculados de forma explícita
    promedio_poblacion = sum(poblaciones) / len(paises)
    promedio_superficie = sum(superficies) / len(paises)
    
    # Conteo por continente
    por_continente = {}
    for p in paises:
        cont = p["continente"].strip().title()
        if cont in por_continente:
            por_continente[cont] += 1
        else:
            por_continente[cont] = 1

    print(f"País con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']:,})")
    print(f"País con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']:,})")
    print("-" * 30)
    print(f"Promedio de población: {int(promedio_poblacion):,}")
    print(f"Promedio de superficie: {int(promedio_superficie):,} km²")
    print("-" * 30)
    print("Cantidad de países por continente:")
    for cont, cant in sorted(por_continente.items()):
        print(f" - {cont}: {cant}")

# --- MENÚ PRINCIPAL ---

def menu():
    """Menú principal del programa."""
    paises = cargar_paises()
    while True:
        print("\n" + "=" * 25)
        print("  GESTIÓN DE DATOS DE PAÍSES")
        print("=" * 25)
        print("1. Agregar país")
        print("2. Actualizar país (Población/Superficie)")
        print("3. Buscar país por nombre")
        print("4. Filtrar países")
        print("5. Ordenar países y mostrar")
        print("6. Mostrar estadísticas")
        print("7. Guardar y salir")
        
        opcion = input("Selecciona una opción (1-7): ").strip()
        
        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            guardar_paises(paises)
            print("Fin del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, selecciona un número del 1 al 7.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()