"""
Los metodos de Clase
"""
class Persona:
    #Atributo de clase
    contador_persona = 0

    def __init__(self, nombre, apellido): #Este es un metodo de instancia
        #Incrementamos el valor del atributo de clase
        Persona.contador_persona += 1
        self.id = Persona.contador_persona
        self.nombre = nombre
        self.apellido = apellido


    def mostrar_info(self):
        print(f'Persona numero {self.id}, Nombre: {self.nombre} {self.apellido}')

    #Metodos de CLASE
    @staticmethod
    def get_contador_personas_estatico():
        print(f'Metodo estatico')
        return Persona.contador_persona

#Segunda forma, mas pythonica, mas simplificada
    @classmethod
    def get_contador_persona_clase(cls):
        print(f'METODO DE CLASE')
        return cls.contador_persona #Metodo de clase e instancia de clase

    # def total_personas(self):
    #     print(f'Se han creado {Persona.contador_persona} personas')

persona_1 = Persona('Misael', 'Martinez')
persona_1.mostrar_info()
persona_2 = Persona('Diana','Te amo mi amor')
persona_2.mostrar_info()

print(Persona.contador_persona) #Imprime el valor de contador persona

#Accedemos al contador de personas con el metodo de clase estatico
print(f'Hola, el numero de personas creadas es: {Persona.get_contador_personas_estatico()}')
print(f' {Persona.get_contador_persona_clase()}')
#Acceder a atributo de clase desde un objeto
print(f'Contador objetos PERSONA(persona_1): {persona_1.contador_persona}')






