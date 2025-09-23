"""
Ejercicio para aplicar conocimientos de while e if.
Sistema de creacion y eliminacion de cuenta.
"""

print('Sistema de administracion de cuenta')
x=0
print('Sistema de administracion de cuentas')
print('Menu:')
while x != 3:
    print('1. Crear cuenta:\n'
        '2. Eliminar cuenta\n'
        '3. Salir\n')
    x = int(input('Elije una opcion: '))
    if x == 1:
        print('Tu cuenta ha sido creada\n')
    elif x == 2:
        print('Tu cuenta ha sido eliminada\n')
    elif x == 3:
        print('Se ha salido del sistema.\n')
    else:
        x=0



