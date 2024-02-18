#!/usr/bin/python3
"""
This script connects to a MySQL database and Searchs for a given State.

Usage: python3 mysql_example.py <username> <password> <database> <state>

Dependencies:
    - MySQL-python library

Example:
    python3 mysql_example.py username password database 'Texas'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def list_states(username, password, database_name):
    """
    Prints the ID of a State whose name is provided.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Name of the MySQL database.
        state (str): Name of the State.

    Returns:
        None
    """
    # Create engine
    engine = create_engine(
        f"mysql://{username}:{password}@localhost:3306/{database_name}"
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    name = sys.argv[4]
    # Query and display states
    state = session.query(State).filter(State.name == name).first()
    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    # Extract username, password, and database name from command line arguments
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the list_states function
    list_states(username, password, database_name)
