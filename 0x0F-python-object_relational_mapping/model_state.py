#!/usr/bin/python3

"""
This script creates a database table using SQLAlchemy.

Usage: python3 create_database_table.py <username> <password> <database_name>

Args:
    username (str): MySQL username
    password (str): MySQL password
    database_name (str): name of the database to create the table in

Returns:
    None

Raises:
    ValueError: if the number of args is not 3
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

if __name__ == "__main__":
    # Create an instance of Base
    Base = declarative_base()

    # Define the State class
    class State(Base):
        __tablename__ = "states"

        id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
        name = Column(String(128), nullable=False)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    mysql_connection_string = (
        f"mysql://{username}:{password}@localhost:3306/{database_name}"
    )

    # Create the SQLAlchemy engine
    engine = create_engine(mysql_connection_string)

    Base.metadata.create_all(engine)
