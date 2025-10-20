import psycopg2  # modulo para conectar python con postgres

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'  # Nombre de la base de datos de Postegres.
)

print(conexion)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'  # %s corresponde a los valores

            valores = (('Carlos', 'Lara', 'Clara@gmail.com'),
                       ('Diana','Villegas','fgh@gmail.com'),
                       ('Te', 'Amo','Diana@gmail.com'),
                       )#Este se convertira en una tupla de tuplas

            cursor.executemany(sentencia, valores) #Excecutemany para varias tuplas.
            # conexion.commit()#Guardamos los cambios, por uso de with no es necesaria esta linea
            registros_insertados = cursor.rowcount  # Contador de registros insertados
            print(f'Registros insertados: {registros_insertados}')
            #El commit se realiza un guardado automaticamente.
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

# Cada que ejecute esto se agregara un nuevo registro.
