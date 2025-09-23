"""
Dibujar un triangulo simetrico
"""

print("***Dibujar triangulo simetrico")
n_filas = int(input('Proporciona el numero de filas: '))

#Itera sobre cada fila del triangulo
for fila in range(1, n_filas+1):
    espacios_blanco = ' ' * (n_filas - fila)
    asteriscos = '*' * (2*fila-1)
    print(f'{espacios_blanco}{asteriscos}')