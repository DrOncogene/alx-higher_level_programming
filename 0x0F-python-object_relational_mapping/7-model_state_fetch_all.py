#!/usr/bin/python3
"""script to print all State objects from a db"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
engine = create_engine(f"mysql+mysqldb://{user}:\
                        {passwd}@localhost:3306/{db}")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
states = session.query(State)
for state in states:
    print(f"{state.id}: {state.name}")

session.close()
