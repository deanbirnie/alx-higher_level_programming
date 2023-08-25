#!/usr/bin/python3
"""
Script to delete all State objects with a name containing the letter "a"
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


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

    states_to_delete = session.query(State).filter(
        State.name.contains('a')
    ).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    session.close()
