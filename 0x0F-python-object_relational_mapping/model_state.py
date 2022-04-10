#!/usr/bin/python3
""" model state """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    class State is an inherit class of Base
    Attributes:
        id (int): id
        name (string): name of filed
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
