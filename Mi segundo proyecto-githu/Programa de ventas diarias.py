#Crea un programa que registre las ventas diarias como tuplas (día, monto) dentro de una lista. Al final, muestra el total y el día con mayor venta.
ventas = []

def registrar_venta():
    dia = input(" Día de la venta: ").strip().capitalize()
    try:
        monto = float(input(" Monto de la venta: "))
        ventas.append((dia, monto))
        print(" Venta registrada correctamente.")
    except ValueError:
        print("❗ El monto debe ser un número válido.")

def mostrar_resumen():
    if not ventas:
        print(" No hay ventas registradas.")
        return

    total = sum(monto for _, monto in ventas)
    dia_mayor_venta = max(ventas, key=lambda x: x[1])

    print("\n Resumen de Ventas:")
    print(f"Ventas registradas: {ventas}")
    print(f"Total vendido: RD${total:.2f}")
    print(f"Día con mayor venta: {dia_mayor_venta[0]} (RD${dia_mayor_venta[1]:.2f})")

def menu():
    while True:
        print("\n--- Menú de Ventas ---")
        print("1. Registrar venta")
        print("2. Ver resumen de ventas")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            mostrar_resumen()
        elif opcion == "3":
            print(" Cerrando el programa.")
            break
        else:
            print(" Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()











