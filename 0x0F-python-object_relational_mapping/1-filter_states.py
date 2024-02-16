#!usr/bin/python3
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
        db=sys.argv[3],
    )
    query = "SELECT id,name FROM `states` WHERE name LIKE 'N%' ORDER BY id;"
    Cursor = Connectivity.cursor()
    Cursor.execute(query)
    [print(state) for state in Cursor.fetchall()]
    Cursor.close()
    Connectivity.close()
