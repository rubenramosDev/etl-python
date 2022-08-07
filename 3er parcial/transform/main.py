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
    
    _trnsPregunta1_7(df)
    _save_data_to_csv(df, file_name)
    
    return df


## * TRANSFORMACIONES
def _trnsPregunta1_7(df):
    
    # P3: Verificar Fecha valida +18
    df["pregunta_3"] = df["pregunta_3"].apply(lambda fh: valiFecha(fh))

    # EDAD: Calculado a partir de la fecha
    df.insert(5, 'edad', df['pregunta_3'].map(lambda fh: calcEdad(fh)))
    
    # Sexo con nombre o caracter F o M
    df["pregunta_4"] = df["pregunta_4"].apply(lambda sexo: "M" if sexo == "Masculino" else "F")
    
    return df

def valiFecha(fecha):
    """
    Valida el formato de la fecha, si es incorrecto retorna con prefijo NV_
    """
    try:
        edad = calcEdad(fecha)
        if type(edad) is int and edad >18:
            return fecha
        else:
            return "NV_{}".format(fecha)
            
    except TypeError:
        return "NV_{}".format(fecha)

def calcEdad(fecha):
    """
    Calcula la edad en base a fecha actual y de nacimiento
    """
    try:
        nw_fecha = datetime.strptime(fecha, '%Y-%m-%d')
        today = datetime.now()
        
        edad = today.year - nw_fecha.year
        if nw_fecha.month < today.month:
            return edad
        elif nw_fecha.month == today.month:
            if nw_fecha.day < today.day:
                return edad
            else:
                return edad -1
        else:
            return edad -1
        
    except TypeError:
        return 0
    
    

def _read_data(file_name):
    logger.info('Leyendo el archivo {}'.format(file_name))
    #Leemos el archvo csv y lo devolvemos el data frame
    return pd.read_csv(file_name,  encoding = 'utf-8')

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