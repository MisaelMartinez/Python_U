from T1_Dispositivo_Entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    i_raton = 0

    def __init__(self,marca,tipo_entrada):
        Raton.i_raton += 1
        self.id_raton = Raton.i_raton
        # self.marca = marca
        # self.tipo_entrada = tipo_entrada
        super().__init__(marca,tipo_entrada)

    def __str__(self):
        return f'Id: {self.id_raton}, Marca: {self.marca}, T_Entrada: {self.tipo_entrada}'



if __name__ == "__main__":
    raton_1 = Raton('HP', 'C')
    print(raton_1)

