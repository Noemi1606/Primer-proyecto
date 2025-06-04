#Escribe un programa que imprima la serie de Fibonacci hasta el enésimo término, donde el valor de n lo ingresa el usuario, utilizando un bucle for.
try:
    n_terminos = int(input("Ingresa el número de términos de la serie de Fibonacci que deseas ver: "))

    if n_terminos <= 0:
        print("Por favor, ingresa un número entero positivo.")
    elif n_terminos == 1:
        print("Serie de Fibonacci:")
        print(0)
    else:
        a, b = 0, 1

        print("Serie de Fibonacci:")
        for _ in range(n_terminos):
            print(a, end=" ")
            a, b = b, a + b
        print()

except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")