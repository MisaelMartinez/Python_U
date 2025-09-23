"""
La funcion range es una funcion incorporada que genera una secuencia de numeros.
Es utilizada para iterar sobre ciclos for.

#Inicio (Opcional)
# Fin
#Incremento

range(inicio, fin, incremento)
"""
#Usar range para imprimir del 0 al 4
for i in range(5): #Fin 5-1
    print(i, end = ',')
print('\n')
#Usar range para imprimir del 0 al 9 con incremento de 2
for i in range(0,10,2): #Fin 10-1, salto de 2 en 2, desde 0.
    print(i, end = ',')

print('\n')
#Range del 20 al 30 con incremento de 2
for i in range(20, 31, 2):
    print(i, end=',')
