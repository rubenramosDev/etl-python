#Importamos las clses que necesitamos de sqlalchemy
from tokenize import Double
from xmlrpc.client import DateTime
from sqlalchemy import Column, String, Integer
#Importamos al objeto Base
from base import Base

#Declaramos la clase Artículo que hereda a Base
class ProductoVenta(Base):
    __tablename__ = 'producto_venta'
    #Definicion de columnass
    venta = Column(Integer, primary_key = True)
    idProducto = Column(Integer)
    cantidad = Column(Integer)
    total = Column(Double)
    fecha = Column(DateTime)
    tipoPago = Column(String)
    rating = Column(Integer)
    nombre = Column(String)
    comentario = Column(String)
    descripcion = Column(String)
    precio = Column(Double)
    proveedor = Column(String)
    
    def __init__(self,venta,
                            idProducto,
                            cantidad,
                            total,
                            fecha,
                            tipoPago,
                            rating,
                            nombre,
                            comentario,
                            descripcion,
                            precio,
                            proveedor):
        self.venta = venta
        self.idProducto = idProducto
        self.cantidad = cantidad
        self.total = total
        self.fecha = fecha
        self.tipoPago = tipoPago
        self.rating = rating
        self.nombre = nombre
        self.comentario = comentario
        self.descripcion = descripcion
        self.precio = precio
        self.proveedor = proveedor
    
    