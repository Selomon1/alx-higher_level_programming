#!/usr/bin/python3
"""
Script that changes the name of a State object from the
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
    nick_Name = session.query(State).filter_by(id=2).first()
    nick_Name.name = "New Mexico"
    session.commit()
    session.close()
