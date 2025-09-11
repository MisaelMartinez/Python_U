"""
Una cadena o string es un tipo de dato que se utiliza para almacenar una secuencia de caracteres
Se deben encerrar entre comillas simples o dobles
Pueden ser letras, numeros, simbolos o espacios.

Los caracteres de una cadena estan indexados de una manera secuencial
Por lo tanto, podemos acceder a cada caracter indicando el indice del caracter que deseamos recuperar
Basicamente, como funciona una arreglo

          0  1  2  3 ...
HOLA -->  H  O  L  A

Inmutabilidad de una cadena
Una vez que se crea una cadena, los caracteres dentro de ella no pueden ser modificados.
Si deseamos modificar una cadena, entonces tenemos que crear una nueva cadena
En el ejemplo de este archivo, cadena apunta al objeto "Hola mundo"
pero al cambiar su valor solamente se crea otro objeto y apunto ahora a "Adios"

"""
# Ejemplo

cadena = "Hola mundo"

#Esto en memoria se almacena cadena, y apunta al objeto str que almacena "Hola mundo"
#La variable cadena esta apuntado a este objeto

cadena = "Adios"
cadena2 = "Python es genial"
cadena3 = """Este es un ejemplo
de multiples lineas
en un cadena
"""
#En este punto ya se crearon 3 objetos, cada variable apunta a sus objetos correspondientes
print(cadena)
print(cadena2)
print(cadena3)

#Recuperar solo X caracter
cadena = "Hola mundo"
print(cadena[1]) #Solamente imprime el segundo caracter. "o"
print(cadena[3]) #Solamente imprime el cuarto caracter. "a"

#Inmutabilidad de cadenas

#cadena[0] = "L"
print(cadena) #Error porque las cadenas no se pueden modificar.










