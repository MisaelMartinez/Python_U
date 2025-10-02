"""
Se tendra que crear una clase se operaciones aritmeticas la cual tendra encapsulameinto
y funciones get y set
"""

class Aritmentica:

    def __init__(self,x1=None,x2=None):
        self._x1 = x1
        self._x2 = x2

    def suma(self):
        r = self._x1 + self._x2
        return r

    def resta(self):
        r = self._x1 - self._x2
        return r

    @property
    def x1(self):
        return self._x1

    @x1.setter
    def x1(self, x1):
        self._x1 = x1

    @property
    def x2(self):
        return self._x2

    @x2.setter
    def x2(self,x2):
        self._x2 = x2

n = Aritmentica(3,5)
print(n.suma())
print(f'{n.resta()}') #Se puede hacer tambien una suma con n.suma()
print(n.x2)
print(n.x1)
n.x1 = 1111
n.x2 = 2929
print(f'hola {n.suma()}')


