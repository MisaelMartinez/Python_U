"""
El operador ternario en Python es una forma compacta de agregar una condicion
El objeto es asignar un valor a una variable dependiendo del valor de la condicion
"""

#Ejemplo
edad = 18
es_adulto = 'Si' if edad>= 18 else 'No'
print(es_adulto)

#Ejemplo Sin operador ternario
if edad>=18:
    es_adulto= 'Si'
else:
    es_adulto = 'No'

print(es_adulto)







