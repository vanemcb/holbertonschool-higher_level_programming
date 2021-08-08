#!/usr/bin/python3
""" script that changes the name of a State object
from the database hbtn_0e_6_usa
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

    state = session.query(State).get(2)
    state.name = 'New Mexico'
    session.add(state)
    session.commit()
