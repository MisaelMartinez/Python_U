import mysql.connector

personar_db = mysql.connector.connect(
    host='localhost', #127.0.0.1
    user='root',
    password = 'Gaspariin',
    database = 'persona'
)

mi_cursor = personar_db.cursor()
mi_cursor.execute('SELECT * FROM persona')
r = mi_cursor.fetchall()
for persona in r:
    print(persona)

personar_db.close() #Siempre se debe cerrar.












