# -*- coding: utf-8 -*-
if __name__ == '__main__':
    from db import *
    
from base import *

#from nitrogim.model.persona import persona_persona
from nitrogym.model import Persona, Item, Lista, RelacionPersona, Ocupacion
from nitrogym.session import item_session


class PersonaSession(BaseSession):
    """
        Session con la base de datos para Persona.
    """
    model = Persona

    def _guardar(self, inst, **kw):
        
        # esto viene desde el formulario, una lista de ids...
        if kw.has_key('tipos_id'):
            inst.tipos = item_session.por_lista_id(kw.pop('tipos_id'))
        
        
#    def guardar(self, **kw):
#        """ Guarda un item """
#
#        obj = self.instancia(**kw)
#        kw_pop(obj, 'nombre', **kw)
#        kw_pop(obj, 'apellido', **kw)
#        kw_pop(obj, 'nacido', **kw)
#        kw_pop(obj, 'genero', **kw) or \
#        kw_pop(obj, '_genero', **kw)
#        kw_pop(obj, 'email', **kw)
#        kw_pop(obj, 'foto', **kw)
#        kw_pop(obj, 'foto_id', **kw)
#        
#        kw_pop(obj, 'ocupacion', **kw) or \
#        kw_pop(obj, 'ocupacion_id', **kw)
#        kw_pop(obj, 'pais', **kw) or \
#        kw_pop(obj, 'pais_id', **kw)
#        
#        kw_pop(obj, 'tipodoc', **kw) or \
#        kw_pop(obj, 'tipodoc_id', **kw)
#        kw_pop(obj, 'nrodoc', **kw)
#        
#        kw_pop(obj, 'tipos', **kw)
#        return self.add(obj)
    
    def tiene_relacion(self, id1, id2):
        pass
    
#    def relacionar(self, **kw):
#        """ Relaciona dos personas """
#        obj = RelacionPersona()
#        kw_pop(obj, 'persona1', **kw) or \
#        kw_pop(obj, 'persona1_id', **kw)
#        kw_pop(obj, 'relacion1', **kw) or \
#        kw_pop(obj, 'relacion1_id', **kw)
#        kw_pop(obj, 'persona2', **kw) or \
#        kw_pop(obj, 'persona2_id', **kw)
#        kw_pop(obj, 'relacion2', **kw) or \
#        kw_pop(obj, 'relacion2_id', **kw)
#        return self.add(obj)
    

    
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



class RelacionPersonaSession(BaseSession):
    model=RelacionPersona
    
    
class OcupacionSession(BaseSession):
    model=Ocupacion
    def _guardar(self, inst, **kw):
        if kw.has_key('nombre'):
            inst.item = item_session.actualizar(kw.pop('nombre'), u'persona_ocupacion')
            
    
persona_session = PersonaSession()
relacionpersona_session = RelacionPersonaSession()
ocupacion_session = OcupacionSession()

if __name__ == '__main__':
    pass
#    x = persona_session.por_id(1)
#    print type(x.horario)
#    
#    import datetime
#    
#    t1 = datetime.time(5,30)
#    t2 = datetime.time(15,30)
##    print t2
##    print t
##
##    persona_session(x,
##                    horario=t)
###    
###  
#
#    #item = item_session.por_nombre(u'programador', u'persona_ocupacion')
#    #print item.nombre
#    #ocupacion_session()  
#
##    ocupacion_session()
#    
#    ocupacion_session(ocupacion_nombre=u'Preseidente de la Rpca.',
#                       inicio=t1,
#                       fin=t2)
#    
#    transaction.commit()
    
    
    