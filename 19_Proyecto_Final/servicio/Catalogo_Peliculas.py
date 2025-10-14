import os #os tiene el metodo de remover
from traceback import print_tb


class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregar_pelicula(cls,pelicula):
        with open(cls.ruta_archivo,'a', encoding = 'utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo,'r', encoding = 'utf8') as archivo:
            print('Catalogo de Peliculas:'.center(50,'_'))
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo Eliminado: {cls.ruta_archivo}')





