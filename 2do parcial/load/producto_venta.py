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
    token_pr_nombre_cant = Column(Integer)
    token_pr_nombre = Column(String)
    token_pr_comentarios_cant = Column(Integer)
    token_pr_comentarios = Column(String)
    
    
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
                            comentario,
                            token_pr_nombre_cant,
                            token_pr_nombre,
                            token_pr_comentarios_cant,
                            token_pr_comentarios
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
        self.token_pr_nombre_cant = token_pr_nombre_cant
        self.token_pr_nombre = token_pr_nombre
        self.token_pr_comentarios_cant = token_pr_comentarios_cant
        self.token_pr_comentarios = token_pr_comentarios
        
    
