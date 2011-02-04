# -*- coding: utf-8 -*-
if __name__ == '__main__':
    from db import *
    
from base import *
from nitrogym.model import Usuario, Grupo, Permiso


class UsuarioSession(BaseSession):
    """ Sesion con la db para usuarios """
    
    model = Usuario
    
#    def guardar(self, **kw):
#        """ Guarda un usuario """
#        
#        obj = self.instancia(**kw)
#        kw_pop(obj, 'login', **kw)
#        kw_pop(obj, 'password', **kw)
#        return self.add(obj)
        
        
class GrupoSession(BaseSession):
    """ Sesion con la bd para grupos """
    
    model = Grupo
    
#    def guardar(self, **kw):
#        """ Guarda un grupo """
#        
#        obj = self.instancia(**kw)
#        kw_pop(obj, 'nombre', **kw)
#        kw_pop(obj, 'decripcion', **kw)
#        return self.add(obj)

            
            
class PermisoSession(BaseSession):
    """ Sesion con la bd para permisos """
    
    model = Permiso
    
#    def guardar(self, **kw):
#        """ Guarda un grupo """
#        
#        obj = self.instancia(**kw)
#        kw_pop(obj, 'nombre', **kw)
#        kw_pop(obj, 'decripcion', **kw)
#        return self.add(obj)
    
#    def _guardar_(self, obj, **kw):
#        """ Guarda un permiso """
#        
#        kw_pop(obj, 'nombre', **kw)
#        kw_pop(obj, 'decripcion', **kw)
            
        
        
usuario_session = UsuarioSession()
grupo_session = GrupoSession()
permiso_session = PermisoSession()



