#!/usr/bin/python3
""" script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).filter(State.name == argv[4]).first()

    if states == None:
        print("Not found")
    else:
        print(states.id)
