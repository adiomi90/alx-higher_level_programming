#!/usr/bin/python3
"""
 This script contains the class state relationship
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Class that defines each city

    Attributes:
        __tablename__ (str): The name of the table
        id (sqlalchemy.Integer): The State id
        name (sqlalchemy.String): The State name
        state_id (sqlalchemy.Integer): Reference column
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
