#!/usr/bin/python3
"""
This script connects to a MySQL database and selects all the states from the states table.

Usage:
    0-select_states.py <username> <password> <database_name>

Example:
    0-select_states.py root password example_database

Note:
    This script assumes that there is a table named "states" in the specified database with the following columns:
    id, name, abbr, capital, population, region
"""

import MySQLdb
import sys


def select_states():
    """Connects to a MySQL database and selects all the states from the states table."""
    # Connect to the MySQL database
    Connectivity = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    # Create a cursor to execute SQL queries
    Cursor = Connectivity.cursor()

    # Execute the SELECT query
    Cursor.execute("SELECT * FROM `states`;")

    # Fetch all the results and print them
    states = Cursor.fetchall()
    [print(state) for state in states]

    # Close the cursor and connection
    Cursor.close()
    Connectivity.close()


if __name__ == "__main__":
    # Check if the correct number of arguments are passed
    if len(sys.argv) != 4:
        print("Error: incorrect number of arguments")
        print("Usage: 0-select_states.py <username> <password> <database_name>")
        sys.exit(1)

    # Call the select_states function
    select_states()
