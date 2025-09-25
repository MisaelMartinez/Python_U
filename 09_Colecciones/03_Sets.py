"""
Los sets son colecciones de datos no ordenados de elementos unicos. Son muy utiles cuando debemos
asegurarnos de que no haya elementos duplicados de nuestra coleccion

NO SE GARANTIZA NINGUN ORDEN

SET = {}
"""
set_1 = {1,2,3,4,5}
set_2 = {1,'Juan',3.5, 10}
set_3 = {1,1,1,1,1}
print(f'{set_3}, {len(set_3)}') #Solamente imprime un 1.
print(f'{set_2}') #Este si se desordena. pero el set_1 no

set_1.add(6)
set_1.add(7)
print(f'{set_1}')

#Eliminar un elemento del set
set_1.remove(4) #Queremos eliminar el valor de 4, no es indice, es valor.
print(f'{set_1}') #El 4 ha sido eliminado

for i in set_1:
    print(i, end = '')
print(f'\n El valor de 4 existe en el set? {4 in set_1}') #No existe, regresa FALSE

print(f'\n El valor de 4 existe en el set? {1 in set_1}') #Si existe, regresa TRUE

#Operaciones con SETS
a = {1,2,3,4}
b = {3,4,5,6}
c = a|b #Union a y b
d = a & b #Interseccion
e = a - b #Diferencia
print(f'\n\nSe unio el conjunto a y b: {c}') #El 3 y 4 no deben de estar duplicados
print(f'\n Se hizo la interseccion de a y b: {d}') #Solo se muestra el 3 y 4
print(f'\n Se muestra la diferencia de a y b: {e}') #Se elimina 3 y 4 porque son los que se repiten








