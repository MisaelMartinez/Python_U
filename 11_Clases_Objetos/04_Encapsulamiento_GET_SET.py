"""
Creacion de metodos SET y GET
"""


class Coche:
    def __init__(self,marca, modelo,color):
        self._marca = marca #Atributo publico
        self._modelo = modelo #Atributo protegido
        self._color = color #Atributo privado

    #Todos los atributos son protegidos "_xxxx"
    def conducir(self):
        print(f""" Conducionedo el coche
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}
        """)
    #ESTA ES LA FORMA ANTIGUA. LO QUE ESTE FUERA DEL COMENTARIO ES MAS SIMPLIFICADO

    # #MARCA
    # def get_marca(self):
    #     return self._marca
    # def set_marca(self, marca):
    #     self._marca = marca
    # #MODELO
    # def get_modelo(self):
    #     return self._modelo
    # def set_modelo(self,modelo):
    #     self._modelo = modelo
    # #COLOR
    # def get_color(self):
    #     return self._color
    # def set_color(self, color):
    #     self._color = color



    #Metodos GET
    @property
    def marca(self):
        return self._marca
    @property
    def modelo(self):
        return self._modelo
    @property
    def color(self):
        return self._color

##Metodos SET
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @color.setter
    def color(self, color):
        self._color = color

#Programa principal
if __name__ == "__main__":
    coche_1 = Coche('Toyota','Yaris','Rojo') #Inicializamos nuestro objeto 1
    coche_1.conducir()#Imprimos datos
# #MALAS PRACTICAS, SE CORRIGE CON EL NUEVO CODIGO DE PROPERTY Y SETTER.
#
#     # coche_1.marca = 'Toyota' #Cambiamos el valor
#     coche_1.set_marca('Toyota_2') #Practica correcta
#
#     # coche_1._modelo = 'Yaris_2' #Cambiar valor de Atributo protegido, se puede pero no se debe
#     coche_1.set_modelo('Yaris_2')#Practica correcta
#
#     # coche_1.__color = 'Azul' #Aunque lo hagamos no se puede cambiar.
#     coche_1.set_color('Verde')
#
#
#     coche_1.conducir()
    coche_1.marca = 'NISSAN'
    print(coche_1.marca)
    coche_1.conducir()

#Agregar un nuevo atributo de manera dinamica unicamente a 1 objeto
    setattr(coche_1,'nuevo_atributo','Valor de nuevo atributo')
    coche_1.Natributo2 = 'Solo funciona para este objeto'
    coche_1.conducir()
    print(coche_1.nuevo_atributo)
    print(coche_1.Natributo2)

    #Preguntar cuales son los atributos de un objeto
    print(coche_1.__dict__) #Diccionario de este objeto.















