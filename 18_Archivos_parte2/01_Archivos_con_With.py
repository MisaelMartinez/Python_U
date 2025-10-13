#De manera automatica abre y cierra el archivo sin necesidad del bloque try except
#Metodo __enter__ sonde se abre el archivo
#Metodo __exit__ para salir o cerrar el archivo
#Estos dos metodos son los que utiliza with

# with open('Prueba.txt','r',encoding = 'utf8') as archivo:
#     print(archivo.read())

#Parte dos con clase propia y metodos propios de __exit__ y __enter__
from Class_Manejo_Archivos import ManejoArchivos
with ManejoArchivos('Prueba.txt') as archivo:
    print(archivo.read())







