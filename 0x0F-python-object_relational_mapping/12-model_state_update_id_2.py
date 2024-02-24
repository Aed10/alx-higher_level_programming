#!/usr/bin/python3
"""
This script connects to a MySQL database and update a state to our database.

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


def update_states(username, password, database_name):
    """
    Update a state in our Database.

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

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    # Extract username, password, and database name from command line arguments
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the list_states function
    update_states(username, password, database_name)