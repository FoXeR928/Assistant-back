from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from config_init import base, tabl_pc

Base = declarative_base()
engine = create_engine(f"sqlite:///{base}.db")

Base.metadata.create_all(engine)
