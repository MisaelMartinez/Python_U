from logger_base import log
#import psycopg2 as db
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    #Un pool de conexiones necesita un minimo y un maximo de conexiones a utilizar.
    _MIN_CON = 1
    _MAX_COM = 5 #No ser tan grande. depende de las necesidades del proyecto
    _pool = None
    # _cursor = None
    # _conexion = None
    #Quitamos cursor y conexion porque se hara su clase respectiva

    @classmethod
    def obtenerPool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_COM,
                                                      host=cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Creacion del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool: {e}')
                sys.exit() #Ya no hay vuelta atras si hay un error.
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn() #getconn regresa un objeto de conexion hacia la BD
        log.debug(f'Conexion obtendia del pool: {conexion}')
        return conexion

        #Este metodo se simplificara.
        # if cls._conexion is None: #Si no se ha creado...
        #     try:
        #         cls._conexion = db.connect(host = cls._HOST,
        #                                    user = cls._USERNAME,
        #                                    password = cls._PASSWORD,
        #                                    port = cls._DB_PORT,
        #                                    database = cls._DATABASE)
        #         log.debug(f'Conexion exitosa: {cls._conexion}')
        #         return cls._conexion
        #     except Exception as e:
        #         log.debug(f'Ocurrio un error: {e}')
        #         sys.exit() #TERMINA EL PROGRAMA EN CASO DE ERROR.
        # else:
        #     return cls._conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion) #Colocar el objeto conexion a su lugar, en el pool de conexiones.
        log.debug(f'Regresamos la conexion al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls): #Ya para cerrar el pool de conexiones
        cls.obtenerPool().closeall() #Ya, fin del pool.

if __name__ == '__main__': #Prueba de Conexion y cursor
    #Prueba de este programa
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1) #Liberamos el pool de la conexion 1
    conexion2 = Conexion.obtenerConexion() #Utiliza la misma direccion de memoria que la conexion1 porque esa ya se cerro
    #Si generamos 6 conexiones ya no funciona por el limite que pusimos



    # Conexion.obtenerConexion()
    # Conexion.obtenerCursor()