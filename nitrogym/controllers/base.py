# -*- coding: utf-8 -*-
"""Sample controller module"""

# turbogears imports
from tg import expose, url, tmpl_context
from tg import redirect, validate, flash

# third party imports
#from pylons.i18n import ugettext as _
from repoze.what import predicates

# project specific imports
from nitrogym.lib.base import BaseController
from nitrogym.model import DBSession, metadata
import sys
import json
import transaction
from formencode.api import Invalid

persona_url = url('/persona')
localizacion_url = url('/localizacion')



ctrl_url = {
'persona': url('/persona'),
'localizacion' : url('/localizacion'),
}



def validar_master(form, **kw):
    d = {}
    try:
        x = form.validate(kw)
    except Invalid, e:
        for k, v in e.error_dict.items():
            if v.error_dict:
                for kk, vv in v.error_dict.items():
                    d[k + '_' + kk] = unicode(vv)
            else:
                d[k] = unicode(v)
    return d


def validar_master2(e, join='_'):
    d = {}
    if e:
        for k, v in e.error_dict.items():
            if v.error_dict:
                for kk, vv in v.error_dict.items():
                    d[k + join + kk] = unicode(vv)
            else:
                d[k] = unicode(v)
    return d

