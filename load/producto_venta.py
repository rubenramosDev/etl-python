#Importamos las clses que necesitamos de sqlalchemy
from sqlalchemy import Column, String, Integer
#Importamos al objeto Base
from base import Base

#Declaramos la clase Artículo que hereda a Base
class ProductoVenta(Base):
    __tablename__ = 'productoventa'
    #Definicion de columnass
    venta = Column(Integer, primary_key = True)
    productoLlave = Column(Integer)
    nombre = Column(String)
    cantidad = Column(Integer)
    total = Column(String)
    fecha = Column(String)
    tipoPago = Column(String)
    ganancia = Column(String)
    rating = Column(Integer)
    valoracion = Column(String)
    descripcion = Column(String)
    precioVenta = Column(String)
    precioCompra = Column(String)
    proveedor = Column(String)
    comentario = Column(String)
    
    
    def __init__(self,      venta,
                            productoLlave,
                            nombre,
                            cantidad,
                            total,
                            fecha,
                            tipoPago,
                            ganancia,
                            rating,
                            valoracion,
                            descripcion,
                            precioVenta,
                            precioCompra,
                            proveedor,
                            comentario
                            
                            ):
        self.venta = venta
        self.productoLlave = productoLlave
        self.nombre = nombre
        self.cantidad = cantidad
        self.total = total
        self.fecha = fecha
        self.tipoPago = tipoPago
        self.ganancia =ganancia
        self.rating = rating
        self.valoracion = valoracion
        self.descripcion = descripcion
        self.precioVenta = precioVenta
        self.precioCompra = precioCompra
        self.proveedor = proveedor
        self.comentario = comentario
        
    
    