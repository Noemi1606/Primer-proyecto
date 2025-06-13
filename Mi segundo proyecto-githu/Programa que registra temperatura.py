#Crea un programa que registre temperaturas diarias durante una semana y calcule la media, la temperatura más alta y la más baja.
def registrar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas diarias de la semana:")

    for i in range(1, 8):
        while True:
            try:
                temp = float(input(f"Día {i}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido para la temperatura.")

    return temperaturas

def calcular_media(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def mostrar_resultados(temperaturas):
    media = calcular_media(temperaturas)
    max_temp = max(temperaturas)
    min_temp = min(temperaturas)

    print("\n--- Resultados ---")
    print(f"Temperaturas registradas: {temperaturas}")
    print(f"Temperatura media: {media:.2f}")
    print(f"Temperatura más alta: {max_temp}")
    print(f"Temperatura más baja: {min_temp}")

def main():
    temperaturas = registrar_temperaturas()
    mostrar_resultados(temperaturas)

if __name__ == "__main__":
    main()
