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