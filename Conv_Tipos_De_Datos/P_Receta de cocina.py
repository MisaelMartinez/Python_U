""""
Receta de cocina

Crear un programa para solicitar algunos valores importantes para una receta de cocina
Los valores que deben introducir son:

*Nombre de la receta
*Ingredientes
*Tiempo de preparacion (Minutos)
*Dificultad (Facil media o alta)
"""
print('*** RECETA DE COCINA ***')
n_receta = input('Ingresa el nombre de la receta: ')
ingredietes = input('Ingresa los ingredientes separados por coma: ')
tiempo_prep = input('Cuanto tiempo tardas en prepararlo (min)? ')
dificultad = input('Ingresa la difucultad (Facil, Media, Alta): ')

print(f'\nEl nombre de la rece es: {n_receta}\n'
      f'Sus ingredientes son: {ingredietes}\n'
      f'Tarda {tiempo_prep} minutos en prepararse\n'
      f'Dificultad: {dificultad}')









