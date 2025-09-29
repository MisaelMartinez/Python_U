"""
Maquina de SNACKS

Crear un programa donde podras comprar snacks donde podras comprar de una lista inicial

Cada snakcs tiene
1. ID
2. NOMBRE
3. PRECIO

Para comprar un snack se debe indicar el ID del snakc a comprar y se agrega a una lista de productos comprados
Ademas se debe mostrar el ticket de venta final con el toal de productos y el total de la vento
"""
opcion =0
total = 0
l = []
productos = [
    {'ID':0, 'nombre': 'Carlos V',  'precio': 15.5},
    {'ID':1, 'nombre': 'Canelitas', 'precio': 20.00},
    {'ID':2, 'nombre': 'Chetos',    'precio': 10.5},
    {'ID':3, 'nombre': 'Sabritas',  'precio': 15.5}
]

def mostrar_snacks():
    for x in productos:
        print(f'ID: {x['ID']}, NOMBRE: {x['nombre']} PRECIO: ${x['precio']}')

def comprar_snacks(total,l):
    compra_id = int(input('Ingresa el ID del producto que deseas comprar: ').strip())
    for x in productos:
        if compra_id == x['ID']:
            total += x['precio']
            l.append(x['ID'])

    return total, l

def mostrar_ticket(total,l):
    print(f'Gracias por preferir nuestra tienda.'
          f'\n\n\nTu compra consta de los siguientes productos')
    for i in l:
        print(f'{productos[i]['nombre']}: ${productos[i]['precio']}')
    print(f'El total de tu compra es ${total}')

print('**MAQUINA DE SNACKS**')
while opcion <=4:
    print('\nMENU:'
          '\n\t1. Mostrar Snacks'
          '\n\t2. Comprar Snacks'
          '\n\t3. Mostrar ticket'
          '\n\t4. Salir\n')
    opcion = int(input('Ingresa la opcion que deseas realizar: ').strip())

    if opcion == 1:
        mostrar_snacks()
    if opcion == 2:
        tupla_compra = comprar_snacks(total,l)
        total, l = tupla_compra

    if opcion == 3:
        mostrar_ticket(total,l)
    if opcion == 4:
        print('Gracias por tu compra. Hasta la proxima')
        opcion =5












