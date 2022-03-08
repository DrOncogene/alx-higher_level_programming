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
    cities = [state.cities for state in states]
    for i in range(len(states)):
        print("{}: {}".format(states[i].id, states[i].name))
        for city in cities[i]:
            print("    {}: {}".format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    list_states_cities()
