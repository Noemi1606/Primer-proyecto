#Implementa un sistema de inventario donde se pueda agregar, consultar y actualizar el stock de productos. Cada producto tendrá nombre, cantidad y precio.
# Sistema de inventario simple

inventario = {}

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    if nombre in inventario:
        print("El producto ya existe en el inventario.")
        return
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio por unidad: "))
    except ValueError:
        print("Error: la cantidad debe ser un número entero y el precio un número válido.")
        return
    inventario[nombre] = {"cantidad": cantidad, "precio": precio}
    print(f"Producto '{nombre}' agregado correctamente.")

def consultar_producto():
    nombre = input("Ingrese el nombre del producto a consultar: ").strip()
    if nombre in inventario:
        producto = inventario[nombre]
        print(f"Producto: {nombre}")
        print(f"Cantidad disponible: {producto['cantidad']}")
        print(f"Precio por unidad: RD${producto['precio']:.2f}")
    else:
        print("Producto no encontrado en el inventario.")

def actualizar_stock():
    nombre = input("Ingrese el nombre del producto para actualizar: ").strip()
    if nombre in inventario:
        try:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario[nombre]["cantidad"] = nueva_cantidad
            print(f"Stock del producto '{nombre}' actualizado a {nueva_cantidad}.")
        except ValueError:
            print("Error: la cantidad debe ser un número entero.")
    else:
        print("Producto no encontrado en el inventario.")

def mostrar_menu():
    while True:
        print("\n----- Menú de Inventario -----")
        print("1. Agregar producto")
        print("2. Consultar producto")
        print("3. Actualizar stock")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_producto()
        elif opcion == "3":
            actualizar_stock()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
