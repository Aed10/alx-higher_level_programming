#!/usr/bin/python3
"""
This script connects to a MySQL database and prints a list of states whose
names start with the letter 'N'.

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
    )

    Cursor = Connectivity.cursor()
    Cursor.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    [print(state) for state in Cursor.fetchall() if state[1][0] == "N"]
