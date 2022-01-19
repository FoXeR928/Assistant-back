from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from config_init import base, table_pc, table_prog

Base = declarative_base()
engine = create_engine(f"sqlite:///{base}.db")

Base.metadata.create_all(engine)

class PC(Base):
    __tablename__ = table_pc
    id=Column(Integer,primary_key=True)
    password=Column(String)
    pc_name=Column(String)
    mac=Column(String, unique=True)
    win=Column(String)

class PROG(Base):
    __tablename__=table_prog
    id=Column(Integer,primary_key=True)
    programm=Column(String)
    path=Column(String)