# -*- coding: utf-8 -*-
from base import *
from jq.ajax_form import AjaxForm
#from jq.autocomplete import AutoCompleteField

from tw.jose.autocomplete import AutoCompleteField
from tw.jose.ajaxform import AjaxForm


#from tw.
#success_js = JSLink(link='/js/success_form.js')



xxx = JSSource("""\
function success_persona_form(responseText, statusText, xhr, form)
{
    if(successForm(responseText, statusText, xhr, form))
    {
        form.clearForm();
    }
    else
    {
    }
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
)



class OcupacionForm(twf.TableFieldSet):
    
    #show_children_errors = True
    #show_error = True
    legend = ''
    fields = [
              AutoCompleteField('nombre', label_text='nombre', validator=twv.String(), url_data='/persona/fetch_ocupacion', matchContains=False),
              twf.TextField('inicio', label_text='Inicio', validator=twv.TimeConverter(use_datetime=True)),
              twf.TextField('fin', label_text='Fin', validator=twv.TimeConverter(use_datetime=True)),
             ]



class PersonaForm(AjaxForm): #(twf.TableForm): # (AjaxForm): #
    
    ##show_error = False
    #show_children_errors = False
    url = '/persona/guardar'
    success = js_function('success_persona_form')
    submit_text = 'Guardar'
    #on_success = js_function('test_form')
    
    
    javascript = [xxx]
    javascript.extend(AjaxForm.javascript)
    
    fields = [
             twf.HiddenField('id'),
             twf.CheckBoxList('tipos_id', label_text='Tipo', validator=twv.ForEach(twv.Int)),
             twf.RadioButtonList('_genero', label_text='Genero', validator=twv.String(if_missing='', if_empty=None), options=[('m', 'Masculino'), ('f', 'Femenino')]),
             twf.TextField('nombre', label_text='Nombre', validator=twv.String(not_empty=True)),
             twf.TextField('apellido', label_text='Apellido', validator=twv.String(if_empty=None)),
             twf.RadioButtonList('tipodoc_id', label_text='Tipo Documento', validator=twv.Int(if_missing=None)),
             twf.TextField('nrodoc', label_text='Nro. Documento', validator=twv.String(if_empty=None)),
             #AutoCompleteField('ocupacion_nombre', label_text='Ocupacion', validator=twv.String(), url_data='/persona/fetch_ocupacion', matchContains=False, parse=js_function("parsear")),
             #twf.TextField('horario', label_text='Horario', validator=twv.TimeConverter(use_datetime=True)),
             
             twf.TextField('email', validator=twv.Email(), label_text='Email', ),
             OcupacionForm('ocupacion'),
             ]
    
persona_form = PersonaForm('persona_form')



#o = OcupacionForm('xxx')

#def validar(form, **kw):
#    d = {}
#    try:
#        x = form.validate(kw)
#    except Invalid, e:
#        for k, v in e.error_dict.items():
#            if v.error_dict:
#                for kk, vv in v.error_dict.items():
#                    d[k + '.' + kk] = vv
#            else:
#                d[k] = v
#    return d


#print validar(persona_form, nombre='', ocupacion={'inicio':'5'})


