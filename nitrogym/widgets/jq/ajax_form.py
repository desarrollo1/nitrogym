# -*- coding: utf-8 -*-
from nitrogym.widgets.base import *
from tw.jquery import AjaxForm

jquery_form_js = JSLink(link='/js/jquery.form.js')
#jquery_ajaxform_css=CSSLink(link='/css/jquery.autocomplete.css')



success_js = JSLink(link='/js/success_form.js')
#success = JSSource("""\
#function success_form(responseText, statusText, xhr, form)
#{
#    if(successForm(responseText, statusText, xhr, form))
#    {
#        form.clearForm();
#    }
#    else
#    {
#    }
#}
#"""
#)

        
        
ajaxform_params = ['url', 'success', 'target', 'resetForm', 'clearForm', 'type', 'data', 
                   'dataType', 'beforeSerialize', 'beforeSubmit', 'semantic', 'iframe', 'iframeSrc',
                   'forceSync']

class AjaxForm(twf.TableForm):
    
    params = ajaxform_params
#    url = None
#    target = None
#    replaceTarget = None
#    type = 'POST'
#    data = None
#    dataType = None
#    beforeSerialize = None
#    beforeSubmit = None
    success = js_function('success_form')
#    semantic = None
#    resetForm = None
#    clearForm = None
#    iframe = None
#    iframeSrc = None
#    forceSync = None
    
    
    #on_success = None
    #template = "genshi:tw.jquery.templates.activeform"
    javascript = [jquery_js, jquery_form_js, success_js]
    include_dynamic_js_calls = True
    
    
    def update_params(self, d):
        super(AjaxForm, self).update_params(d)
        if not getattr(d, "id", None):
            raise ValueError, "AjaxForm is supposed to have id"
        options = update_options(self, {}, d, *ajaxform_params)
        
        

        
#        update_option(self, options, 'url', d)
#        update_option(self, options, 'success', d)
#        update_option(self, options, 'target', d)
#        update_option(self, options, 'resetForm', d)
#        update_option(self, options, 'clearForm', d)
#        update_option(self, options, 'type', d)
#        update_option(self, options, 'data', d)
#        update_option(self, options, 'dataType', d)
#        update_option(self, options, 'beforeSerialize', d)
#        update_option(self, options, 'beforeSubmit', d)
#        update_option(self, options, 'semantic', d)
#        update_option(self, options, 'iframe', d)
#        update_option(self, options, 'iframeSrc', d)
#        update_option(self, options, 'forceSync', d)
        #self.update_attrs(d, 'url', 'success')
        
        
        
        #on_success = d.get('on_success', self.on_success)
        call = js_function('$("#%s").ajaxForm' % d.id)(options)#.data('on_success', on_success)
        self.add_call(call)

