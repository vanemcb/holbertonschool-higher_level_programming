#!/usr/bin/python3
""" Script that lists all City objects from the
database hbtn_0e_101_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    cities = session.query(City.id, City.name, State.name).join(State).all()

    for element in cities:
        print("{}: {} -> {}".format(element[0], element[1], element[2]))
