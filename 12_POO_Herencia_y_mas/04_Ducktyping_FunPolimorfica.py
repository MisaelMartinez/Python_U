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

def funcion_polimorfica(animal):
    animal.hacer_ruido()#No llamamos a print porque en la funcion ya esta
print('\n')
#DUCKTYPKING es Si parece perro y se comporta como perro es un perro. o aplicado en gato, etc.
funcion_polimorfica(perrito)
funcion_polimorfica(perrito_1)
funcion_polimorfica(gatito)






