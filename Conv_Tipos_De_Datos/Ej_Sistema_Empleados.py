"""
Crea un programa para solicitar la informacion de un empleado,

Nombre del empleado (str)
Edad (Int)
Salario (Float)
El jefe (Bool)
"""

name = input('Introduce tu nombre: ')
age = int(input('Introduce tu edad: '))
salario = float(input('Cual es tu salario actual? '))
es_jefe = input('Eres jefe de departamento (Si/No)? ')

#Convertir a bool es_Jefe
es_jefe = es_jefe.lower() == "si"

print(f'\n{name} tienes {age} años y ganas {salario:.2f} pesos mensuales.')

if es_jefe == True:
    print('Y eres jefe de depto')
else:
    print('Y eres un pobre perro jajaja')



