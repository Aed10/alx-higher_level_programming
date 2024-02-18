#!/usr/bin/python3
"""Defines a State model.
Inherits from SQLAlchemy Base and links to the MySQL table states.

Args:
    None

Returns:
    None

Raises:
    None

Attributes:
    Base (sqlalchemy.ext.declarative.declarative_base):
    The SQLAlchemy base class.
    Column (sqlalchemy.Column): The SQLAlchemy column class.
    Integer (sqlalchemy.Integer): The SQLAlchemy integer column type.
    String (sqlalchemy.String): The SQLAlchemy string column type.
    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
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
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name=None):
        """
        Initialize a new State instance.

        Args:
            name (str): The name of the state.

        Returns:
            None

        Raises:
            ValueError: If the name is not provided.
        """
        self.name = name
