from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from config_init import base, table_pc, table_prog

Base = declarative_base()
engine = create_engine(f"sqlite:///{base}.db")

Base.metadata.create_all(engine)

class PC(Base):
    __tablename__ = table_pc
    id=Column(String,primary_key=True, nullable=False)
    pc_name=Column(String)
    mac=Column(String, unique=True)
    win=Column(String)