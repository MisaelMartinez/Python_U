"""
Los operadores logicos se utilizan para realizar operacion logicas con valores booleanos

* and
* or
* not
"""

a = False
b = True

r= a and b
print(r)
r = a or b
print(r)
r = not b
print(r)

#Operador or
print('***Sistema de prestamo de Libros')
distancia_permitida = 3 #km
credencial = input('Cuentas con credencial de estudiante? (Si/no)')
km_casa_biblio = int(input('Cuantos kilometros recorres de tu casa a la biblioteca? '))

x = ((credencial.strip().lower() == 'si' )or (km_casa_biblio <= distancia_permitida))
print(f' ¿Eres elegible para un libro? {x}')




