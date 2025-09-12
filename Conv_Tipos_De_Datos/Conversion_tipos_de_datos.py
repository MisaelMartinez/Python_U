"""La conversion de tipos de datos (casting) es una tecnica para manipular datos que estan
en el tipo requerido
Podemos hacer conversiones desde y hacia distintos tios de datos

* Convertir a entero: int()
* Convertior a flotante: float()
* Convertir a cadena: str()
* Convertir a booleano: bool()

"""

# Convertir de cadena a numero
num_cadena = '10'
print(type(num_cadena))
numero = int(num_cadena)
print(f'Es es un: {type(numero)}, el numero es {numero}')

#Covertir de cade a flotante
num_cadena = '3.14'
numero_f = float(num_cadena)
print(f'Es es un: {type(numero_f)}')

# Convertir numero a cadena
num_cadena = str(numero)
print(f'{num_cadena} es {type(num_cadena)}' )

#Convertir a booleano
numero_entero = ""
booleano = bool(numero_entero)
print(f'Este valor de {booleano}, es {type(booleano)}')
#Si es 0 devuelve False
#Si es diferente de 0 es true
#Si es una cadena vacia es falso.
#Si el valor es None, el el booleano es False

# EJEMPLO DE CONCATENACION O SUMA DE VALORES.

n1_cadena = '10'
print(f'Numero 1 en cadena: {n1_cadena}')
n2_cadena = '20'
print(f'Numero 2 en cadena: {n2_cadena}')
r_cadena = n1_cadena + n2_cadena

r_num = int(n1_cadena) + int(n2_cadena)
print(f'La concatenacion es: {r_cadena} y la suma de datos convertidos a int es: {r_num}')























