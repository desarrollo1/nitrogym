# -*- coding: utf-8 -*-
"""Modulo persona controller"""
from base import *
from nitrogym.widgets.localizacion import localizacion_form #, form_pais
from nitrogym.session import distrito_session, localizacion_session #lista_session, item_session, persona_session #, pais_session
from nitrogym.model import Localizacion
import json

class LocalizacionController(BaseController):
    
    
    allow_only = predicates.in_group('administradores')
    
    
    def __init__(self, _url):
        self.url = _url
    
    @expose()
    def index(self):
        return u'hello world...2'
    
    
    @validate(localizacion_form)
    @expose('json')
    def guardar(self, **kw):
        
        e = tmpl_context.form_errors
        
        if not e:
            try:
                
                padre = None
                pais_nombre = kw.pop('pais_nombre', None)
                dpto_nombre = kw.pop('dpto_nombre', None)
                ciudad_nombre = kw.pop('ciudad_nombre', None)
                barrio_nombre = kw.pop('barrio_nombre', None)
                calle1_nombre = kw.pop('calle1_nombre', None)
                calle2_nombre = kw.pop('calle2_nombre', None)
                
                if pais_nombre:
                    padre = kw['pais'] = distrito_session.actualizar(pais_nombre, u'pais', padre=padre)
                if dpto_nombre:
                    padre = kw['dpto'] = distrito_session.actualizar(dpto_nombre, u'departamento', padre=padre)
                if ciudad_nombre:
                    padre = kw['ciudad'] = distrito_session.actualizar(ciudad_nombre, u'ciudad', padre=padre)
                if barrio_nombre:
                    kw['barrio'] = distrito_session.actualizar(barrio_nombre, u'barrio', padre=padre)
                if calle1_nombre:
                    kw['calle1'] = distrito_session.actualizar(calle1_nombre, u'calle', padre=padre)
                if calle2_nombre:
                    kw['calle2'] = distrito_session.actualizar(calle2_nombre, u'calle', padre=padre)

                localizacion_session.save(**kw)
                
                e['__success__'] = u'Guardado...'
            except:
                e['__error__'] = str(sys.exc_info()) # u'Ocurrió un error...'
        return e
    
    
    @expose('nitrogym.templates.paginas.test_form')
    def agregar(self, **kw):
        
        try:
            if kw.get('id'):
                value = localizacion_session.por_id(kw['id'])
            else:
                value = kw
                
            child_args = {}
            return dict(form=localizacion_form, 
                        action='/localizacion/guardar', 
                        titulo=u'Localización',
                        value=value,
                        child_args=child_args)
        except:
            flash(sys.exc_info())
        redirect('/')
        
    def json_parse(self, data):
        r = []
        for i in data:
            r.append([i.nombre])
        return json.JSONEncoder().encode(r)
    
    
    
#    @expose('json')
#    def autocompletar_pais(self, **kw):
#        
#        x = kw['x'].split('\t')
#        q = kw['q']+'%'
#        data = distrito_session.autocompletar((q, u'pais')).all()
#        return self.json_parse(data)
#    
#    @expose('json')
#    def autocompletar_dpto(self, **kw):
#        
#        x = kw['x'].split('\t')
#        q = kw['q']+'%'
#        data = distrito_session.autocompletar((x[0], u'pais'),
#                                              (q, u'departamento')).all()
#        return self.json_parse(data)
#
#    @expose('json')
#    def autocompletar_ciudad(self, **kw):
#        
#        x = kw['x'].split('\t')
#        q = kw['q']+'%'
#        x[1] = None
#        
#        data = distrito_session.autocompletar((x[0], u'pais'),
#                                              (x[1], u'departamento'),
#                                              (q, u'ciudad')).all()
#        return self.json_parse(data)
#    
#    @expose('json')
#    def autocompletar_barrio(self, **kw):
#        
#        x = kw['x'].replace('%', '')
#        x = [i for i in x.split('\t') if i]
#        
#        x = x.split('\t')
#        
#        
#        li = []
#        for i in kw['x'].split('\t'):
#            i = i.replace('%', '')
#            if not i:
#                i = None
#            li.append(i)
#        
#        q = kw['q'].replace('%', '')+'%'
#        data = distrito_session.autocompletar((li[0], u'pais'),
#                                              (li[1], u'departamento'),
#                                              (li[2], u'ciudad'),
#                                              (q, u'barrio')).all()
#        return self.json_parse(data)
#    
#    @expose('json')
#    def autocompletar_calle(self, **kw):
#        
#        
#        print kw
#        x = kw['x'].split('\t')
#        q = kw['q']+'%'
#        data = distrito_session.autocompletar((x[0], u'pais'),
#                                              (x[1], u'departamento'),
#                                              (x[2], u'ciudad'),
#                                              (q, u'calle')).all()
#        return self.json_parse(data)
#    
#    
#    
#    
    @expose('json')
    def autocompletar(self, **kw):
        """ Esto funciona con nodos y padres """
        
        s = kw['nn'].split('-')
        indice = int(s[0])
        lista_nombre = s[1]
        
        li = []
        for i in kw['x'].split('\t'):
            i = i.replace('%', '')
            if not i:
                i = None # esto es para ignorar los campos...
            li.append(i)
            
        ll = [
              (li[0], u'pais'),
              (li[1], u'departamento'),
              (li[2], u'ciudad'),
             ][:indice] # nivel de busqueda...
             
        q = kw['q'].replace('%', '')+'%'
        ll.append((q, lista_nombre))
        data = distrito_session.autocompletar(*ll)
        return self.json_parse(data)
#        return self.json_parse([])
    
    
    
    
    
    