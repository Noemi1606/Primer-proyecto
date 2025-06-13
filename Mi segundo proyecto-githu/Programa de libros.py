#Desarrolla una clase Libro con atributos como título, autor y año. Luego, crea una lista de libros y permite buscar por autor o año.
class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __str__(self):
        return f"'{self.titulo}', de {self.autor} ({self.año})"

def buscar_por_autor(libros, autor_buscar):
    encontrados = [libro for libro in libros if libro.autor.lower() == autor_buscar.lower()]
    return encontrados

def buscar_por_año(libros, año_buscar):
    encontrados = [libro for libro in libros if libro.año == año_buscar]
    return encontrados

def main():
    libros = [
        Libro("Cien años de soledad", "Gabriel García Márquez", 1967),
        Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605),
        Libro("La sombra del viento", "Carlos Ruiz Zafón", 2001),
        Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985)
    ]

    print("Buscar libros por autor o año.")
    opcion = input("Escribe 'autor' para buscar por autor o 'año' para buscar por año: ").strip().lower()

    if opcion == "autor":
        autor = input("Introduce el nombre del autor: ").strip()
        resultados = buscar_por_autor(libros, autor)
        if resultados:
            print(f"\nLibros de {autor}:")
            for libro in resultados:
                print(f"- {libro}")
        else:
            print("No se encontraron libros de ese autor.")
    elif opcion == "año":
        try:
            año = int(input("Introduce el año de publicación: ").strip())
            resultados = buscar_por_año(libros, año)
            if resultados:
                print(f"\nLibros publicados en {año}:")
                for libro in resultados:
                    print(f"- {libro}")
            else:
                print("No se encontraron libros de ese año.")
        except ValueError:
            print("El año debe ser un número entero.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()