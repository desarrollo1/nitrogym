# -*- coding: utf-8 -*-
from base import *


class Blob(DeclarativeBase):
    """ Guarda datos binarios """
    
    #content_type="image/jpg")
    
    __tablename__ = 'blob'
    id = Column(Integer, primary_key=True)
    tipo = Column(Unicode(25)) # "image/jpg"
    nombre = Column(Unicode(50), nullable=False)
    descripcion = Column(Unicode(255))
    data = Column(LargeBinary)
    data2 = Column(LargeBinary) # miniatura...
    creado = Column(DateTime, default=datetime.now())
    modificado = Column(DateTime, default=datetime.now())
