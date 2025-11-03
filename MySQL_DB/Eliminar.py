import mysql.connector

personar_db = mysql.connector.connect(
    host='localhost', #127.0.0.1
    user='root',
    password = 'Gaspariin',
    database = 'persona'
)

cursror = personar_db.cursor()
sentencia = 'DELETE FROM persona WHERE id_persona = 4' #Eliminamos el 4 de nuestra base de datos.
cursror.execute(sentencia)

personar_db.commit()
personar_db.close()



