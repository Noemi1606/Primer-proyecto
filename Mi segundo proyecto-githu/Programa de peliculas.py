#Define una clase Pelicula con atributos como título, director y género. Guarda varias películas en un diccionario con clave única.
class Pelicula:
    def __init__(self, titulo, director, genero):
        self.titulo = titulo
        self.director = director
        self.genero = genero

    def __str__(self):
        return f"Título: {self.titulo}, Director: {self.director}, Género: {self.genero}"

# Diccionario para guardar las películas
peliculas = {}

def agregar_pelicula():
    clave = input(" Ingresa un ID único para la película: ").strip()
    if clave in peliculas:
        print(" Ya existe una película con ese ID.")
        return

    titulo = input(" Título de la película: ").strip()
    director = input(" Director: ").strip()
    genero = input(" Género: ").strip()

    pelicula = Pelicula(titulo, director, genero)
    peliculas[clave] = pelicula
    print(" Película registrada correctamente.")

def mostrar_peliculas():
    if not peliculas:
        print(" No hay películas registradas.")
        return
    print("\n Películas registradas:")
    for clave, pelicula in peliculas.items():
        print(f"ID: {clave} → {pelicula}")

def menu():
    while True:
        print("\n--- Menú de Películas ---")
        print("1. Agregar película")
        print("2. Ver todas las películas")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "1":
            agregar_pelicula()
        elif opcion == "2":
            mostrar_peliculas()
        elif opcion == "3":
            print(" Saliendo del programa.")
            break
        else:
            print(" Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()