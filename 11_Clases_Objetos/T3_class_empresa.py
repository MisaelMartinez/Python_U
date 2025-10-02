from T3_Sistema_Empleados import Empleado

class Empresa:

    def __init__(self,nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar_empleado(self,nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self.empleados.append(empleado)

    def obtener_n_empleados_depto(self,departamento):
        contador_empleador_por_depto = 0
        for i in self.empleados:
            if i.departamento == departamento:
                contador_empleador_por_depto += 1
        return contador_empleador_por_depto
    def total_empleados(self):
        return len(self.empleados)

#CREANDO OBJETOS
