#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost:\
            3306/{argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).all()
    if a_state in states:
        print("{}: {}".format(a_state.id, a_state.name))
    session.close()
