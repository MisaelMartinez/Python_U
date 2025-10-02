print('**MUNDO PC**')
from T1_Computadora import  Computadora
from T1_Raton import Raton
from T1_Orden import Orden
from T1_Teclado import Teclado
from T1_Monitores import  Monitor

teclado_1 = Teclado('HP','USB')
raton_1 = Raton('HP','C')
monitor_1 = Monitor('Hisense','USB')
compu_1 = Computadora('HP',monitor_1,teclado_1,raton_1)
#print(compu_1)

teclado_2 = Teclado('Acer','USB')
raton_2 =  Raton('Acer','C')
monitor_2 = Monitor('Xiaomi','USB')
compu_2 = Computadora('Acer',monitor_2,teclado_2,raton_2)

l_compu = [compu_1,compu_2]

ticket = Orden(l_compu)
print(ticket)