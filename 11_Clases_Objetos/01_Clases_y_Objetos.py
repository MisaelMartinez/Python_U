"""
Python es un lenguaje orientado a objetos

Un objeto es una representacion de una entidad de la vida real en nuestro programa
Para crear un objeto primero necesitamos crear una CLASE
Una clase representa las caracteristicas en comun de nuestros objetos es la abstraccion

ELEMENTOS DE UNA CLASE (Atributos y metodos)
Atributos: Caracteristicas de nuestros objetos
Metodos: Son las acciones que pueden realizar nuestros objetos. En si, estas acciones son funciones,
pero cuando se asocian a una clase son metodos.

EJEMPLO

Persona:
    Atributos:
        Nombre
        Apellido
        email
        Telefono
    Metodos:
        agregar_nombre()
        mostrar_persona()
"""
#EJEMPLO: Clase persona

class Persona:

    def inicializar_persona(self,nombre,apellido):
        #Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')


##Creacion de objetos
if __name__ == '__main__':
    #Creacion de nuestro primer objeto
    persona_1 = Persona() #Creamos un objeto vacio en memoria
    persona_1.inicializar_persona('Misael','Martinez')
    persona_1.mostrar_persona()

    #Creando persona2, objeto 2
    persona_2 = Persona()
    persona_2.inicializar_persona('Diana','Bautista')
    persona_2.mostrar_persona()

"""
Constructores en Python
Un construcctor es un metodo especual y se utiliza para crear un objeto o instancias una clase.
Ademas puede servir para crear e inicializar los atributos de un nuevo objeto.
"""

class People:
    def __init__(self,nombre,apellido): #__INIT__ metodo magico o dunder (doble underscove)
        self.nombre = nombre
        self.apellido = apellido
    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        print(f'Direccion decimal en memoria: {id(self)}')
        print(f'Direccion en memoria hex: {hex(id(self))}')

if __name__ == '__main__':
    Persona_3 = People('Misael','Martinez')
    Persona_3.mostrar_persona()

#print(Persona_3) #Imprime la misma direccion que la linea 67










