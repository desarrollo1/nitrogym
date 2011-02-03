# -*- coding: utf-8 -*-

import tw.forms as twf
import tw.forms.validators as twv
from util import form_validator
from tw.jquery import AjaxForm
from tw.api import JSLink, js_function, JSSource, Link
from tw.jquery import jquery_js




jQuery= js_function('$')

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