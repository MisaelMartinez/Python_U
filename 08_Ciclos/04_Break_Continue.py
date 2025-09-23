"""
Funcion de Break y Continue
"""
#Ejemplo de break
for i in range(1,10):
    if i%2 ==0:#Numero par
        print(i)
        break #Romper el ciclo inmediatamente.

#Ejemplo con continue
for i in range(1,10):
    if i%2 == 1: #Numero impar
        continue #Continua con la siguiente operacion
        print('No se imprime nada por el \'continue\'')
    print(f'Es numero  par {i}')


