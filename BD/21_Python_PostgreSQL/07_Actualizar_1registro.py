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
            sentencia = 'UPDATE persona SET nombre = %s,apellido = %s, email = %s WHERE id_persona = %s'
            valores = ('Misael','Campistrano','Gas@gmai.com','10')

            cursor.execute(sentencia, valores) #Excecute PARA 1 VALOR
            registros_act = cursor.rowcount  # Contador de registros insertados
            print(f'Registros act: {registros_act}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

# Cada que ejecute esto se agregara un nuevo registro.