"""
Crear aplicacion de cajero automatico

*Depositar, retirar y consultar saldo
"""

print('***Sistema de cajero automatico***')
x=0
saldo = 1000
print('Menu:')
while x != 4:
    print('1. Depositar saldo:\n'
        '2. Retirar saldo\n'
        '3. Consultar saldo\n'
        '4. Salir\n')
    x = int(input('Elije una opcion: '))
    if x == 1:
        y = int(input('¿Cuanto dinero depositaras? '))
        saldo = saldo + y
    elif x == 2:
        y = int(input('¿Cuanto dinero deseas retirar\n'))
        saldo = saldo - y
    elif x == 3:
        print(f'Tu saldo es: {saldo}\n')
    elif x == 4:
        print('Saliendo del sistema')