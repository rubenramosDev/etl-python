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

from config import mysqlconnect

from functools import reduce   
#Obtenemos una referencia al logger
logger = logging.getLogger(__name__)
#Instanceamos la conexion a la BD
conn=mysqlconnect()

#Definimos la Función principal
def main(_carrera):
    logger.info('Iniciando Proceso de Extracción...')
    

    #Invocamos a la función para leer los datos.
    df = _read_data_sql(_carrera)

    #Invocamos a la función que guarda los datos del DataFrame en un archivo csv
    _save_data_to_csv(df)
    
    #Devolvemos el dataFrame resultante
    return df

####################################################################
#              Función para leer los datos del Data Set            #
####################################################################
def _read_data_sql(carrera_name):
    
    carrera =""
    if(carrera_name =="IDGS" or carrera_name =="idgs"):
        carrera="Ingenieria en Desarrollo y Gestion de Software"
        logger.info('Consultando en la BD sobre la carrera {}'.format(carrera))
    elif (carrera_name=="IRC" or carrera_name=="irc"):
         carrera="Ingeniería en Redes y Ciberseguridad"
         logger.info('Consultando en la BD sobre la carrera {}'.format(carrera))
    elif (carrera_name=="IEVND" or carrera_name=="IEVND"):
          carrera="Ingeniería en Entornos Virtuales y Negocios Digitales"
          logger.info('Consultando en la BD sobre la carrera {}'.format(carrera))
    
    if(carrera_name!="Todas"):
        cur = conn.cursor() 
        cur.execute("select * from  formulario where pregunta_5 = %s", [carrera] ) 
        output = cur.fetchall()      
        df = pd.DataFrame(output,columns=(i[0] for i in cur.description))
        conn.close() 
    else:
        logger.info('Consultando en la BD todas las carreras')
        cur = conn.cursor()
        cur.execute("select * from  formulario " ) 
        output = cur.fetchall()     
        df = pd.DataFrame(output,columns=(i[0] for i in cur.description))
        conn.close() 

    return df

def _save_data_to_csv(df):
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = 'EncuestasVendido_{fdatetime}.csv'.format(
         fdatetime=now)
    logger.info('Guardando el dataset: {}'.format(out_file_name))
    df.to_csv(out_file_name)
    
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

  