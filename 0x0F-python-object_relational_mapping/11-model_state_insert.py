#!/usr/bin/python3
"""script to add State object Loisiana a db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state(state: str):
    """adds a State object to states"""
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{user}:\
                           {passwd}@localhost:3306/{db}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name=state))
    session.commit()
    louisiana = session.query(State).filter(State.name == state).all()[0]
    print(louisiana.id)
    session.close()


if __name__ == "__main__":
    add_state("Louisiana")
