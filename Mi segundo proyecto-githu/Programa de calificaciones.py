#Crea un programa que almacene las calificaciones de varios estudiantes en distintas asignaturas usando diccionarios y listas. Permite calcular el promedio por estudiante y mostrar quién tiene la mejor nota.
calificaciones = {
    "Ana": {"Matemáticas": 85, "Historia": 90},
    "Luis": {"Matemáticas": 78, "Historia": 88},
    "Sofía": {"Matemáticas": 95, "Historia": 92}
}

mejor_estudiante = ""
mejor_promedio = 0

for estudiante, materias in calificaciones.items():
    promedio = sum(materias.values()) / len(materias)
    print(f"{estudiante} tiene un promedio de {promedio:.2f}")
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = estudiante

print(f"\nEl mejor promedio es de {mejor_estudiante} con {mejor_promedio:.2f}")