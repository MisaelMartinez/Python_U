#Un patron de diseño es como un plano que podemos utilizar para resolver problemas de nuestra app.
from Conexion import Conexion
from Cliente import Cliente

class clienteDAO:

    _SELECCIONAR = 'SELECT * FROM cliente'
    _INSERTAR = 'INSERT INTO cliente(nombre,apellido,membresia) VALUES (%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id_cliente = %s'
    _ELIMINAR = 'DELETE FROM cliente WHERE id_cliente = %s'

    @classmethod
    def sel(cls):
        cnx = None
        try:
            cnx = Conexion.obtenerConexion()
            cursor = cnx.cursor()
            cursor.execute(cls._SELECCIONAR)
            reg =  cursor.fetchall()
            clientes= []
            for i in reg:
                cliente = Cliente(i[0], i[1],i[2],i[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes_ {e}')
        finally:
            if cnx is not None:
                cursor.close()
                Conexion.liberar_conexion(cnx)

    @classmethod
    def ins(cls,cliente):
        cnx = None
        try:
            cnx = Conexion.obtenerConexion()
            cursor = cnx.cursor()
            valores=(cliente.nombre,cliente.apellido,cliente.membresia)
            cursor.execute(cls._INSERTAR,valores)
            cnx.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar: {e}')
        finally:
            if cnx is not None:
                cursor.close()
                Conexion.liberar_conexion(cnx)

    @classmethod
    def act(cls,cliente):
        cnx = None
        try:
            cnx = Conexion.obtenerConexion()
            cursor = cnx.cursor()
            valores = (cliente.nombre,cliente.apellido,cliente.membresia,cliente.id)
            cursor.execute(cls._ACTUALIZAR,valores)
            cnx.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar: {e}')
        finally:
            if cnx is not None:
                cursor.close()
                Conexion.liberar_conexion(cnx)

    @classmethod
    def eliminar(cls,cliente):
        cnx = None
        try:
            cnx = Conexion.obtenerConexion()
            cursor = cnx.cursor()
            valores = (cliente.id,)
            cursor.execute(cls._ELIMINAR,valores)
            cnx.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar: {e}')
        finally:
            if cnx is not None:
                cursor.close()
                Conexion.liberar_conexion(cnx)

if __name__ == '__main__':
    # #INSERTAR nuevo cliente
    # cliente_T = Cliente(nombre='Misael',apellido= 'Diana',membresia=401)
    # cliente_insert = clienteDAO().act(cliente_T)
    # print(f'Se inserto correctamente el cliente: {cliente_insert}')

    # #ACTUALIZAR cliente
    # cliente_A = Cliente(nombre ='TE AMO DIANA',apellido= 'MUCHO',membresia=500,id=2)
    # clientes_act = clienteDAO.ins(cliente_A)
    # print(f'Registros actualizados: {clientes_act}')

    #ELIMINAR.
    cliente_E = Cliente(id = 2)
    clientes_eliminados = clienteDAO.eliminar(cliente_E)
    print(f'Se eliminaron {clientes_eliminados} clientes.')

    #SELECCIONAR
    clientes = clienteDAO.sel()
    # print(clientes)#Muestra direccion en memoria del objeto.
    for i in clientes:
        print(i)

