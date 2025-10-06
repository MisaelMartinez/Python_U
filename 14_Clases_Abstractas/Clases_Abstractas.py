#Clase ABC - Abstract Base Class
from abc import ABC, abstractmethod


class FigGeometrica(ABC):
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto

#No puede contener ninguna implementacion porque desconocemos en que se usara.
    #Forza a las clases hijas a implementar este metodo
    @abstractmethod
    def calcular_area(self):
        pass
#No se puede instanciar una clase abstracta
#figura = FigGeometrica()


class Color:
    def __init__(self,color):
        self.color = color

class Cuadrado(FigGeometrica,Color):
    def __init__(self,lado,color):
        FigGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)

    def calcular_area(self):
        return self.alto * self.alto

    def caracteristicas_cuadrado(self):
        print(f'El cuadrado es: {self.color} y tiene {self.alto * self.alto} metros cuadrados')

class Rectangulo(FigGeometrica,Color):

    def __init__(self,alto,ancho,color):
        FigGeometrica.__init__(self, ancho, alto)
        Color.__init__(self,color)

    def area_rectangulo(self):
        return self.alto * self.ancho


cuadrado_1 = Cuadrado(4,'Rojo')
cuadrado_1.caracteristicas_cuadrado()
print(cuadrado_1.calcular_area())

