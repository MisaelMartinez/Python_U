import mysql.connector

personar_db = mysql.connector.connect(
    host='localhost', #127.0.0.1
    user='root',
    password = 'Gaspariin',
    database = 'persona'
)

cursor = personar_db.cursor()
sentencia = 'UPDATE persona SET nombre=%s,apellido =%s, edad = %s WHERE id_persona = %s'
valores = ('Diana','Te amo',3,5)
cursor.execute(sentencia,valores)

personar_db.commit()
personar_db.close()