# -*- coding: utf-8 -*-
from base import *
from util import *


class Lista(DeclarativeBase):
    """ Se refirere a una lista de algo ej: profesion """
    
    __tablename__ = 'lista'
    id = Column(Integer, primary_key=True)
    nombre = Column(Unicode(50), nullable=False, unique=True)
    descripcion = Column(Unicode(50))


class Item(DeclarativeBase):
    """ Items de una lista ej: arquitecto, estudiante, ama de casa, etc """
    
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    _nombre = Column('nombre', Unicode(50), nullable=False)
    descripcion = Column(Unicode(50))
    lista_id = Column(Integer, ForeignKey(Lista.id))
    lista = relation(Lista, backref=backref('items', order_by=_nombre))
    
    def _set_nombre(self, nombre):
        self._nombre = nombre #.upper()
    def _get_nombre(self):
        return capitalizar(self._nombre)
    nombre = synonym('_nombre', descriptor=property(_get_nombre, 
                                                    _set_nombre))
    
    
    