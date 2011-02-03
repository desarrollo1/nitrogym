# -*- coding: utf-8 -*-
if __name__ == '__main__':
    from db import *
    
from base import *
from nitrogym.model import Blob




class BlobSession(BaseSession):
    model = Blob
    
    def _guardar_(self, obj, **kw):
        kw_pop(obj, 'tipo', **kw)
        kw_pop(obj, 'nombre', **kw)
        kw_pop(obj, 'descripcion', **kw)
        kw_pop(obj, 'data', **kw)
        kw_pop(obj, 'data2', **kw)
        kw_pop(obj, 'modificado', **kw)
        
        
#class JpegImage(BlobSession):
#    
#    
#    def _guardar_(self, obj, **kw):
#        
#        obj.type = u'image/jpg'
#        
#        
#        BlobSession._guardar_(obj)
        
        
        
        
    
    