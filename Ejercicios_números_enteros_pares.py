#Escribe un programa que pida al usuario un número entero positivo y luego imprima todos los números impa
try:
    numero_limite = int(input("Ingresa un número entero positivo: "))

    if numero_limite <= 0:
        print("Por favor, ingresa un número entero positivo.")
    else:
        numero_actual = 1

        print(f"Números impares desde 1 hasta {numero_limite}:")

        while numero_actual <= numero_limite:
            if numero_actual % 2 != 0:
                print(numero_actual)
            
            numero_actual += 1

except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")