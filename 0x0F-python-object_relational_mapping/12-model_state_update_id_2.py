#!/usr/bin/python3
"""script to update the name of the state with id 2"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state(id: int):
    """updates the name of the state with id 2"""
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{user}:\
                           {passwd}@localhost:3306/{db}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == id).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()


if __name__ == "__main__":
    update_state(2)
