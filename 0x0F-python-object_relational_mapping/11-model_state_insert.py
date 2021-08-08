#!/usr/bin/python3
""" Script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
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

    state = State(name='Louisiana')
    session.add(state)
    session.new
    session.commit()

    name = session.query(State).filter(State.name == 'Louisiana').first()

    print(name.id)
