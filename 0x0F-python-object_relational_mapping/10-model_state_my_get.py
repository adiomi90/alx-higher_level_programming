#!/usr/bin/python3
"""Script that prints the State Onject with the name as an arg
from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_fil = session.query(State).filter(State.name == (sys.argv[4],)).first()

    if state_fil is not None:
        print(state_fil.id)
    else:
        print("Not found")
