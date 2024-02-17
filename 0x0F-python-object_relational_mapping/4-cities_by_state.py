#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves the names of all cities
in the database, along with their state names.

Usage: python3 mysql_select.py <username> <password> <database>

Dependencies:
    - MySQL-python library

Example:
    python3 mysql_select.py username password database
"""

import MySQLdb
import sys

if __name__ == "__main__":

    Connectivity = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    Cursor = Connectivity.cursor()
    Cursor.execute(
        "SELECT c.id, c.name, s.name FROM \
                   cities as c INNER JOIN states as s ON c.state_id = s.id\
                   ORDER BY c.id ASC"
    )

    [print(city) for city in Cursor.fetchall()]
    Cursor.close()
    Connectivity.close()
