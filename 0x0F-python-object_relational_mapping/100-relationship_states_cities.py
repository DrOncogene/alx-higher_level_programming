#!/usr/bin/python3
"""script to create a state with a new city"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


def create_state(state: str, new_city: str):
    """create a state called california with San Francisco"""
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{user}:\
                           {passwd}@localhost:3306/{db}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    san_francisco = City(name=new_city)
    california = State(name=state, cities=[san_francisco])
    session.add(california)
    session.commit()
    session.close()


if __name__ == "__main__":
    create_state("California", 'San Francisco')
