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
import pymysql
import pandas as pd
from sqlalchemy import create_engine

from config import connection

from functools import reduce   
#Obtenemos una referencia al logger
logger = logging.getLogger(__name__)


#Definimos la Función principal
def main(_carrera):
    logger.info('Iniciando Proceso de Extracción...')

    #Invocamos a la función para leer los datos.
    df = _read_data_sql(_carrera,connection)

    #Invocamos a la función que guarda los datos del DataFrame en un archivo csv
   # _save_data_to_csv(df)
    
    #Devolvemos el dataFrame resultante
    return df

####################################################################
#              Función para leer los datos del Data Set            #
####################################################################
def _read_data_sql(carrera_name,connection):
    #logger.info('Leyendo el archivo {}'.format(file_name))
    sql=('select * from  formulario where pregunta_5=?',carrera_name)
    
    df = pd.read_sql_query(sql, con=connection)

    #Leemos el archvo csv y lo devolvemos el data frame
    return df


####################################################################
#   Función  unir en un solo dataframe los archivos csv #
####################################################################

    
##################################################################################
# Función que guarda los datos del DataFrame en un archivo csv #
##################################################################################

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

  