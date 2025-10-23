#Las transacciones en SQL son cuando todos lo Query se ejecutan correctamente y se haven commit
#Cuando una tiene un error se realiza un rollback y se deshacen todos los cambios.

#Con with se hace el commit o rollback de manera automatica
import psycopg2  as bd #modulo para conectar python con postgres

conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'  # Nombre de la base de datos de Postegres.
)

try:
    conexion.autocommit = False #Lo desactivamos para ver el lugar del commit o rollback
    #Si es TRUE puedo guardar errores en la base de datos, no es lo deseable.

    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
    valores = ('Maria','Esparaza', 'me@gmai.com')
    cursor.execute(sentencia, valores)
    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Juan','Mart','gasper@live.com','2')
    cursor.execute(sentencia,valores)
    conexion.commit() #Hacemos el commit de manera manual


except Exception as e:
    conexion.rollback() #Rollback de manera manual
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close()

# Cada que ejecute esto se agregara un nuevo reg


















