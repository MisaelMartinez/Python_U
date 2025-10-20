import psycopg2 #modulo para conectar python con postgres

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db' #Nombre de la base de datos de Postegres.
)

print(conexion)

#Cursor: nos va a permitir ejecutar sentencias en SQL.
cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall() #Recuera todos los registros de la sentencia que se ha ejecutado
print(registros)
#Los datos vienen en una tupla cada 1. es decir, una lista de tuplas.

cursor.close()
conexion.close()

#Esta es la forma basica para poder conectarnos a la base de datos.







