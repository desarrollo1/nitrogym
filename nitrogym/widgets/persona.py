# -*- coding: utf-8 -*-
from base import *
from jq.ajax_form import AjaxForm
from jq.autocomplete import AutoCompleteField


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
"""
)




class PersonaForm(AjaxForm): #(twf.TableForm):
    
    url = '/persona/guardar'
    success = js_function('success_persona_form')
    submit_text = 'Guardar'
    #on_success = js_function('test_form')
    
    
    javascript = [xxx]
    javascript.extend(AjaxForm.javascript)
    
    fields = [
             twf.HiddenField('id'),
             twf.CheckBoxList('tipos_id', label_text='Tipos', validator=twv.ForEach(twv.Int)),
             twf.RadioButtonList('_genero', label_text='Sexo', validator=twv.String(if_missing=''), options=[('m', 'Masculino'), ('f', 'Femenino')]),
             twf.TextField('nombre', label_text='Nombre', validator=twv.String(not_empty=True)),
             twf.TextField('apellido', label_text='Apellido', validator=twv.String()),
             twf.RadioButtonList('tipodoc_id', label_text='Tipo Documento', validator=twv.Int(if_missing=None)),
             twf.TextField('nrodoc', label_text='Nro. Documento', validator=twv.String()),
             AutoCompleteField('ocupacion_nombre', label_text='Ocupacion', validator=twv.String(), url_data='/persona/fetch_ocupacion', matchContains=False),
             twf.TextField('email', validator=twv.Email(), label_text='Email', ),
             ]
    
persona_form = PersonaForm('persona_form')
