while True:
    try:
        cantidad = int(input("Ingrese la cantidad de calificaciones: "))
        if cantidad > 0:
            break
        print("La cantidad debe ser mayor que cero.")
    except ValueError:
        print("La cantidad debe ser un número entero.")

calificaciones = []

while len(calificaciones) < cantidad:
    try:
        calificacion = float(input(f"Ingrese la calificación {len(calificaciones) + 1}: "))
        if 0 <= calificacion <= 10:
            calificaciones.append(calificacion)
        else:
            print("La calificación debe estar entre 0 y 10.")
    except ValueError:
        print("La calificación debe ser numérica.")

promedio = sum(calificaciones) / len(calificaciones)
aprobados = sum(calificacion >= 6 for calificacion in calificaciones)

print(f"Promedio: {promedio:.2f}")
print(f"Nota máxima: {max(calificaciones):.2f}")
print(f"Nota mínima: {min(calificaciones):.2f}")
print(f"Estudiantes aprobados: {aprobados}")
