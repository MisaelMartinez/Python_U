"""
Son bloques de codigo para realizar una tera en particular

def nombre(x1,x2):
    r = x1 +x2
    return r
"""
#import Modulo_fsuma   #Forma mas larga. Modulo_fsuma.suma()
from Modulo_fsuma import suma, resta

n = suma(2,3)
print(f'El resultado de la suma es: {n}')

#Se requiere todos los argumentos
n = resta(x2=5,x1=1) #Llamada a la funcion por argumentos, puede ser en desorden.
print(f' El resultado de 1 -5 es: {n}')

#Que pasa cuando quiero solamente ingresar un valor y no los demas?
def datos(nombre, apellido= ' ', edad = 0): #Estos valores son por default en caso de que no ingresen nada al llamar a la funcion
    print(f'Nombre: {nombre}, Apellido: {apellido},Edad: {edad}')

datos('Misael') #Solo NOMBRE es obligatorio, apellido y edad no por sus valores por default.

#Funcion para retornar una TUPLA
def nombre_mayus(nombre, apellido = ' '):
    print(f'\n\nEsta funcion retorna una tupla con los datos en mayuscuala')
    return nombre.upper(), apellido.upper()

tuppla = nombre_mayus('Misael','martinez')
print(tuppla)


#UNPACKING DE TUPLA
a1, a2 = tuppla
print(f'Ya no es una tupla, ya son STR Nombre:{a1}, Apellido: {a2}')








