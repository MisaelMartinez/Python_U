"""
Crear un sistema de bibliotecas y cada objeto de bibliotecas almacena libros
Se debe aplicar POO para resolver este problema

Un libro tiene los atributos de titulo, autor, genero.
Debe aplicar el concepto de encapsulamiento

La clase de biblioteca contiene
Nombre y lista de libros
Metodos de biblioteca:
Agregar lbro
Buscar libros por autor
Buscar Libros por genero
Mostrar todos los libros
Mostrar un libro

Aplicar encapsulamiento
"""
from T4_class_libro import Libro
from T4_class_biblioteca import Biblioteca

biblioteca_1 = Biblioteca('Atizapan')
biblioteca_1.agregar_libro('Diccionario','Larousse','Idiomas')
biblioteca_1.agregar_libro('100 años de soledad','Gabriel Garcia Marquez','Drama')
print(Libro.i_libros)
biblioteca_1.buscar_por_autor('Larousse')
biblioteca_1.agregar_libro('Diccionario Ingles - Español','Larousse','Idiomas')

biblioteca_1.buscar_por_genero('Idiomas')
biblioteca_1.mostrar_todos_libros()








