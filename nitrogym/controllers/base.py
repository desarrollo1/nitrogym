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

persona_url = url('/persona')
localizacion_url = url('/localizacion')


