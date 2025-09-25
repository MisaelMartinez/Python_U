"""
Una coleccion es un conjutno de datos. En python tenemos varios tipos que podemos utilizar con el objetivo
de almacenar, organizar y manipular multiples cnjutnos de datos, por ello tambien se les conoce como Estructuras de datos.

Tipos:

*Listas
*Tuplas
*Set (Conjuto)
*Diccionario

"""

"""
LISTAS
Son colecciones ordenaras y mutables de elementos que pueden ser de diferentes tipos. 
Las listas son dinamicas, lo que significa que pueden cambiar de tamaño, podemos añadir, modificar o eliminar elementos
"""

numeros = [1,2,3,4,5]
frutas = ['mango', 'fresa', 'Uva']
mixta = [1, 'Diana', 3.14, [4,5]]

#Largo de una lista
print(f'El largo de la lista es: {len(numeros)}')

#Acceder a los elementos de la lista por indice
print(f'Accedemos al valor del indice 2: {frutas[1]}')
print(f'Accedemos al ultimo indice: {frutas[-1]}')

#Modificar elementos de una lista
numeros[2] = 'Hola Mundo'
print(f'Los nuevos valores de numeros son: {numeros}')

#Agregar nuevo elementos
numeros.append('222')
print(f'Los nuevos valores de numeros son: {numeros}')

#Añadir un nuevo elementos en un indice especifico
numeros.insert(3, 'Adios mundo') #4to espacio porque empieza en 0 los indices.
print(f'Los nuevos valores de numeros son: {numeros}')

#Eliminar elementos de una lista. REMOVE
numeros.remove(1) #Valor del elemento que queremos eliminar. Quita el 1 indice 0
print(f'Los nuevos valores de numeros son: {numeros}')

#Eliminar por indice. POP
numeros.pop(4) # Elimina el indice 4. En este caso es el numero 5.
print(f'Los nuevos valores de numeros son: {numeros}')

#Eliminar usando DEL
del numeros[3] #Se elimina el 4
print(f'Los nuevos valores de numeros son: {numeros}')

#Obtener sublista
sublista = numeros[1:3] #Indice del 1 al 2, el 3 no se incluye
print(f'Esta es la sublista: {sublista} \n\n')

#Iterar una lista
for i in numeros:
    print(f'El elemento es: {i}')





