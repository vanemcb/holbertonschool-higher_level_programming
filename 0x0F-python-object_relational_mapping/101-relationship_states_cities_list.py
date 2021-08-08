#!/usr/bin/python3
""" Script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
"""

from sys import argv
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, state

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    query = session.query(State).order_by(State.id)

    for element in query:
        print("{}: {}".format(element.id, element.name))
        for element2 in element.cities:
            print("\t{}: {}".format(element2.id, element2.name))

    session.close()
