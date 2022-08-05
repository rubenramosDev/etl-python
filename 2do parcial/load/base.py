from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Declaramos el motor de la BD a usar
engine = create_engine('sqlite:///exame_bd_2parcial.db')
#Creamos la sesión
Session = sessionmaker(bind=engine)
#Creamos el objeto Base
Base = declarative_base()