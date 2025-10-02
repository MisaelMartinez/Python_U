class Orden:
    i_ordenes = 0

    def __init__(self,l_compu):
        Orden.i_ordenes +=1
        self.id_ordenes = Orden.i_ordenes
        self.l_compu = l_compu

    def __str__(self):
        str_compu = ''
        for computadora in self.l_compu:
            str_compu += '\n'+ computadora.__str__()
        return (f'Orden: {self.id_ordenes}'
                f'Computadoras: {str_compu}')

    def agregar_computadoras(self,computadoras):
        self.l_compu.append(computadoras)


