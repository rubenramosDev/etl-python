#Importamos la libreria para mostrar mensajes en la consola
import logging
import datetime
import subprocess # Nos permite manipular comandos de la terminal

#Hacemos la configuración básica
logging.basicConfig(level=logging.INFO)
#Obtenemos una referencia al logger
logger = logging.getLogger(__name__)


####################################################################
#              Función principal paso a paso                       #
####################################################################
def main():
    _extract()
    _transform()
    _load()
    logger.info('..::Proceso ETL finalizado::..')

####################################################################
#   Función pencargada de invocar el proceso de extracción         #
####################################################################
def _extract():
    logger.info('..::Iniciando el proceso de extracción::..')
    subprocess.run(['python', 'main.py'], cwd='./extract')   
    subprocess.run(['move', r'extract\*.csv', r'transform'], shell=True)
        
####################################################################
#   Función encargada de invocar el proceso de transformación         #
####################################################################
def _transform():
    logger.info('..::Iniciando el proceso de transformación::..')
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    dirty_data_filename = 'VentasProductosUnion_{datetime}.csv'.format(
         datetime=now)
    #Corremos un subproceso para ejecutar el segundo programa en la carpeta /transform
    subprocess.run(
            ['python', 'main.py', dirty_data_filename], cwd='./transform')
    subprocess.run(['del', dirty_data_filename],
                       shell=True, cwd='./transform')
    subprocess.run(['move', r'transform\*.csv', r'load'], shell=True)
    
####################################################################
#   Función encargada de invocar el proceso de carga         #
####################################################################
def _load():
    logger.info('..::Iniciando el proceso de carga::..')
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    
    for news_site_uid in news_sites_uids:
        clean_data_filename = 'clean_{}_{datetime}_articles.csv'.format(
             news_site_uid, datetime=now)
        #Corremos un subproceso para ejecutar el tercer programa en la carpeta /extract
        subprocess.run(
            ['python', 'main.py', clean_data_filename], cwd='./load')
        #Eliminar el archivo csv limpio
        subprocess.run(['del', clean_data_filename], shell=True, cwd='./load')
       
if __name__ == '__main__':
    main()