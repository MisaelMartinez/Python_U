class Animal:
    def comer(self):
        print(f'Este animal come diario')

    def dormir(self):
        print('Este animal duerme diario')

class Perro(Animal): #Perro hereda los metodos de ANIMAL.
    def ladrar(self):
        print('Este animal ladra porque es un perro.')

#Perro puede utilizar los metodos de ANIMAL y lo Propios.
Animal_1 = Perro()
Animal_1.comer()
Animal_1.ladrar()
Animal_1.dormir()

#Pero Animal no puede utilizar ladrar. solo perro.





