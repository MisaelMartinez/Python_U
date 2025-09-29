"""
Crear un sistema de inventarios que tenga las siguientes opciones

Mostrar Menu:
1. Mostrar inventario
2. Agregar un nuevo producto
3. Buscar producto por ID
4. Salir

Detalles del producto:
1. ID
2. NOMBRE
3. PRECIO
4. CANTIDAD
"""


id=2
i=0
chetos = {'ID': 0,
          'nombre': 'chetos',
          'precio': 15.5,
          'cantidad': 20
          }

queso = {'ID': 1,
         'nombre': 'queso',
         'precio': 34.00,
         'cantidad': 3
         }

productos = [chetos, queso]

while i <= 4:
    print('\nMENU:'
          '\n\t1. Mostrar Inventario'
          '\n\t2. Agregar nuevo producto'
          '\n\t3. Buscar producto por ID'
          '\n\t4. Salir\n')
    i = int(input('Ingresa la opcion que deseas realizar: ').strip())

    if i ==1:
        print(f'\n\nEl inventario que tenemos actualmente es:')
        for x in productos:
            print(f'Nombre:{x['nombre']}, Precio: {x['precio']}, Cantidad disponible: {x['cantidad']}.')
    if i == 2:
        n_productos = int(input('Cuantos productos deseas agregar al inventario? ').strip())
        nombre = input('Ingresa el nombre del producto: ').strip()
        precio = input('Ingresa el precio en pesos del producto: ').strip()
        cantidad = int(input('Ingresa la cantidad disponible del producto: ').strip())

        productos.append( {'ID':id,
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad})
        id += 1

    if i==3:
        buscar_id = int(input('Ingresa el ID del producto que deseas buscar: ').strip())
        if buscar_id> len(productos):
            print('No es posible encontrarlo.')
        else:
            for a in productos:
                if a['ID'] == buscar_id:
                    print(f' El producto solicitado es: '
                          f'{a['nombre']}')
    if i==4:
        print('Saliendo del menu')
        i = 5

print(f'Regrese pronto')





























