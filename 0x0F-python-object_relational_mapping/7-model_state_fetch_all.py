#!/usr/bin/python3
"""
Lists all state objects from the database hbtn_0e_6_usa
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from sys import argv
from model_state import Base, State

if __name__ = "__main__":
    eng = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost:\
         3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    for obj in session.query(State).all():
        print("{}: {}".format(obj.id, obj.name))
    session.close()
