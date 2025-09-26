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

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

print ("Ejercicio 7")
print (" ") 
frase = ""
frase =input("Por favor, ingresá una frase o palabra: ") 
print("")
# Verifica si termina con vocal
if frase[-1].lower() in ['a', 'e', 'i', 'o', 'u']:
   #añade el signo de exclamación
   frase = frase + "!"
#imprime el resultado
print(frase)   

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.   
print ("Ejercicio 8")
print (" ") 
nombre = ""
nombre =input("Por favor, ingresá tu nombre: ") 
print("")
opcion = 0
opcion =int(input("Por favor, ingresá el número 1, 2 o 3 dependiendo de la opción que desees: \n1. Si querés tu nombre en mayúsculas. \n2. Si querés tu nombre en minúsculas. \n3. Si querés tu nombre con la primera letra mayúscula. \n"))
print("")
# Verifica la opción seleccionada
if opcion == 1:
   #convierte a mayúsculas
   nombre = nombre.upper() 
   #imprime el resultado
   print(nombre)
elif opcion == 2:
   #convierte a minúsculas
   nombre = nombre.lower() 
   #imprime el resultado
   print(nombre)
elif opcion == 3:
   #convierte la primera letra a mayúscula
   nombre = nombre.title() 
   #imprime el resultado
   print(nombre)
else:
   #muestra el mensaje
   print("Opción no válida")  

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
print ("Ejercicio 9")
print (" ") 
magnitud = 0.0
magnitud =float(input("Por favor, ingresá la magnitud del terremoto: "))      
print("")
# Verifica la categoría según la escala de Richter
if magnitud < 3:
   #muestra el mensaje
   print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
   #muestra el mensaje
   print("Leve (ligeramente perceptible)")   
elif magnitud >= 4 and magnitud < 5:
   #muestra el mensaje
   print("Moderado (sentido por personas, pero generalmente no causa daños)") 
elif magnitud >= 5 and magnitud < 6:
   #muestra el mensaje
   print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
   #muestra el mensaje
   print("Muy Fuerte (puede causar daños significativos)")     
else: 
   #muestra el mensaje
   print("Extremo (puede causar graves daños a gran escala)")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Periodo del año
# Estación en el
# hemisferio norte
# Estación en el
# hemisferio sur
# Desde el 21 de diciembre hasta el 20 de
# marzo (incluidos)
# Invierno Verano
# Desde el 21 de marzo hasta el 20 de junio
# (incluidos)
# Primavera Otoño
# Desde el 21 de junio hasta el 20 de
# septiembre (incluidos)
# Verano Invierno
# Desde el 21 de septiembre hasta el 20 de
# diciembre (incluidos)
# Otoño Primavera
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

print ("Ejercicio 10")
print (" ")
hemisferio = ""
hemisferio =input("Por favor, ingresá en cuál hemisferio te encontrás (N/S): ")
mes = 0
mes =int(input("Por favor, ingresá el mes del año (1-12): "))
dia = 0
dia =int(input("Por favor, ingresá el día del mes (1-31): "))
print("")
# Verifica la estación según el hemisferio, mes y día
if hemisferio.upper() == "N":
   if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20) or (mes < 3):
      print("Invierno")
   elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20) or (mes < 6):
      print("Primavera")
   elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20) or (mes < 9):
      print("Verano")
   elif (mes == 9 and dia >= 21) or (mes <= 12 and dia <= 20) or (mes < 12):
      print("Otoño")
   else:
      print("Fecha no válida")   
elif hemisferio.upper() == "S":
   if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20) or (mes < 3):
      print("Verano")
   elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20) or (mes < 6):
      print("Otoño")
   elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20) or (mes < 9):
      print("Invierno")
   elif (mes == 9 and dia >= 21) or (mes <= 12 and dia <= 20) or (mes < 12):
      print("Primavera")
   else:
      print("Fecha no válida")

else:
   print("Hemisferio no válido")
   






