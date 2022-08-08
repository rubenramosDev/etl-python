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

def _load():
    logger.info('..::Iniciando el proceso de carga::..')

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

  