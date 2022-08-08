from datetime import datetime
from nltk.corpus import stopwords
import nltk
import numpy as np
import pandas as pd
from urllib.parse import urlparse
import hashlib
import argparse
import logging
logging.basicConfig(level=logging.INFO)

# Obtenemos una referencia al logger
logger = logging.getLogger(__name__)


def main(file_name):
    logger.info('Iniciando Proceso de limpieza de Datos...')
    df = _read_data(file_name)

    _trnsPregunta1_7(df)
    _trnsPregunta8_15(df)
    _trnsPregunta23_30(df)
    _save_data_to_csv(df, file_name)

    return df


# * TRANSFORMACIONES
def _trnsPregunta1_7(df):

    # P3: Verificar Fecha valida +18
    df["pregunta_3"] = df["pregunta_3"].apply(lambda fh: valiFecha(fh))

    # EDAD: Calculado a partir de la fecha
    df.insert(5, 'edad', df['pregunta_3'].map(lambda fh: calcEdad(fh)))

    # Sexo con nombre o caracter F o M
    df["pregunta_4"] = df["pregunta_4"].apply(
        lambda sexo: "M" if sexo == "Masculino" else "F")

    return df


def _trnsPregunta8_15(df):

    # Pregunta 8 con cambio a:
    #   Compartido
    df["pregunta_8"] = df["pregunta_8"].apply(
        lambda opcion: "Compartido" if opcion == "Era Compartido" else (
            "Si" if opcion == "Si" else "No"))

    # Pregunta 10 con cambios a:
    #   50 a 100
    #   101 a 300
    #   301 a 500
    #   501 o más
    df["pregunta_10"] = df["pregunta_10"].apply(
        lambda opcion: "50 a 100" if opcion == "50 a 100 pesos" else (
            "101 a 300" if opcion == "101 a 300 pesos" else (
                       "301 a 500" if opcion == "301 a 500 pesos" else
                       "501 o más")))

    # Pregunta 13 con cambios a frases:
    #   Correo electrónico
    #   Plataformas como classroom, teams, etc.
    df["pregunta_13"] = df["pregunta_13"].apply(
        lambda opcion: "Correo electrónico,Plataformas como classroom, teams, etc.,Grupos de WhatsApp,"
        if opcion == "Vía correo electrónico,Plataformas como classroom, teams, etc,Grupos de WhatsApp,"

        else ("Correo electrónico,Plataformas como classroom, teams, etc.,"
              if opcion == "Vía correo electrónico,Plataformas como classroom, teams, etc,"

              else ("Plataformas como classroom, teams, etc.,Grupos de WhatsApp,"
                    if opcion == "Plataformas como classroom, teams, etc,Grupos de WhatsApp,"

                    else ("Plataformas como classroom, teams, etc.,"
                          if opcion == "Plataformas como classroom, teams, etc,"

                          else ("Correo electrónico,"
                                if opcion == "Vía correo electrónico,"

                                else "Ninguno"

                                )))))

    # Pregunta 15 con cambios a frases:
    #   Elaboración de trabajos, proyectos y casos
    df["pregunta_15"] = df["pregunta_15"].apply(
        lambda opcion: "Examen oral,Examen en línea,Prueba escrita abierta,Elaboración de trabajos, proyectos y casos,"
        if opcion == "Examen oral,Examen en línea,Prueba escrita abierta,Elaboración de trabajos, proyectos, casos,"

        else ("Examen en línea,Prueba escrita abierta,Elaboración de trabajos, proyectos y casos,"
              if opcion == "Examen en línea,Prueba escrita abierta,Elaboración de trabajos, proyectos, casos,"

              else ("Examen oral,Prueba escrita abierta,Elaboración de trabajos, proyectos y casos,"
                    if opcion == "Examen oral,Prueba escrita abierta,Elaboración de trabajos, proyectos, casos,"

                    else ("Examen oral,Examen en línea,Elaboración de trabajos, proyectos y casos,"
                          if opcion == "Examen oral,Examen en línea,Elaboración de trabajos, proyectos, casos,"

                          else ("Examen en línea,Elaboración de trabajos, proyectos y casos,"
                                if opcion == "Examen en línea,Elaboración de trabajos, proyectos, casos,"

                                else ("Examen en línea,Prueba escrita abierta,"
                                      if opcion == "Examen en línea,Prueba escrita abierta,"

                                      else ("Examen oral,Examen en línea,"
                                            if opcion == "Examen oral,Examen en línea,"

                                            else "Examen en línea,"
                                            )))))))

    return df


def _trnsPregunta23_30(df):
    # Pregunta 23 con cambios a:
    #   Mas que si hubiera ido a clase a Más que si hubiera ido a clase
    df["pregunta_23"] = df["pregunta_23"].apply(
        lambda opcion: "50 a 100"
        if opcion == ""
        else ("Más que si hubiera ido a clase")
    )

    # Duda pregunta 28
    # Duda pregunta 30

    return df


def valiFecha(fecha):
    """
    Valida el formato de la fecha, si es incorrecto retorna con prefijo NV_
    """
    try:
        edad = calcEdad(fecha)
        if type(edad) is int and edad > 18:
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
                return edad - 1
        else:
            return edad - 1

    except TypeError:
        return 0


def _read_data(file_name):
    logger.info('Leyendo el archivo {}'.format(file_name))
    # Leemos el archvo csv y lo devolvemos el data frame
    return pd.read_csv(file_name,  encoding='utf-8')


def _save_data_to_csv(df, filename):
    clean_filename = 'clean_{}'.format(filename)
    logger.info(
        'Guardando los datos limpios en el archivo: {}'.format(clean_filename))
    df.to_csv(clean_filename)


# Inicio de la aplicación #
if __name__ == '__main__':
    # Creamos un nuevo parser de argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name',
                        help='La ruta al dataset sucio',
                        type=str)
    # Parseamos los argumentos.
    args = parser.parse_args()
    df = main(args.file_name)

    # Mostramos el Data Frame
    print("-------------- DataFrame Completo --------------")
    print(df)
