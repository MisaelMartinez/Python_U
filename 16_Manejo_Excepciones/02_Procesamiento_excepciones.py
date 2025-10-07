"""
Ejemplo de manejo de excepcion cuando un numero se divide sobre 0.
"""
from types import NoneType

r = NoneType
a = 10
b = 0
try:
    r = a/b
except Exception as e:
    print(f'Ocurrio un error: {e}')

print(f'El resultado de: {r}')
print('Continuamos...')

#El valor impreso es "None" porque el valor de la excepcion no se asigna a r debido a que marca un error.
#En esta clase puede ver la tabla de clases de excepciones, en Udemy.

#Ejemplo al usar otra clase de menor rango

r = None
a = '10'
b = 0
try:
    r = a/b
except TypeError as e:
    print(f'Ocurrio un error: {e}')

print(f'El resultado de: {r}')
print('Continuamos...')
#Con la clase TypeError se trabaja esta excepcion de str/int


