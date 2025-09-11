"""
Las cadenas en Python vienen con una serie de metodos utiles que facilitan su manipulacion
upper() --> cambia las letras a mayusculas
lower() --> Cambia todas las letras a minusculas
strip() --> Elimina espacios en blanco al inicio y al final de la cadena
"""

c1 = "   Hola mundo"
print(f'Cadena original: {c1}')
mayus = c1.upper()
minus = c1.lower()
esp   = c1.strip()

print(f'Cadena en mayusculas: {mayus}')
print(f'Cadena en minisculas: {minus}')
print(f'Cadena sin espacios al princio y final: {esp} \n')

print(f'Cadena sin asignar a varible: {c1.upper()}')








