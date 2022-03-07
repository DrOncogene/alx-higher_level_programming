#!/usr/bin/python3
"""script to print the first State object from a db"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def get_first_state():
    """selects the first state in the states table"""
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{user}:\
                           {passwd}@localhost:3306/{db}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()
    print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    get_first_state()
