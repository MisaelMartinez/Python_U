"""
Crear un sistema de majeor de empleados de una empresa, aplicando la POO
La empresa desea saber el total de empleados asi como el total de empleados un departamento en particular

Se debe de crear la clase de Empleado y la clase de Empresa en archivos por separado, asi como la creacion de objetos en un
archivo por separado

"""
class Empleado:

    i_empleado = 0

    def __init__(self,nombre,departamento):
        Empleado.i_empleado += 1
        self.id = Empleado.i_empleado
        self.nombre = nombre
        self.departamento = departamento

    @classmethod
    def obtener_total_empleados(cls):
        print(f'El total de empleados es: {cls.i_empleado}')
        return cls.i_empleado

    #
    # @property
    # def nombre(self):
    #     return self.nombre
    # @nombre.setter
    # def nombre(self,nombre):
    #     self.nombre = nombre
    #
    # @property
    # def departamento(self):
    #     return self.departamento
    # @departamento.setter
    # def departamento(self,departamento):
    #     self.departamento = departamento
















