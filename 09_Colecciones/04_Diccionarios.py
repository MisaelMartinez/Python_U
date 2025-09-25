"""
Los diccionarios son una coleccion de datos ordenada. Y se almacenan en forma de CLAVE:VALOR
Es una estructura muy util cunado necesitas asociar un conjunto de valores con un conjunto de claves que sirven
como indices unicos

DICCIONARIO = {X1:Y1, X2:Y2}
Los diccionarios tambien no aceptan valores duplicados
"""

persona = {'nombre':'Misael',
           'edad':27,
           'ciudad':'México'
            }

print(persona) #Imprimimos el diccionario

#Acceder a los elementos del diccionario
print(f'Nombre: {persona['nombre']}') #Con la clave imprimimos el valor. Si nos marca error en las comillas, utilizar comillas dobles
print(f'Edad: {persona.get('edad')}') #Segundo metodo para obtener el valor a partir de la clave edad.
print(f'Ciudad: {persona['ciudad']}')

#Modificando valores
persona['edad'] = 35
print(f'\nEdad nueva: {persona['edad']}')

#Agregar nuevo elemento
persona['profesion'] = 'Ingeniero'
print(f'\n{persona}')

#Eliminar un elemento del diccioanrio
del persona['profesion']
print(f'\n{persona}')

persona.pop('ciudad') #Tambien elimina un elemento
print(f'\n{persona}')

#Iterar
for i,j in persona.items():#Clave y valor
    print(f'{i}:{j}')

for i in persona.keys(): #Solo clave
    print(f'{i}:')

for i in persona.values(): #Solo valor.
    print(f':{i}')


















