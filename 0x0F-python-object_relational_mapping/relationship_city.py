#!/usr/bin/python3
"""Defines a City class as the ORM for the cities table"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """mapping class for the cities table"""
    __tablename__ = 'cities'

    id = Column('id', Integer, primary_key=True,
                unique=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'),
                      nullable=False)
    state = relationship("State", back_populates='cities')
