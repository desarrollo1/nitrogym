# -*- coding: utf-8 -*-
"""
Auth* related model.

This is where the models used by :mod:`repoze.who` and :mod:`repoze.what` are
defined.

It's perfectly fine to re-use this definition in the nitrogim application,
though.

"""
import os
from datetime import datetime
import sys
try:
    from hashlib import sha1
except ImportError:
    sys.exit('ImportError: No module named hashlib\n'
             'If you are on python2.4 this library is not part of python. '
             'Please install it. Example: easy_install hashlib')

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import relation, synonym

from nitrogym.model import DeclarativeBase, metadata, DBSession

__all__ = ['Usuario', 'Grupo', 'Permiso']


#{ Association tables


# This is the association table for the many-to-many relationship between
# groups and permissions. This is required by repoze.what.
grupo_permiso_table = Table('grupo_permiso', metadata,
    Column('grupo_id', Integer, ForeignKey('grupo.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('permiso_id', Integer, ForeignKey('permiso.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)

# This is the association table for the many-to-many relationship between
# groups and members - this is, the memberships. It's required by repoze.what.
usuario_grupo_table = Table('usuario_grupo', metadata,
    Column('usuario_id', Integer, ForeignKey('usuario.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('grupo_id', Integer, ForeignKey('grupo.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)


#{ The auth* model itself


class Grupo(DeclarativeBase):
    """
    Group definition for :mod:`repoze.what`.
    Only the ``group_name`` column is required by :mod:`repoze.what`.

    """

    __tablename__ = 'grupo'

    # columnas
    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(Unicode(16), unique=True, nullable=False)
    creado = Column(DateTime, default=datetime.now)

    # relaciones
    usuarios = relation('Usuario', secondary=usuario_grupo_table, backref='grupos')
    
    # sinonimos
    group_name = synonym('nombre')
    permissions = synonym('permisos')


# The 'info' argument we're passing to the email_address and password columns
# contain metadata that Rum (http://python-rum.org/) can use generate an
# admin interface for your models.
class Usuario(DeclarativeBase):
    """
    User definition.
    This is the user definition used by :mod:`repoze.who`, which requires at
    least the ``user_name`` column.

    """
    __tablename__ = 'usuario'

    # columnas
    id = Column(Integer, autoincrement=True, primary_key=True)
    login = Column(Unicode(16), unique=True, nullable=False)
    _password = Column('password', Unicode(80),
                       info={'rum': {'field':'Password'}})
    creado = Column(DateTime, default=datetime.now)

    # sinonimos.
    groups = synonym('grupos')
    user_name = synonym('login')


    def _set_password(self, password):
        """Hash ``password`` on the fly and store its hashed version."""
        # Make sure password is a str because we cannot hash unicode objects
        if isinstance(password, unicode):
            password = password.encode('utf-8')
        salt = sha1()
        salt.update(os.urandom(60))
        hash = sha1()
        hash.update(password + salt.hexdigest())
        password = salt.hexdigest() + hash.hexdigest()
        # Make sure the hashed password is a unicode object at the end of the
        # process because SQLAlchemy _wants_ unicode objects for Unicode cols
        if not isinstance(password, unicode):
            password = password.decode('utf-8')
        self._password = password

    def _get_password(self):
        """ Retorna la version hasheada del password """
        return self._password

    password = synonym('_password', descriptor=property(_get_password,
                                                        _set_password))


    def validate_password(self, password):
        """
        Check the password against existing credentials.

        :param password: the password that was provided by the user to
            try and authenticate. This is the clear text version that we will
            need to match against the hashed one in the database.
        :type password: unicode object.
        :return: Whether the password is valid.
        :rtype: bool

        """
        hash = sha1()
        if isinstance(password, unicode):
            password = password.encode('utf-8')
        hash.update(password + str(self.password[:40]))
        return self.password[40:] == hash.hexdigest()


class Permiso(DeclarativeBase):
    """
    Permission definition for :mod:`repoze.what`.
    Only the ``permission_name`` column is required by :mod:`repoze.what`.
    """

    __tablename__ = 'permiso'

    # columnas
    id = Column(Integer, primary_key=True)
    nombre = Column(Unicode(50), nullable=False)
    descripcion = Column(Unicode(255))
    grupos = relation(Grupo, secondary=grupo_permiso_table,
                      backref='permisos')
    
    # sinonimos
    permission_name = synonym('nombre')
    groups = synonym('grupos')
