# -*- coding: utf-8 -*-

from sqlalchemy import *
import transaction
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relation, backref, synonym, sessionmaker
#from sqlalchemy import types, sql, Table, ForeignKey, Column, CheckConstraint, DefaultClause, UniqueConstraint
#from miweb import model #import init_model
from nitrogym.model import DeclarativeBase, metadata, DBSession, init_model
#from sqlalchemy.exc.IntegrityError.params


#from sqlalchemy.sql.alias()

engine = create_engine('postgresql://postgres:secreto@127.0.0.1:5432/nitrogym', echo=True)
init_model(engine)



#
#def session_commit():
#    transaction.commit()
    
    
#DeclarativeBase = declarative_base(engine)
#metadata = DeclarativeBase.metadata
#Session = sessionmaker(engine)
#DBSession = Session()



