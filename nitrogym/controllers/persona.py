# -*- coding: utf-8 -*-
"""Modulo persona controller"""
from base import *
from nitrogym.widgets.persona import persona_form #, form_pais
from nitrogym.session import lista_session, item_session, persona_session #, pais_session
import json

class PersonaController(BaseController):
    
    
    allow_only = predicates.in_group('administradores')
    
    @expose()
    def index(self):
        return u'hello world...2'
    
    
    @validate(persona_form)
    @expose('json')
    def guardar(self, **kw):
        
        e = tmpl_context.form_errors
        
        if not e:
            try:
                
                #print '*********************'
                #print kw['tipos']
                
                #kw['pais'] = pais_session.por_nombre(kw['pais_nombre'])
                kw['tipos'] = item_session.por_lista_id(kw['tipos_id'])
                kw['ocupacion'] = item_session.actualizar(kw['ocupacion_nombre'], u'persona_ocupacion')
                
                print '****************************'
                print kw
                
                #obj.tipos = item_session.por_lista_id(kw.pop('tipos_id', []))
                
                persona_session(**kw)
                e['__success__'] = u'Guardado...'
            except:
                e['__error__'] = str(sys.exc_info()) # u'Ocurrió un error...'
        return e
    
    
    
    
    @expose('nitrogym.templates.paginas.test_form')
    def agregar(self, **kw):
        
        try:
            # lista de id del tipo_persona.
            tipos = lista_session.por_nombre('tipo_persona').items
            tipos = [(i.id, i.nombre) for i in tipos]
            
            tipodoc = lista_session.por_nombre('tipo_documento').items
            tipodoc = [(i.id, i.nombre) for i in tipodoc]
            
            
            
            #paises = pais_session.listar()
            #paises = [[i.id, i.nombre] for i in paises]
        
            if kw.get('id'):
                value = persona_session.por_id(kw['id'])
            else:
                value = kw
            
            child_args = dict(tipos_id={'options':tipos},
                              tipodoc_id={'options':tipodoc},
                              #pais_nombre={'url_data':paises},
                              )
            return dict(form=persona_form, 
                        action='guardar', 
                        titulo='Persona',
                        value=value,
                        child_args=child_args)
        except:
            flash(sys.exc_info())
        redirect('/')
        
    @expose('json')
    def fetch_ocupacion(self, **kw):
        print '*************************'
        print kw
        
        #x = [{"name":"Peter Pan","to":"peter@pan.de"},{"name":"Forneria Marconi","to":"live@japan.jp"},{"name":"Master Sync","to":"205bw@samsung.com"},{"name":"Donnie Darko","to":"dd@timeshift.info"},{"name":"Quake The Net","to":"webmaster@quakenet.org"}]
        
        r = []
        kw['q'] = kw['q'].replace('%','') + '%' 
        l = item_session.autocompletar('persona_ocupacion', **kw)
        for i in l:
            r.append([i.nombre])
        
        
        return json.JSONEncoder().encode(r)
        
        
        return {'data':'jose'}
        return "jose\nlacognata\nmedina"
        
    @expose('nitrogym.templates.paginas.test_form')
    def pais(self, **kw):
            return dict(form=form_pais)
            
    @expose()
    def autocompletar(self, **kw):
        return 'Paraguay\nBolivia'
        
        