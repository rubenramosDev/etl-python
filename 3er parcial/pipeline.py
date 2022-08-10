import datetime
import logging
import subprocess
import argparse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(_carrera):
    _extract(_carrera)
    _transform()
    _load()
    logger.info('..::Proceso ETL finalizado::..')

def _extract(_carrera):
    logger.info('..::Iniciando el proceso de extracción::..')
    subprocess.run(['python', 'main.py', _carrera], cwd='./extract')
    subprocess.run(['move', r'extract\*.csv', r'transform'], shell=True)

def _transform():
   
    logger.info('..::Iniciando el proceso de transformación::..')
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    dirty_data_filename = 'EncuestasCovid_{datetime}.csv'.format(
         datetime=now)
    subprocess.run(
            ['python', 'main.py', dirty_data_filename], cwd='./transform')
    subprocess.run(['del', dirty_data_filename],
                       shell=True, cwd='./transform')
    subprocess.run(['move', r'transform\*.csv', r'load'], shell=True)
   
def _load():
    logger.info('..::Iniciando el proceso de carga::..')
    now = datetime.datetime.now().strftime('%Y_%m_%d')

    clean_data_filename = 'clean_EncuestasCovid_{datetime}.csv'.format(
             datetime=now)
    #Corremos un subproceso para ejecutar el tercer programa en la carpeta /extract
    subprocess.run(
            ['python', 'main.py', clean_data_filename], cwd='./load')
    #Eliminar el archivo csv limpio
    subprocess.run(['del', clean_data_filename], shell=True, cwd='./load')

##################################################################################
# Inicio de la aplicación #
##################################################################################
if __name__ == '__main__':    
    #Creamos un nuevo parser de argumentos
    parser = argparse.ArgumentParser()
  
    parser.add_argument('carrera_name',
                         help='La ruta al dataset sucio',
                        type=str)
    
    #Parseamos los argumentos.
    args = parser.parse_args()
    df = main(args.carrera_name)
    print("-------------------------------------")
    print(df)

  