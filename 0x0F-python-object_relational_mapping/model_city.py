#!/usr/bin/python3
"""defining a class City that iherits from Base"""
from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """Class City with id, state_id, and name attributes"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
