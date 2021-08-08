#!/usr/bin/python3
""" Module that contains the class definition of a State and an
instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """  Class State that inherits from Base """

    __tablename__ = 'states'
    id = Column(Integer(),
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete",
                          passive_deletes=True)
