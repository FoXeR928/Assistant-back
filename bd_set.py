from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from config_init import base, table_users,table_pc, table_prog

Base = declarative_base()
engine = create_engine(f"sqlite:///{base}.db")

Base.metadata.create_all(engine)

class USERS(Base):
    __tablename__ = table_users
    id=Column(Integer, primary_key=True, unique=True)
    user=Column(String, primary_key=True)
    password=Column(String)
    access=Column(String)

class PC(Base):
    __tablename__ = table_pc
    id=Column(Integer,primary_key=True, unique=True)
    user=Column(String, ForeignKey("users.user"))
    host=Column(String)
    mac=Column(String, unique=True)
    pc_name=Column(String)
    password=Column(String)

class PROG(Base):
    __tablename__=table_prog
    id=Column(Integer,primary_key=True, unique=True)
    user=Column(String, ForeignKey("users.user"))
    pc=Column(String)
    programm=Column(String)
    path=Column(String)