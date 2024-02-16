#!/usr/bin/python3
"""
This script connects to a MySQL server and retrieves all states
from the database hbtn_0e_0_usa.

Usage: python3 list_states.py <mysql_username> <mysql_password> <database_name>

The script takes 3 arguments: mysql username, mysql password, and database name
(no argument validation is done).

It uses the MySQLdb module to connect to the MySQL server.

The results are sorted in ascending order by states.id and displayed
as they are in the example below.

The code is not executed when the script is imported.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    Connectivity = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    Cursor = Connectivity.cursor()
    Cursor.execute("SELECT * FROM `states` ORDER BY id ASC;")
    [print(state) for state in Cursor.fetchall()]
    Cursor.close()
    Connectivity.close()
