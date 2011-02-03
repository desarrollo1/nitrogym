# -*- coding: utf-8 -*-
from base import *
from util import *
from nitrogym.model import Lista


class Distrito(DeclarativeBase):
    """ Items de una lista ej: , etc """
    
    __tablename__ = 'distrito'
    id = Column(Integer, primary_key=True)
    _nombre = Column('nombre', Unicode(50), nullable=False)
    descripcion = Column(Unicode(50))
    lista_id = Column(Integer, ForeignKey(Lista.id))
    padre_id = Column(Integer, ForeignKey(id))
    
    lista = relation(Lista, backref=backref('distritos', order_by=_nombre))
    padre = relation('Distrito', remote_side=[id])
    
    def _set_nombre(self, nombre):
        self._nombre = nombre #.upper()
    def _get_nombre(self):
        return capitalizar(self._nombre)
    nombre = synonym('_nombre', descriptor=property(_get_nombre, 
                                                    _set_nombre))
    
    
class Localizacion(DeclarativeBase):
    __tablename__ = 'localizacion'
    
    id = Column(Integer, primary_key=True)
    lugar = Column(Unicode(50))
    pais_id = Column(Integer, ForeignKey(Distrito.id))
    dpto_id = Column(Integer, ForeignKey(Distrito.id))
    ciudad_id = Column(Integer, ForeignKey(Distrito.id))
    barrio_id = Column(Integer, ForeignKey(Distrito.id))
    calle1_id = Column(Integer, ForeignKey(Distrito.id))
    calle2_id = Column(Integer, ForeignKey(Distrito.id))
    
    #esquina = Column(Unicode(4))
    nro_casa = Column(Unicode(10))
    nro_depto = Column(Unicode(10))
    bloque = Column(Unicode(10))
    piso = Column(Unicode(10))
    codigo_postal = Column(Unicode(16))
    
    pais = relation(Distrito, primaryjoin=pais_id==Distrito.id)
    dpto = relation(Distrito, primaryjoin=dpto_id==Distrito.id)
    ciudad = relation(Distrito, primaryjoin=ciudad_id==Distrito.id)
    barrio = relation(Distrito, primaryjoin=barrio_id==Distrito.id)
    referencia = Column(Unicode(255))
    
    #contacto = relation(Contacto, secondary=locacion_contacto, backref='locaciones')
    calle1 = relation(Distrito, primaryjoin=calle1_id==Distrito.id)
    calle2 = relation(Distrito, primaryjoin=calle2_id==Distrito.id)
    
    
    # para los widgets...
    pais_nombre = property(lambda self : self.pais.nombre)
    dpto_nombre = property(lambda self : self.dpto.nombre)
    ciudad_nombre = property(lambda self : self.ciudad.nombre)
    barrio_nombre = property(lambda self : self.barrio.nombre)
    calle1_nombre = property(lambda self : self.calle1.nombre)
    calle2_nombre = property(lambda self : self.calle2.nombre)
    
    
    
    

    