#!/usr/bin/python3
"""script to list all states and their cities"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


def list_states_cities():
    """lists all states and their cities"""
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{user}:\
                           {passwd}@localhost:3306/{db}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        cities = state.cities
        for city in cities:
            print(f"\t{city.id}: {city.name}")

    session.close()


if __name__ == "__main__":
    list_states_cities()
