#!/usr/bin/python3
"""
Module containing the definition of State class and creating Base instance.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that represents a state in the MySQL table states.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    from sqlalchemy import create_engine

    # Modify the connection URI based on your MySQL configuration
    db_uri = "mysql://username:password@localhost:3306/dbname"
    engine = create_engine(db_uri)

    # Create the table defined by the State class
    Base.metadata.create_all(engine)
