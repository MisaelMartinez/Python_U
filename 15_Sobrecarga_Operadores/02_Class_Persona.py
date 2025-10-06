#Vamos a sobreescribir el metodo __ad__(self,other) de OBJECT para el ejercicio
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return self.nombre + other.nombre

    def __sub__(self, other):
        return self.edad - other.edad
persona1 = Persona('Misael',27)
persona2 = Persona('Diana',29)
print(persona1 + persona2)
print(f'Diferencia de edad: {persona2-persona1}')
print(6+6)