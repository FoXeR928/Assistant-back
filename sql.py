from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config_init import base
from bd_set import Base, engine

def open_base(base):
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

def read_mac(user, table):
    try:
        session=open_base(base)
        sirch=session.query(table).filter(table.user==user).first()
        result={"error":0, "result":sirch.mac}
    except Exception as err:
        result={"error":1, "result":err}
    return result

def write_path(user, pc,programm, path, table, table_check):
    try:
        session=open_base(base)
        check=session.query(table_check).filter(table_check.user==user).all()
        if len(check)>0:
            point=table(user=user, pc=pc, programm=programm, path=path)
            session.add(point)
            session.commit()
            result={"error":0, "result":"Create"}
        else:
            result={"error":0, "result":"No user in base"}
    except Exception as err:
        result={"error":1, "result":err}
    return result

def write_pc(user, host,mac, pc_name, password, table, table_check):
    try:
        session=open_base(base)
        check=session.query(table_check).filter(table_check.user==user).all()
        if len(check)>0:
            point=table(user=user, host=host,mac=mac,pc_name=pc_name, password=password)
            session.add(point)
            session.commit()
            result={"error":0, "result":"Create"}
        else:
            result={"error":0, "result":"No user in base"}
    except Exception as err:
        result={"error":1, "result":err}
    return result

def read_path(programm, table):
    try:  
        session=open_base(base)
        sirch=session.query(table).filter(table.programm.like("%" + programm + "%")).all()
        result={"error":0, "result":sirch.path}
    except Exception as err:
        result={"error":1, "result":err}
    return result

def read_win(user, table):
    try:
        session=open_base(base)
        sirch=session.query(table).filter(table.user==user).first()
        result={"error":0, "host":sirch.host, "pc_name":sirch.pc_name, "password":sirch.password}
    except Exception as err:
        result={"error":1, "result":err}
    return result