"""
"""
from T3_class_empresa import Empresa
from T3_Sistema_Empleados import Empleado

print('SISTEMA DE EMPLEADOS')

#Crear una instancia de una empresa
empresa1 = Empresa('Global Mentoring')
#Contratar empleados
empresa1.contratar_empleado('Juan','RH')
empresa1.contratar_empleado('Diana','Marquetink')
empresa1.contratar_empleado('Te amo DIANA','RH')
empresa1.contratar_empleado('Misael', 'RH')

#Obtener el total de objetos tipo EMPLEADO
print(f'Total de empleados: {Empleado.obtener_total_empleados()}')

#Obtener el numero de empleados en el departamento RH
print(f'El numero de empleados en RH es: {empresa1.obtener_n_empleados_depto('RH')}')
print(f'El total de empleados de {empresa1.nombre} es: {empresa1.total_empleados()}')














