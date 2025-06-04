#Escribe un programa que pida al usuario un número entero positivo. El programa debe contar cuántos dígit
numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("Por favor, ingresa un número positivo.")
else:
    contador_digitos = 0
    if numero == 0:
        contador_digitos = 1
    else:
        temp_numero = numero
        while temp_numero > 0:
            temp_numero = temp_numero // 10
            contador_digitos += 1

    print(f"El número {numero} tiene {contador_digitos} dígitos.")