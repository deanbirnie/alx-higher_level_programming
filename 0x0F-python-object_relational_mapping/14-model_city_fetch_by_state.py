#!/usr/bin/python3
"""
Script to print all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_name = session.query(State).filter(
            State.id == city.state_id
        ).first().name
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    session.close()
