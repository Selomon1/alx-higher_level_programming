#!/usr/bin/python3
"""
Python file that contains the class definition of a state and an instance
"""


import sqlalchemy
from sqlalchemy import Column, Integer, String
import sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents the states
    """


    __tablename__ = "states"

    id = Column)Integer, primary_key=True)
    name = Column(String(128), nullable=False)
