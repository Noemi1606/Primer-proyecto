 #Escribe un  programa que imprima la tabla de multiplicar de un número dado por el usuario, desde el 1 hasta el 10, utilizando un bucle for.
try:
    numero = int(input("Ingresa un número entero para ver su tabla de multiplicar: "))

    print(f"Tabla de multiplicar del {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")