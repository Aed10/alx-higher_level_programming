#!/usr/bin/python3
"""
This script connects to a MySQL database and prints all the cities Objects.

Usage: python3 mysql_example.py <username> <password> <database>

Dependencies:
    - MySQL-python library

Example:
    python3 mysql_example.py username password database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from relationship_state import State
from relationship_city import City


def list_cities(username, password, database_name):
    """
    List all the Cities Object from a given MySQL database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): MySQL database name.

    Returns:
        None

    Raises:
        ValueError: If the name is not provided.
    """
    engine = create_engine(
        f"mysql://{username}:{password}@localhost:3306/{database_name}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        if state.cities:
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")


if __name__ == "__main__":
    # Check if correct number of arguments is provided

    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(username, password, database_name)
