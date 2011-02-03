# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, synonym, backref
from sqlalchemy import Table, ForeignKey, Column, UniqueConstraint
from sqlalchemy.types import Integer, Unicode, Date, DateTime, BLOB, LargeBinary, SmallInteger, Time

#from sqlalchemy.types.LargeBinary

from nitrogym.model import DeclarativeBase, metadata, DBSession
from hashlib import sha1
from datetime import datetime

#from sqlalchemy.types.Time
#from sqlalchemy.PrimaryKeyConstraint