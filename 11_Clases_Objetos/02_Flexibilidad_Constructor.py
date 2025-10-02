"""
Crear clase aritmetica

Operador 1.
Operador 2

suma()
resta()
multiplicacion()
division()
"""

class Artimetica:
    # Python solo toma en cuenta el ultimo constructor. Este lo va a ignorar.
    # def __init__(self,x1):
    #     self.x1 = x1

    def __init__(self,x1=None,x2 = None): #Agregando None solo se puede agregar 1 parametro.
        self.x1 = x1
        self.x2 = x2

    def suma(self):
        print(f'La suma de {self.x1}+{self.x2} es igual a: {self.x1+self.x2}')

    def resta(self):
        print(f'La resta de {self.x1} - {self.x2} es igual a: {self.x1-self.x2}')

    def mutl(self):
        print(f'El resultado es: {self.x1 * self.x2}')

ari1 = Artimetica(3,4)
ari1.suma()
ari1.resta()

#Agregando valores a un solo valor
ari_1valor = Artimetica(10) #Solo se agrego x1, x2 tendra el valor de None
ari_1valor.x2 = 5 #X1 =10, x2 = 5
ari_1valor.suma()
ari_1valor.x1 = 5 #Cambiamos el valor de x1 de nuestro ultimo objeto.
ari_1valor.suma()





