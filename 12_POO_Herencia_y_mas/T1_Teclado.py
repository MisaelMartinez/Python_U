from T1_Dispositivo_Entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    i_teclado = 0
    def __init__(self,marca,tipo_entrada):
        Teclado.i_teclado +=1
        self.id_teclado = Teclado.i_teclado
        super().__init__(marca,tipo_entrada)

    def __str__(self):
        return f'Id: {self.id_teclado}, Marca: {self.marca}, T_Entrada: {self.tipo_entrada}'


if __name__ == '__main__':
    teclado_1 = Teclado('ACER','USB')
    print(teclado_1)