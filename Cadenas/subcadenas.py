"""
Una subacadena es una parte de una una cadena principal y hay varias maneras de extraer subcadenas
Podemos extraer subcadenas, buscarlas, reemplazarlas, etc.
Extraccion de cadenas (slicing): Es una segmentacion que permite indicar el indice de inicio y final
    (Sin incluir este ultimo caracter)

scad_1= cad_1[inicio:fin]}
"""
cad_1 = "0123456789"
scad_1 = cad_1[0:9]
print(cad_1)
print(scad_1)
#Imprime solo de 0 a 8 porque el caracter en la posicion se ignora. [0,9)

"""
Buscar subcadenas (find): El metodo find() devuelve el indice de la primera aparicion de la subcadena. 
Si no la encuentra, devuelve -1

Tiene que ser exactamente como los buscas, incluyendo mayusculas o minusculas.
"""
cad_f = "Ho, Hol, Hola"
posicion = cad_f.find("Hola")
print(f'Indice de donde empieza \"Hola\": {posicion}') #Imprime 9. recuerda que el conteo empieza en 0.

"""
Reemplazar subcadenas
El metodo replace() reemplaza una subcadena por otra dentro de una cadena principal
.replace("reemplazar", "Reemplazador")
"""

c_original = "Hola mundo"
c_nueva = c_original.replace('mundo', 'a todos mis perros')
print(c_nueva)

"""
Extraer subcadenas por sepado:
split(): Permite dividir una cadena en una lista de subcadenas basadas en un caracter separador.
"""

datos = "Juan, 30, Mexico"
lista = datos.split(',') #Separar cada dato cuando se encuentre una ,
#Si no se le asigna ningun caracter a split, por defecto es una espacio.
print(lista) #Una lista corresponde a []








