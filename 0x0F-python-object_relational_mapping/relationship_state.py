#!/usr/bin/python3
"""
Contains State class and Base, an instance of
declarative_base() to work with MySQLAlchemy ORM.
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Attributes:
        __tablename__(sqlalchemy.String): The table name
        id (sqlalchemy.Integer): id of the state class
        name(sqlalchemy.String): The state name
        cities(sqlaclchemy.String): the cities referencing states
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
