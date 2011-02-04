# -*- coding: utf-8 -*-
from base import *

#jquery_ajaxform_js = JSLink(link='/js/jquery.form.js')
#jquery_ajaxform_css=CSSLink(link='/css/jquery.autocomplete.css')
#success_js = JSLink(link='/js/success_form.js')


jquery_form_js = JSLink(modname=__name__, filename='static/js/jquery.form.js', javascript=[jquery_extra_js])    
ajaxform_params = ['url', 'success', 'target', 'resetForm', 'clearForm', 'type', 'data', 
                   'dataType', 'beforeSerialize', 'beforeSubmit', 'semantic', 'iframe', 'iframeSrc',
                   'forceSync']

class AjaxForm(twf.TableForm):
    
    params = ajaxform_params
    success = js_function('success_form')

    #template = "genshi:tw.jquery.templates.activeform"
    javascript = [jquery_js, jquery_form_js]
    include_dynamic_js_calls = True
    
    def update_params(self, d):
        super(AjaxForm, self).update_params(d)
        if not getattr(d, "id", None):
            raise ValueError, "AjaxForm is supposed to have id"
        options = update_options(self, {}, d, *ajaxform_params)
        call = js_function('$("#%s").ajaxForm' % d.id)(options)#.data('on_success', on_success)
        self.add_call(call)

