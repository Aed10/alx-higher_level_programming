#!/usr/bin/python3
"""
This script connects to a MySQL database and prints a list of states whose
names matches @name argument.

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
    Cursor.execute(
        "SELECT * FROM `states` WHERE BINARY \
                   name = '{}'".format(
            name
        )
    )
    [print(state) for state in Cursor.fetchall()]
