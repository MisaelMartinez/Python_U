"""Lista de Reproduccion"""

print('PlayList de canciones')

canciones = []
n_canciones = int(input('Cuantas canciones deseas agregar? ').strip())

for i in range(n_canciones):
    name_cancion = input(f'Ingresa el nombre de la cancion {i+1}:')
    canciones.append(name_cancion.strip())

#Agregamos canciones
canciones.append('Tu ultima cancion')
canciones.append('Dream on')
canciones.append('El gato volador')

#Ordenando por de A-Z
canciones.sort()
print(f' caciones en orden alfabetico:\n{canciones}')
#Ordenamiento de Z-A
"""canciones.sort(reverse=True)
print(f' caciones en orden alfabetico:\n{canciones}')
"""












