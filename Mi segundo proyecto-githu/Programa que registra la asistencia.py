#Elabora un programa que permita registrar la asistencia de estudiantes por día en una clase. Luego, muestra cuántas veces asistió cada estudiante.
asistencia = {}

def registrar_asistencia():
    dia = input(" Día de asistencia (Ej: lunes, martes...): ").strip().capitalize()
    presentes = input(" Escribe los nombres de los estudiantes presentes separados por comas: ").split(",")

    for estudiante in presentes:
        nombre = estudiante.strip().capitalize()
        if nombre:  # Solo si el nombre no está vacío
            if nombre in asistencia:
                asistencia[nombre] += 1
            else:
                asistencia[nombre] = 1

    print(f"Asistencia registrada para el día {dia}.")

def mostrar_asistencias():
    if not asistencia:
        print(" No hay asistencias registradas.")
        return
    print("\n Asistencia total por estudiante:")
    for nombre, veces in asistencia.items():
        print(f"- {nombre}: {veces} asistencias")

def menu():
    while True:
        print("\n--- Menú de Asistencia ---")
        print("1. Registrar asistencia")
        print("2. Ver resumen de asistencia")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "1":
            registrar_asistencia()
        elif opcion == "2":
            mostrar_asistencias()
        elif opcion == "3":
            print(" Cerrando el programa.")
            break
        else:
            print(" Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()