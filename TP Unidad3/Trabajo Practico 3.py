# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

print ("Ejercicio 1")
print (" ")
edad = 0
edad =int(input("Por favor, ingresá tu edad: "))
print("")
# Verifica si es mayor de edad 
if edad >= 18:
   #muestra el mensaje
   print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”
print ("Ejercicio 2")
print (" ")
nota = 0
nota =int(input("Por favor, ingresá la nota: "))
print("")
# Verifica si es mayor o igual o menor que 6
if nota >= 6:
   #muestra el mensaje
   print("Aprobado") 
else:
   #muestra el mensaje
   print("Desaprobado")

#3) Escribir un programa que solicite al usuario un número entero. Si el número es par, deberá
#mostrar un mensaje que diga “El número es par”; en caso contrario, deberá mostrar el mensaje “El número es impar”.
print ("Ejercicio 3")         
print (" ")
numero = 0  
numero =int(input("Por favor, ingresá un número entero: "))
print("")      
# Verifica si es par o impar
if numero % 2 == 0:
   #muestra el mensaje
   print("El número es par")     
else:
   #muestra el mensaje
   print("El número es impar")   

 #4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

print ("Ejercicio 4")
print (" ") 
edad = 0
edad =int(input("Por favor, ingresá tu edad: "))   
print("")
# Verifica a cual categoria pertenece
if edad < 12:
   #muestra el mensaje
   print("Niño/a")   
elif edad >= 12 and edad < 18:
   #muestra el mensaje
   print("Adolescente") 
elif edad >= 18 and edad < 30:
   #muestra el mensaje
   print("Adulto/a joven") 
else:
   #muestra el mensaje
   print("Adulto/a") 

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.
print ("Ejercicio 5")
print (" ") 
contrasenia = ""
contrasenia =input("Por favor, ingresá una contraseña (entre 8 y 14 caracteres): ")   
print("")      
# Verifica la longitud de la contraseña
if len(contrasenia) >= 8 and len(contrasenia) <= 14:
   #muestra el mensaje
   print("Ha ingresado una contraseña correcta")      
else:
   #muestra el mensaje
   print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")   

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.
print ("Ejercicio 6")
print (" ") 
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print("La lista de números aleatorios es: ") 
print(numeros_aleatorios)
print("")   
# Calcula la moda, mediana y media
moda = mode(numeros_aleatorios)     
mediana = median(numeros_aleatorios)     
media = mean(numeros_aleatorios) 
# Verifica si hay sesgo positivo, negativo o no hay sesgo
if media > mediana and mediana > moda:
   #muestra el mensaje
   print("Hay sesgo positivo o a la derecha")      
elif media < mediana and mediana < moda:
   #muestra el mensaje
   print("Hay sesgo negativo o a la izquierda") 
elif media == mediana and mediana == moda:
   #muestra el mensaje
   print("No hay sesgo")
else:
   #muestra el mensaje
   print("No se puede determinar el sesgo")  
print("")
print("La moda es: ", moda)   
print("La mediana es: ", mediana)
print("La media es: ", media) 
