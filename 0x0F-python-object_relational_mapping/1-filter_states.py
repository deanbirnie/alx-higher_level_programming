#!/usr/bin/python3
"""
Script to list all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def main():
    """
    Main function to connect to the MySQL server and retrieve and display data.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    cursor = db.cursor()

    query = """
        SELECT * FROM states
        WHERE name LIKE 'N%'
        ORDER BY id;
    """
    cursor.execute(query)

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
