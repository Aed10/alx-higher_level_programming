#!/usr/bin/python3
"""
This script connects to a MySQL database and deletes all State objects
with a name containing the letter 'a' from the database hbtn_0e_6_usa.

Usage: python3 mysql_example.py <username> <password> <database>

Dependencies:
    - MySQL-python library

Example:
    python3 mysql_example.py username password database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def del_states(username, password, database):
    """
    Delete all State objects with a name containing the letter 'a'
    from the database hbtn_0e_6_usa.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database.

    Returns:
        None
    """
    # Create engine
    engine = create_engine(
        f"mysql://{username}:{password}@localhost:3306/{database}"
        )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete all State objects with a name containing the letter 'a'
    session.query(State).filter(State.name.contains("a")).delete()
    session.commit()


if __name__ == "__main__":
    username, password, databas = sys.argv[1], sys.argv[2], sys.argv[3]
    del_states(username, password, databas)
