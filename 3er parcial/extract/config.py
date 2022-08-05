import pymysql
from sqlalchemy import create_engine

#Definimos una variable global para la configuracion

#Verificamos si existe la configuración y si no la cargamos
def connection():
    try:
        #Creamos conexion a la base de datos de manera local
        conn='mysql+pymysql://root:root@localhost:3306/encuentacovid'
        conexion = create_engine(conn)
        print("Se hizo la conexion a la base de datos encuestacovid")
        return conexion
    except:
        print("Ocurrió un problema al realizar la conexión a la Base de datos")
