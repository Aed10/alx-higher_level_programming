#!/usr/bin/python3
"""
This script connects to a MySQL database and prints the first state Object.

Usage: python3 mysql_example.py <username> <password> <database>

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
    """
    Prints the first State Object from a given MySQL database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Name of the MySQL database.

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

    # Query and display states
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("No states found")


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    # Extract username, password, and database name from command line arguments
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the list_states function
    list_states(username, password, database_name)
