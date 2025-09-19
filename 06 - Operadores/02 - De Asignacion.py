#Operadores de asignacion
"""
El signo = es utilizado para asignar un valor a una variable.
Pero existe la asignacion multiple como se muestra a continuacion
Tambien se cuenta con la asignacion encadenada, el mimso valor puede ser asignado a multiples variables.
"""

x = 80
print(x)

#Asigacion multiple
x1,x2,x3 = 10, 'Hola Mundo', 97.7
print(f'Se realizo la asignacion multiple: x1= {x1}, x2 = {x2}, x3 = {x3}')

#Asignacion encadenada
x1 = x2 = x3 = 10
print(f'Se realizo la asignacion ecadenada: x1 = {x1}, x2 = {x2}, x3 ={x3}')



#Intercambio de valores de una variable, sin utilizar temporales
x,y = 5,10
print(f'El valor de x es {x} y el valor de y es {y}')
x,y = y,x #El valor se intercambia
print(f'El valor de x es {x} y el valor de y es {y}. Sus valores han sido intercambiados')


nombre, apellido = input('Ingresa tu nombre y apellido separado por coma: ').split(',')
# Con .split separamos el apellido del nombre debido a la coma. Se ve en el ()




