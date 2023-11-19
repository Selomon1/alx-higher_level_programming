#!/usr/bin/python3
"""
Script that prints the State object with name passes as argument from the
database hbtn_0e_6_usa
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql://{argv[1]}:{argv[2]}@localhost:\
            3306/{argv[3]}")
    Base.metadata.create_all(engine)
    session = Session()
    state = session.query(State).filter_by(name=argv[4]).first()
    if state:
        print(str(state.id))
    else:
        print("Not found")
    session.close()
