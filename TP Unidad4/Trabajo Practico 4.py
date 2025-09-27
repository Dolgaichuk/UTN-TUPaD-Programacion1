# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("Ejercicio 1")
print(" ")
for i in range(101):
    print(i)    
print("")

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene.

print("Ejercicio 2")
print(" ")
num = input("Por favor, ingresá un número entero: ")
#
print("")   
print("El número ingresado tiene", len(num), "dígitos.")
print("")   


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

print("Ejercicio 3")
print(" ")
num1 = int(input("Por favor, ingresá el primer número entero: "))   
num2 = int(input("Por favor, ingresá el segundo número entero: "))
suma = 0    
for n in range(num1 + 1, num2):
    suma += n   
print("")
print("La suma de los números comprendidos entre", num1, "y", num2, "es:", suma)
print("")   

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
print("Ejercicio 4")
print(" ")
suma = 0
while num != 0:
    num = int(input("Por favor, ingresá un número entero (ingresá 0 para finalizar): "))
    
    suma += num 
print("")   
print("La suma total de los números ingresados es:", suma)
print("")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. Hacerlo con bucles 
#  
# while y for.
import random
print("Ejercicio 5")
print(" ")
num_aleatorio = random.randint(0, 9)
intentos = 0
num = -1
while num != num_aleatorio:
    num = int(input("Por favor, ingresá un número entero entre 0 y 9: "))
    intentos += 1   
    if num < 0 or num > 9:
        print("El número ingresado no está entre 0 y 9. Por favor, intentá nuevamente.")
    
print("¡Felicidades! Adivinaste el número.")
print("Número de intentos:", intentos)
print("")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.

print("Ejercicio 6")
print(" ")  
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)        
print("")   

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.
print("Ejercicio 7")
print(" ") 
num = int(input("Por favor, ingresá un número entero positivo: "))
suma = 0
for i in range(num + 1):
    suma += i   
print("")
print("La suma de los números comprendidos entre 0 y", num, "es:", suma)
print("")   

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print("Ejercicio 8")
print(" ")      
pares = 0
impares = 0
positivos = 0
negativos = 0
cantidad_numeros = 5  # Cambiar este valor a 100 para el caso real
for i in range(cantidad_numeros):
    num = int(input("Por favor, ingresá un número entero: "))   
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1   
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1  
print("")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)      
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
print("")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).
print("Ejercicio 9")
print(" ")     
suma = 0    
cantidad_numeros = 5  # Cambiar este valor a 100 para el caso real
for i in range(cantidad_numeros):
    num = int(input("Por favor, ingresá un número entero: "))   
    suma += num 
media = suma / cantidad_numeros
print("")       
print("La media de los números ingresados es:", media)
print("")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
print("Ejercicio 10")
print(" ")  
num = input("Por favor, ingresá un número entero: ")
num_invertido = ""
for i in range(len(num) - 1, -1, -1):
    num_invertido += num[i]
print("")                   
print("El número invertido es:", num_invertido)
print("")


