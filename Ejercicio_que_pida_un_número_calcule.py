#Escribe un programa que pida al usuario un número y luego calcule su factorial utilizando un bucle while. El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.
try:
    numero = int(input("Ingresa un número entero positivo para calcular su factorial: "))

    if numero < 0:
        print("El factorial no está definido para números negativos.")
    elif numero == 0:
        print("El factorial de 0 es: 1")
    else:
        factorial = 1
        contador = 1
        while contador <= numero:
            factorial *= contador
            contador += 1
        print(f"El factorial de {numero} es: {factorial}")

except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")