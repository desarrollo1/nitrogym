# -*- coding: utf-8 -*-
if __name__ == '__main__':
    from db import *
    
from base import *
from nitrogym.model import Distrito, Lista, Localizacion
from nitrogym.session import lista_session



class DistritoSession(BaseSession):
    model = Distrito
    
    
    def base2(self):
        return DBSession.query(Distrito).join(Lista) 
    

    
    def _guardar_(self, obj, **kw):
        """ Guarda un item """
        kw_pop(obj, 'nombre', **kw)
        kw_pop(obj, 'descripcion', **kw)
        kw_pop(obj, 'lista', **kw) or \
        kw_pop(obj, 'lista_id', **kw)
        kw_pop(obj, 'padre', **kw) or \
        kw_pop(obj, 'padre_id', **kw)
        
        if not obj.lista and kw.has_key('lista_nombre'):
            obj.lista = lista_session.por_nombre(kw.pop('lista_nombre'))
        
        
    
    def por_nombre(self, nombre, lista_nombre, **kw):

        if kw.get('padre'):
            padre_id = kw['padre'].id
        else:
            padre_id = kw.get('padre_id')
        
        q = self.base2(). \
        filter(Lista.nombre==lista_nombre). \
        filter(Distrito.nombre.ilike(nombre)). \
        filter(Distrito.padre_id==padre_id)
        return q.first()
        
    def autocompletar(self, *args):
        
        q = None
        hijo = None
        x = padre = aliased(Distrito)
        for v in reversed(args):
            if not v[0] is None:
                lista = aliased(Lista)
                if not hijo:
                    q = DBSession.query(padre).outerjoin((lista, padre.lista_id==lista.id))
                else:
                    q = q.outerjoin((padre, hijo.padre_id==padre.id)).outerjoin((lista, padre.lista_id==lista.id))
                q = q.filter(padre.nombre.ilike(v[0])).filter(lista.nombre==v[1])
                hijo = padre
                padre = aliased(Distrito)
        if q:
            return q.order_by(x.nombre)
        
        
    def actualizar_arbol(self, *args):
        """ 
            El formato de args debe ser de tipo tupla(nombre, lista_nombre)
        """
        padre = None
        li = [i for i in args if i[0]] # limpia los vacios...
        if li:
            for v in li:
                if not v[0] is None:
                    padre = self.actualizar(v[0], v[1], padre=padre)
                    DBSession.flush()

    
    def actualizar(self, nombre, lista_nombre, **kw):
        obj = self.por_nombre(nombre, lista_nombre=lista_nombre, **kw)
        if not obj:
            obj = self(nombre=nombre, lista_nombre=lista_nombre, **kw)
        return obj
 
 

class LocalizacionSesison(BaseSession):
    model = Localizacion


        
distrito_session = DistritoSession()
localizacion_session = LocalizacionSesison()


def setup():
    
    try:
        lista = lista_session(nombre=u'pais')
        lista = lista_session(nombre=u'departamento')
        lista = lista_session(nombre=u'ciudad')
        lista = lista_session(nombre=u'barrio')
        lista = lista_session(nombre=u'calle')
        transaction.commit()
        print 'hecho...'
    except:
        print sys.exc_info()
    


if __name__ == '__main__':
    pass

#    x = distrito_session.autocompletar((u'Alemania', u'pais'),
#                                   (u'm%', u'ciudad'),
#                                   )
#    print x.all()[0].nombre

#    x = distrito_session.autocompletar((u'Alemania', u'pais'),
#                                   (u'Skungen', u'departamento'),
#                                   (u'Bayer', u'ciudad'),
#                                   (u'Baviera', u'calle'))
#    
#    print x.all()

#    distrito_session.arbol((u'Alemania', u'pais'), 
#                           (u'Skungen', u'departamento'), 
#                           (u'Bayer', u'ciudad'), 
#                           #(u'Munchen', u'barrio'), 
#                           (None, u'calle'),
#                           (u'Baviera', u'calle') )

#    pais = distrito_session.actualizar(u'Paraguay', u'pais', padre=None)
#    dpto = distrito_session.actualizar(u'', u'', padre=pais)
#    ciudad = distrito_session.actualizar(u'San juan Bautista', u'ciudad', padre=dpto)
##    barrio = distrito_session.actualizar(u'Nuestra Señora de la Asuncion', u'barrio', padre=ciudad)
##    calle1 = distrito_session.actualizar(u'Via Férrea', u'calle', padre=ciudad)
##    calle2 = distrito_session.actualizar(u'San Juan', u'calle', padre=ciudad)
#    barrio = distrito_session.actualizar(u'', u'barrio', padre=ciudad)
#    calle1 = distrito_session.actualizar(u'', u'calle', padre=ciudad)
#    calle2 = distrito_session.actualizar(u'', u'calle', padre=ciudad)
#    
##    
##    
##    
##    
#    localizacion_session.save(id=None,
#                            lugar=u'casa',
#                            pais=pais,
#                            dpto=dpto,
#                            ciudad=ciudad,
#                            barrio=barrio,
#                            calle1=calle1,
#                            calle2=calle2
#                            )


    #print Localizacion.__mapper__

    #for i in dir(Localizacion.__mapper__):
    
#    l = Localizacion()
#    for i in l.__mapper__.iterate_properties:
#        #i = None
#        print i.key
        #break
    #x = distrito_session.actualizar(u'Brasil', u'pais', padre=None)
    #print x
    
    
    #autocompletar_dpto(u'argentina', u'boca')
    #x = distrito_session.autocompletar(None, u'argentina', u'boca', u'san lorenzo', u'%') #, u'boca', u'San lorenzo')
    
    #print x.all()[0].nombre
    
    #print x
#    print x #[0].nombre
#    pais = distrito_session.actualizar(u'Paraguay', u'pais')
#    dpto = distrito_session.actualizar(u'Central', u'departamento', padre=pais)
#    
#    
#    print '**********/////////***********'
#    print dpto.id
#    
#    ciudad = distrito_session.actualizar(u'San Lorenzo', u'ciudad', padre=dpto)
#    barrio = distrito_session.actualizar(u'Universitario', u'barrio', padre=ciudad)
#    calle1 = distrito_session.actualizar(u'Mcal. Estigarribia', u'calle', padre=ciudad)
#    
#    print calle1.nombre
    
#    pais = distrito_session.pais_por_nombre(u'argentina')
#    dpto = distrito_session.dpto_por_nombre(u'misiones', padre=pais)
#    
#    print pais.nombre
#    print dpto.nombre
#    
#    
#    
#    print dpto.nombre
    #setup()
#    lista = lista_session(nombre=u'departamentos')
#         
#    padre= distrito_session.por_nombre(u'Paraguay')   
#    dpto = distrito_session(nombre=u'Misiones', padre=padre, lista=lista)
#    
#    
#    
##    print x.nombre
    #DBSession.rollback()
    
#    for i in dir(DBSession):
#        print i
#    
    transaction.commit()
    
        
        
        
        