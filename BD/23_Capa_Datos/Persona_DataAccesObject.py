#PROGRAMA PRINCIPAL.
from Conexion import Conexion
from Persona import Persona
from logger_base import log

class PersonaDAO:
    """
    DAO (Data Access Object)
    CRUD (Create - Read - Update - Delete)
    """
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona =%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores=(persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Se inserto correctamente: {persona}')
                return cursor.rowcount

    @classmethod
    def Actualizar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores  = (persona.nombre,persona.apellido,persona.email,persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Se actualizo correctamente: {persona}')
                return cursor.rowcount

    @classmethod
    def Eliminar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR,valores)
                log.debug(f'Registro {persona.id_persona} eliminado')
                return cursor.rowcount


if __name__ == '__main__':
    # #INSERTAR PERSONA
    # persona_1 = Persona(nombre = 'Misael',apellido = 'Novio de Diana',email ='DianaYMisael@gmail.com')
    # personas_insertadas = PersonaDAO.insertar(persona_1)
    # log.debug(f'Personas_insertadas: {personas_insertadas}')

    # # ACTUALIZAR PERSONA
    # persona_1 = Persona(12,'Aurora','Campistrano','AC@gmail.com')
    # persona_act = PersonaDAO.Actualizar(persona_1)
    # log.error(f'Personas actualizadas: {persona_act}')

    #ELIMINAR PERSONA
    persona_1 = Persona(id_persona=12)
    personas_eliminadas = PersonaDAO.Eliminar(persona_1)
    log.error(f'Personas_eliminadas: {personas_eliminadas}')
    

    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)







