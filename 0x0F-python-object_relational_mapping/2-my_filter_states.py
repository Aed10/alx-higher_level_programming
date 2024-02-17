#!/usr/bin/python3
"""
This script connects to a MySQL database and prints a list of states whose
names matches @name argument.

Usage: python3 mysql_example.py <username> <password> <database>

Dependencies:
    - MySQL-python library

Example:
    python3 mysql_example.py username password database
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
    Cursor.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    [print(state) for state in Cursor.fetchall() if state[1] == name]
