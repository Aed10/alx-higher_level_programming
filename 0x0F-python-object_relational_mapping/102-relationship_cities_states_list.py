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
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import State


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
    states = session.query(State).options(joinedload(State.cities)).all()
    for state in states:
        if state.cities:
            sorted_cities = sorted(state.cities, key=lambda city: city.id)
            for city in sorted_cities:
                print(f"{city.id}: {city.name} -> {state.name}")
        else:
            print(f"{state.name}: None")


if __name__ == "__main__":
    # Check if correct number of arguments is provided

    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(username, password, database_name)
