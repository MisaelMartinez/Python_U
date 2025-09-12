"""
Generar valores aleatorios
La funcion randint() es parte del modulo random para generar numero aleatorios

randint(a,b) devuelve un numero aleatorio entre a y b, incluyendo estos valores. [a,b]
Es necesario importar en primer lgar el modulo random antes de usar la funcion
"""

import random
from random import randint

#Generar un numero aleatorio entre 3 y 50 [3,50] a < b siempre
n = randint(3,50)
print(f' Numero aleatorio entre 3 y 50: {n}')

#Simular dado de 6 caras

d = randint(1,6)
print(f'Resultado del dado es: {d}')



