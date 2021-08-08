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

    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    new_s = State(name='California')
    new_c = City(name='San Francisco', state=new_s)
    session.add(new_s)
    session.add(new_c)
    session.commit()
    session.close()
