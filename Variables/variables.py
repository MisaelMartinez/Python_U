"""
Variables en python.
Siempre es necesario asignarle un valor a las varibales.

Las cadenas pueden ser con comilla simple o doble.

REGLAS Y BUENAS PRACTICAS DE VARIABLES
*Pueden tener mayusculas o minisculas, numero o guion bajo
*No puede comenzar con digitos
*No se pueden utiizar palabras reservadas (keyword)
*Es sensible a mayusculas y minusculas.

CONVENCIONES Y BUENAS PRACTICAS
-Snake Case: Unicamente palabras en minusculas separadas con guion bajo.
            juan_misael
"""

#Declaracion de variables.
edad = 26
altura = 1.68
pais = "Mexico"

#Utilizaremos las variables antes declaradas

print(edad)
print(altura)
print(pais)

edad += 3

print("La edad nueva es: ", edad) #Por cada coma, el compilador agrega un espacio.
print("La edad nueva es:", edad) #Texto corregido.

#Modificar el valor de una variable.
edad -=3
print("\nLa edad regreso a su valor original:", edad)

"""
El tipado en python no es fuerte, las varibles almacenan cualquier tipo de dato
en cualquier momento.
"""

#Reglas estrictas
#Sensible a mayusculas y minusculas
juan = 26
Juan = 28

print(juan) #Imprime 26
print(Juan) #Imprime 28

#Snake case
juan_misael = "Yo"