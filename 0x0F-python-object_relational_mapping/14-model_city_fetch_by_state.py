#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ = "__main__":
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost:\
            3306/{argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(City, State).filter(City.state_id == State.id)\
                                       .order_by(City.id).all() 
    for city, state in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
