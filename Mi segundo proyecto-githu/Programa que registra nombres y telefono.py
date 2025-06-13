#Diseña un programa que permita registrar nombres y teléfonos. Al buscar un nombre, debe mostrar todos los números asociados.
agenda = {
    "Noemi": ["809-123-4567", "829-555-1234"],
    "Maritza": ["849-000-7890"]
}

nombre = input("Ingrese el nombre a buscar: ")
telefonos = agenda.get(nombre)

if telefonos:
    print(f"Números de {nombre}: {', '.join(telefonos)}")
else:
    print("Nombre no encontrado.")
