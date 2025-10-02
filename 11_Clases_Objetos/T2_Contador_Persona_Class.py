class Persona:
    #Atributo de clase
    contador_persona = 0

    def __init__(self, nombre, apellido):
        #Incrementamos el valor del atributo de clase
        Persona.contador_persona += 1
        self.id = Persona.contador_persona
        self.nombre = nombre
        self.apellido = apellido


    def mostrar_info(self):
        print(f'Persona numero {self.id}, Nombre: {self.nombre} {self.apellido}')

    # def total_personas(self):
    #     print(f'Se han creado {Persona.contador_persona} personas')

persona_1 = Persona('Misael', 'Martinez')
persona_1.mostrar_info()
persona_2 = Persona('Diana','Te amo mi amor')
persona_2.mostrar_info()

print(Persona.contador_persona) #Imprime el valor de contador persona



