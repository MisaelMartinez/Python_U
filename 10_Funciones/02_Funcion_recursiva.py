"""
Se tiene que llamar a si misma
Cada vez que se mande llamar debemos que acercarnos a un caso base.
"""

def f_recursiva(numero):
    if numero==1:#Caso base
        print(numero)
    else: #Caso recursivo
        print(numero) #Se imprime primero el 10
        f_recursiva(numero-1)
        #print(numero) #Se imprime primero el 1.


f_recursiva(10)



