#!/usr/bin/python3
""" Module that contains the class definition of a City
"""

from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """  Class City that inherits from Base """

    __tablename__ = 'cities'
    id = Column(Integer(),
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(ForeignKey('states.id'))
