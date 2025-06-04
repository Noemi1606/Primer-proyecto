# Escribe un programa que pida al usuario un número entero y luego imprima todos los números desde ese número hasta el 0 en orden descendente utilizando un bucle while.
numero_inicial = int(input("Ingresa un número entero: "))

numero_actual = numero_inicial
print(f"Contando desde {numero_inicial} hasta 0:")

while numero_actual >= 0:
    print(numero_actual)
    numero_actual -= 1