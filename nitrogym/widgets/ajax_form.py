# -*- coding: utf-8 -*-
from base import *
#from tw.jquery import AjaxForm

jquery_form_js = JSLink(link='/js/jquery.form.js')
#jquery_ajaxform_css=CSSLink(link='/css/jquery.autocomplete.css')




def update_option(cls, options, name, d):
    x = d.get(name, getattr(cls, name))
    if not x is None:
        options[name] = x

class AjaxForm(twf.TableForm):
    
    params = ['on_success',
        "id", "target", "beforeSubmit", "action"
        "success", "type", "dataType",
        "clearForm", "resetForm", "timeout"]

    url = None
    replaceTarget = None
    type = 'POST'
    data = None
    dataType = None
    beforeSerialize = None
    beforeSubmit = None
    success = None
    semantic = None
    resetForm = None
    clearForm = None
    iframe = None
    iframeSrc = None
    forceSync = None
    on_success = None
    
    template = "genshi:tw.jquery.templates.activeform"
    javascript = [jquery_js, jquery_form_js]
    include_dynamic_js_calls = True
    
    
    def update_params(self, d):
        super(AjaxForm, self).update_params(d)
        if not getattr(d, "id", None):
            raise ValueError, "AjaxForm is supposed to have id"
        
        options = {}
        update_option(self, options, 'url', d)
        update_option(self, options, 'success', d)
        update_option(self, options, 'target', d)
        update_option(self, options, 'resetForm', d)
        update_option(self, options, 'clearForm', d)
        update_option(self, options, 'type', d)
        update_option(self, options, 'data', d)
        update_option(self, options, 'dataType', d)
        update_option(self, options, 'beforeSerialize', d)
        update_option(self, options, 'beforeSubmit', d)
        update_option(self, options, 'semantic', d)
        update_option(self, options, 'iframe', d)
        update_option(self, options, 'iframeSrc', d)
        update_option(self, options, 'forceSync', d)
        
        
        
        on_success = d.get('on_success', self.on_success)
        call = js_function('$("#%s").ajaxForm' % d.id)(options).data('on_success', on_success)
        print call
        self.add_call(call)
        
        
        
        
        
        
#x = AjaxForm('x')
#print x(success=js_function('alert'))

