class Monitor:
    i_monitor = 0
    def __init__(self,marca, tamanio):
        Monitor.i_monitor +=1
        self.marca = marca
        self.tamanio = tamanio
        self.id_monitor = Monitor.i_monitor

    def __str__(self):
        return f'Id: {self.id_monitor}, Marca: {self.marca}, Tamaño: {self.tamanio}'

if __name__ == '__main__':
    monitor_1 = Monitor('Dell','14')
    print(monitor_1)
