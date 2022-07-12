import argparse
import logging
logging.basicConfig(level=logging.INFO)
import hashlib
from urllib.parse import urlparse
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from datetime import datetime

#Obtenemos una referencia al logger
logger = logging.getLogger(__name__)

def main(file_name):
    logger.info('Iniciando Proceso de limpieza de Datos...')
    df = _read_data(file_name)
    
    #df = _limpieza_datos(df)
    #df = _obtener_tokens(df)
    #df = _obtener_tokens_comentarios(df)
    df = _agregar_fila_recomendado(df)
    df = _calcular_ganancia(df)
    df.set_index('venta',inplace=True)
    _save_data_to_csv(df, file_name)
    
    return df

def _read_data(file_name):
    logger.info('Leyendo el archivo {}'.format(file_name))
    #Leemos el archvo csv y lo devolvemos el data frame
    return pd.read_csv(file_name,  encoding = 'utf-8')

def _limpieza_datos():

    #Limpieza de Cantidad
    missingTitlesMask = df['cantidad'].isna()
    missing_tittles = (df[missingTitlesMask]['total']/df[missingTitlesMask]['precio venta'])
    df.loc[missingTitlesMask, 'cantidad'] = missing_tittles.iloc[:len(missing_tittles)]

    #Limpieza de Fecha
    missingTitlesMask = df['fecha'].isna()
    today = (datetime.today().strftime('%d/%m/%Y'))
    missing_tittles = (df[missingTitlesMask]['fecha'])
    missing_tittles = df.fillna(value=today)
    df.loc[missingTitlesMask, 'fecha'] = missing_tittles.iloc[:len(missing_tittles)]

    #Limpieza de Tipo de Pago
    missingTitlesMask = df['tipo pago'].isna()
    missing_tittles = (df[missingTitlesMask]['tipo pago'])
    missing_tittles = df.fillna(value='Sin especificar')
    df.loc[missingTitlesMask, 'tipo pago'] = missing_tittles.iloc[:len(missing_tittles)]

    #Limpieza de Comentarios
    missingTitlesMask = df['comentarios'].isna()
    missing_tittles = (df[missingTitlesMask]['comentarios'])
    missing_tittles = df.fillna(value='Sin comentarios')
    df.loc[missingTitlesMask, 'comentarios'] = missing_tittles.iloc[:len(missing_tittles)]

    #Limpieza de Descripcion
    missingTitlesMask = df['descripcion'].isna()
    missing_tittles = (df[missingTitlesMask]['descripcion'])
    missing_tittles = df.fillna(value='Sin informacion')
    df.loc[missingTitlesMask, 'descripcion'] = missing_tittles.iloc[:len(missing_tittles)]

    #Limpieza de Proveedores
    missingTitlesMask = df['proveedor'].isna()
    missing_tittles = (df[missingTitlesMask]['proveedor'])
    missing_tittles = df.fillna(value='Anonimo')
    df.loc[missingTitlesMask, 'proveedor'] = missing_tittles.iloc[:len(missing_tittles)]

    return df

def _obtener_tokens():
    return 0
def _obtener_tokens_comentarios():
    return 0
def _agregar_fila_recomendado(df):
    conditionlist = [
    (df['rating'] <= 5) ,
    (df['rating'] <= 7),
    (df['rating'] > 7)]
    choicelist = ['Malo', 'Regular', 'Bueno']
    df['valoracion'] = np.select(conditionlist, choicelist, default='Not Specified')
    return df

####################################################################
#              Función para calcular la ganancia de ventas            #
####################################################################
def _calcular_ganancia(df):
    col_precio_venta = df['precioVenta']
    col_precio_compra = df['precioCompra']
    
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