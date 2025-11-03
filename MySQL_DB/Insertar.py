import mysql.connector

personar_db = mysql.connector.connect(
    host='localhost', #127.0.0.1
    user='root',
    password = 'Gaspariin',
    database = 'persona'
)

cursor = personar_db.cursor()
sentencia = 'INSERT INTO persona(nombre,apellido,edad) VALUES(%s,%s,%s)'
valores = ('Misael','Novio de Diana', 346)
cursor.execute(sentencia,valores)

personar_db.commit() #Guardar cambios

personar_db.close()



