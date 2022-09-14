#!/usr/bin/python3
"""Defines a State as the ORM for states table"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """mapping class for the states table"""
    __tablename__ = 'states'

    id = Column('id', Integer, primary_key=True,
                unique=True, nullable=False)
    name = Column('name', String(128), nullable=False)
