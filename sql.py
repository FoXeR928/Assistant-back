from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config_init import base
from bd_set import Base, PC

def open_base(base):
    engine = create_engine(f"sqlite:///{base}.db")
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

def read_mac(id, table):
    session=open_base(base)
    mac=session.query(table).filter(table.id==id).one()


print(read_mac(1,PC))
