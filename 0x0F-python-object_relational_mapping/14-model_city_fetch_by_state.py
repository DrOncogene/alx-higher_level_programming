#!/usr/bin/python3
"""script to delete states with a in their name"""
from model_state import Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
import sys


def get_cities():
    """deletes states with a in their name from the database"""
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{user}:\
                           {passwd}@localhost:3306/{db}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.commit()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":
    get_cities()
