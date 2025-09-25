"""
Solicitar el numero de calificaiones a utilizar para el promedio
Solicitar calificaciones
Realizar suma de todas las calificaiones e imprimir promedio
"""

calificaciones = []
alumnos = int(input('Cuantos alumnos tienes? ').strip())
suma = 0
for i in range(alumnos):
    calificacion_ind = int(input(f'Ingresa la calificacion del alumno{i+1}: ').strip())
    calificaciones.append(calificacion_ind)
    suma = suma + calificacion_ind

print(f'El promedio grupal es: {suma/alumnos}')







