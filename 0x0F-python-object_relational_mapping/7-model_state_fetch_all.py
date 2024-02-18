#!/usr/bin/python3
"""
This script connects to a MySQL database and prints a list of cities whose
belongs to a given @state_name as argument.
Safe from SQL injection

Usage: python3 mysql_example.py <username> <password> <database> <state_name>

Dependencies:
    - MySQL-python library

Example:
    python3 mysql_example.py username password database 'Arizona'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, database_name):
    """Prints a list of states whose names matches @name argument.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database_name (str): The MySQL database name."""
    # Create engine
    engine = create_engine(
        f"mysql://{username}:{password}@localhost:3306/{database_name}"
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and display states
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database_name)
