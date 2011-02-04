# -*- coding: utf-8 -*-


from hashlib import sha1
from datetime import datetime
from nitrogym.model import DeclarativeBase, metadata, DBSession
from sqlalchemy.exc import IntegrityError#.params
import transaction
from tg import request
from sqlalchemy import *
from sqlalchemy import sql
from sqlalchemy.orm import aliased
import sys



#from sqlalchemy.orm import query








def kw_pop(instance, name, **kw):
    if kw.has_key(name):
        setattr(instance, name, kw.pop(name))
        return True
    return False

#def kw_pop(object, name, **kw):
#    if kw.has_key(name):
#        object = kw.pop(name)
#        return True
#    return False


    
def like(value):
    if not '%' in value:
        return '%'+value+'%'
    return value

class BaseSession(object):
    """ Base para las sesiones """


    model = None
    debug = False

    def base(self):
        """ No usar <base> en esta clase por que se puede modificar en el futuro """
        return DBSession.query(self.model)
    
    def __call__(self, inst=None, **kw):
        if kw:
            return self.guardar(inst, **kw)
        
    def por_id(self, id):
        if id:
            return DBSession.query(self.model).get(id)
        
    def add(self, inst):
        DBSession.add(inst)
        return inst
        
    def instancia(self, **kw):
        id = kw.pop('id', None)
        if id:
            obj = self.por_id(id)
        else:
            #obj = kw.pop(self.model.__name__.lower(), self.model()) # si ya existe una instancia...
            obj = self.model() #kw.pop(self.model.__name__.lower(), self.model()) # si ya existe una instancia...
        return obj
    
    
#    def guardar(self, **kw):
#        """ Agrega una instancia a la sesion """
#        
#        obj = self.instancia(**kw)
#        self._guardar_(obj, **kw)
#        
#        if self.debug:
#            kw.pop('id', None)
#            if kw:
#                raise KeyError(kw)
#        return self.add(obj)
        
    def _guardar(self, inst, **kw):
        """ Extension de self.guardar """
        pass
        
    def guardar(self, inst=None, **kw):
        """ Esto es util por que relaciona los atributos del modelo con los del kwargs """
        if not inst:
            inst = self.instancia(**kw)
        for i in self.model.__mapper__.iterate_properties:
            kw_pop(inst, i.key, **kw )
        self._guardar(inst, **kw)
        return self.add(inst)
        

        
        
        