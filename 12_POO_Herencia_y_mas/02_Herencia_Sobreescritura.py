class Animal:
    def comer(self):
        print(f'Este animal come diario')

    def dormir(self):
        print('Este animal duerme diario')

class Perro(Animal): #Perro hereda los metodos de ANIMAL.
    def ladrar(self):
        print('Este animal ladra porque es un perro.')

    def comer(self):
        print('Este animal duerme 8 horas porque es un perro.')

perro1 = Perro()
perro1.dormir()
perro1.comer() #Se utiliza el metodo de la Clase Hija. El de superclase no.
#Esto es la sobreescritura, el estandar es nombrar igual este metodo en las 2 clases pero con diferente cuerpo.

