from Excepcion_Numeros_iguales import NumeroIdenticosException

r = None
try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a ==b:
        raise NumeroIdenticosException('Numeros Identicos') #Para lanzar una excepcion
    r = a/b
except ZeroDivisionError as e: #Se utilizara esta clase para errores numericos
    print(f'Ocurrio un error ZeroDivisionError: {e}')
except TypeError as e: #Se utiliza en caso de str/int
    print(f'Ocurrio un error TypeError: {e}')
except ValueError as e: #Para cuando ingremos un caracter en lugar de un numero para a o b
    print(f'Ocurrio un error ValueError: {e}')
except Exception as e: #Siempre utilizar la excepcion general al final.
    print(f'Ocurrio un error Exception: {e}')

#OPCIONAL
else:
    print('Eres la mera pistola porque no hubo errores.')
finally: #Siempre se ejecutara con o sin excepcion
    print('\nEjecucion de FINALLY')

print(f'El resultado de: {r}')
print('Continuamos...')


