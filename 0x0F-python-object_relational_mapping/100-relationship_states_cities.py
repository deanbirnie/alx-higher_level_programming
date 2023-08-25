#!/usr/bin/python3
"""
Script to create the State "California" with the City "San Francisco".
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

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California", cities=[City(name="San Francisco")])
    session.add(new_state)
    session.commit()

    session.close()
