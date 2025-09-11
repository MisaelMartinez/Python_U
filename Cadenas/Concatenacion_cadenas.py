"""
La concatenacion de cadenas es una operacion que permite combinar dos cadenas o mas para
formar una nueva cadena

En python existen varias formas.
- Uso del operador +: Simplemente tenemos que poner el operador + entre dos cademas

Ej. cadena_conc "Hola" + "mundo"

-Funcion join: Esta funcion nos permite unir tantas cadenas como necesitemos. Solo necesitamos pasar cada cadena
a concatenar sepraras por coma y entre parentesis.

" ".join(["cadena1","cadena2","cadena3"])
"""

#Concatenacion.
cadena1 = "Hola" + "Mundo"
print(cadena1)

cadena2 = "Te"
cadena3 = "Amo"
cadena4 = "Diana"
cadena5 = "a".join([cadena2," ",cadena3," ",cadena4])
print(cadena5) #Imprime Tea aAmoa aDiana. debemos solo de poner "" en lugar de "a"









