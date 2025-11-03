from ClienteDAO import clienteDAO
from Zona_fit_mysql.Cliente import Cliente

print(f'ZONA FIT. SISTEMA PRINCIPAL.')

n= None
while n !=5:
    print('MENU PRINCIPAL:\n'
          '1. Ver todos los clientes\n'
          '2. Agregar cliente\n'
          '3. Actualizar cliente\n'
          '4. Eliminar cliente\n'
          '5. Salir...\n')
    n = int(input('Selecciona una opción (1-5): '))

    if n == 1:
        print('Mostrando todos los clientes')
        clientes  = clienteDAO.sel()
        for i in clientes:
            print(i)
        print('\n')
    if n ==2:
        print('Ingresando un cliente')
        name = input('Ingresa el nombre del cliente: ')
        surname = input('Ingresa el apellido del cliente: ')
        memb = input('Ingresa el numero de la membresia: ')
        cliente = Cliente(nombre = name, apellido= surname, membresia=memb)
        clienteDAO.ins(cliente)
        print('Se ingreso un nuevo cliente')
    if n==3:
        print('Actualizando un cliente')
        name = input('Ingresa el nombre del cliente: ')
        surname = input('Ingresa el apellido del cliente: ')
        memb = input('Ingresa el numero de la membresia: ')
        id_c = input('Que ID tiene el cliente que quieres actualizar: ')
        cliente = Cliente(nombre=name, apellido=surname, membresia=memb,id=id_c)
        clienteDAO.act(cliente)
        print('Se actualizo un cliente')

    if n ==4:
        id_c = input('Que ID tiene el cliente que quieres eliminar: ')
        cliente = Cliente(id = id_c)
        clienteDAO.eliminar(cliente)
        print('Se elimino un cliente')

print('HASTA LA PROXIMA.')
