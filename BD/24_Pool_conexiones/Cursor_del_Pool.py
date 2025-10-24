from logger_base import log
from Conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self): #realizar conexion
        log.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_exp, valor_exp, detalle_exp):
        log.debug(f'Se ejecuta metodo __exit__')
        if valor_exp:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, se hace rollback: {valor_exp}.{tipo_exp},{detalle_exp}')
        else:
            self._conexion.commit()
            log.debug(f'Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        print(f'Estamos dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())







