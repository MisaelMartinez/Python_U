# Recuperar solo 1 registro.

import psycopg2  # modulo para conectar python con postgres

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'  # Nombre de la base de datos de Postegres.
)

print(conexion)

# En prueba2 utilizaremos With

try:
    with conexion:

        # Cursor: nos va a permitir ejecutar sentencias en SQL.

        # cursor = conexion.cursor() La linea de abajo sustituye esta.
        with conexion.cursor() as cursor:
            sentencia = 'SELECT *FROM persona WHERE id_persona IN %s'  # In es para 1 o varios.
            entrada = input('Proporciona los id a buscar separado por comas: ')
            primary_keys = (tuple(entrada.split(',')),)  #esta es una tupla de tuplas. solo separa cuando hay ,

            cursor.execute(sentencia, primary_keys)  # ingresado como tupla
            registros = cursor.fetchall()  # Recuera todos los registros de la sentencia que se ha ejecutado
            # fetchone() solo regresa 1 registro.

            print(registros)
            # Los datos vienen en una tupla cada 1. es decir, una lista de tuplas.
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    # cursor.close() con el bloque with conex... nos ahorramos esta cerrada
    conexion.close()

# Esta es la forma basica para poder conectarnos a la base de datos.




