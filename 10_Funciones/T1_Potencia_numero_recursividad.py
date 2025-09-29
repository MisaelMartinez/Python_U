"""
Calcular la potencia de un numero usando funciones recursivas.
a^b
a=2
b=7
2*2*2*2*2*2*2 = 128
"""

a = int(input('Ingresa un numero: ').strip())
b = int(input('Ingresa la potencia a la que quieres elevar tu numero: '))

def potencia(x,y):
    if y ==0:
        print(f'{x} elevado a la potencia {y} es 1')
        return 1
    else:
        r = x*potencia(x,y-1)
        print(f'{x} Elevado a la {y} es: {r}')
        return r

pot = potencia(a,b)
print(f'El resultado de la potencia final es: {pot}')




