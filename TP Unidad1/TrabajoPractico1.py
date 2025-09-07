# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print ("Ejercicio 1")
print (" ")
print ("Hola Mundo")
print (" ")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

print (" ")
print ("Ejercicio 2")
print (" ")
nombre=input("Ingrese su nombre ",)
print("")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

print (" ")
print ("Ejercicio 3")
print (" ")
nombre=input("Ingrese su Nombre ",)
print("")
apellido=input("Ingrese su Apellido ",)
print("")
edad=input("Ingrese su Edad ",)
print("")
residencia=input("Ingrese su lugar de residencia actual ",)
print("")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro

print (" ")
print ("Ejercicio 4")
print (" ")
rad=input("Ingrese el radio del círculo a calcular ",)
rad = int(rad)
pi= 3.14
areaC= rad * rad * pi
perimetro= 2 * pi * rad 
print (f"El area del círculo es {areaC} y su perimetro es {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

print (" ")
print ("Ejercicio 5")
print (" ")
min=input("Ingrese una cantidad de minutos para calcular a cuántas horas equivale ",)
min= int(min)
hora= min // 60
print (f"La cantidad de horas dentro de los {min} minutos es {hora} hora/s")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

print (" ")
print ("Ejercicio 6")
print (" ")
numero=input("Ingrese Número para imprimir la tabla de multiplicar ",)
numero= int(numero)
resultado=0
print (f"{numero} x 0 = {resultado}")
resultado= numero * 1
print (f"{numero} x 1 = {resultado}")
resultado= numero * 2
print (f"{numero} x 2 = {resultado}")
resultado= numero * 3
print (f"{numero} x 3 = {resultado}")
resultado= numero * 4
print (f"{numero} x 4 = {resultado}")
resultado= numero * 5
print (f"{numero} x 5 = {resultado}")
resultado= numero * 6
print (f"{numero} x 6 = {resultado}")
resultado= numero * 7
print (f"{numero} x 7 = {resultado}")
resultado= numero * 8
print (f"{numero} x 8 = {resultado}")
resultado= numero * 9
print (f"{numero} x 9 = {resultado}")
resultado= numero * 10
print (f"{numero} x 10 = {resultado}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print (" ")
print ("Ejercicio 7")
print (" ")
num1=input("Ingrese el primer Número para para realizar los cálculos que sea distinto a cero ",)
num1= int(num1)
num2=input("Ingrese el segundo Número distinto de cero ",)
num2= int(num2)
resultado = num1 * num2
print (f"{num1} x {num2} = {resultado}")
resultado = num1 / num2
print (f"{num1} / {num2} = {resultado}")
resultado = num1 + num2
print (f"{num1} + {num2} = {resultado}")
resultado = num1 - num2
print (f"{num1} - {num2} = {resultado}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 
# IMC = peso en kg / (altura en m)**2

print (" ")
print ("Ejercicio 8")
print (" ")
altura = input("Ingrese su altura en metros ",)
altura = float(altura)
peso = input("Ingrese su peso en kg ",)
peso = float(peso)
resultado = peso / (altura**2)
print (f"Calculando su peso de {peso} Kg y su altura {altura} mts, su IMC es = {resultado}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
print (" ")
print ("Ejercicio 9")
print (" ")
tempC = input("Ingrese una temperatura en grados Celsius para imprimir su equivalente en grados Fahrenheit ",)
tempC = float(tempC)
resultado = 1.8 * tempC + 32
print (f"Teniendo en cuenta los {tempC}º Celsius la conversión es de {resultado}º Fahrenheit")
# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

print (" ")
print ("Ejercicio 10")
print (" ")
num1 =input("Ingrese el primer número ",)
num1 = float(num1)
num2 =input("Ingrese el segundo número ",)
num2 = float(num2)
num3 =input("Ingrese el tercer número ",)
num3 = float(num2)
resultado = (num1 + num2 + num3)/ 3
print (f"El promedio entre los numeros {num1}, {num2}, {num3} es {resultado} ")