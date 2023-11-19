#1/usr/bin/python3
"""
Script that adds the State object "Lousiana to the data base
hbtn_0e_6_usa
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
    Base.metadata.create_all()
    Session = sessionmaker(bind=engine)
    session = Session()
    add_state = State(name='Louisiana')
    session.add(add_state)
    session.commit()
    print(add-state.id)
    session.close()
