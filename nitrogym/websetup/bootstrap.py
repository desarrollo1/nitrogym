# -*- coding: utf-8 -*-
"""Setup the nitrogim application"""

import logging
from tg import config
from nitrogym import model

import transaction
from nitrogym.session import grupo_session, permiso_session, usuario_session#, pais_session

def bootstrap(command, conf, vars):
    """Place any commands to setup nitrogim here"""
    try:
        u = usuario_session.guardar(login=u'admin',
                                    password=u'admin')
        
        
        g1 = grupo_session.guardar(nombre=u'administradores')
        g1.usuarios.append(u)
        
        p1 = permiso_session.guardar(nombre=u'administrador')
        p1.grupos.append(g1)
        
        g2 = grupo_session.guardar(nombre=u'usuarios')
        g2.usuarios.append(u)
        
        p2 = permiso_session.guardar(nombre=u'usuario')
        p2.grupos.append(g2)
        
        transaction.commit()
        
    except:
        import sys
        print 'no se pudo crear usuario...'
        print sys.exc_info()
        pass


#    pais_session.setup()




    # <websetup.bootstrap.before.auth
#    from sqlalchemy.exc import IntegrityError
#    try:
#        u = model.User()
#        u.user_name = u'manager'
#        u.display_name = u'Example manager'
#        u.email_address = u'manager@somedomain.com'
#        u.password = u'managepass'
#    
#        model.DBSession.add(u)
#    
#        g = model.Group()
#        g.group_name = u'managers'
#        g.display_name = u'Managers Group'
#    
#        g.users.append(u)
#    
#        model.DBSession.add(g)
#    
#        p = model.Permission()
#        p.permission_name = u'manage'
#        p.description = u'This permission give an administrative right to the bearer'
#        p.groups.append(g)
#    
#        model.DBSession.add(p)
#    
#        u1 = model.User()
#        u1.user_name = u'editor'
#        u1.display_name = u'Example editor'
#        u1.email_address = u'editor@somedomain.com'
#        u1.password = u'editpass'
#    
#        model.DBSession.add(u1)
#        model.DBSession.flush()
#        transaction.commit()
#    except IntegrityError:
#        print 'Warning, there was a problem adding your auth data, it may have already been added:'
#        import traceback
#        print traceback.format_exc()
#        transaction.abort()
#        print 'Continuing with bootstrapping...'
        

    # <websetup.bootstrap.after.auth>
