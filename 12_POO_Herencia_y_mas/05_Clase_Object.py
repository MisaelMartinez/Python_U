"""
Cuando trabajamos en python la clase OBJECT es la de mayor jerarquia
__init__
__str__
__eq__ --> Si dos objetos son iguales

class Persona: -->Automaticamente heredamos de la clase OBJECT
Sobreescribimos el __init__ o podemos sobreescribir __str__
esta clase tiene sus propios metodos descritos por nosotros.
"""
class Persona: #Sin decirlo ya se esta heredando de la clase Object
    def __init__(self,nombre,apellido): #Primer sobreescritura de OBJECT
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self): #Default: Imprime la direccion de memoria del objeto con el que estamos trabajando
        return f'''Persona:
        nombre: {self.nombre}
        apellido: {self.apellido}
        Direccion mem: {super.__str__(self)}''' #Llamar el metodo de OBJECT o superclase.



#main
persona_1 = Persona('Misael','Martinez')
print(persona_1) #Se llama al metodo __str__ en automatico desde print.
#El metodo __str__ de OBJECT solo imprime el __main__.Persona object at 0xDireccion...
#Es mejor hacer nuestro metodo __str__

#Acceder al comportamiento de la superclase sin quitar metodo de busclase
print(super.__str__(persona_1)) #Metodo de la superclase y no subclase.


