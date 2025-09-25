"""
La comprension de listas es una forma consica y eficiente de crear listas a partir de otros iterables.
Permite filtrar elementos y aplicar expresiones a cada elemento de un iterable, de manera muy legible y en una sola linea
de codigo

[nueva_expresion FOR i IN Iterable IF condicion]

*nueva expresion: Define como se modifica o procesa cada elemento del iterable
*i: Representa cada elemento iterable original
*iterable: Coleccion la cual se itera
*Condicion: Condicion para filtrar los elementos del iterable. OPCIONAL
"""

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = [x for x in numeros if x%2 == 0]
print(pares)

#Ejemplo de cuadrados
cuadrados = [x**2 for x in numeros]
print(cuadrados)



