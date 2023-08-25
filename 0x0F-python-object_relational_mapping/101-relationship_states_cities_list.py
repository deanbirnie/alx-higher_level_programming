#!/usr/bin/python3
"""
Script to list all State objects and their corresponding City objects
from the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db_uri = "mysql://{}:{}@localhost:3306/{}".format(
        username, password, database
    )
    engine = create_engine(db_uri, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_and_cities = session.query(State).order_by(State.id, City.id).all()
    for state in states_and_cities:
        for city in state.cities:
            print("{}: {} -> {}".format(state.id, state.name, city.name))

    session.close()
