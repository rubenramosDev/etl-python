import argparse
from ast import parse
from asyncio.log import logger
import logging
import pandas as pd
import datetime
from functools import reduce  

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Deficnion de la fucnion main
def main(filename):

    # Leemos nuestro archivo cvs
    encuentas = pd.read_csv(filename, encoding='utf-8')
    encuentas=_quitar_columnas_autogeneradas(encuentas)
    _save_data_to_csv(encuentas,filename)
    return encuentas
    
def _quitar_columnas_autogeneradas(df):
    #clean_filename = 'clean_{}'.format(filename)
    #logger.info('Guardando los datos limpios en el archivo: {}'.format(clean_filename))
    #df.to_csv(clean_filename)
    df= df.drop(['Unnamed: 0.1'], axis=1)
    df= df.drop(['Unnamed: 0'], axis=1)
    print("____________________________________")
    df.set_index('id_formulario',inplace=True)
    return df

def _save_data_to_csv(df,filename):
    clean_filename = 'clean_final_{}'.format(filename)
    logger.info('Guardando el dataset en el archivo final...: {}'.format(clean_filename))
    df.to_csv(clean_filename)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='El archivo que deseas cargar hacia la BD',
                        type=str)
    args = parser.parse_args()
    df=main(args.filename)
    print(df)
