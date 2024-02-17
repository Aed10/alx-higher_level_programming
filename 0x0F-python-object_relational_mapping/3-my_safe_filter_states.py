#!/usr/bin/python3
"""
This script connects to a MySQL database and prints a list of states whose
names matches @name argument.
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
    query = "SELECT * FROM `states` WHERE name = %s"
    Cursor.execute(query, (name,))
    [print(state) for state in Cursor.fetchall() if state[1] == name]
    Cursor.close()
    Connectivity.close()
