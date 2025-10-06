class FigGeometrica:
    def __init__(self,ancho,alto):
        self._ancho = ancho
        self._alto = alto

    def __str__(self):
        return (f'El ancho de la figura es: {self._ancho}'
                f'El alto de la figura es: {self._alto}')

    @property
    def ancho(self):
        return self._ancho
    @property
    def alto(self):
        return self._alto

    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho
    @alto.setter
    def alto(self,alto):
        self._alto = alto

class Color:
    def __init__(self,color):
        self._color = color

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color = color

class Cuadrado(FigGeometrica,Color):
    def __init__(self,lado,color):
        FigGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)

    def calcular_area(self):
        return self.alto * self.alto

    def __str__(self):
        return f'''CUADRADO:
        Su color es: {self.color} 
        Su altura es: {self.alto}
        Su ancho es : {self.ancho}
        Su area total es: {self.alto * self.alto} metros cuadrados'''

class Rectangulo(FigGeometrica,Color):

    def __init__(self,ancho,alto,color):
        FigGeometrica.__init__(self, ancho, alto)
        Color.__init__(self,color)

    def area_rectangulo(self):
        return self.alto * self.ancho

    def __str__(self):
        return  f'''RECTANGULO:
        El ancho es: {self.ancho}
        El alto es: {self.alto}
        El color es: {self.color}
        El area total es: {Rectangulo.area_rectangulo(self)}'''


cuadrado_1 = Cuadrado(4,'Rojo')
print(cuadrado_1)
rectangulo_1 = Rectangulo(5,4,'Amarillo')
print(rectangulo_1)