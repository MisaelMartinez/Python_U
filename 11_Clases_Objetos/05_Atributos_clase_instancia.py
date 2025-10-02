class Persona:

    atributo_clase = 0

    def __init__(self,atr_instancia):
        self.atr_instancia = atr_instancia

if __name__ == '__main__':
    print(f'Atributos de CLASE')
    print(f'Atributo de Clase: {Persona.atributo_clase}')

    #Modificar el atributo de clase
    Persona.atributo_clase = 10
    print(f'Atributo de clase: {Persona.atributo_clase}')

    #Creamos objetos de persona 1
    p1 = Persona(15)
    print(f'Atributo de Clase desde P1: {p1.atr_instancia}')
    print(f'Atributo de Clase desde P1: {p1.atributo_clase}')





