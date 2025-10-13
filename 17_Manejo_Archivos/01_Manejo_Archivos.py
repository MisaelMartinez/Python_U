#La funcion Open abre o crea el archivo. y la w dentro de la funcion Open es para poder editar

#Modos de OPEN
#r, read. Por default
#a, Append. Anexar mas informacion o crea el archivo en caso de que no exista
#w, Write. Escribir informacion y crear si no ecite
#x, Create. Crea.
#w+, para escribir y leer
#r+, leer pero tambien para escribir

#t, para texto
#b, binario

#Esta funcion Archivo = Open(...) usualmente se encuentra dentro de un bloque try except.
#

#Si agregamos un acento el contenido mostrara un ?
#Para solucionar esto tendremos que agregar en open(..., encoding = 'utf8')
try:
    archivo = open('Prueba.txt','w',encoding = 'utf8') #
    archivo.write('Agregamos información al archivo')
    archivo.write('\nAdios'
    )
except Exception as e:
    print(e)
finally:
    archivo.close()
    #archivo.write('Ya no se puede escribir porque ya cerramos el archivo')
    print('Archivo Cerrado')









