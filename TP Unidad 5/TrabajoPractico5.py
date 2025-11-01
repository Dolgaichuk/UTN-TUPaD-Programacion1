#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.
notas = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
print("Lista completa de notas:", notas)
suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
print ("El promedio de las notas es de: ", promedio)
notaMasAlta = 0
notaMasBaja = 100
for nota in notas:
    if nota > notaMasAlta:  
        notaMasAlta = nota
    if nota < notaMasBaja:
        notaMasBaja = nota
print("La nota más alta es:", notaMasAlta)
print("La nota más baja es:", notaMasBaja)  
#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista
productos = []
for i in range(5):
    producto = input("Ingrese el nombre del producto: ")
    productos.append(producto)
print("Lista de productos:", productos)
print("Lista de productos ordenada alfabéticamente:", sorted(productos))
producto_a_eliminar = input("¿Qué producto desea eliminar? ")
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print("Producto eliminado. Lista actualizada:", productos)
else:
    print("El producto no se encuentra en la lista.")

#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.

numeros =[]
for i in range(15):
    print ("Ingrese un número entero entre 1 y 100: ")
    numero = int(input())
    if numero < 1 or numero > 100:
        print("Número fuera de rango, intente nuevamente.")
    else:
        numeros.append(numero)

numerosPares = []
numerosImpares = []
for num in numeros:
    if num % 2 == 0:
        numerosPares.append(num)
    else:
        numerosImpares.append(num)

print("Cantidad de números pares:", len(numerosPares))
print("Cantidad de números impares:", len(numerosImpares))      
print("Números pares:", numerosPares)
print("Números impares:", numerosImpares)
#4) Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_unicos = set(datos)
print("Lista original:", datos)
print("Lista sin elementos repetidos:", datos_unicos)

#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).
numeros = [10, 20, 30, 40, 50, 60, 70]
# rotar una posición a la derecha usando un for
ultimo = numeros[-1]
for i in range(len(numeros) - 1, 0, -1):
    numeros[i] = numeros[i - 1]
numeros[0] = ultimo
print("Lista rotada:", numeros)
#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.
temperaturas = [
    [15, 25],  # Día 1
    [17, 28],  # Día 2
    [14, 22],  # Día 3
    [16, 30],  # Día 4
    [18, 27],  # Día 5
    [13, 24],  # Día 6
    [19, 29]   # Día 7
]   
suma_minimas = 0
suma_maximas = 0    
mayor_amplitud = 0
dia_mayor_amplitud = 0
for i in range(len(temperaturas)):
    suma_minimas += temperaturas[i][0]
    suma_maximas += temperaturas[i][1]
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1
promedio_minimas = suma_minimas / len(temperaturas)
promedio_maximas = suma_maximas / len(temperaturas)
print("Promedio de temperaturas mínimas:", promedio_minimas)
print("Promedio de temperaturas máximas:", promedio_maximas)
print("Día con mayor amplitud térmica:", dia_mayor_amplitud)

#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia
notas = []
for i in range(5):
    estudiante = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota del estudiante {i + 1} en la materia {j + 1}: "))
        estudiante.append(nota)
    notas.append(estudiante)

# Promedio de cada estudiante
for i in range(len(notas)):
    suma = 0
    for nota in notas[i]:
        suma += nota
    promedio = suma / len(notas[i])
    print(f"El promedio del estudiante {i + 1} es: {promedio}")

# Promedio de cada materia
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    promedio = suma / 5
    print(f"El promedio de la materia {j + 1} es: {promedio}")

#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.

tablero = [["-" for _ in range(3)] for _ in range(3)]

# Mostrar tablero inicial
for fila in tablero:
    print(" ".join(fila))
print()

jugador_actual = "X"
for _ in range(9):
    for fila in tablero:
        for fila in tablero:
            print(" ".join(fila))
    print()
    fila = int(input(f"Jugador {jugador_actual}, ingrese fila (0-2): "))
    col = int(input(f"Jugador {jugador_actual}, ingrese columna (0-2): "))
    if tablero[fila][col] == "-":
        tablero[fila][col] = jugador_actual
        jugador_actual = "O" if jugador_actual == "X" else "X"
    else:
        print("Casilla ocupada, intente nuevamente.")
# Mostrar tablero después de cada jugada
for fila in tablero:
    print(" ".join(fila))
print()
#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana
ventas = [
    [10, 15, 20, 25, 30, 35, 40],  # Producto 1
    [5, 10, 15, 20, 25, 30, 35],   # Producto 2
    [8, 12, 16, 20, 24, 28, 32],   # Producto 3
    [7, 14, 21, 28, 35, 42, 49]    # Producto 4
]
total_por_producto = []
for i in range(len(ventas)):        
    total = 0
    for v in ventas[i]:
        total += v
    total_por_producto.append(total)
    print(f"Total vendido del producto {i + 1}: {total}")
total_por_dia = [0] * 7
for j in range(7):
    for i in range(len(ventas)):
        total_por_dia[j] += ventas[i][j]    
dia_mayores_ventas = total_por_dia.index(max(total_por_dia)) + 1
print(f"Día con mayores ventas totales: Día {dia_mayores_ventas}")
total_ventas_productos = []
for i in range(len(ventas)):
    total = 0
    for v in ventas[i]:
        total += v
    total_ventas_productos.append(total)
producto_mas_vendido = total_ventas_productos.index(max(total_ventas_productos)) + 1
print(f"Producto más vendido en la semana: Producto {producto_mas_vendido}")    



