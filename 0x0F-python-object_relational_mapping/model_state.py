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
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
