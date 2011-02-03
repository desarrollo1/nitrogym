# -*- coding: utf-8 -*-
if __name__ == '__main__':
    from db import *
    
from base import *

#from nitrogim.model.persona import persona_persona
from nitrogym.model import Persona, Item, Lista, RelacionPersona
from nitrogym.session import item_session


class PersonaSession(BaseSession):
    """
        Session con la base de datos para Persona.
    """
    model = Persona

    
    def guardar(self, **kw):
        """ Guarda un item """

        obj = self.instancia(**kw)
        kw_pop(obj, 'nombre', **kw)
        kw_pop(obj, 'apellido', **kw)
        kw_pop(obj, 'nacido', **kw)
        kw_pop(obj, 'genero', **kw) or \
        kw_pop(obj, '_genero', **kw)
        kw_pop(obj, 'email', **kw)
        kw_pop(obj, 'foto', **kw)
        kw_pop(obj, 'foto_id', **kw)
        
        kw_pop(obj, 'ocupacion', **kw) or \
        kw_pop(obj, 'ocupacion_id', **kw)
        kw_pop(obj, 'pais', **kw) or \
        kw_pop(obj, 'pais_id', **kw)
        
        kw_pop(obj, 'tipodoc', **kw) or \
        kw_pop(obj, 'tipodoc_id', **kw)
        kw_pop(obj, 'nrodoc', **kw)
        
        kw_pop(obj, 'tipos', **kw)
        return self.add(obj)
    
    def tiene_relacion(self, id1, id2):
        pass
    
    def relacionar(self, **kw):
        """ Relaciona dos personas """
        obj = RelacionPersona()
        kw_pop(obj, 'persona1', **kw) or \
        kw_pop(obj, 'persona1_id', **kw)
        kw_pop(obj, 'relacion1', **kw) or \
        kw_pop(obj, 'relacion1_id', **kw)
        kw_pop(obj, 'persona2', **kw) or \
        kw_pop(obj, 'persona2_id', **kw)
        kw_pop(obj, 'relacion2', **kw) or \
        kw_pop(obj, 'relacion2_id', **kw)
        return self.add(obj)
    

    
    def paginar_relaciones(self, persona_id, relacion1_nombre=None, relacion2_nombre=None):
        """ Busca relaciones de una persona """
        
        
        
        # resultados de la derecha...
        q1 = DBSession.query(Persona, Item). \
        join((RelacionPersona, RelacionPersona.persona2_id==Persona.id), \
        (Item, Item.id==RelacionPersona.relacion2_id)).filter(RelacionPersona.persona1_id==persona_id)
        if relacion1_nombre:
            q1 = q1.filter(Item.nombre==relacion1_nombre)

        q2 = DBSession.query(Persona, Item). \
        join((RelacionPersona, RelacionPersona.persona1_id==Persona.id), \
        (Item, Item.id==RelacionPersona.relacion1_id)).filter(RelacionPersona.persona2_id==persona_id)
        if relacion1_nombre:
            q2 = q2.filter(Item.nombre==relacion1_nombre)

        x = q1.union(q2).order_by(asc(Item.nombre))
        return x


    
persona_session = PersonaSession()



if __name__ == '__main__':
    pass

    