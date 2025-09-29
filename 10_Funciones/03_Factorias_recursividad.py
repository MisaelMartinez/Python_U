"""
Calcula el factorial de x, Siendo X un numero ingresado por el usuario
Utiliza recursividad
"""

x = int(input('Ingresa el numero que deseas para obtener su factorial: ').strip())
def factorial(x):
    if x == 0 or x ==1:
       # print(f'El factorial de {x} es igual a 1')
        return 1
    else:
        fact = x * factorial(x-1)
        #print(f'El factorial de {x} es {fact}')
        return fact


r = factorial(x)

print(f'El factorial de {x} es: {r}')