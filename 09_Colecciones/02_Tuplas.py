"""
Las tuplas son una coleccion de datos ordenados, son inmutables.
Una vez creada una tupla no es posible modificar su tamaño, ni podemos agregar mas elementos,
no se pueden modificar ni eliminarlos.

Las tuplas suelen utilizarse para crear colecciones de daos que no deben de cambiar con el tiempo
TUPLA = ()
TUPLA = x1, x2, x3
"""
from pydoc import describe

print('MANEJO DE TUPLAS')
tupla_1 = (1,2,3,4,5) #Tupla.
tupla_2 = ('Hola', 1, 3.4, [1,2]) #Tupla mixta
tupla_3 = 1,1,1,1,1 #Tupla sin parentesis
tupla_4 = 1, #Tupla unitaria. Obligatorio llevar coma para que se considere tupla
tupla_5 = (1,2,3,(2,4,5),(10,)) #Tupla con tuplas
print(tupla_5)

#Unpacking tuples
producto = ('P001','Camisa', 20.00)
id,descripcion,precio = producto #Asignacion a su respectiva variable.
print(f'{id}.{descripcion},{precio}')

#Convinacion de listas con tuplas.
producto_lt = [('P001','Camisa',30),('P002','Pantalon',50),('P003','Lentes', 200)]











