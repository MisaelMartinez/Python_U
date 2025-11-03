from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'Gaspariin'
    HOST = 'localhost'
    DB_PORT = 3306
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: #Se crea el pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name= cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener el POOL: {e}')
        else:
            return cls.pool

    @classmethod
    def obtenerConexion(cls):
        return cls.obtener_pool().get_connection() #Nos regresa un objeto de conexion a la DB.

    @classmethod
    def liberar_conexion(cls,cnx):
        cnx.close()


if __name__ == '__main__':
    #Creacion del objeto pool
    #pool = Conexion.obtener_pool()#En comentario para las siguientes lineas y evitar erroes.
    #print(pool)
    #Obtener un objeto conexion
    cnx1 = Conexion.obtenerConexion()
    print(cnx1)

    ##cnx1.close() #Se regresa al pool de conexiones.
    Conexion.liberar_conexion(cnx1)





