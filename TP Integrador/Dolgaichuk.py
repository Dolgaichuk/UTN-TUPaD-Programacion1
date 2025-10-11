
# Menú principal usando condicionales, bucles y listas

seguir = True
while seguir:
    print("\n--- Menú Principal ---")
    print("1. Convertir Binario-Decimal o Decimal-Binario")
    print("2. Calculadora de Expresiones Booleanas")
    print("3. Juego de Lógica")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\n--- Traductor Binario-Decimal ---")
        tipo = input("¿Qué deseas convertir? (1: Binario a Decimal, 2: Decimal a Binario): ")
        if tipo == "1":
            binario = input("Ingresa el número binario: ")
            # Validación básica
            valido = True
            for bit in binario:
                if bit != "0" and bit != "1":
                    valido = False
                    break
            if not valido:
                print("Entrada inválida. Asegúrate de ingresar solo 0 y 1.")
            else:
                # convierte el string en una lista de caracteres
                bits = list(binario)
                decimal = 0
                i = 0
                # Bucle para convertir binario a decimal
                # Se recorre la lista de bits desde el final hacia el principio
                while i < len(bits):
                    # Cálculo del valor.
                    # Se utiliza un índice negativo (-(i+1)) para empezar desde el último carácter 
                    # y avanzar hacia la izquierda. int() convierte el carácter ('0' o '1') de cada índice en un número entero.
                    # luego, se multiplica por 2 elevado a la potencia de i (la posición del bit desde la derecha, empezando en 0).
                    # Finalmente, se suma este valor al total acumulado en decimal.
                    decimal = decimal + int(bits[-(i+1)]) * (2 ** i)
                    i = i + 1
            print(f"El número decimal es: {decimal}")
        elif tipo == "2":
            decimal_str = input("Ingresa el número decimal: ")
            # 
            valido = True
            # Verifica que todos los caracteres sean dígitos
            for c in decimal_str:
                if c < "0" or c > "9":
                    valido = False
                    break
            if not valido:
                print("Entrada inválida. Ingresa un número entero positivo.")
            else:
                decimal = 0
                i = 0
                # Convertir string a entero 
                #
                while i < len(decimal_str):
                    decimal = decimal * 10 + int(decimal_str[i])
                    i = i + 1
                binario = []
                if decimal == 0:
                    binario.append("0")
                else:
                    while decimal > 0:
                        #Calcula el resto de la división del número actual entre 2 (decimal % 2). Este resto es el bit (0 o 1). 
                        # Luego, lo inserta en la posición inicial (índice 0) de la lista binario. 
                        # Esto es crucial porque el primer resto es el bit menos significativo, que debe ir al final de la secuencia binaria. 
                        # Al usar insert(0, ...), se acumulan los bits en el orden correcto.
                        binario.insert(0, str(decimal % 2))
                        # Actualiza el valor de decimal dividiéndolo por 2 y descartando la parte decimal (decimal //= 2).
                        # Esto prepara el número para la siguiente iteración.
                        decimal = decimal // 2
                print("El número binario es:", end=" ")
                for bit in binario:
                    # Imprime cada bit sin saltar línea.
                    print(bit, end="")
                print()
        else:
            print("Opción inválida.")

    elif opcion == "2":
        print("\n--- Calculadora de Expresiones Booleanas ---")
        expr = input("Ingresa una expresión booleana (ejemplo: True and not False): ")
        # 

        palabras = []
        temp = ""
        for c in expr:
            if c == "(" or c == ")":
                if temp:
                    palabras.append(temp)
                    temp = ""
            elif c == " ":
                if temp:
                    palabras.append(temp)
                    temp = ""
            else:
                temp += c
        if temp:
            palabras.append(temp)
        # Solo permite True/False y and/or/not
        operadores = ["and", "or", "not"]
        valores = ["True", "False"]
        valido = True
        for palabra in palabras:
            if palabra not in operadores and palabra not in valores:
                valido = False
        if valido:
            # 
            if "(" in expr or ")" in expr:
                print("No uses paréntesis. Usa solo True/False y and/or/not.")
            else:
                eval = True
                for palabra in palabras:
                    if palabra not in operadores and palabra not in valores:
                        try_eval = False
                if eval:
                    try:
                        resultado = eval(expr)
                        print(f"Resultado: {resultado}")
                    except Exception:
                        print("Expresión inválida. Usa True/False y operadores and, or, not.")
                else:
                    print("Expresión inválida. Usa solo True/False y and/or/not.")
        else:
            print("Expresión inválida. Usa solo True/False y and/or/not.")

    elif opcion == "3":
        print("\n--- Juego de Lógica ---")
        acertijos = [
            ["Si todos los gatos son mamíferos y algunos mamíferos son negros, ¿puede haber gatos negros? (si/no): ", "si"],
            ["Si hoy es martes y mañana no es miércoles, ¿es posible? (si/no): ", "no"],
            ["Si A implica B y B es falso, ¿A puede ser verdadero? (si/no): ", "no"]
        ]
        puntaje = 0
        for a in acertijos:
            resp = input(a[0]).strip().lower()
            if resp == a[1]:
                print("¡Correcto!")
                puntaje += 1
            else:
                print("Incorrecto.")
        print(f"Puntaje final: {puntaje}/{len(acertijos)}")

    elif opcion == "4":
        print("¡Hasta luego!")
        seguir = False
    else:
        print("Opción inválida. Intenta de nuevo.")

