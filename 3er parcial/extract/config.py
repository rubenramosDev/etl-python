import pymysql
from sqlalchemy import create_engine

#Definimos una variable global para la configuracion

def mysqlconnect(): 
    #Creamos conexion a la base de datos de manera local
    try:
        conn = pymysql.connect( 
            host='localhost', 
            user='root',  
            password = "root", 
            db='encuestacovid', 
            ) 
        print("Se hizo la conexion a la base de datos encuestacovid")
        return conn
    except:        
        print("Ocurrió un problema al realizar la conexión a la Base de datos") 
    