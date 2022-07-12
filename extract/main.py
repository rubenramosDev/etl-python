#Importamos la librería argparse para generar un CLI
import argparse
import datetime
#Importamos la librería loggig para mostrar mensajes al usuario
import logging
logging.basicConfig(level=logging.INFO)
#Importamos la librería hashlib para encriptación
import hashlib
#Importamos la librería urlparse para parsean la forma de las url's
from urllib.parse import urlparse
#Importamos la librería de pandas para análisi de datos
import pandas as pd
#Importamos la librería nltk para extraer tokens del texto
import nltk
from nltk.corpus import stopwords

from functools import reduce   
#Obtenemos una referencia al logger
logger = logging.getLogger(__name__)

#Definimos la Función principal
def main(filename_1,filename_2):
    logger.info('Iniciando Proceso de Extracción...')

    #Invocamos a la función para leer los datos.
    dfVentas = _read_data(filename_1)
    dfProductos = _read_data(filename_2)
    #Invocamos a la funcion para  unir los dos dataframes con un merge
    df = _join(dfVentas, dfProductos)

    #Invocamos a la función que guarda los datos del DataFrame en un archivo csv
    _save_data_to_csv(df)
    
    #Devolvemos el dataFrame resultante
    return df

####################################################################
#              Función para leer los datos del Data Set            #
####################################################################
def _read_data(file_name):
    logger.info('Leyendo el archivo {}'.format(file_name))
    #Leemos el archvo csv y lo devolvemos el data frame
    return pd.read_csv(file_name, encoding=("utf-8"))


####################################################################
#   Función  unir en un solo dataframe los archivos csv #
####################################################################
def _join(dfVentas, dfProductos):
    data_merge= reduce(lambda left, right:     # Merge three pandas DataFrames
                     pd.merge(left , right,
                              on = ["productoLlave"]),
                     [dfVentas, dfProductos])
    data_merge.set_index('venta',inplace=True)

    data_merge   
    return data_merge
 
    
##################################################################################
# Función que guarda los datos del DataFrame en un archivo csv #
##################################################################################
def _save_data_to_csv(df):
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = 'VentasProductosUnion_{fdatetime}.csv'.format(
         fdatetime=now)
    logger.info('Guardando el dataset: {}'.format(out_file_name))
    df.to_csv(out_file_name)

##################################################################################
# Inicio de la aplicación #
##################################################################################
if __name__ == '__main__':
    #Creamos un nuevo parser de argumentos
    parser = argparse.ArgumentParser()
  
    parser.add_argument('filename_1',
                         help='La ruta al dataset sucio',
                         type=str)
    parser.add_argument('filename_2',
                         help='La ruta al dataset sucio',
                         type=str)
    #Parseamos los argumentos.
    args = parser.parse_args()
    df = main(args.filename_1, args.filename_2)
    print("-------------------------------------")
    print(df)

  