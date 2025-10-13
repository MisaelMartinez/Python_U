
archivo = open('C:\\Users\\gaspe\\Documents\\Python\\17_Manejo_Archivos\\Prueba.txt','r',encoding = 'utf8')

# #Iterar lineas
# for i in archivo:
#     print(i)


# #Leer lineas
# print(archivo.readlines()) #Lo imprime como una lista.

# #Acceedemos solo a una linea en especifico
# print(archivo.readlines()[0]) #El metodos es readlineS con s.

#Crear copia del archivo original.
#a, append, anexar informacion

archivo_2 = open('Copia.txt','a', encoding = 'utf8') #a agregara informacion cada que se corra el programa.
archivo_2.write(archivo.read())

archivo_2.close()
archivo.close()

print('Fin de la clase')





