"""
Ejemplo de manejo de excepcion cuando un numero se divide sobre 0.
"""
try:
    1/0 #Resultado es infinito.
except Exception as e:
    print(f'Ocurrio un error: {e}')



