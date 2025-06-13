#Crea una clase Tarea con nombre, prioridad y estado. Almacena las tareas en un diccionario y permite marcarlas como completadas.
class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
        self.estado = "Pendiente"

    def marcar_completada(self):
        self.estado = "Completada"

    def __str__(self):
        return f"Tarea: {self.nombre} | Prioridad: {self.prioridad} | Estado: {self.estado}"

# Diccionario para almacenar las tareas
tareas = {}

def agregar_tarea():
    clave = input("ID o nombre corto de la tarea: ").strip()
    if clave in tareas:
        print("Ya existe una tarea con esa clave.")
        return
    nombre = input("Nombre de la tarea: ").strip()
    prioridad = input("Prioridad (Alta, Media, Baja): ").strip().capitalize()
    tarea = Tarea(nombre, prioridad)
    tareas[clave] = tarea
    print("Tarea agregada con éxito.")

def mostrar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    print("\nLista de Tareas:")
    for clave, tarea in tareas.items():
        print(f"{clave} → {tarea}")

def completar_tarea():
    clave = input("ID de la tarea a marcar como completada: ").strip()
    if clave in tareas:
        tareas[clave].marcar_completada()
        print("Tarea marcada como completada.")
    else:
        print("No se encontró ninguna tarea con ese ID.")

def menu():
    while True:
        print("\n--- Menú de Tareas ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Salir")
        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()