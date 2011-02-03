# -*- coding: utf-8 -*-
if __name__ == '__main__':
    from db import *
    
from base import *
from nitrogym.model import Lista, Item




    


class ListaSession(BaseSession):
    """
        Session con la base de datos para listas.
    """
    model = Lista
    
    def guardar(self, **kw):
        """ Guarda una lista """
        
        lista = self.instancia(**kw)
        kw_pop(lista, 'nombre', **kw)
        kw_pop(lista, 'descripcion', **kw)
        return self.add(lista)
            
    def por_nombre(self, nombre):
        return self.base().filter_by(nombre=nombre).first()
    
            
class ItemSession(BaseSession):
    """
        Session con la base de datos para Items.
    """
    model = Item
    
    
    def base2(self):
        return DBSession.query(Item).join(Lista) 

    def _guardar_(self, item, **kw):
        """ Guarda un item """

        #item = self.instancia(**kw)
        kw_pop(item, 'nombre', **kw)
        kw_pop(item, 'descripcion', **kw)
        kw_pop(item, 'lista', **kw) or \
        kw_pop(item, 'lista_id', **kw)
        #return self.add(item)
    
    def por_nombre(self, nombre, lista_nombre):
        return DBSession.query(Item).join(Lista). \
        filter(Item.nombre==nombre). \
        filter(Lista.nombre==lista_nombre).first()
        
        
    def por_lista_id(self, lista_id):
        """ 
            Retorna lista de ids de acuerda a lista_id.
        """
        if lista_id:
            return DBSession.query(Item). \
            filter(Item.id.in_(lista_id)).all()
        return []
    
    
    def autocompletar(self, lista_nombre, **kw):
        return self.base2(). \
        filter(Item.nombre.ilike(like(kw['q']))). \
        filter(Lista.nombre==lista_nombre).limit(kw['limit']).all()
        
    
    def actualizar(self, nombre, lista_nombre):
        i =  self.base2(). \
        filter(Item.nombre.ilike(nombre)). \
        filter(Lista.nombre==lista_nombre).first()
        if not i:
            lista = lista_session.por_nombre(lista_nombre)
            i = self(nombre=nombre, lista=lista)
        return i
        
        
        
        
class NodoSession(BaseSession):
    """ 
        En este nodo los campos mas importantes son:
        nombre, lista_id y padre_id.
    """
    model = None


    def base2(self):
        """ """
        return DBSession.query(self.model).join(Lista) 
    
    def por_nombre(self, nombre, lista_nombre, **kw):

        if kw.get('padre'):
            padre_id = kw['padre'].id
        else:
            padre_id = kw.get('padre_id')
        
        q = self.base2(). \
        filter(Lista.nombre==lista_nombre). \
        filter(self.model.nombre.ilike(nombre)). \
        filter(self.model.padre_id==padre_id)
        return q.first()
    
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
        """ 
            Devuelve el nodo deseado,
            Si no existe lo crea primero.
        """
        obj = self.por_nombre(nombre, lista_nombre=lista_nombre, **kw)
        if not obj:
            obj = self(nombre=nombre, lista_nombre=lista_nombre, **kw)
        return obj


    def autocompletar(self, *args):
        """
            Formato:
                args = ((nombre, nombre_lista),(nombre, nombre_lista))
            
            Esto ignora los valores None en los nombres.
        """
        q = None
        hijo = None
        padre = x = aliased(self.model)
        for v in reversed(args):
            if not v[0] is None:
                lista = aliased(Lista)
                if not hijo:
                    q = DBSession.query(padre).outerjoin((lista, padre.lista_id==lista.id))
                else:
                    q = q.outerjoin((padre, hijo.padre_id==padre.id)).outerjoin((lista, padre.lista_id==lista.id))
                
                q = q.filter(padre.nombre.ilike(v[0])).filter(lista.nombre==v[1])
                hijo = padre
                padre = aliased(self.model)
                n += 1
        if q:
            return q.order_by(x.nombre) #.first().nombre
        
        
        

lista_session = ListaSession()
item_session = ItemSession()










def setup():

    try:
        transaction.begin()
        l = lista_session(nombre=u'tipo_persona')
        l.items.append(item_session(nombre=u'Cliente'))
        l.items.append(item_session(nombre=u'Profesor'))
        transaction.commit()
        
        l = lista_session(nombre=u'tipo_documento')
        l.items.append(item_session(nombre=u'Cédula'))     
        transaction.commit()
        
        print 'hecho...'
    except:
        print sys.exc_info()
        
    try:
        transaction.begin()
        l = lista_session(nombre=u'persona_ocupacion')
        l.items.append(item_session(nombre=u'Ama de casa'))
        l.items.append(item_session(nombre=u'Abogado'))
        l.items.append(item_session(nombre=u'Profesor'))
        l.items.append(item_session(nombre=u'Estudiante'))
        l.items.append(item_session(nombre=u'Desempleado'))
        l.items.append(item_session(nombre=u'Deportista'))
        transaction.commit()
        
        print 'hecho...'
    except:
        print sys.exc_info()


if __name__ == '__main__':
    pass
    setup()
    





#x = item_session.por_lista_id([3, 2])
#print x

#l = item_session.por_lista_id([2, 3, 4])
#print l



#i = item_session.por_nombre(u'ESTUDIANTE', u'profesion')
#item_session(item=i, nombre=u'Estudiante')
#transaction.commit()

#print Item.__name__.lower()


#i = item_session.por_nombre(u'estudiante', u'profesion')
#print i.nombre
#lista = lista_session.por_nombre(u'tipo_persona')
#for i in lista.items:
#    print i.nombre


#item_session(nombre=u'profesor', lista=lista)
#item_session(nombre=u'alumno', lista=lista)
#item_session(nombre=u'profesor', lista=lista)
#print lista.descripcion
#lista_session(nombre=u'tipo_persona', descripcion=u'Indica el tipo de persona')
#transaction.commit()







        