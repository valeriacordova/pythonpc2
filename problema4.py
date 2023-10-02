cant_alumnos = int(input("Ingrese el número de alumnos: "))
for i in range(cant_alumnos):
    alumno = input(f"Ingrese el nombre del alumno {i + 1}: ")
    notas = []
    for j in range(3):
        calificacion = float(input(f"Ingrese la calificación {j + 1} para {alumno}: "))
        notas.append(calificacion)
    print("\nAlumno:", alumno)
    print("Notas:", notas)