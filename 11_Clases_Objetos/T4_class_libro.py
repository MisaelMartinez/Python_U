"""CLASE LIBRO PARA SISTEMA DE BIBLIOTECAS"""
class Libro:

    i_libros = 0
    def __init__(self,nombre,autor,genero):
        self._nombre = nombre
        self._autor = autor
        self._genero = genero
        Libro.i_libros +=1
        self._id = Libro.i_libros

    @property
    def nombre(self):
        return self._nombre
    @property
    def autor(self):
        return self._autor
    @property
    def genero(self):
        return self._genero

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    @autor.setter
    def autor(self,autor):
        self._autor = autor
    @genero.setter
    def genero(self,genero):
        self._genero = genero




