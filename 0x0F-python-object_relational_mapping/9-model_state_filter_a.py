#!/usr/bin/python3
"""script to print any State object that contains 'a' from a db"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def get_states_with_a():
    """selects all states with 'a' in their name from states"""
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{user}:\
                           {passwd}@localhost:3306/{db}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    get_states_with_a()
