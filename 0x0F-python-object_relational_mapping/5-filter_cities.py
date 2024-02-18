#!/usr/bin/python3
"""
This script connects to a MySQL database and prints a list of cities whose
belongs to a given @state_name as argument.
Safe from SQL injection

Usage: python3 mysql_example.py <username> <password> <database> <state_name>

Dependencies:
    - MySQL-python library

Example:
    python3 mysql_example.py username password database 'Arizona'
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
    name = sys.argv[4]
    Cursor = Connectivity.cursor()
    query = "SELECT c.name FROM cities c\
    JOIN states s ON c.state_id = s.id WHERE s.name = %s"
    Cursor.execute(query, (name,))
    city_names = [city[0] for city in Cursor.fetchall()]
    print(", ".join(city_names))

    Cursor.close()
    Connectivity.close()
