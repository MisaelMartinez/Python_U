"""
Solicitar al usuario un valor entre 0 y 5 e indicarle si el valor proporcionado esta dentro de rango
"""

x = int(input('Ingresa un valor entre 0 y 5: ').strip())
y = 0 <= x <= 5

print(f'El valor ingresado esta dentro del rango? {y}')