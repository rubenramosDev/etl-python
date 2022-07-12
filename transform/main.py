import argparse
import logging
logging.basicConfig(level=logging.INFO)
import hashlib
from urllib.parse import urlparse
import pandas as pd
import nltk
from nltk.corpus import stopwords

#Obtenemos una referencia al logger
logger = logging.getLogger(__name__)

def main(file_name):
    logger.info('Iniciando Proceso de limpieza de Datos...')
    df = _read_data(file_name)
    
    df = _limpieza_datos(df)
    df = _obtener_tokens(df)
    df = _obtener_tokens_comentarios(df)
    df = _agregar_fila_recomendado(df)
    df = _calcular_ganancia(df)
    _save_data_to_csv(df, file_name)
    return df

def _read_data(file_name):
    logger.info('Leyendo el archivo {}'.format(file_name))
    #Leemos el archvo csv y lo devolvemos el data frame
    return pd.read_csv(file_name,  encoding = 'utf-8')

def _limpieza_datos():
    return 0
def _obtener_tokens():
    return 0
def _obtener_tokens_comentarios():
    return 0
def _agregar_fila_recomendado():
    return 0

####################################################################
#              Función para calcular la ganancia de ventas            #
####################################################################
def _calcular_ganancia(df):
    col_precio_venta = df['precio venta']
    col_precio_compra = df['precio compra']
    
    df['ganancia'] = col_precio_venta - col_precio_compra
    return df

def _save_data_to_csv(df, filename):
    clean_filename = 'clean_{}'.format(filename)
    logger.info('Guardando los datos limpios en el archivo: {}'.format(clean_filename))
    df.to_csv(clean_filename)

# Inicio de la aplicación #
if __name__ == '__main__':
    #Creamos un nuevo parser de argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name',
                        help='La ruta al dataset sucio',
                        type=str)
    #Parseamos los argumentos.
    args = parser.parse_args()
    df = main(args.file_name)

    #Mostramos el Data Frame
    print("-------------- DataFrame Completo --------------")
    print(df)