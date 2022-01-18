from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config_init import base
from bd_set import PROG, Base

def open_base(base):
    engine = create_engine(f"sqlite:///{base}.db")
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

def read_mac(password, table):
    session=open_base(base)
    result=session.query(table).filter(table.password==password).one()
    return result.mac

def read_path(programm, table):
    session=open_base(base)
    result=session.query(table).filter(table.programm.like("%" + programm + "%")).one()
    return result.path