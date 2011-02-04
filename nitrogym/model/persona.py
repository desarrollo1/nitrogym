# -*- coding: utf-8 -*-
from base import *
from util import *
from nitrogym.model import Item


persona_tipo = Table('persona_tipo', metadata,
    Column('persona_id', Integer, ForeignKey('persona.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('tipo_id', Integer, ForeignKey('item.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)


class Ocupacion(DeclarativeBase):
    __tablename__ = 'ocupacion'
    
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'))
    inicio = Column(Time)
    fin = Column(Time)
    item = relation('Item') #, primaryjoin=id==Item.id)
    
    nombre = property(lambda self : self.item.nombre)
    
    

class Persona(DeclarativeBase):
    __tablename__ = 'persona'
    
    
    id = Column(Integer, primary_key=True)
    tipodoc_id = Column(Integer, ForeignKey('item.id'))
    
    nrodoc = Column(Unicode(25))
    _nombre = Column('nombre', Unicode(50), nullable=False)
    _apellido = Column('apellido', Unicode(50))
    
    nacido = Column(Date)
    _genero = Column('genero', Unicode(1))
    _email = Column('email', Unicode(100), unique=True)
    creado = Column(DateTime, default=datetime.now())
    modificado = Column(DateTime, default=datetime.now())
    foto_id = Column(Integer, ForeignKey('blob.id'))
    ocupacion_id = Column(Integer, ForeignKey('ocupacion.id'))
    #horario = Column(Time)
    #pais_id = Column(Integer, ForeignKey('paises.id'))
    
    
    __table_args__ = (UniqueConstraint('tipodoc_id', 'nrodoc'), {}) 
    
    # Relaciones:
    tipodoc = relation('Item', primaryjoin=tipodoc_id==Item.id)
    tipos = relation('Item', secondary=persona_tipo)
    ocupacion = relation('Ocupacion') #, primaryjoin=ocupacion_id==Item.id)
    
    # Sininimos:
    email = synonym('_email')
    
    def _set_nombre(self, nombre):
        self._nombre = nombre #.upper()
    def _get_nombre(self):
        return capitalizar(self._nombre)
    nombre = synonym('_nombre', descriptor=property(_get_nombre, 
                                                    _set_nombre))
    
    def _set_apellido(self, apellido):
        self._apellido = apellido #.upper()
    def _get_apellido(self):
        return capitalizar(self._apellido)
    apellido = synonym('_apellido', descriptor=property(_get_apellido, 
                                                        _set_apellido))    

    def _set_genero(self, genero):
        """ Setea el sexo o genero de la persona """
        
        g = genero.lower()
        if g in ['m', 'masculino', 'h', 'hombre']:
            self._genero = u'm'
        if g in ['f', 'femenino', 'm', 'mujer']:
            self._genero = u'f'
    
    def _get_genero(self):
        """ Retorna el sexo o genero de la persona """
        
        g = str(self._genero).lower()
        if g in 'm':
            return u'Hombre'
        if g in 'f':
            return u'Mujer'
        return u''
    genero = synonym('_genero', descriptor=property(_get_genero,
                                                    _set_genero))
    
    # util con el widget...    
    tipos_id = property(lambda self : [i.id for i in self.tipos]) # retorna lista de ids del tipo de persona
    #ocupacion_nombre = property(lambda self : self.ocupacion.nombre)
    
    #pais_nombre = property(lambda self: self.pais.nombre) # retorna nombre del pais de la persona.
    
    
    
class RelacionPersona(DeclarativeBase):
    __tablename__ = 'persona_persona'

    id = Column(Integer, primary_key=True)
    
    persona1_id = Column(Integer, ForeignKey('persona.id'))
    relacion1_id = Column(Integer, ForeignKey('item.id'))
    persona2_id = Column(Integer, ForeignKey('persona.id'))
    relacion2_id = Column(Integer, ForeignKey('item.id'))
    
    persona1 = relation('Persona', primaryjoin=persona1_id == Persona.id)
    persona2 = relation('Persona', primaryjoin=persona2_id == Persona.id)
    relacion1 = relation('Item', primaryjoin=relacion1_id == Item.id)
    relacion2 = relation('Item', primaryjoin=relacion2_id == Item.id)
    
    
    

    
    
    
    