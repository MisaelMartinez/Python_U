#No se agregara el bloque de try except. por motivos de simplicidad.



#Podemos agregar la ruta del archivo....
archivo = open('C:\\Users\\gaspe\\Documents\\Python\\17_Manejo_Archivos\\Prueba.txt','r',encoding = 'utf8')

print(archivo.read(5)) #Lee solamente Agreg
print(archivo.read(3)) #Leemos amos
print(archivo.readline()) #Lee el restante de la linea 1
print(archivo.readline())#Lee la segunda linea
#print(archivo.read()) #Lee por completo el archivo