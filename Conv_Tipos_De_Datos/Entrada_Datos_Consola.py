"""
Entrada de datos por consola

En python, la entrada de datos se realiza usando la funcion input()
Esta funcion pausa la ejecucion del programa y espera a que el usario introduzca algun texto desde el teclado

Una vez que el usuario presiona Enter, el texto introducido se devulve como una cadena str.
Si se ingresa un 10, es tipo de dato es str.

Caracteristicas de la funcion INPUT

*Interactividad: Permite a los usuarios de nuestros programas proporcionar valores dinamicos,
en lugar de utilizar valores en codigo duro o estaticos.
*Sencillez: La funcion input es muy facil de usar y solo neccesita, opcionalmete, indicar la cadena o mensaje a mostrar
al usuario, para que este sepa lo que se esta solicitando.
*Tipo de dato: Siempre devuelve una cadena y requiere una conversion de tipo de datos.
"""

#Entrada de datos por consola.

name = input('Introduce tu nombre: ') #Escribimos en la consola y damos Enter
print(f'Recibimos el valor de nombre: {name}')

#Pedir la edad. (Es necesario convertir a int.)
edad = int(input('Introduce tu edad: '))
print(f'Tu edad {name} es: {edad}')









