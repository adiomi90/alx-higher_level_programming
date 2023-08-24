#!/usr/bin/python3
"""
use table relationship to access and print city and state
parameters given to script: username, password, database
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instances = session.query(State).order_by(State.id)
    for instance in instances:
        print(instance.id, instance.name, sep=": ")
        for city_instance in instance.cities:
            print("    ", end="")
            print(city_instance.id, city_instance.name, sep=": ")
