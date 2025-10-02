class Animal:
    def comer(self):
        print(f'Este animal come diario')

    def dormir(self):
        print('Este animal duerme diario')

    def hacer_ruido(self):
        print('Este animal hace un sonido')


class Perro(Animal): #Perro hereda los metodos de ANIMAL.
    def hacer_ruido(self):
        print('Este animal Ladra')

class Gato(Animal):
    def hacer_ruido(self):
        print('Este animal Maulla')

perrito = Animal()
perrito.hacer_ruido()#CLASE PADRE O SUPERCLASE

perrito_1 = Perro()
perrito_1.hacer_ruido()#SUBCLASE

gatito = Gato()
gatito.hacer_ruido() #SUBCLASE







