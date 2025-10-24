#El majeor de logging es para mandar mensajes a la consola en caso de un error.
#El nivel mas basico de mensajes es el debug, este es utilizado en el desarrollo.
#El nivel siguiente es Info, warning, several, critical.
#El nivel Warning esta por defecto.

#Siempre que creemos un nuevo entorno virutal tenemos que instalar pip install psycopg2
import logging as log

#HANDLER es un recurso para enviar informacion del error.
log.basicConfig(level = log.DEBUG,
                format='%(asctime)s: %(levelname)s, [%(filename)s:%(lineno)s %(message)s]',
                datefmt = '%I:%M:%S %p',
                handlers = [
                    log.FileHandler('capa_datos.log'), #Crea un archivo con el mensaje que se arroja.
                    log.StreamHandler() #Consola que hemos utilizado hasta el momento

                ])


if __name__ == '__main__':

    log.basicConfig(level = log.DEBUG)#Queremos ver todo el detalle
    log.debug('Mensaje a nivel de bug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')
#Si en la linea 7 esta DEBUG, se ven todos los mensaje.
#Si tenemos INFO se ven en consola todos menos el de DEBUG.














