import argparse
from ast import parse
from asyncio.log import logger
import logging
import pandas as pd
from producto_venta import ProductoVenta
from base import Base, engine, Session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Deficnion de la fucnion main
def main(filename):
    # Generamos el esquema de la BD
    Base.metadata.create_all(engine)
    # Iniciamos sesión
    session = Session()
    # Leemos nuestro archivo cvs
    productos = pd.read_csv(filename, encoding='utf-8')

    # Iteramos entre las filas de cvs mediante el metodo iterrows() y vamos carfando
    # los articulos a la base de datos.
    for index, row in productos.iterrows():
        logger.info(
            'Cargando el producto con el id: {} en la BD'.format(row['venta']))
        producto = ProductoVenta(row['venta'],
                                 row['idProducto'],
                                 row['cantidad'],
                                 row['total'],
                                 row['fecha'],
                                 row['tipoPago'],
                                 row['rating'],
                                 row['nombre'],
                                 row['comentario'],
                                 row['descripcion'],
                                 row['precio'],
                                 row['proveedor'])

        session.add(producto)
        session.commit()
        session.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='El archivo que deseas cargar hacia la BD',
                        type=str)
    args = parser.parse_args()
    main(args.filename)
