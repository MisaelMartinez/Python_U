"""
Crear un programa para gestionar el inventario de un almacen.
Para ello se debe utilizar una lista de python para mantener un registro de los productos disponibles
Y para almacenar el detalle del producto utilizar un diccionario
ID
NOMBRE
PRECIO
CANTIDAD DISPONIBLE
"""

x = int(input('Cuantos productos deseas agregar al inventario? '))
i=0
lista = []
while i < x:
    id = i
    nombre = input('Ingresa el nombre del producto: ')
    precio = input('Ingresa el precio es pesos del producto: ')
    cantidad = int(input('Ingresa la cantidad disponible del producto: '))

    lista.append( {'nombre': nombre,
                'precio': precio,
                'cantidad': cantidad})
    i +=1

print(f'{lista}')









