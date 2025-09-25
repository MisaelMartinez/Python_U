"""
Crear una agenda de contactos utilizando un diccionario de Python
con la sig estructutra

nombre{telefono, email, direccion }

"""

carlos = {'telefono': '5511223344',
        'email':'carlos@gmail.com',
        'direccion': 'Galerias'}

maria = {'telefono': '5522222222',
        'email':'maria@gmail.com',
        'direccion':'San Feroz'}

pedro = {'telefono': '5511111111',
        'email':'pedro@gmail.com',
        'direccion':'Jaral'}

agenda = {'carlos': carlos,
        'maria':maria,
        'pedro':pedro}

print(f'{agenda['carlos']['email']}')
print(f'{agenda['maria'].get('direccion')}')
print(f'{agenda['pedro'].values()}')

ana = {
    'telefono': '5566778899',
    'email': 'ana@gmail.com',
    'direccion': 'CU'
}

agenda['ana'] = ana

print(f'{agenda['carlos']['email']}')

del agenda['pedro']
print(agenda.keys())

for i,j in agenda.items():
    print(f'Nombre: {i}\n'
    f'\t\tTelefono: {j.get('telefono')}'
    f'\t\tEmail: {j.get('email')}'
    )





