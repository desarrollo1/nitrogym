# -*- coding: utf-8 -*-

from tw.forms import validators as twv 
import tw.forms as twf 
import tw.api as twa

from tw.jquery import jquery_js
from tw.jquery import AjaxForm
from formencode.api import Invalid



__all__ = ['ValidarFormulario',
           'form_validator',
           'twf',
           'twv',
           'twa']
        
class ValidarFormulario(twv.FormValidator):
    """
    Parametros:
        method: (fields, errors)
    """

    def validate_python(self, fields, state):
        errors = {}
        self.method(fields, errors)
        
        #---------------------------------------------------------------
        # esto es muy importante para usar el tmpl_context.form_errors
        msg = u''
        for k, v in errors.items():
            msg += '%s:%s\n' % (k, v)
        #--------------------------------------------------------------

        if any(errors):
            raise twv.Invalid(msg, fields, state, None, errors) # error_dict=errors


def form_validator(method):
    return twv.Schema(chained_validators=[ValidarFormulario(method=method)])
