"""
Generar un ID aleatorio

*Nombre     JU
*Apellido   MA
Año         98
Valor aleatorio.    ranint
"""
import random
from random import randint

print('*** Id aleatorio ***')
name = input('Ingresa tu nombre: ')
surname = input('Ingresa tu apellido: ')
año_nacimiento = input('¿En que año naciste ')
x = randint(1000,9999)

id = name.strip().upper()[0:2] + surname.strip().upper()[0:2] + año_nacimiento.strip()[2:4] + str(x)

print(f'\nTu ID unico es: {id}')