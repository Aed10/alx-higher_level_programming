#!usr/bin/python3
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
