# -*- coding: utf-8 -*-
from base import *
from ajax_form import AjaxForm


success_js = JSLink(link='/js/success_form.js')




class PersonaForm(AjaxForm): #(twf.TableForm):
    
    url = '/guardar'
    success = js_function('successForm')
    on_success = js_function('test_form')
    javascript = [success_js]
    
    fields = [
             twf.TextField('id'),
             twf.TextField('nombre', validator=twv.String(not_empty=True)),
             ]
    
persona_form = PersonaForm('persona_form')
persona_form2 = PersonaForm('persona_form2')
