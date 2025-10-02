"""
El encapsulamiento nos permite ocultar la informacion que almacena un objeto tambien conocido como el estado del objeto
Para aplicar el concepto de encapsulameinto se deben aplicar 2 caracteristicas

1. Atributos protegidos o privados
    self.-nombre #Atributo protegido
    self.--apellido #Atributo privado

2. Crear metodos conocidos como get(leer) y set(modificar)
"""

class Coche:
    def __init__(self,marca, modelo,color):
        self.marca = marca #Atributo publico
        self._modelo = modelo #Atributo protegido
        self.__color = color #Atributo privado

    #Dentro de la misma clase no es necesario utiliar get y set
    def conducir(self):
        print(f""" Conducionedo el coche
        Marca: {self.marca}
        Modelo: {self._modelo}
        Color: {self.__color}
        """)
#Programa principal
if __name__ == "__main__":
    coche_1 = Coche('Toyota','Yaris','Rojo') #Inicializamos nuestro objeto 1
    coche_1.conducir()#Imprimos datos

    coche_1.marca = 'Toyota' #Cambiamos el valor
    coche_1._modelo = 'Yaris_2' #Cambiar valor de Atributo protegido, se puede pero no se debe
    coche_1.__color = 'Azul' #Aunque lo hagamos no se puede cambiar.
    coche_1.conducir()
    coche_1._Coche__color = ('Azul') #Asi si lo cambia, pero no se debe de hacer.
    coche_1.conducir()











