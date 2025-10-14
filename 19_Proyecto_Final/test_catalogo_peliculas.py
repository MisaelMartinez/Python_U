opcion = None
from dominio.Pelicula import Pelicula
from servicio.Catalogo_Peliculas import CatalogoPeliculas as cp
while opcion != 4:
    try:
        print(f'Opciones \n'
              f'1. Agregar Pelicula\n'
              f'2. Listar Peliculas\n'
              f'3. Eliminar catalogo de Peliculas\n'
              f'4. Salir\n\n')
        opcion = int(input('Escribre una opcion, del 1 al 4: '))

        if opcion == 1:
            nombre_peli = input('Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_peli)
            cp.agregar_pelicula(pelicula)
        elif opcion ==2:
            cp.listar_peliculas()
        elif opcion ==3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None
else:
    print('Salimos del programa')




