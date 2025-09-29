"""
En python los argumentos variables permiten que una funcon acepte un numero arbitrario de elementos.
Existen 2 tipos:

*Agumentos posicionales *args: Permiten pasar multiples argumentos posicionales a una funcion
                              recibiendolos como una tupla dentro de la funcion
Agumetos con palabra clave **kwargs: Recibe los argumentos en forma de diccionario.
"""
#ARGUMENTOS VARIABLES *ARGS
def super_heroes(super_heroe, nombre, *args):
    print(f'Superheroe: {super_heroe} - {nombre} ')
    for i in args:
        print(f'\tSuperpoder: {i}')

super_heroes('Spiderman','Peter Parker', 'Instinto aracnido', 'Telaraña')
#Podemos asignarle a args desde 0 hasta x valores

#ARGUMENTOS VARIBLES **KWARGS

def superH_kwargs(nombre, *args, **kwargs):
    print(f'SuperHeroe: {nombre} - {args} - Mas informacion {kwargs}')

superH_kwargs('Spiderman','Instinto aracnido','Telaraña',edad = 17, empresa = 'Marvel')

#ejemplo con arg varibales

print('\n\n\n')
def sum_arg(*args):
    total = 0
    for i in args:
        total += i
    return total

print(f'Resultado: {sum_arg(1,2,3,4,5)}')

#EJEMPLO KWARGS
print('\n\n\n')

def persona_detalles(**kwargs):
    print('Valores recibidos: ')
    for clave, valor in kwargs.items():
        print(f'{clave} : {valor}')

persona_detalles(edad=17, nombre = 'Misael', Novia = True)





