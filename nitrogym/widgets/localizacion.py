# -*- coding: utf-8 -*-
from base import *
from jq.ajax_form import AjaxForm
from jq.autocomplete import AutoCompleteField


def extraParam():
    
    x = \
    """
    function x_nombre() 
    { 
    return $("* [name='pais_nombre']").val()+ "\t" + \
            $("* [name='dpto_nombre']").val()+ "\t" + \
            $("* [name='ciudad_nombre']").val()+ "\t"
            //$("* [name='barrio_nombre']").val()+ "\t" + \
            //$("* [name='calle1_nombre']").val()+ "\t" + \
            //$("* [name='calle2_nombre']").val()+ "\t"
    }

    function parsear(data) {
            return $.map(data, function(row) {
                return {
                    data: row,
                    value: row[0],
                    result: row[0] // + " <" + row.to + ">"
                }
            });
        }
    """
    return JSSource(x)
#    x = \
#    """
#    function() { return $("input [name=%(nombre)s]").val(); }
#    """ % {'nombre':nombre}
#    return js_function(x)


#class TextArea(twf.TextArea):
#    javascript = [JSLink(link='/js/jquery.NobleCount.js')]
#    
#    def update_params(self,d):
#        super(TextArea, self).update_params(d)
#        
#        options = {
#    'on_negative': 'go_red',
#    'on_positive': 'go_green',
#    'max_chars': 25,
#    'block_negative':True,
#                   }
#        
#        call = js_function('$("#%s").NobleCount' % d.id)("#count3", options)
#        self.add_call(call)

#              AutoCompleteField('calle2_nombre', , , extraParams=ext_calle, , label_text=u'Calle2'),

class Autocompletar(AutoCompleteField):
    dataType='json'
    parse=js_function("parsear")
    url_data = '/localizacion/autocompletar'
    cacheLength=0, 
    minChars=1, 
    #extraFields = ['nro_casa']
    
    #validator=twv.String(not_empty=True)

class LocalizacionForm(AjaxForm): #(twf.TableForm):
    
    _String = twv.String(if_empty=None)
    javascript = [extraParam()]
    javascript.extend(AjaxForm.javascript)

    #extra = {'x':extraParam()}
    ext = {'x':js_function('x_nombre')}
    ext_pais = {'x':js_function('x_nombre'), 'nn':'0-pais' }
    ext_dpto = {'x':js_function('x_nombre'), 'nn':'1-departamento' }
    ext_ciudad = {'x':js_function('x_nombre'), 'nn':'2-ciudad' }
    ext_barrio = {'x':js_function('x_nombre'), 'nn':'3-barrio' }
    ext_calle = {'x':js_function('x_nombre'), 'nn':'3-calle' }
    
    submit_text = 'Guardar'
    

    
    fields = [
              twf.HiddenField('id', validator=twv.Int, ),
              twf.HiddenField('persona_id', validator=twv.Int, ),
              twf.TextField('lugar', validator=twv.String(), label_text=u'Lugar', size=50),
              Autocompletar('pais_nombre', extraParams=ext_pais, label_text=u'País', validator=twv.String(not_empty=True)),
              Autocompletar('dpto_nombre', extraParams=ext_dpto, label_text=u'Departamento', url_data='/localizacion/autocompletar'),
              Autocompletar('ciudad_nombre', extraParams=ext_ciudad, label_text=u'Ciudad', validator=twv.String(not_empty=True)),
              Autocompletar('barrio_nombre', extraParams=ext_barrio, label_text=u'Barrio', url_data='/localizacion/autocompletar'),
              Autocompletar('calle1_nombre', extraParams=ext_calle, label_text=u'Calle1', url_data='/localizacion/autocompletar'),
              Autocompletar('calle2_nombre', extraParams=ext_calle, label_text=u'Calle2', url_data='/localizacion/autocompletar'),
              
              #AutoCompleteField('pais_nombre', url_data = '/localizacion/autocompletar', cacheLength=1, minChars=2, dataType='json',extraParams=ext_pais, validator=twv.String, label_text=u'País'),
#              AutoCompleteField('dpto_nombre', size=50, url_data = '/localizacion/autocompletar', cacheLength=1, minChars=2, dataType='json',extraParams=ext_dpto, label_text=u'Departamento'),
#              AutoCompleteField('ciudad_nombre', url_data = '/localizacion/autocompletar', cacheLength=0, minChars=2, dataType='json', extraParams=ext_ciudad, validator=twv.String(not_empty=True), label_text=u'Ciudad'),
#              AutoCompleteField('barrio_nombre', url_data = '/localizacion/autocompletar', cacheLength=1, minChars=2, dataType='json', extraParams=ext_barrio, validator=twv.String(not_empty=True), label_text=u'Barrio'),
#              AutoCompleteField('calle1_nombre', url_data = '/localizacion/autocompletar', cacheLength=1, minChars=2, dataType='json', extraParams=ext_calle, validator=twv.String(not_empty=True), label_text=u'Calle1'),
#              AutoCompleteField('calle2_nombre', url_data = '/localizacion/autocompletar', cacheLength=1, minChars=2, dataType='json', extraParams=ext_calle, validator=twv.String(not_empty=True), label_text=u'Calle2'),
              
              twf.TextField('nro_casa', validator=_String, label_text=u'Nro. Casa', maxlength=10, size=10),
              twf.TextField('nro_depto', validator=_String, label_text=u'Nro. Dpto', maxlength=10, size=10),
              twf.TextField('piso', validator=_String, label_text=u'Piso', maxlength=10, size=10),
              twf.TextField('bloque', validator=_String, label_text=u'Bloque', maxlength=10, size=10),
              twf.TextField('codigo_postal', validator=_String, label_text=u'Código Postal', maxlength=16, size=10),
              twf.TextArea('referencia', validator=_String, label_text=u'Referencia', maxlength=255),
             ]


localizacion_form = LocalizacionForm('localizacion_form')
    
    
