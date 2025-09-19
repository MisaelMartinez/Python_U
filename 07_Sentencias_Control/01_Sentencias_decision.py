"""
Las sentencias de desicion nos permiten controlar el flujo de control de nuestro programa
La funcion utilizada es (if)
"""

x = int(input('¿Cuantos años tienes? ').strip())
if x>= 18: #Es mayor a 18
    print(f'Eres mayor de edad. Tienes {x} años') #Imprimir mensaje
elif x>= 12: #Sino es mayor de 18, entonces es mayor o igual a 12
    print(f'Ya eres todo un chavo. Tienes {x} años')#Imprime mensaje
else: #Es menor de 12 años
    print('Eres un bebé aún porque tienes menos de 12 años')














