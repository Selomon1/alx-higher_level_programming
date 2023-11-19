#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from sys import srgv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost:\
            3306/{argv[3]}")
    Base.metadata.create_all(engine)
    Sesion = session maker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)
        session.commit()
        session.close()
