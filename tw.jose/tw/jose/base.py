# -*- coding: utf-8 -*-

import tw.forms as twf
import tw.forms.validators as twv
#from util import form_validator
from tw.jquery import AjaxForm
from tw.api import JSLink, js_function, JSSource, Link
from tw.jquery import jquery_js
from formencode.api import Invalid


jQuery= js_function('$')
jquery_extra_js = JSLink(modname=__name__, filename='static/js/extra.js')
#def update_option(cls, options, name, d):
#    x = d.get(name, getattr(cls, name))
#    if not x is None:
#        options[name] = x
        
def update_options(cls, options, d, *args):
    for name in args:
        # con None va a tomar el dafault del plugin... 
        x = d.get(name, getattr(cls, name, None))
        if not x is None:
            options[name] = x
    return options


#def validar_master(form, **kw):
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


