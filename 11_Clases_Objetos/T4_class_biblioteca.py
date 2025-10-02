# La clase de biblioteca contiene
# Nombre y lista de libros

# Metodos de biblioteca:
# Agregar lbro *
# Buscar libros por autor*
# Buscar Libros por genero*
# Mostrar todos los libros*
# Mostrar un libro
#
# Aplicar encapsulamiento

from T4_class_libro import Libro

class Biblioteca:

    def __init__(self,nombre):
        self.nombre = nombre
        self.libros_t = []

    def agregar_libro(self,nombre,autor,genero):
        libro = Libro(nombre, autor, genero)
        self.libros_t.append(libro)

    def buscar_por_autor(self,autor):
        contador = 0
        for i in self.libros_t:
            contador +=1
            if i.autor == autor:
                print(f'Nombre del libro: {i.nombre}, Autor: {i.autor}, Genero: {i.genero}')

    def buscar_por_genero(self,genero):
        contador =0
        print(f'Los libros encontrados del genero {genero} son:')
        for i in self.libros_t:
            contador +=1
            if i.genero == genero:
                print(f"""{contador}.- {i.nombre}""")

    def mostrar_todos_libros(self):
        contador = 0
        print(f'Mostrando todos los libros')

        for i in self.libros_t:
            contador +=1
            print(f'{contador}.- {i.nombre} - {i.autor} - {i.genero}')