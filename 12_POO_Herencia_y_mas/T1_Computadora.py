from T1_Teclado import Teclado
from T1_Monitores import Monitor
from T1_Raton import Raton

class Computadora:
    i_compu = 0
    def __init__(self,nombre, monitor,teclado,raton):
        Computadora.i_compu += 1
        self.id_compu = Computadora.i_compu
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f'''Nombre de computadora: {self.nombre}
        ID: {self.id_compu}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}'''

#MAIN
if __name__ == '__main__':
    teclado_1 = Teclado('HP','USB')
    raton_1 = Raton('HP','C')
    monitor_1 = Monitor('Hisense','USB')
    compu_1 = Computadora('HP',monitor_1,teclado_1,raton_1)
    print(compu_1)
